from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import defaultdict
import json
import re

"""
CATH DATABASE REST API
"""


def scop2_get_interrelationship_id():
    """IR - Interrelationship - SCOP2 green color\n
    This function returns list of dictionaries containing Interrelationship id's , Uniprot id's and IR sequence
    for SCOP2 database. Interrelationship (other relationships) is new function in SCOP2. Interrelationship
    is a leaf has no parents.

    :return: list of dictionaries
    :rtype: list
    """
    get_interrelationship_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/IR_scop2dom_20140205.aa")
    get_interrelationship_url = get_interrelationship_url.read()
    get_interrelationship_toXML = BeautifulSoup(get_interrelationship_url, "lxml")
    get_interrelationship_toText = get_interrelationship_toXML.p.get_text()
    get_interrelationship_splitted = get_interrelationship_toText.split("\n")
    inter_relationship = {}
    inter_relationship_list_all = []

    for x in range(1, len(get_interrelationship_splitted), 2):
        inter_relationship['domain'] = 'IR'
        inter_relationship['domain_id'] = get_interrelationship_splitted[x - 1][1:17]
        inter_relationship['pdb_code'] = get_interrelationship_splitted[x - 1][12:16]
        inter_relationship['pdb_chain'] = get_interrelationship_splitted[x - 1][16:17]
        inter_relationship['UniProt_id'] = get_interrelationship_splitted[x - 1][18:]
        inter_relationship['IR_seq'] = get_interrelationship_splitted[x]
        inter_relationship_list_all.append(inter_relationship)
        inter_relationship = {}
    return inter_relationship_list_all


# print(scop2_get_interrelationship_id())


def scop2_get_protein_species_id():
    """SP - Protein Species - SCOP2 blue/green color\n
    This function returns list of dictionaries containing Protein Species id's , Uniprot id's and protein species
    common sequence for SCOP2 database.\n Protein Species is parent of interrelationship.

    :return: list of dictionaries
    :rtype: list
    """
    get_protein_species_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/SP_scop2dom_20140205.aa")
    get_protein_species_url = get_protein_species_url.read()
    get_protein_species_toXML = BeautifulSoup(get_protein_species_url, "lxml")
    get_protein_species_toText = get_protein_species_toXML.p.get_text()
    get_protein_species_splitted = get_protein_species_toText.split("\n")
    protein_species = {}
    protein_species_list_all = []

    for x in range(1, len(get_protein_species_splitted), 2):
        protein_species['domain'] = 'SP'
        protein_species['domain_id'] = get_protein_species_splitted[x - 1][1:17]
        protein_species['pdb_code'] = get_protein_species_splitted[x - 1][12:16]
        protein_species['pdb_chain'] = get_protein_species_splitted[x - 1][16:17]
        protein_species['UniProt_id'] = get_protein_species_splitted[x - 1][18:]
        protein_species['SP_seq'] = get_protein_species_splitted[x]
        protein_species_list_all.append(protein_species)
        protein_species = {}
    return protein_species_list_all


# print(scop2_get_protein_species_id())


def scop2_get_proteins_id():
    """PR - Proteins - SCOP2 - orange color\n
    This function returns list of dictionaries containing Proteins id's , Uniprot id's and proteins common sequence
    for SCOP2 database.\n Proteins are parent of Protein Species and IR.

    :return: list of dictionaries
    :rtype: list
    """
    get_proteins_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/PR_scop2dom_20140205.aa")
    get_proteins_url = get_proteins_url.read()
    get_proteins_toXML = BeautifulSoup(get_proteins_url, "lxml")
    get_proteins_toText = get_proteins_toXML.p.get_text()
    get_proteins_splitted = get_proteins_toText.split("\n")
    proteins = {}
    proteins_list_all = []

    for x in range(1, len(get_proteins_splitted), 2):
        proteins['domain'] = 'PR'
        proteins['domain_id'] = get_proteins_splitted[x - 1][1:17]
        proteins['pdb_code'] = get_proteins_splitted[x - 1][12:16]
        proteins['pdb_chain'] = get_proteins_splitted[x - 1][16:17]
        proteins['UniProt_id'] = get_proteins_splitted[x - 1][18:]
        proteins['PR_seq'] = get_proteins_splitted[x]
        proteins_list_all.append(proteins)
        proteins = {}
    return proteins_list_all


# print(scop2_get_proteins_id())


def scop2_get_families_id():
    """FA - Family - SCOP2 - pink color\n
    This function returns list of dictionaries containing Family id's , Uniprot id's and family common sequence
    for SCOP2 database.\n Family can be parent of PR, SP, IR.

    :return: list of dictionaries
    :rtype: list
    """
    get_families_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/FA_scop2dom_20140205.aa")
    get_families_url = get_families_url.read()
    get_families_toXML = BeautifulSoup(get_families_url, "lxml")
    get_families_toText = get_families_toXML.p.get_text()
    get_families_splitted = get_families_toText.split("\n")

    families = {}
    families_list_all = []

    for x in range(1, len(get_families_splitted), 2):
        families['domain'] = 'FA'
        families['domain_id'] = get_families_splitted[x - 1][1:17]
        families['pdb_code'] = get_families_splitted[x - 1][12:16]
        families['pdb_chain'] = get_families_splitted[x - 1][16:17]
        families['UniProt_id'] = get_families_splitted[x - 1][18:]
        families['FA_seq'] = get_families_splitted[x]
        families_list_all.append(families)
        families = {}
    return families_list_all


# print(scop2_get_families_id())


def scop2_get_super_families_id():
    """SF - Super Family - SCOP2 - purple color\n
    This function returns list of dictionaries containing Super Family id's , Uniprot id's and Super Family common
    sequence for SCOP2 database.\n Super Family can be parent of FA, PR, SP

    :return: list of dictionaries
    :rtype: list
    """
    get_super_family_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/SF_scop2dom_20140205.aa")
    get_super_family_url = get_super_family_url.read()
    get_super_family_toXML = BeautifulSoup(get_super_family_url, "lxml")
    get_super_family_toText = get_super_family_toXML.p.get_text()
    get_super_family_splitted = get_super_family_toText.split("\n")

    super_family = {}
    super_family_list_all = []

    for x in range(1, len(get_super_family_splitted), 2):
        super_family['domain'] = 'SF'
        super_family['domain_id'] = get_super_family_splitted[x - 1][1:17]
        super_family['pdb_code'] = get_super_family_splitted[x - 1][12:16]
        super_family['pdb_chain'] = get_super_family_splitted[x - 1][16:17]
        super_family['UniProt_id'] = get_super_family_splitted[x - 1][18:]
        super_family['SF_seq'] = get_super_family_splitted[x]
        super_family_list_all.append(super_family)
        super_family = {}
    return super_family_list_all


# print(scop2_get_super_families_id())


def scop2_get_fold_id():
    """CF - Fold - SCOP2 - blue color\n
    This function returns list of dictionaries containing Fold id's , Uniprot id's and Fold common
    sequence for SCOP2 database.\n Fold can be parent of FA,PR,SP,IR,SF

    :return: list of dictionaries
    :rtype: list
    """
    get_fold_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/CF_scop2dom_20140205.aa")
    get_fold_url = get_fold_url.read()
    get_fold_toXML = BeautifulSoup(get_fold_url, "lxml")
    get_fold_toText = get_fold_toXML.p.get_text()
    get_fold_splitted = get_fold_toText.split("\n")

    fold = {}
    fold_list_all = []

    for x in range(1, len(get_fold_splitted), 2):
        fold['domain'] = 'CF'
        fold['domain_id'] = get_fold_splitted[x - 1][1:17]
        fold['pdb_code'] = get_fold_splitted[x - 1][12:16]
        fold['pdb_chain'] = get_fold_splitted[x - 1][16:17]
        fold['UniProt_id'] = get_fold_splitted[x - 1][18:]
        fold['CF_seq'] = get_fold_splitted[x]
        fold_list_all.append(fold)
        fold = {}
    return fold_list_all


# print(scop2_get_fold_id())


def scop2_get_nodes_names():
    """This function returns list of dictionaries containing all names of nodes

    :return: list of dictionaries
    :rtype: list
    """
    get_nodes_names_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/scop2_nodes_names_20140205")
    get_nodes_names_url = get_nodes_names_url.read()
    get_nodes_names_toXML = BeautifulSoup(get_nodes_names_url, "lxml")
    get_nodes_names_toText = get_nodes_names_toXML.p.get_text()
    get_nodes_names_splitted = get_nodes_names_toText.split("\n")

    nodes_names = {}
    nodes_names_list_all = []

    for lines in get_nodes_names_splitted[6:]:
        if len(lines) > 0:
            nodes_names["node_id"] = lines[:7]
            nodes_names["name"] = lines[8:]
            nodes_names_list_all.append(nodes_names)
            nodes_names = {}
    return nodes_names_list_all

# print(scop2_get_nodes_names())

def scop2_get_nodes_names_by_id(node_id):
    """
    This function returns node name by given id\n

    :param node_id: node id
    :type node_id: int, string
    :return: name of given node_id
    :rtype: String
    """
    if isinstance(node_id, int):
        node_id = str(node_id)

    get_nodes_names_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/scop2_nodes_names_20140205")
    get_nodes_names_url = get_nodes_names_url.read()
    get_nodes_names_toXML = BeautifulSoup(get_nodes_names_url, "lxml")
    get_nodes_names_toText = get_nodes_names_toXML.p.get_text()
    get_nodes_names_splitted = get_nodes_names_toText.split("\n")

    searched_node_name = ""
    for lines in get_nodes_names_splitted[6:]:
        if node_id in lines:
            searched_node_name = lines[8:]
    searched_node_name = searched_node_name.replace("\t", "")
    return searched_node_name


# print(scop2_get_nodes_names_by_id("5000859"))
# http://scop2.mrc-lmb.cam.ac.uk/graph/restapi/domain?id=SF-8004077-3R6NA
def scop2_get_domain_data_by_domain_id(domain_id):
    """
    Returns all information about domain by given domain_id. Works for all domains id's (IR,SP,PR,FA,SF,CF)

    :param: domain_id: specified domain_id for example SF-8004077-3R6NA
    :type domain_id: String
    :return: list of dictionaries
    :rtype: list
    """
    if not isinstance(domain_id, str):
        raise Exception("domain_id must be string type")

    get_domain = urlopen("http://scop2.mrc-lmb.cam.ac.uk/graph/restapi/domain?id=" + domain_id)
    get_domain_url = get_domain.read()
    get_domain_toXML = BeautifulSoup(get_domain_url, "lxml")
    get_domain_toText = get_domain_toXML.p.get_text()
    json = get_domain_toText
    domain_dict = eval(json)
    return domain_dict


# print(scop2_get_domain_data_by_domain_id("PR-8004118-1S70B"))


def scop2_get_ontology_tree_by_term_id(term_id):
    """
     Retrieves the ontology tree for the given term

     :param: term_id: specified term_id for example SP:6001071
     :type term_id: String
     :return: list of dictionaries
     :rtype: list
     """
    if not isinstance(term_id, str):
        raise Exception("term_id must be string type")

    get_ontology_tree = urlopen("http://scop2.mrc-lmb.cam.ac.uk/graph/restapi/chart?term=" + term_id)
    get_ontology_tree_url = get_ontology_tree.read()
    get_ontology_tree_toXML = BeautifulSoup(get_ontology_tree_url, "lxml")
    get_ontology_tree_toText = get_ontology_tree_toXML.p.get_text()
    json = get_ontology_tree_toText
    ontology_tree_dict = eval(json)
    return ontology_tree_dict


# for x in scop2_get_ontology_tree_by_term_id("PR:5000085"):
#     print(x)


# print(scop2_get_ontology_tree_by_term_id("PR:5000959"))

def scop2_get_term_data_by_term_id(term_id):
    """
        Retrieves all data for the given term, including its parents and children

        :param: term_id: specified term_id for example SP:6001071
        :type term_id: String
        :return: list of dictionaries
        :rtype: list
        """
    if not isinstance(term_id, str):
        raise Exception("term_id must be string type")

    get_term_data = urlopen("http://scop2.mrc-lmb.cam.ac.uk/graph/restapi/term?id=" + term_id)
    get_term_data_url = get_term_data.read()
    get_term_data_toXML = BeautifulSoup(get_term_data_url, "lxml")
    get_term_data_toText = get_term_data_toXML.p.get_text()
    json = get_term_data_toText
    term_data_dict = eval(json)
    return term_data_dict


# print(scop2_get_term_data_by_term_id("SP:6001071"))

#
def get_domain_id_list_by_pdb_code(pdb_code):
    """
    Returns list of dictionaries with all domain id's related with given pdb_code
    :param pdb_code:
    :return: list of dictionaries
    :rtype: list
    """
    get_domain_id_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/domain_segments_pdb_20140205")
    get_domain_id_url = get_domain_id_url.read()
    get_domain_id_toXML = BeautifulSoup(get_domain_id_url, "lxml")
    get_domain_id_toText = get_domain_id_toXML.p.get_text()
    get_domain_id_splitted = get_domain_id_toText.split("\n")

    domain_id_list = []

    for lines in get_domain_id_splitted[6:]:
        if (len(lines) > 0):
            if pdb_code in lines:
                domain_id_list.append(lines.split()[0])

    get_domain_id_url = urlopen("http://scop2.mrc-lmb.cam.ac.uk/downloads/scop2-rel20140205.sql")
    get_domain_id_url = get_domain_id_url.read()
    get_domain_id_toXML = BeautifulSoup(get_domain_id_url, "lxml")
    get_domain_id_toText = get_domain_id_toXML.p.get_text()
    get_domain_id_splitted = get_domain_id_toText.split("\n")

    all_id_dict = {}
    all_id_list = []

    for lines in get_domain_id_splitted[52840:56551]:
        lines = lines.replace("'", "")
        lines = lines.replace("(", "")
        lines = lines.replace(")", "")
        lines = lines.replace(",", " ")
        lines = lines.split()
        for id in domain_id_list:
            if id in lines[1]:
                all_id_dict["pdb_code"] = pdb_code
                all_id_dict["domain_id"] = lines[1]
                all_id_dict["term_id"] = lines[0]
                all_id_list.append(all_id_dict)
                all_id_dict = {}

        # print(lines.split()[0],lines.split()[1] )

    return all_id_list


# print("\n\n")
# for x in get_domain_id_list_by_pdb_code("2JHF"):
#     print(x["term_id"])


def scop2_get_IR_protein_classification_by_term_id(term_id):
    """
    Retrieves all classification by given hierarchy of proteins\n
    :TODO: Works only for IR hierarchy\n

    :param term_id: term_id
    :type term_id: String
    :return: list of dicionaries
    :rtype: list
    """
    term_id_ontology = scop2_get_ontology_tree_by_term_id(term_id)

    term_classification = {}
    term_classification_list_all = []
    relations_list = []
    for category in term_id_ontology:
        if category.get('rank') == "Interrelation":
            term_classification['rank'] = category.get('rank')
            term_classification['name'] = category.get('name')
            category_relation = category['rels']
            category_relation = category_relation.replace('part_of', '')
            category_relation = category_relation.replace('is_a', '')
            category_relation = category_relation.replace('occurred_in', '')
            for x in category_relation.split():
                x = x.replace(',', '')
                print("test", category['id'])
                print(x)
            term_classification['relations'] = relations_list
            term_classification_list_all.append(term_classification)
            term_classification = {}
    for category in term_id_ontology:
        if category.get('rank') == "Protein":
            term_classification['rank'] = category.get('rank')
            term_classification['name'] = category.get('name')
            term_classification_list_all.append(term_classification)
            term_classification = {}
    print(term_classification_list_all)


# scop2_get_IR_protein_classification_by_term_id("IR:7000008")


def scop2_get_PR_protein_classification_by_protein_term_id(term_id):
    """
    Returns protein classification by given term id. Returns list of dictionaries\n
    :param term_id: term_id
    :type term_id: String
    :return: list of dictionaries
    :rtype: list
    """
    term_id_ontology = scop2_get_ontology_tree_by_term_id(term_id)
    term_classification = {}
    term_small_classification = {}
    term_classification_list_all = []
    relations_list = []

    for category in term_id_ontology:
        if category.get('rank') == "Type":
            term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
    term_classification_list_all.append(term_small_classification)
    term_small_classification = {}

    for category in term_id_ontology:
        if category.get('rank') == "Class":
            term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
    term_classification_list_all.append(term_small_classification)
    term_small_classification = {}

    for category in term_id_ontology:
        if category.get('rank') == "Fold":
            term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
    term_classification_list_all.append(term_small_classification)
    term_small_classification = {}

    for category in term_id_ontology:
        if category.get('rank') == "Event":
            term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
    term_classification_list_all.append(term_small_classification)
    term_small_classification = {}

    for category in term_id_ontology:
        if category.get('rank') == "Hyperfamily":
            term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
    term_classification_list_all.append(term_small_classification)
    term_small_classification = {}

    for category in term_id_ontology:
        if category.get('rank') == "Superfamily":
            term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
    term_classification_list_all.append(term_small_classification)
    term_small_classification = {}

    for category in term_id_ontology:
        if category.get('rank') == "Family":
            term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
    term_classification_list_all.append(term_small_classification)
    term_small_classification = {}

    return term_classification_list_all


# print()
# for x in scop2_get_IR_protein_classification_by_protein_term_id("PR:5000091"):
#     print(x)


def scop2_get_PR_protein_classification_by_protein_pdb_code(pdb_code):
    """
      Returns protein classification by given pdb code. Returns list of dictionaries\n
      :param pdb_code: pdb_code
      :type pdb_code: String
      :return: list of dictionaries
      :rtype: list
      """
    all_id = get_domain_id_list_by_pdb_code(pdb_code)
    protein_term_id_list = []
    for x in all_id:
        if 'PR' in x['term_id']:
            protein_term_id_list.append(x['term_id'])
        # term_id_list.append(x[3])
    # print(protein_term_id_list)

    print(protein_term_id_list)
    whole_list = []
    for x_pdb_code in protein_term_id_list:

        term_id_ontology = scop2_get_ontology_tree_by_term_id(x_pdb_code)
        term_classification = {}
        term_small_classification = {}
        term_classification_list_all = []
        relations_list = []

        for category in term_id_ontology:
            if category.get('rank') == "Protein":
                term_small_classification.setdefault("ProteinName", []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Family":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Superfamily":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Hyperfamily":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Fold":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Class":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Type":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Event":
                term_small_classification.setdefault("Event", []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}
        whole_list.append(term_classification_list_all)

    return term_classification_list_all


# for x in scop2_get_IR_protein_classification_by_protein_term_id("1VL6"):
#     print(x)


def scop2_get_PR_multiple_protein_classification_by_protein_pdb_code(pdb_code):
    """
      Returns multiple given proteins classification by given list of pdb codes. Returns list of lists with dictionaries
      \n
      :param pdb_code: pdb_code
      :type pdb_code: String
      :return: list of list dictionaries
      :rtype: list
      """
    # print(pdb_code)
    protein_term_id_list = []
    for codes in pdb_code:
        all_id = get_domain_id_list_by_pdb_code(codes)
        for x in all_id:
            if 'PR' in x['term_id']:
                protein_term_id_list.append(x['term_id'])
            # term_id_list.append(x[3])
        # print(protein_term_id_list)

    # print(protein_term_id_list)
    whole_list = []
    for x_pdb_code in protein_term_id_list:

        term_id_ontology = scop2_get_ontology_tree_by_term_id(x_pdb_code)
        term_classification = {}
        term_small_classification = {}
        term_classification_list_all = []
        relations_list = []

        for category in term_id_ontology:
            if category.get('rank') == "Protein":
                term_small_classification.setdefault("ProteinName", []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Family":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Superfamily":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Hyperfamily":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Fold":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Class":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Type":
                term_small_classification.setdefault(category.get('rank'), []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}

        for category in term_id_ontology:
            if category.get('rank') == "Event":
                term_small_classification.setdefault("Event", []).append(category.get('name'))
        term_classification_list_all.append(term_small_classification)
        term_small_classification = {}
        whole_list.append(term_classification_list_all)

    return whole_list


