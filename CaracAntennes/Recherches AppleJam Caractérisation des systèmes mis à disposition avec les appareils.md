# Recherches AppleJam Caractérisation des systèmes mis à disposition avec les appareils

## Caractérisation des antennes utilisées pour contrôler les appareils

+ Pour l'antenne du drone Snaptain S5C
    + Fonctionne pour des fréquences entre 2430 et 2475 MHz
    + Antenne monopôle fil de 2,5cm
    + Pour nous on a 
    $$ 
    \lambda = 0,125 m 
    $$
    donc la longueur de l'antenne est égale à 0,2 Lambdas, ce qui permet un diagramme de rayon indépendant de l'angle (ie le diagramme de rayonnement à le même gain dans toutes les directions horizontales), d'où rayonnement omnidirectionnel.
    Mais efficacité << 50%
    + D'autres drones vont utiliser des protocoles sans fil spécifiques (Wi-Fi, Zigbee), qui ont du frequency-hopping donc plsu compliqué à brouiller
    + 3,7 dBi rayonné pour l'antenne, à vérifier avec Pluto

+ Pour voiture (pas encore présente ici)
    + Fréquences possibles : 27 MHz, 49 MHz, 72 MHz, 2,4 GHz (la plus probable)
    + AM ou FM ?
        + Spread-spectrum radio system

+ Pour l'antenne du drone 


+ Smart plug
    + De manière générale :

        + Besoin de <1MHz de bande-passante
        + UE : 868MHz
        + US : 915 MHz
        + Standard LoRa pour l'IoT

    + Pour la prise concernée en particulier :
        + Fonctionne à 433.92MHz
        + Puissance <10mW

+ Drone Kidomo F02

    + Fréquence d'émission : 2437 MHz


+ Clé Citroën C1
    + Fréquence de fonctionnement : 433.94MHz
    + Puissance : 11dB pour la clé à 20cm du récepteur
    + Modulation : ASK

