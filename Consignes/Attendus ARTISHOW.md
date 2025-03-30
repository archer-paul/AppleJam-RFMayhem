# Attendus ARTISHOW

## Attendus mi-projet :



+ Développement d'un modèle de la chaîne d'émission/réception en Python/Matlab
    + Mise en équation du E propageant l'information (28/02/2024) [Fait]
    + Déterminer puissance & forme du signal reçu par l'appareil (20/03/2024) [Fait]
        + Voir ce qu'il se passe en ajoutant des paramètres dans l'environnement (ex : obstacles) [Fait]
    + Visualisation (02/04/20240) [Fait.] 
+ Prise en main de la plateforme Pluto et automatiser son contrôle
    + Découverte / Prise en main de l'API de Pluto (14/02/2024) [Fait]
    + Émission de signaux simples avec l'API (sinus, créneau, ...) (26/03/2024) [Fait]
    + Réceptionner des signaux émis par les controlleurs de l'appareil et les analyser (26/03/2024) [Fait]
    + Émettre un signal dès que Pluto détecte un signal spécifique automatiquement (09/04/2024)
+ Caractérisation des systèmes (Voitures, drones, ...) mis à disposition avec la plateforme Pluto ou avec des instruments de mesure de laboratoire
    + Caractérisation des antennes utilisées pour contrôler les appareils (28/02/2024) [Fait]
    + Caractérisation des antennes des appareils et de la puissance qu'ils reçoivent (13/03/2024) [Fait]
    + Faire les diagrammes de rayonnement avec la Pluto (02/04/2024) 
+ État de l'art des techniques de brouillage 
    + Étudier les techniques de brouillage (02/04/2024) 
    + Déterminer 2 techniques utilisables de brouillage (13/03/2024) [Fait]


## Attendus fin de projet :

+ Démonstration de plusieurs techniques de brouillage
    + Rejouer une séquence envoyée par une manette (Maëliss, Amine, Paul)
    + Blocage du signal entre commande et appareil (appareil de base : prise connectée, voiture, drone) (Maëliss, Amine, Paul)
    + Blocage des stores (07/05/2024)
    + Prise de contrôle des clés de voiture (24/06/2024)

+ Caractérisation dans plusieurs configurations 
    + Test de prise de contrôle à longue distance (~10m max) des appareils de base 
    + Efficacité du blocage dans des environnements problématiques (ex : dans le parking de Télécom pour les voitures)
    + Test de la prise de contrôle dans un environnement réel (avec appareils parasites)
    + Vérifier que le blocage n'interfère pas avec d'autres signaux électromagnétiques



+ Tâches à réaliser d'ici la fin du projet :
    + Envoyer un message simple (text string) d'une Pluto à une autre (Maëliss, Amine, Paul, 02/05/2024)
    + Rejouer une séquence envoyée par une manette/télécommande (Maëliss, Amine, Paul, 15/05/2024)
    + Refaire le logiciel de modélisation (Alexander, Thomas, )
    + Caractériser tous les appareils susceptibles d'être brouillés - trouver fréquence de fontionnement et puissance reçue de la télécommande des stores et des clés de voiture (Alexander, Thomas, 02/05/2024)
    + Prise de contrôle de clés de voiture pour ouvrir une voiture (24/06/2024)




## Planification de la dernière semaine

+ 24/06/2024 :
    Spot jammer (donner en entrée une fréquence à un programme, il émet un signal statique à cette fréquence ) (Maeliss & Thomas -> 8h30 - 17h)
        + S'assurer qu'on sache émettre un signal OK-
        + Savoir émettre des signaux avec la Pluto OK--
        + Programme prend en entrée une fréquence
        + Il émet en sortie un signal de bande passante maximale avec comme fréquence centrale la f en entrée
    Bibliothèque des différents types types de modulation en temporel et sur des spectrogrammes (Paul -> 8h30 - 17h)
        + Savoir recevoir des signaux et les sauvegarder
        + Savoir faire un spectrogramme d'un signal
        + Analyser les différences entre les signaux temporels et fréquentiels des différents types de modulation

+ 25/06/2024 :
    Écouter l'environnement et rejouer des séquences (Amine) OK----
        + Savoir enregistrer des séquences temporelles OK+
        + Savoir émettre des séquences précises sur la Pluto : Pas du tout

+ 26/06/2024 :
    Reactive Jammer (Alexander)
        + Savoir générer un spectrogramme d'un signal OK+
        + Savoir identifier une fréquence qui a un gain plus élevé que la moyenne OK
        + Savoir émettre un signal bloqueur à cette fréquence OK

+ 27/06/2024 :
    Essayer d'ouvrir les voitures en rejouant les signaux des clefs (Tout le monde, mais probablement ne va pas être réalisé) 
        + Même capacité que pour la prise de contrôle du drone