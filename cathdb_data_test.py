from cathdb import *

print(get_catch_versions())
#
#
print("version 4_2_0")
print(get_protein_domain_id_list()[0:50])

for x in get_protein_chain_id_list(version="4_2_0", chain_character="A")[0:20]:
    print(x["domain_name"], end = " ")
print()

print(get_protein_pdb_id_list())

# for x in get_id_domain_short_description(version="4_2_0", id_domain="4ayoA00"):
#     print(x)

#
#
print("version 3_5_0")
print(get_protein_domain_id_list(version="3_5_0")[0:50])

for x in get_protein_chain_id_list(version="3_5_0", chain_character="A")[0:20]:
    print(x["domain_name"], end = " ")
print()

print(get_protein_pdb_id_list(version="3_5_0"))


# get_id_domain_full_description(version = "4_2_0", id_domain = "2ynzC01")

cath_download_pdb_id(version="4_1_0", pdb_id="2zjp", save_file_path="C:/Users/zerg/Downloads/")

cath_download_domain_id(version="4_1_0", domain_id="2zjpS01", save_file_path="C:/Users/zerg/Downloads/")

cath_download_chain_id(version="4_1_0", chain_id="101mA00", save_file_path="C:/Users/zerg/Downloads/")

cath_download_pdb_id(version="4_0_0", pdb_id="2c9v", save_file_path="C:/Users/zerg/Downloads/")

cath_download_domain_id(version="4_0_0", domain_id="3friA01", save_file_path="C:/Users/zerg/Downloads/")

cath_download_chain_id(version="4_0_0", chain_id="111lA00", save_file_path="C:/Users/zerg/Downloads/")

cath_download_pdb_id(version="4_0_0", pdb_id="1c6y", save_file_path="C:/Users/zerg/Downloads/")

cath_download_domain_id(version="4_0_0", domain_id="1oksA00", save_file_path="C:/Users/zerg/Downloads/")

cath_download_chain_id(version="4_0_0", chain_id="2yyuA00", save_file_path="C:/Users/zerg/Downloads/")
