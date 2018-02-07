from cathdb import *
import time

start_time = time.time()
print("Catch versions")
print(get_catch_versions())
print("--- %s seconds ---" % (time.time() - start_time))
print()

print("version 4_2_0")
print("get protein domain id list:")
start_time = time.time()
print(get_protein_domain_id_list()[0:50])
print("--- %s seconds ---" % (time.time() - start_time))
print()
print("get protein chain ids list:")
test_list = []
start_time = time.time()
for x in get_protein_chain_id_list(version="4_2_0", chain_character="A")[0:20]:
    test_list.append(x["domain_name"])
    # print(x["domain_name"])
print("--- %s seconds ---" % (time.time() - start_time))
print(test_list)
print()

print("get protein pdb_id list")
start_time = time.time()
print(get_protein_pdb_id_list())
print("--- %s seconds ---" % (time.time() - start_time))
print()
# for x in get_id_domain_short_description(version="4_2_0", id_domain="4ayoA00"):
#     print(x)

#
#
print("version 3_5_0")
print("get protein domain id list:")
start_time = time.time()
print(get_protein_domain_id_list(version="3_5_0")[0:50])
print("--- %s seconds ---" % (time.time() - start_time))
print()
print("get protein chain ids list:")
test_list = []
start_time = time.time()
for x in get_protein_chain_id_list(version="3_5_0", chain_character="A")[0:20]:
    test_list.append(x["domain_name"])
    # print(x["domain_name"])

print(test_list)
print("--- %s seconds ---" % (time.time() - start_time))
print()

print("get protein pdb_id list")
start_time = time.time()
print(get_protein_pdb_id_list(version="3_5_0"))
print("--- %s seconds ---" % (time.time() - start_time))
print()

# get_id_domain_full_description(version = "4_2_0", id_domain = "2ynzC01")
start_time = time.time()
while (True):
    try:
        cath_download_pdb_id(version="2_6_0", pdb_id="2bcx", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_domain_id(version="2_6_0", domain_id="1kyiF2", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_chain_id(version="2_6_0", chain_id="12e8L0", save_file_path="C:/Users/zerg/Downloads/")
        break
    except Exception:
        print("Version 2_6_0 Something gone wrong. CATHDB Api works only for version 4_0_0, 4_1_0, 4_2_0")
        break
print("--- %s seconds version 2_6_0---\n" % (time.time() - start_time))

start_time = time.time()
while (True):
    try:
        cath_download_pdb_id(version="3_5_0", pdb_id="2zjp", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_domain_id(version="3_5_0", domain_id="2zjpS01", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_chain_id(version="3_5_0", chain_id="101mA00", save_file_path="C:/Users/zerg/Downloads/")
        break
    except Exception:
        print("Version 3_5_0 Something gone wrong. CATHDB Api works only for version 3_5_0 4_0_0, 4_1_0")
        break
print("--- %s seconds version 3_5_0---\n" % (time.time() - start_time))

start_time = time.time()
while (True):
    try:
        cath_download_pdb_id(version="3_0_0", pdb_id="1v8h", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_domain_id(version="3_0_0", domain_id="1mn3A00", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_chain_id(version="3_0_0", chain_id="101m000", save_file_path="C:/Users/zerg/Downloads/")
        break
    except Exception:
        print("Version 3_0_0 Something gone wrong. CATHDB Api works only for version 4_0_0, 4_1_0, 4_2_0")
        break
print("--- %s seconds version 3_0_0---\n" % (time.time() - start_time))

start_time = time.time()
while (True):
    try:
        cath_download_pdb_id(version="3_4_0", pdb_id="2zjp", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_domain_id(version="3_4_0", domain_id="2zjpS01", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_chain_id(version="3_4_0", chain_id="101mA00", save_file_path="C:/Users/zerg/Downloads/")
        break
    except Exception:
        print("Version 3_4_0 Something gone wrong. CATHDB Api works only for version 3_5_0 4_0_0, 4_1_0")
        break
print("--- %s seconds version 3_5_0---\n" % (time.time() - start_time))

start_time = time.time()
while (True):
    try:
        cath_download_pdb_id(version="4_2_0", pdb_id="2bcx", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_domain_id(version="4_2_0", domain_id="1t6oA00", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_chain_id(version="4_2_0", chain_id="2yz7A00", save_file_path="C:/Users/zerg/Downloads/")
        break
    except Exception:
        print("Version 4_2_0 Something gone wrong. CATHDB Api works only for version 3_5_0 4_0_0, 4_1_0")
        break
print("--- %s seconds version 4_2_0---\n" % (time.time() - start_time))

start_time = time.time()
while (True):
    try:
        cath_download_pdb_id(version="4_1_0", pdb_id="1qtr", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_domain_id(version="4_1_0", domain_id="1oaiA00", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_chain_id(version="4_1_0", chain_id="2yytA00", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_pdb_id(version="4_0_0", pdb_id="2c9v", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_domain_id(version="4_0_0", domain_id="3friA01", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_chain_id(version="4_0_0", chain_id="111lA00", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_pdb_id(version="4_0_0", pdb_id="1c6y", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_domain_id(version="4_0_0", domain_id="1oksA00", save_file_path="C:/Users/zerg/Downloads/")

        cath_download_chain_id(version="4_0_0", chain_id="2yyuA00", save_file_path="C:/Users/zerg/Downloads/")
        break
    except Exception:
        print("Something gone wrong. CATHDB Api works only for version 3_5_0 4_0_0, 4_1_0")
        break
print("--- %s seconds version 4_2_0---\n" % (time.time() - start_time))

"""
Testing domain_id information recieving
"""

start_time = time.time()
while True:
    try:
        print(get_id_domain_short_description(version="4_2_0", id_domain="2ynzC01"))
        print(get_id_domain_short_description(version="4_2_0", id_domain="1oaiA00"))
        print(get_id_domain_short_description(version="4_2_0", id_domain="1wvfA04"))

        break
    except Exception:
        print("Something gone wrong")
print("--- %s seconds version 4_2_0---\n" % (time.time() - start_time))

start_time = time.time()
while True:
    try:
        print(get_id_domain_short_description(version="4_1_0", id_domain="2ynzC01"))
        print(get_id_domain_short_description(version="4_1_0", id_domain="1oaiA00"))
        print(get_id_domain_short_description(version="4_1_0", id_domain="1wvfA04"))

        break
    except Exception:
        print("Something gone wrong")
print("--- %s seconds version 4_1_0---\n" % (time.time() - start_time))

start_time = time.time()
while True:
    try:
        print(get_id_domain_short_description(version="4_0_0", id_domain="2ynzC01"))
        print(get_id_domain_short_description(version="4_0_0", id_domain="1oaiA00"))
        print(get_id_domain_short_description(version="4_0_0", id_domain="1wvfA04"))

        break
    except Exception:
        print("Something gone wrong")
print("--- %s seconds version 4_0_0---\n" % (time.time() - start_time))

start_time = time.time()
while True:
    try:
        print(get_id_domain_short_description(version="3_5_0", id_domain="2ynzC01"))
        print(get_id_domain_short_description(version="3_5_0", id_domain="1oaiA00"))
        print(get_id_domain_short_description(version="3_5_0", id_domain="1wvfA04"))

        break
    except Exception:
        print("Something gone wrong")
print("--- %s seconds version 3_5_0---\n" % (time.time() - start_time))


"""
Test Domain_id get full description (Very slow so much data)
"""

start_time = time.time()
while True:
    try:
        print(get_id_domain_full_description(version="4_2_0", id_domain="3frhA01"))
        print(get_id_domain_full_description(version="4_2_0", id_domain="3b89A01"))

        break
    except Exception:
        print("Something gone wrong")
print("--- %s seconds version 4_2_0---\n" % (time.time() - start_time))
print()

start_time = time.time()
while True:
    try:
        print(get_id_domain_full_description(version="4_1_0", id_domain="3frhA01"))
        print(get_id_domain_full_description(version="4_1_0", id_domain="3b89A01"))

        break
    except Exception:
        print("Something gone wrong")
print("--- %s seconds version 4_1_0---\n" % (time.time() - start_time))
print()
start_time = time.time()
while True:
    try:
        print(get_id_domain_full_description(version="2_6_0", id_domain="3frhA01"))
        print(get_id_domain_full_description(version="2_6_0", id_domain="3b89A01"))

        break
    except Exception:
        print("Something gone wrong")
print("--- %s seconds version 2_6_0---\n" % (time.time() - start_time))
print()
while True:
    try:
        print(get_id_domain_full_description(version="3_5_0", id_domain="3frhA01"))
        print(get_id_domain_full_description(version="3_5_0", id_domain="3b89A01"))

        break
    except Exception:
        print("Something gone wrong")
print("--- %s seconds version 2_6_0---\n" % (time.time() - start_time))
print()