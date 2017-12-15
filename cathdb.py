from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

"""
CATH DATABASE REST API
"""


def get_catch_versions():
    """
    prints out all versions of cath databases

    """
    get_cath_version_url = urlopen("http://download.cathdb.info/cath/known-version-differences.README")
    catch_versions_toXML = BeautifulSoup(get_cath_version_url, "lxml")
    cath_version_toText = catch_versions_toXML.p.get_text()
    re1 = '(\\/)'  # Any Single Character 1
    re2 = '(v)'  # Any Single Character 2
    re3 = '(\\d)'  # Any Single Digit 1
    re4 = '(_)'  # Any Single Character 3
    re5 = '(\\d)'  # Any Single Digit 2
    re6 = '(\\/)'  # Any Single Character 4
    re66 = '(_)'
    re7 = '(\\d)'  # Any Single Digit 3
    re8 = '(\\/)'  # Any Single Character 5
    rg = re.compile(re1 + re2 + re3 + re4 + re5 + re6, re.IGNORECASE | re.DOTALL)
    rg3 = re.compile(re1 + re2 + re3 + re4 + re5 + re66 + re7 + re8, re.IGNORECASE | re.DOTALL)
    version_list = ["4_1_0"]  # not added version in documentation ???
    for lines in cath_version_toText.split():
        m = rg.search(lines)
        m3 = rg3.search(lines)
        if m3:
            d1 = m3.group(3)
            c3 = m3.group(4)
            d2 = m3.group(5)
            c4 = m3.group(6)
            d3 = m3.group(7)
            version_list.append(d1 + c3 + d2 + c4 + d3)
        if m:
            d1 = m.group(3)
            c3 = m.group(4)
            d2 = m.group(5)
            version_list.append(d1 + c3 + d2)

    print('\n'.join((sorted(set(version_list)))))


def get_protein_domain_id_list(version="4_2_0", ):
    get_cath_domain_list = urlopen(
        "http://download.cathdb.info/cath/releases/all-releases/v" + version +
        "/cath-classification-data/cath-domain-list-v" + version + ".txt")

    cath_domain_list_toXML = BeautifulSoup(get_cath_domain_list, "lxml")
    cath_domain_list_toText = cath_domain_list_toXML.p.get_text()
    cath_domain_list_toText = cath_domain_list_toText[
                              500:]  # without not needed description start after 500 letters
    cath_domain_list_splitted = cath_domain_list_toText.split("\n")
    print_range = 0
    if version in ["2_0", "2_4", "2_5", "2_6_0"]:  # Old version got other format in file
        for line in cath_domain_list_splitted[1:]:
            print(line[0:6], end=" ")
            print_range += 1
            if (print_range % 20 == 0):
                print()

    else:
        for line in cath_domain_list_splitted[1:]:
            print(line[0:7], end=" ")
            print_range += 1
            if (print_range % 20 == 0):
                print()


def get_protein_pdb_id_list(version="4_2_0"):
    """
    Prints all pdb_id needed to download protein database or check description od protein
    For example those pdb_id can be used in rest link:
    http://www.cathdb.info/version/v4_1_0/api/rest/id/<pdb_id>.pdb

    :type: version: string
    :param version: version of cath database, default "4_2_0"
    :Example:
    get_protein_pdb_id_list("4_2_0")
    """
    get_cath_domain_list = urlopen(
        "http://download.cathdb.info/cath/releases/all-releases/v" + version +
        "/cath-classification-data/cath-domain-list-v" + version + ".txt")

    cath_domain_list_toXML = BeautifulSoup(get_cath_domain_list, "lxml")
    cath_domain_list_toText = cath_domain_list_toXML.p.get_text()
    cath_domain_list_toText = cath_domain_list_toText[500:]  # without description start after 500 letters
    cath_domain_list_splitted = cath_domain_list_toText.split("\n")
    print_range = 0
    pdb_id_set = set()
    if version in ["2_0", "2_4", "2_5", "2_6_0"]:  # Old version got other format in file
        for line in cath_domain_list_splitted[1:]:
            pdb_id_set.add(line[0:4])

    else:
        for line in cath_domain_list_splitted[1:]:
            pdb_id_set.add(line[0:4])

    set_to_list = list(pdb_id_set)
    for element in set_to_list:
        print(element, end=" ")
        if (print_range % 10 == 0 and print_range > 0):
            print()
        print_range += 1


def check_id_domain_descrqiption(version="4_2_0", id_domain=""):
    """
    prints out node, domain and description of protein

    :type version: string
    :param version: version of cath database, default "4_2_0"
    :type id_domain: string
    :param id_domain: the id_domain of protein, default "2ynzC01"
    :Example:
    check_id_domain_description(version = "4_2_0", id_domain = "2ynzC01")
    """

    if id_domain == "":
        raise Exception('id_domain is null, must be filled ')
    if version == "":
        raise Exception('version is null, must be filled ')

    get_cath_names_url = urlopen(
        "http://download.cathdb.info/cath/releases/all-releases/v" + version + "/cath-classification-data/cath-names-v"
        + version + ".txt")
    cath_names_toXML = BeautifulSoup(get_cath_names_url, "lxml")
    cath_names_toText = cath_names_toXML.p.get_text()
    for lines in cath_names_toText.split("\n"):
        if id_domain in lines:
            splitted_line = lines.split()
            print("Node ", splitted_line[0], " Protein domain ", splitted_line[1],
                  " Node description ", ''.join(splitted_line[2:]))


def cath_download_domain_id():
    pass


def cath_download_chain_id():
    pass


def cath_download_pdb_id():
    pass


def cath_get_domain_id_by_superfamily_id():
    """https://github.com/sergiuszwojcik/ProteinClassificationAPI/blob/master/cathdb.py"""
    pass
