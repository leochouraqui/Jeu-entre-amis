# By Léo Chouraqui | Marie-Estelle Chouraki | Chirozaan Srikantharajah | Kélia Siao
import pygame


def text(text_str, font, surface, pos, center_type="center", color=(255,255,255),
         shadow=False, shadow_color=(22,22,22), shadow_offset=3, split=None):


    if split is not None: # si le texte doit être scindé (faire en sorte que le texte s'affiche comme un paragraphe)
        text_str_split = text_str
        y_pos = pos[1]

        if len(text_str) < 24:
            if shadow: # ombre
                shadow_label = font.render(text_str, 1, shadow_color)
                surface.blit(shadow_label, (pos[0]-shadow_offset, y_pos+shadow_offset))
            label = font.render(text_str, 1, color)
            surface.blit(label, (pos[0], y_pos))
        else:
            while len(text_str) >= 24:

                try:
                    split_spot = text_str[:24].rindex(" ") # faire en sorte que la scission soit sur un espace
                except: # si pas d'espace
                    print("no space")
                    split_spot = 24

                if shadow: # ombre
                    shadow_label = font.render(text_str[:split_spot], 1, shadow_color)
                    surface.blit(shadow_label, (pos[0]-shadow_offset, y_pos+shadow_offset))
                label = font.render(text_str[:split_spot], 1, color)
                surface.blit(label, (pos[0], y_pos))
                text_str = text_str[split_spot:]

                y_pos += 32

                if len(text_str) < 24:
                    if shadow: # ombre
                        shadow_label = font.render(text_str[:split_spot], 1, shadow_color)
                        surface.blit(shadow_label, (pos[0]-shadow_offset, y_pos+shadow_offset))
                    label = font.render(text_str[:split_spot], 1, color)
                    surface.blit(label, (pos[0], y_pos))



    else: # texte

        label = font.render(text_str, 1, color)
        label_rect = label.get_rect()

        if center_type == "center":
            label_rect.center = pos
        elif center_type == "right":
            label_rect.right = pos[0]
            label_rect.y = pos[1]
        elif center_type == "left":
            label_rect.left = pos[0]
            label_rect.y = pos[1]

        if shadow: # ombre
            shadow_label = font.render(text_str, 1, shadow_color)
            surface.blit(shadow_label, (label_rect.x-shadow_offset, label_rect.y+shadow_offset))
        surface.blit(label, label_rect)



def button(text_str, font, surface, pos, size, user_click, color=(227, 163, 61),
            second_color=(255, 200, 112), text_color=(22,22,22), split=1):
    rect = pygame.Rect(0, 0, size[0], size[1])
    rect.center = pos
    click_on_button = False
    if rect.collidepoint(pygame.mouse.get_pos()): # si la souris de l'utilisateur est sur le bouton
        color = second_color # changer la couleur du bouton
        if user_click: # si l'utilisateur clique sur le bouton
            click_on_button = True

    # bouton
    pygame.draw.rect(surface, color, rect)
    # écrire le texte
    if split == 1:
        text(text_str, font, surface, pos, color=text_color)
    if split == 2: # diviser la phrase en 2 lignes
        try:
            split_spot = len(text_str)//2 + text_str[len(text_str)//2:].index(" ") # faire en sorte que la scission soit sur un espace
        except: # si pas d'espace
            split_spot = len(text_str)//2
        text(text_str[:split_spot], font, surface, (pos[0], pos[1]-8), color=text_color)
        text(text_str[split_spot:], font, surface, (pos[0], pos[1]+8), color=text_color)


    return (click_on_button, text_str)
