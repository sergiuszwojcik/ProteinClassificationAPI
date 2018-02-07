from scop2db import *
import time

"""
Test poprawności funkcji oraz sprawdzenie czasu wykonania (Zalezne od polaczenia internetowego):
Jako iż dane muszę pobierać ze strony SCOP2 nie posiadam ich lokalnie, a polega to pobieraniu
z danych URL potrzebnych informacji, testy poprawności wypisu są sprawdzone także ręcznie.
"""

"""
Pobieranie domain id z hierarchi IR - InterRelationShip
"""

"""
http://scop2.mrc-lmb.cam.ac.uk/downloads/IR_scop2dom_20140205.aa
Strona do sprawdzenia poprawnosci danych
ilosc linijek 416 pakuje po 2 liniki w 1 wiec
416/2 = 208
"""
page_data_lenght = 208
start_time = time.time()
for line in scop2_get_interrelationship_id():
    print(line)
print("--- %s seconds ---\n" % (time.time() - start_time))
"""Len powinno miec dlugosc 208"""

scop_id_count = len(scop2_get_interrelationship_id())
print("Porównaj ilosc danych:")
print(scop_id_count == page_data_lenght)
print("\n")

"""
Pobieranie domain id z hierarchi SP - Protein Species
Strona do sprawdzenia poprawnosci danych
http://scop2.mrc-lmb.cam.ac.uk/downloads/PR_scop2dom_20140205.aa
"""

page_data_lenght = 780
start_time = time.time()
for line in scop2_get_protein_species_id():
    print(line)
print("--- %s seconds ---\n" % (time.time() - start_time))
"""Len powinno miec dlugosc 780"""

scop_id_count = len(scop2_get_protein_species_id())
print(scop_id_count)
print("Porównaj ilosc danych:")
print(scop_id_count == page_data_lenght)
print("\n")

"""
Pobieranie domain id z hierarchi PR - Protein
Strona do sprawdzenia poprawnosci danych
http://scop2.mrc-lmb.cam.ac.uk/downloads/PR_scop2dom_20140205.aa
"""

page_data_lenght = 634
start_time = time.time()
for line in scop2_get_proteins_id():
    print(line)
print("--- %s seconds ---\n" % (time.time() - start_time))
"""Len powinno miec dlugosc 634"""

scop_id_count = len(scop2_get_proteins_id())
print(scop_id_count)
print("Porównaj ilosc danych:")
print(scop_id_count == page_data_lenght)
print("\n")


"""
Pobieranie domain id z hierarchi FA - Family
Strona do sprawdzenia poprawnosci danych
http://scop2.mrc-lmb.cam.ac.uk/downloads/FA_scop2dom_20140205.aa
"""

page_data_lenght = 599
start_time = time.time()
for line in scop2_get_families_id():
    print(line)
print("--- %s seconds ---\n" % (time.time() - start_time))
"""Len powinno miec dlugosc 599"""

scop_id_count = len(scop2_get_families_id())
print(scop_id_count)
print("Porównaj ilosc danych:")
print(scop_id_count == page_data_lenght)
print("\n")

"""
Pobieranie domain id z hierarchi SF - SuperFamily
Strona do sprawdzenia poprawnosci danych
http://scop2.mrc-lmb.cam.ac.uk/downloads/SF_scop2dom_20140205.aa
"""

page_data_lenght = 481
start_time = time.time()
for line in scop2_get_super_families_id():
    print(line)
print("--- %s seconds ---\n" % (time.time() - start_time))
"""Len powinno miec dlugosc 481"""

scop_id_count = len(scop2_get_super_families_id())
print(scop_id_count)
print("Porównaj ilosc danych:")
print(scop_id_count == page_data_lenght)
print("\n")


"""
Pobieranie domain id z hierarchi CF - Fold
Strona do sprawdzenia poprawnosci danych
http://scop2.mrc-lmb.cam.ac.uk/downloads/CF_scop2dom_20140205.aa
"""

page_data_lenght = 606
start_time = time.time()
for line in scop2_get_fold_id():
    print(line)
print("--- %s seconds ---\n" % (time.time() - start_time))
"""Len powinno miec dlugosc 606"""

scop_id_count = len(scop2_get_fold_id())
print(scop_id_count)
print("Porównaj ilosc danych:")
print(scop_id_count == page_data_lenght)
print("\n")


"""
Pobieranie wszystkich node names
Strona do sprawdzenia poprawnosci danych
http://scop2.mrc-lmb.cam.ac.uk/downloads/scop2_nodes_names_20140205
"""

page_data_lenght = 1994 # po odjeciu 6 linijek naglowka i pustej random linii w bazie
start_time = time.time()
for line in scop2_get_nodes_names():
    print(line)
print("--- %s seconds ---\n" % (time.time() - start_time))
"""Len powinno miec dlugosc 1994"""

scop_id_count = len(scop2_get_nodes_names())
print(scop_id_count)
print("Porównaj ilosc danych:")
print(scop_id_count == page_data_lenght)
print("\n")


"""
Testowanie danych
Strona do sprawdzenia poprawnosci danych
http://scop2.mrc-lmb.cam.ac.uk/downloads/scop2_nodes_names_20140205
"""
"""
Dane do testu
6000113	MJ_0490
6000157	TM_1834
6000502	Plafa_LDH
6000090	Clote_LDH
6000106	Hs_LDHA
6000107	Hs_LDHB
6000356	Plabe_MDH
6000361	Toxgo_MDH
6000492	Lacpe_MDH
6000493	Pig_MDH
6000495	Mm_LDH
6000498	Squac_LDH
6000504	Bst_LDH
Bledne dane powinny dac False
6000495	Pig_MDH
6000498	SHs_LDHB
6000504	Squac_LDH
"""
start_time = time.time()
print("sprawdzanie poprawnosci zwracanych danych POWINNO DAC TRUE")
print(scop2_get_nodes_names_by_id(6000113) == "MJ_0490")
print(scop2_get_nodes_names_by_id(6000157) == "TM_1834")
print(scop2_get_nodes_names_by_id(6000502) == "Plafa_LDH")
print(scop2_get_nodes_names_by_id(6000090) == "Clote_LDH")
print(scop2_get_nodes_names_by_id(6000106) == "Hs_LDHA")
print(scop2_get_nodes_names_by_id(6000107) == "Hs_LDHB")
print("sprawdzanie poprawnosci zwracanych danych POWINNO DAC FALSE")
print(scop2_get_nodes_names_by_id(6000495) == "Pig_MDH")
print(scop2_get_nodes_names_by_id(6000498) == "Plafa_LDH")
print(scop2_get_nodes_names_by_id(6000504) == "SHs_LDHB")
print("--- %s seconds avg---\n" % ((time.time() - start_time)/9))
print("\n")

"""
Testowanie danych
Strona do sprawdzenia poprawnosci danych
http://scop2.mrc-lmb.cam.ac.uk/graph/restapi/domain?id=" + "domain_id"

Dane zostały zweryfikowane ręcznie
"""
print("Test pobierania informacji")
for x in scop2_get_domain_data_by_domain_id("PR-8004118-1S70B"):
    print(x['id'])
    print(x['node'])
    print(x['segments'])
print()

for x in scop2_get_domain_data_by_domain_id("IR-8003982-1D5YA"):
    print(x['id'])
    print(x['node'])
    print(x['segments'])
print()

for x in scop2_get_domain_data_by_domain_id("SF-8004171-2YVIA"):
    print(x['id'])
    print(x['node'])
    print(x['segments'])
print()

print()

"""
Klasyfikacja białek + weryfikacja trzeba odpalic strone z grafem danego białka
http://scop2.mrc-lmb.cam.ac.uk/graph/#/GEc0/ZDES/vyJmguhk.dat#1#is_a,part_of,occurred_in 
"""
print()
print("Test białek porownywane ze strona SCOP2 graf")

for x in scop2_get_PR_protein_classification_by_protein_pdb_code("1VL6"):
    print(x)

for x in scop2_get_PR_protein_classification_by_protein_pdb_code("1PQW"):
    print(x)

for x in scop2_get_PR_protein_classification_by_protein_pdb_code("1UDC"):
    print(x)

for x in scop2_get_PR_protein_classification_by_protein_pdb_code("1OAA"):
    print(x)

for x in scop2_get_PR_protein_classification_by_protein_pdb_code("1ZMT"):
    print(x)

for x in scop2_get_PR_protein_classification_by_protein_pdb_code("1DHR"):
    print(x)

for x in scop2_get_PR_protein_classification_by_protein_pdb_code("1NP3"):
    print(x)

for x in scop2_get_PR_multiple_protein_classification_by_protein_pdb_code(["1VL6","1PQW","1UDC","1OAA","1ZMT","1DHR"]):
    print(x)

