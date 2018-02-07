from scop2db import *

"""
Test poprawności funkcji oraz sprawdzenie czasu wykonania (Zalezne od polaczenia internetowego):
Jako iż dane muszę pobierać ze strony SCOP2 nie posiadam ich lokalnie, a polega to pobieraniu 
z danych URL potrzebnych informacji, testy poprawności wypisu są sprawdzone także ręcznie.
"""

"""
Pobieranie domain id z hierarchi IR - InterRelationShip
"""

for line in scop2_get_interrelationship_id():
    print(line)

"""Len"""
get_interrelationship_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/IR_scop2dom_20140205.aa")


scop2_IR_id_count = len(scop2_get_interrelationship_id())
print(scop2_IR_id_count)