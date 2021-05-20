# By Léo Chouraqui | Marie-Estelle Chouraki | Chirozaan Srikantharajah | Kélia Siao
import pygame
import random
import time
from gui import text, button
from insults import INSULTS


class Game: # classe qui rendra tout le jeu fonctionnel
    def __init__(self, surface):
        self.surface = surface
        self.surface_size = (self.surface.get_width(), self.surface.get_height())
        self.user_first_click = True
        self.WRONG_SCORE_DECREASE = 10 # l'utilisateur perdra X points de score lorsqu'il cliquera sur le mauvais bouton
        self.WRONG_TIME = 2.5 # le mauvais message sera affiché X sec

        # images
        self.images = {"right": {}, "left": {}, "background": []}
        for img_name in ("bête", "fille", "gros", "méchant", "moche", "sale"):
            img = pygame.image.load("Assets/"+img_name+".png").convert_alpha()
            self.images["left"][img_name] =  img # l'image -> celle des personnages regardant la gauche
            self.images["right"][img_name] =  pygame.transform.flip(img, True, False)

        for nb in range(4):
            self.images["background"].append(pygame.transform.smoothscale(pygame.image.load(f"Assets/background{nb}.png"), self.surface_size))


        # polices d'écriture
        self.mini_font = pygame.font.Font(None, 22)
        self.small_font = pygame.font.Font(None, 26)
        self.small_font_2 = pygame.font.Font(None, 34)
        self.medium_font = pygame.font.Font(None, 38)
        self.medium_font_2 = pygame.font.Font(None, 48)
        self.big_font = pygame.font.Font(None, 60)
        self.big_font_2 = pygame.font.Font(None, 72)

        # compteur
        self.timer = {"wrong": 0}
        self.reset()


    def reset(self): # réinitialiser toutes les variables nécessaires
        self.state = "characters_selection"
        self.players_categorie = {1: None, 2: None}
        self.characters_categorie = ["fille", "gros", "méchant", "bête", "sale", "moche"]

        # ici, stocker la phrase complète des 2 joueurs, celle de la lecture aléatoire et juste le groupe de mots
        self.sentences = {1: {"current": []}, 2: {"current": []}, "all": {"Sujet": [], "Verbe": [], "Complément": [], "Liaison": []}}

        self.player_turn = random.randint(1,2) # choisir au hasard qui commencera

        self.scores = {1: 100, 2: 100} # les deux joueurs commencent avec un score de 100

        # sélectionner au hasard un arrière-plan
        self.background = random.choice(self.images["background"])


    def click(self): # rendre la capacité de clic de l'utilisateur
        self.user_click = False
        if pygame.mouse.get_pressed()[0] and self.user_first_click:
            self.user_click = True
            self.user_first_click = False
        elif not pygame.mouse.get_pressed()[0]:
            self.user_first_click = True


    def draw_image(self): # apparition des deux images des deux joueurs
        # image de gauche (joueur 1)
        img = self.images["right"][self.players_categorie[1]]
        img_rect = img.get_rect()
        img_rect.x = 2
        img_rect.y = 5
        if self.player_turn == 1:
            pygame.draw.rect(self.surface, (125,227,61), img_rect, 4)
        self.surface.blit(img, img_rect)

        # image de droite (joueur 2)
        img = self.images["left"][self.players_categorie[2]]
        img_rect = img.get_rect()
        img_rect.x = self.surface_size[0] - img_rect.w - 2
        img_rect.y = 5
        if self.player_turn == 2:
            pygame.draw.rect(self.surface, (125,227,61), img_rect, 4)
        self.surface.blit(img, img_rect)



    def players_categorie_selection(self, player_nb, adj_num): # rendre fonctionnel l'écran des sélections de caractères
        text(f"Le {adj_num} joueur peut choisir son type de personnage.", self.medium_font_2,
             self.surface, (self.surface_size[0]//2, 80), shadow=True, shadow_offset=2)
        buttons_size = (220, 70)
        button_y_pos = reset_button_y_pos = 200 # où sera le premier bouton (en y)
        button_x_pos = self.surface_size[0] // 2 - buttons_size[0]//2 - 25
        for button_number in range(len(self.characters_categorie)):
            if button_number == (len(self.characters_categorie)+1) // 2:
                button_y_pos = reset_button_y_pos
                button_x_pos = self.surface_size[0] // 2 + buttons_size[0]//2 + 25


            button_out = button(self.characters_categorie[button_number], self.big_font,
                                 self.surface, pos=(button_x_pos, button_y_pos), size=buttons_size, user_click=self.user_click)

            # vérifier si l'utilisateur appuie sur le bouton
            if button_out[0] is not False:
                self.players_categorie[player_nb] = button_out[1]
                self.characters_categorie.remove(button_out[1])
                break
            # changer la position y
            button_y_pos += buttons_size[1] + 50


    def sentences_selection(self): # choisir au hasard les 2 sens et "randomiser" les mots
        players_categorie = (self.players_categorie[2], self.players_categorie[1]) # faire que les insultes soient inversées
        for player_number, player_categorie in enumerate(players_categorie):
            player_number += 1
            insult = random.choice(INSULTS[player_categorie]) # choisir au hasard une insulte
            self.sentences[player_number]["sentence"] = insult["sentence"]
            for words_group in ("Sujet", "Verbe", "Complément", "Liaison"):
                words = list(insult[words_group])
                self.sentences[player_number][words_group] = words
                self.sentences["all"][words_group] += words
                random.shuffle(self.sentences["all"][words_group]) # mélanger le groupe de mots


    def draw_words(self): # dessiner tous les mots triés par catégorie
        buttons_size = (262, 32)
        space = 10 # espace entre les boutons
        button_x_pos = buttons_size[0]//2 + space
        button_y_pos = reset_button_y_pos = 350 # où sera le premier bouton (en y)

        to_return =  None, None

        for words_group in ("Sujet", "Verbe", "Complément", "Liaison"):
            text(words_group, self.medium_font_2, self.surface, (button_x_pos, button_y_pos-40), color=(164,61,227), shadow=True, shadow_offset=2) # dessiner le nom de la catégorie
            for word in self.sentences["all"][words_group]:
                if len(word) > 24:
                    split_number = 2
                else:
                    split_number = 1

                button_out = button(word, self.small_font, self.surface, pos=(button_x_pos, button_y_pos),
                                     size=buttons_size, user_click=self.user_click,  split=split_number)

                if button_out[0] is not False: # lorsque l'utilisateur clique sur un bouton
                    to_return = (words_group, button_out[1]) # renverra le groupe de mots et le texte du bouton


                button_y_pos += buttons_size[1] + space
            button_x_pos += buttons_size[0] + space
            button_y_pos = reset_button_y_pos

        return to_return


    def check_correct_word(self, words_group, button_out_text): # vérifier si le mot que l'utilisateur a sélectionné est correcte
        if button_out_text in self.sentences[self.player_turn][words_group]:

            if self.sentences[self.player_turn]["sentence"].index(button_out_text) == 0: # si c'était le premier mot de la phrase
                # imprimer ("correct")
                self.sentences[self.player_turn]["sentence"] = self.sentences[self.player_turn]["sentence"].replace(button_out_text, "", 1) # supprimer le mot de la phrase du joueur
                # supprimer le mot
                self.sentences[self.player_turn][words_group].remove(button_out_text)
                self.sentences["all"][words_group].remove(button_out_text)

                if len(self.sentences[self.player_turn]["sentence"]) > 0 and self.sentences[self.player_turn]["sentence"][0] == " ": # supprimer les espaces au début du mot
                    self.sentences[self.player_turn]["sentence"] = self.sentences[self.player_turn]["sentence"][1:]

                self.sentences[self.player_turn]["current"].append(button_out_text)

                self.scores[self.player_turn] += 10 # augmenter le score du joueur
                self.change_player_turn()

            else:

                self.timer["wrong"] = time.time() + self.WRONG_TIME
                self.scores[self.player_turn] -= self.WRONG_SCORE_DECREASE  # réduire le score du joueur
        else:

            self.timer["wrong"] = time.time() + self.WRONG_TIME
            self.scores[self.player_turn] -= self.WRONG_SCORE_DECREASE


    def draw_players_current_sentences(self):
        # joueur 1
        text_str = " ".join(self.sentences[1]["current"])
        text(f"{text_str}", self.small_font_2, self.surface, (248, 80), color=(244,244,244),
                center_type="left", split=self.surface_size[0]//2,
                shadow=True, shadow_color=(22,22,22), shadow_offset=1)

        # joueur 2
        text_str = " ".join(self.sentences[2]["current"])
        text(f"{text_str}", self.small_font_2, self.surface, (self.surface_size[0]//2+44, 80), color=(244,244,244),
                center_type="left", split=self.surface_size[0]//2,
                shadow=True, shadow_color=(22,22,22), shadow_offset=1)


    def change_player_turn(self): # changer le tour actuel du joueur
        if self.player_turn == 1:
            if len(self.sentences[2]["sentence"]) > 0:
                self.player_turn = 2

        else:
            if len(self.sentences[1]["sentence"]) > 0:
                self.player_turn = 1

        if len(self.sentences[1]["sentence"]) == 0 and len(self.sentences[2]["sentence"]) == 0: # si les 2 joueurs ont terminé leur phrase
            self.player_turn = None
            self.state = "score"



    def make_wrong_guess(self): # afficher un message et diminuer le score du joueur
        if self.timer["wrong"] > time.time():
            text("Faux! Essaye à nouveau", self.big_font_2, self.surface,
                  (self.surface_size[0]//2, 255), color=(209, 69, 59), shadow=True)


    def draw_scores(self):
        # joueur 1
        if self.scores[1] > self.scores[2]:
            color = (125,227,61)
        else:
            color=(227,81,61)
        text(f"Score : {self.scores[1]}", self.big_font_2, self.surface,
              (80, self.surface_size[1]//2-20), color=color, shadow=True, center_type="left")

        # joueur 2
        if self.scores[2] > self.scores[1]:
            color = (125,227,61)
        else:
            color=(227,81,61)

        text(f"Score : {self.scores[2]}", self.big_font_2, self.surface,
              (self.surface_size[0]-80, self.surface_size[1]//2-20), color=color, shadow=True, center_type="right")



    def do(self): # rendre le jeu fonctionnel
        self.surface.blit(self.background, (0, 0))
        self.click()

        if self.state == "characters_selection":
            if self.players_categorie[1] is None:
                self.players_categorie_selection(1 ,"premier")

            elif self.players_categorie[2] is None:
                self.players_categorie_selection(2, "second")
            else:
                self.sentences_selection()
                self.state = "game"


        elif self.state == "game":
            # self.user_click = True
            self.draw_image()
            self.draw_players_current_sentences()
            words_group, button_out_text = self.draw_words()
            if words_group is not None:
                self.check_correct_word(words_group, button_out_text)

            self.make_wrong_guess()


        elif self.state == "score":
            self.draw_image()
            self.draw_players_current_sentences()
            self.draw_scores()
            if button("Continuer", self.big_font, self.surface, pos=(self.surface_size[0]//2, self.surface_size[1]-120),
                                 size=(240, 60), user_click=self.user_click)[0]:
                self.reset()
