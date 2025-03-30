# Suivi de la progression du projet

+ 09/02/2024
    + Création du planning jusqu'à mi-semestre & répartition des tâches
    + Paul & Amine : Lecture de documentation de la plateforme Pluto et prise en main de la plateforme
    + Maëliss : Lecture d'articles sur les techniques de brouillage du signal
    + Alexander : Recherche et caractérisation de l'antenne du drone Snaptain S5C fourni 
    + Thomas : Travail sur la modélisation de la chaîne d'émission/réception des signaux EM 

+ 28/02/2024
      + Rendu du planning avec Mr Jabbour qui a validé ce dernier + nous a conseillé de nous intéresser à la doc des objets que l'on souhaite brouiller
      + Présentation de l'utilisation du logiciel par Mr Jabbour (Jouer sur la freq d'echantillonage, le gain, la distance entre les antennes etc)
      + Amine : Résolution problème de compatibilité HorNDIS avec ma version mac Sonoma 14.3
      + Paul : Résolution problème terminal qui ne s'ouvrait pas sur VM Ubuntu 18 ( résolu via une réinstallation complète d'une nouvelle VM)
      + Thomas : Avancee sur la modelisation, resolution de bug (evident).
      + Alexander : Recherche de caractéristiques sur les appareils de base ; fin de recherche sur la prise, début de recherche sur le drone Kidomo F02
      + Amine : Impossibilité d'utilser HorNDIS, résolution du problème avec Mr Pham en utilisant "Screen" en tant qu'alternative.
      + Maeliss : malade

+ 13/03/2024
    + Paul : Visualisation avec Alexander de la fréquence de la commande on/of de la prise connectée sur l'application IIO. 
    + Alexander : configuration de la plateforme Pluto & de l'osc, réception & identification du signal d'activation d'une prise
    + Amine : Résolution problème installation de l'oscilloscope, incapacité de passer par l'installation fourni par la documentation "error : Error: Failed to load cask: ./gtkdatabox-prev1.rb Cask 'gtkdatabox-prev1' Résolution en installant tout les fichiers un à un et en modifiant le contenu de certains d'entre eux.
    + Thomas : Fin mise en équation + programme de modélisation global, début animation
    + Maeliss : lecture de docs sur différentes méthodes de brouillage

+ 20/03/2024
    + Paul : Correction des (nombreux) bugs liés à la VM avec Tarik. Prise en main de l'API python de Pluto. J'arrive maintenant à recevoir des signaux avec Python. 
    + Maeliss : lecture de docs sur différentes méthodes pour se sauver d'un brouilleur / se battre contre
    + Alexander : Brouillage manuel du signal de la prise connectée, premières émissions / réceptions faites via Python, modifications des échéances à mi-semestre pour refléter la réalité du projet & mise à jour des tâches déjà faites. 
        Liens utiles :
        + Vision fréquentielle en live via PlutoSDR (appli CLI) : https://github.com/r4d10n/retrogram-plutosdr
        + Spectrogramme via PlutoSDR : https://github.com/jorgejc2/PlutoSDR/tree/master
    + Amine: malade    
    + Thomas : Fin animation + reglage bug des obstacle, decouverte pb conditions aux bords et reglage partiel du pb.

+ 26/03/2024
    + Maeliss : lecture de doc sur DoS (denial of service)
    + Maeliss : Continué de lire les docs, quasi fini
    + Thomas : Fin première version du prgm de modélisation, pb conditions au bord limités. Prise de conscience du probleme avec les conditions initiales concernant la dérivée du champ électrique. Idee de résolution : trouver la bonne valeur pour une sinusoïde simple, puis décomposer le champ initial en série de fourier, et prier pour que le facteur entre dérivée et champ soit une constante.
    + Paul : Correction de nombreux bug liés à ma VM et à l'API python grâce à Alexander.
    + Alexander : Développement d'un programme permettant de tracer les diagrammes de rayonnement avec la Pluto ; pour l'instant j'arrive à récupérer la puissance d'une fréquence donnée au cours du temps et à tracer le graphique correspondant
    + Amine : Je pouvais recevoir des signaux mais pas en transmettre, c'est dorénavant possible, je dois maintenant réussir à faire les deux simultanément, à savoir transmettre et recevoir des signaux en même temps.

+ 02/04/2024
    + Paul : Mise en oeuvre d'un script pour connaitre le taux de transmission maximal du cable USB reliant la Pluto à l'ordinateur. On observe qeu lorsque le sample rate commandé à la Pluto est trop élevé, tous les signaux ne parviennnent pas à l'ordinateur. Ajout de deux scripts python permettant à deux plutos différentes de communiquer et de tracer les graphes des signaux obtenus.
    + Thomas : aide a Alexander + on commence a quelle antenne a quelle frequence pout tel dipositif
    + Alexander : Fin de réalisation du programme pour réaliser les diagrammes de réception des dispositifs avec la Pluto. Si on a accès aux bancs tournants des salles de TP de COM, on pourra réaliser les diagrammes de rayonnement
    + Amine : Impossibilité d'utiliser l'oscilloscope suite à une mise à jour. Impossibilité d'utiliser VirtualBox car Puce M2 incompatible et version béta tester ne fonctionne pas correctement.Réinstallation complète de toutes les librairies et OS via Parallels Desktop.
    + Maeliss : lecture des docs

+ 09/04/2024
    + Thomas : Installation du logiciel pour utiliser la pluto sur mon pc, et recherche de la fréquence de transmission du drone. Idée : Faire une aquisition du spectre entre 2350 et 2500MHz sur 1 min avec et sans le drone, puis tracer sur un graph le max des amplitudes pour chacune des fréquences, si un pic existe avec le drone, mais n'existe pas sans, on aura trouvé (surement) une fréquence de transmission du drone
    + Amine : Résolution d'un problème m'empéchant de lancer l'oscilloscope avec Mr Graba et explication de la raison pour laquelle l'application me demande un mot de passe à chaque lancement. Début création d'un code permettant de récuperer et afficher les données qui nous intéressent pour re-synthéthiser un signal identique à celui reçu dans le but de pouvoir reconstituer tous les signals qui nous intéresseront à l'avenir. Début réflexion avec Paul sur les diapos et le contenu que nous allons présenter à l'évaluation intermédiaire.
    + Maeliss : terminé de lire docs sur DoS
    + Paul : Résolution de nouveaux problèmes sur la VM grâce à l'intervention de Tarik. Lecture de la documentation sur l'implémentation de la fft en python. Réflexion avec Amine sur le contenu des diapos à préparer pour l'évaluation intermédiare. 
    + Alexander : Rectification du code de spectrogramme. Le drone kidomo f02 fait du frequency hopping autour de la fréquence de communication annoncée, tracer le diagramme d'émission pour la manette va être difficile. 

+ 24/04/2024
    + Tout le monde : Point sur l'avancement du projet et l'attribution des tâches en fonctions des attendus de fin de projet.
    + Amine : Développement de scripts permettant de communiquer entre 2 plutos (1 script émetteur et 1 script récépteur).
    + Alexander + Thomas : recherche de la fréquence (a priori a 2,4GHz) de la télécommande des stores, et on a regardé de la doc pour les clés de la voiture, AMDR angel
    
+ 02/05/2024
    + Alexander & Thomas : on a déterminé la fréquence de transmission de l'interrupteur, on cherche à extraire le signal utile du signal enregistré
    + Paul : Travail et lecture de documentation pour reproduire une radio AM et/ou FM afin de pouvoir communiquer entre deux Pluto.
    + Maeliss : installation de la VM sur pc portable

+ 07/05/2024
    + Paul : Ajout d'un script qui permet de passer d'une chaine de caractères à une séquence de bits. La séquence de bits module en amplitude une porteuse (ScriptEmeteurAM). ScriptRecepteurAM permet ensuite de récupérer la chaîne de caractère y compris s'il y a quelques erreurs. Débuts d'un script de modulation FM-QSPK
    + Alexander & Thomas : réalisation d'un programme d'analyse d'un signal à un instant t en temps & en fréquence + début du code du spectrogramme
    + Maeliss : tentative d'installation de bibliothèques sur la VM du pc portable mais échec donc passage sur ordinateurs de l'école
    
+ 15/05/2024
    + Paul : Decouverte d'un grand nombre d'erreurs lors d'une transmission via le code AM. Création d'un script AM Binary pour visualiser le nombre de bits changés par le canal
    + Maeliss : abandon de la VM et passage sur ordinateur école 
    + Alexander : travail sur spectrogram_signal : visualisaiton plus précise du spectrogramme avec les valeurs pour chaque fréquence

+ 22/05/2024
    + Alexander & Thomas : fin de la réalisation du spectrogramme & détermination du type de modulation sur le drone Kidomo F02 : FSK, début du travail de récupération des données sur une modulation de ce type
    + Paul : Essais (infructueux) de comprendre pourquoi les scripts emissions et réception ne marchent pas. Ce qu'on obtient s'apparente plus à du bruit qu'autre chose.

+ 29/05/2024
    + Paul : Présentation et audit des différents groupe. Nous avons pu récolter lors de nos deux présentations des remarques intéressantes que ce spoit sur notre organisation ou sur différentes idées que nous pourront implémenter (si nous avons le temps).
    + Alexander : Présentation de l'audit d'AppleJam & audit des projets synthese-image-2, threshold encryption
    + Maëliss : présentation de l'audit AppleJam et audit des projets swarm-rescue et sportsmate
    + Thomas : j'ai travaillé avec Alexander sur le premier audit, et sinon on a tous fait la séance normalement

+  05/06/2024
    + Thomas : On a essayé de brouiller la télécommande avec Alexander. On a rapidement eu des problemes, ce qui fait qu'on a pas beaucoup avancé. En fait on avait du mal a détecter sur nos spectrogramme la trace laissée par la télécommande. Ensuite, Paul et Maeliss ont eu des problemes. On s'est dit qu'on allait les régler ensemble, en essayant de faire une communication basique, avec 2 plutos, une émétant, une autre recevant. On y arrivait pas, on a progressivement éliminé les sources d'erreurs, en changeant les fréquences de transmission. Ca nous a pris beaucoup de temps, car pour chaque fréquence à laquelle on essayait de transmettre, il y avait déja des appareils qui émétait, donc on n'arrivait pas a savoir si on y arrivait ou pas. Apres beaucoup de temps, on s'est rendu compte qu'il y avait un problème à l'émission. Une fois mis a 2 cm l'antenne d'émission de l'antenne de réception, on s'est rendu compte qu'on y arrivait, mais que la puissance était trop faible. On a voulu changer de pluto pour avoir plus de puissance, sauf que cette 3e n'arrivait pas a se connecter au pc de Paul, et cela nous a pris jusqu'a la fin de la séance.
    + Paul : Explications très instructives avec Germain sur les différentes modulation AM et FM. On essaye avec Alexander d'émettre un signal modulé AM et PM et d'observer les différences dans le spectrogramme. Echec cuisant. On s'aperçoit que le signal émis par ma Pluto est extrêmement faible. J'essaye de changer de Pluto mais les deux autres Pluto ne sont pas détectées par mon ordinateur. Pourquoi ? Nous n'en avons pas la moindre idée. Lorsqu'on entre ifconfig dans le terminal, mon ordi ne les détecte pas. J'ai donc une seule Pluto qui fonctionne avec mon ordi : la 2024 Plt 3/. 
    + Maeliss : mêmes observation que Paul car travail en binôme. Tentative de travail sur PC de l'école, mais la bibliothèque adi ne marchait pas, et je n'étais pas sudoers...
    + Alexander : Travail sur la génération du spetrogramme et sur son exploitation pour mettre en place un reactive jammer

+ 12/06/2024 :
    + Alexander : Élaboraiton du programme de fin de projet et réparation du spectrogramme
    + Maeliss : réalisation du poster
    + Paul : Connection de la Pluto sur les machines de l'école grâce à Germain. Utilisation grâce à l'interface USB obligatoire. Essai de communication entre deux Plutos (une connectée à mon PC portable et une autre connectée à la machine de l'école). Le signal reçu n'est pas le même que le signal émis (ce à quoi on s'attendait) mais -plus problématique- la fréquence centrale d'émission n'apparait même pas sur le spectrogramme.
    + Maeliss : réalisation du poster
    + Thomas : Démarage du plan "Atomisation", son objectif ? : Rendre toutes les taches non élémentaires élémentaires en créant des fichier qui executent ces actions non élémentaire. Exemple : Avoir un programme prenant en entrée un signal, et qui construit le spectrogramme de se signal. Un autre fichier d'émission, un autre de récepetion etc etc, afin de facilite grandement les taches pdt le sprint final

+ 24/06/2024 :
    + Alexander : Élaboration d'un première version d'un reactive jammer qui marche sur la prise connectée
    + Thomas & Maëliss : On a rempli notre contrat, on a réussi a brouiller la prise. En revanche, impossible de la controler a partir de notre ordinateur. On a fait un programme qui écoute l'environnement, puis qui réémet. Le problème c'est que le signal est détérioré, et donc quand on réémet, la prise ne détecte pas le signal. A priori, ce n'est pas un problème de puissance étant donné qu'avec un ampli 13dBm, on n'y parvient pas non plus.


+ 25/06/2024 :
    + Alexander : Tentative de brouillage du drone via receptive jammer avec blocage d'une fréquence : échec
    