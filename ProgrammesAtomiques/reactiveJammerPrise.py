import StaticJammer as sj
import spectogram as spect
import staticJammerWide as sjw
import sys

import time

sys.path.insert(0, '/home/ah/Documents/telecom/Cours20232024/PROJ104/applejam/ProgrammesAtomiques')



max_freq_enregistree = spect.max_freq(RXLO=int(2458e6), samples=2000, affichage=True)[0]

print(max_freq_enregistree)


link = "ip:192.168.2.1"

sj.emettre(center_freq=max_freq_enregistree, lien = link)
# sjw.emission(sample_rate=30e6,center_freq=max_freq_enregistree,lien = link)
