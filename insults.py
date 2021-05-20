# By Léo Chouraqui | Marie-Estelle Chouraki | Chirozaan Srikantharajah | Kélia Siao
INSULTS = {
    "fille": [
               {"sentence": "Tes cheveux sont tellement gras que je peux cuire mes frites avec.",
                "Sujet": ("Tes cheveux", "je"),
                "Verbe": ("sont", "peux"),
                "Complément": ("tellement gras", "cuire mes", "frites avec."),
                "Liaison" : ("que", )
               },
               {"sentence": "Tu te la joues mais la seule chose que tu as réussi à serrer dans ta vie, c'est tes lacets.",
                "Sujet": ("Tu", "tu"),
                "Verbe": ("te la joues", "c'est", "as réussi"),
                "Complément": ("la seule chose", "à serrer", "ta vie,", "tes lacets."),
                "Liaison" : ("mais", "que", "dans")
               }
             ],

    "gros": [
               {"sentence": "Tu danses comme un hippopotame qui a mangé un truc périmé",
                "Sujet": ("Tu", ),
                "Verbe": ("danses", "a mangé"),
                "Complément": ("un", "hippopotame", "un truc", "périmé"),
                "Liaison" : ("comme", "qui")
               },
               {"sentence": "Ton prof d'EPS t'as dis de faire un jogging autour du pâté de maison. Toi, tu manges du pâté en jogging dans ta maison.",
                "Sujet": ("Ton prof", "d'EPS", "Toi,"),
                "Verbe": ("t'as dis", "tu manges"),
                "Complément": ("de faire un jogging autour du pâté de maison.", "du pâté en jogging dans ta maison."),
                "Liaison" : ()
               },
               {"sentence": "T'es comme un soleil, t'es gros et tu fais mal aux yeux",
                "Sujet": ("T'","t'", "tu" ),
                "Verbe": ("es", "es", "fais"),
                "Complément": ("un soleil", "gros", "mal aux yeux", "et"),
                "Liaison" : ("comme", ", ")
               },
             ],

    "méchant": [
               {"sentence": "Tu es dispo le soir? J'aimerais que tu viennes me parler, ça me permettrait de m'endormir plus vite",
                "Sujet": ("Tu", "J'"),
                "Verbe": ("es", "aimerais", "permettrait"),
                "Complément": ("ça me", "dispo le soir?", "que tu viennes me parler" ,"de m'endormir plus vite"),
                "Liaison" : (",",)
                },
               {"sentence": "J'ai demandé à être muté en Syrie pour ne plus voir ta tête",
                "Sujet": ("J'",),
                "Verbe": ("ai demandé",),
                "Complément": ("à être muté", "en Syrie", "ne plus voir ta tête"),
                "Liaison" : ("pour",)
               },
               {"sentence": "Tu ne m'arrives pas à la cheville mais si un jour tu l'atteins, sois gentille et fais-moi mes lacets.",
                "Sujet": ("Tu", ),
                "Verbe": ("ne m'arrives pas", ),
                "Complément": ("à la cheville mais si un jour tu l'atteins,", "sois gentille et fais-moi mes lacets."),
                "Liaison" : ()
                },
               {"sentence": "Il y a des gens c'est comme des pièces : deux faces mais aucune valeur.",
                "Sujet": ("Il",),
                "Verbe": ("y a",),
                "Complément": ("des gens c'est comme des pièces : deux faces", "aucune valeur."),
                "Liaison" : ("mais",)
                },
               {"sentence": "Tu te prends trop pour un(e) prince/princesse mais le seul trône où tu es assis(e) c'est les toilettes.",
                "Sujet": ("Tu", "tu"),
                "Verbe": ("te prends", "es assis(e)"),
                "Complément": ("trop pour un(e) prince/princesse", "le seul trône où", "c'est les toilettes."),
                "Liaison" : ("mais",)
                },
               {"sentence": "Désolé si je t'ai blessé en te traitant d'idiot, je pensais que tu le savais déjà",
                "Sujet": ("Désolé si je", "je"),
                "Verbe": ("t'ai blessé", "pensais que", ),
                "Complément": ("en te traitant d'idiot", "tu le savais déjà"),
                "Liaison" : (",",)
                },
               {"sentence": "Avec tous les rateaux que tu as pris, tu vas pouvoir ouvrir un Jardinland!",
                "Sujet": ("Avec tous les rateaux que tu", "tu"),
                "Verbe": ("as pris", "vas pouvoir ouvrir"),
                "Complément": ("un Jardinland!",),
                "Liaison" : (",",)
                },
               {"sentence": "Je t'aime en cachette. Bah reste caché s'il te plait.",
                "Sujet": ("Je",),
                "Verbe": ("t'aime", "reste caché"),
                "Complément": ("en cachette.", "Bah", "s'il te plait."),
                "Liaison" : ()
                },
               {"sentence": "Je n'ai pas changé, j'ai grandi. Tu devrais essayer.",
                "Sujet": ("Je", "Tu", "j'"),
                "Verbe": ("n'ai pas changé,", "ai grandi.", "devrais essayer."),
                "Complément": (),
                "Liaison" : ()
                },
             ],

    "bête": [
               {"sentence": "T'es tellement con que ton QI est un nombre imaginaire.",
                "Sujet": ("T'"),
                "Verbe": ("es", "est"),
                "Complément": ("tellement con que ton QI", "un nombre imaginaire."),
                "Liaison" : ()
                },
               {"sentence": "Ton cerveau est tellement petit qu'il est soumis au principe d'incertitude.",
                "Sujet": ("Ton cerveau", "il"),
                "Verbe": ("est", "est soumis"),
                "Complément": ("tellement petit qu'", "au principe d'incertitude."),
                "Liaison" : ()
                },
               {"sentence": "Toi et l'intelligence, vous êtes comme deux droites parallèles : vous allez jamais vous croiser.",
                "Sujet": ("Toi et l'intelligence, vous", "vous"),
                "Verbe": ("êtes", "allez"),
                "Complément": ("comme deux droites parallèles", "jamais vous croiser."),
                "Liaison" : (":",)
                },
               {"sentence": "Ta bêtise glisse sur mon intelligence",
                "Sujet": ("Ta bêtise",),
                "Verbe": ("glisse",),
                "Complément": ("sur mon intelligence",),
                "Liaison" : ()
                },
               {"sentence": "Tu sais ce qu'est un oxymore Michel? Je vais t'en donner un : l'intelligence de Michel",
                "Sujet": ("Tu", "Je"),
                "Verbe": ("sais", "est", "vais"),
                "Complément": ("ce qu'", "un oxymore Michel?", "t'en donner un", "l'intelligence de Michel"),
                "Liaison" : (":",)
                },
               {"sentence": "C'est marrant ça fait 5mn que tu me parles et je peux déjà dire que ce sont les 5mn les plus insipides de ma vie.",
                "Sujet": ("tu", "je"),
                "Verbe": ("C'est", "fait", "me parles", "peux", "sont"),
                "Complément": ("marrant ça", "5mn", "déjà dire que ce", "les 5mn les plus insipides", "de ma vie."),
                "Liaison" : ("que", "et")
                },
               {"sentence": "Des fois, je me sens bête… Puis je te regarde et ça va mieux",
                "Sujet": ("je", "je"),
                "Verbe": ("me sens", "te regarde"),
                "Complément": ("Des fois,", "bête…", "ça va mieux"),
                "Liaison" : ("Puis", "et")
                },
    ],

    "sale": [
               {"sentence": "Tes cheveux sont tellement gras que je peux cuire mes frites avec.",
                "Sujet": ("Tes cheveux", "je"),
                "Verbe": ("sont", "peux"),
                "Complément": ("tellement gras", "cuire mes", "frites avec."),
                "Liaison" : ("que", )
               },

    ],
    "moche": [
               {"sentence": "Tu es tellement moche que quand tu te regardes dans le miroir il se brise",
                "Sujet": ("Tu", "tu te", "il"),
                "Verbe": ("es", "regardes", "se brise"),
                "Complément": ("tellement moche", "dans le miroir"),
                "Liaison" : ("que quand",)
                },
               {"sentence": "Moi j'aime beaucoup le port du masque, ça camoufle les effluves de pourriture qui émanent de ta bouche dès que tu l'ouvres",
                "Sujet": ("Moi j'", "tu"),
                "Verbe": ("aime", "émanent", "l'ouvres"),
                "Complément": ("beaucoup le port du masque", "ça camoufle les effluves", "de pourriture qui", "de ta bouche dès que"),
                "Liaison" : (",",)
                },
               {"sentence": "Ta tête me fait penser au film “la guerre des boutons”",
                "Sujet": ("Ta tête",),
                "Verbe": ("me fait penser",),
                "Complément": ( "au film", "“la guerre des boutons”"),
                "Liaison" : ()
                },
               {"sentence": "Tu pleures ? Non, je fais une réaction allergique à ta tête",
                "Sujet": ("Tu", "je"),
                "Verbe": ("pleures ?", "fais"),
                "Complément": ("une réaction allergique", "à ta tête"),
                "Liaison" : ("Non,",)
                },
               {"sentence": "Je t'aurai bien passé mon miroir mais je ne voudrais pas que tu fasses des cauchemars",
                "Sujet": ("Je", "je", "tu"),
                "Verbe": ("t'aurai", "ne voudrais pas que", "fasses"),
                "Complément": ("bien passé mon miroir", "des cauchemars"),
                "Liaison" : ("mais",)
                },
               {"sentence": "Tu n'as peut-être aucune ride mais tu restes ridicule.",
                "Sujet": ("Tu", "tu"),
                "Verbe": ("n'as", "restes"),
                "Complément": ("peut-être aucune ride", "ridicule"),
                "Liaison" : ("mais",)
                },
               {"sentence": "Tu sors avec mon ex ? Je mange une pomme, tu veux manger le trognon ?",
                "Sujet": ("Tu", "tu", "Je"),
                "Verbe": ("sors", "mange", "veux manger"),
                "Complément": ("avec mon ex", "une pomme", "le trognon ?"),
                "Liaison" : ("?", ",")
                },



    ],
         }


"""
# preset ton add insults

               {"sentence": "Blalalalalalalalal",
                "Sujet": (),
                "Verbe": (),
                "Complément": (),
                "Liaison" : ()
                },


"""
