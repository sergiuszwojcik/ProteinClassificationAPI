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


def get_protein_domain_id_list(version):
    get_cath_domain_list = urlopen(
        "http://download.cathdb.info/cath/releases/all-releases/v4_2_0/cath-classification-data/cath-domain-list-v4_2_0.txt")


def check_id_domain_description(version, id_domain):
    """
    prints out node, domain and description of protein

    :type version: string
    :param version: version of cath database
    :type id_domain: string
    :param id_domain: the id_domain of protein for example "2ynzC01"
    :Example:
    check_id_domain_description("4_2_0", "2ynzC01")
    """
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


