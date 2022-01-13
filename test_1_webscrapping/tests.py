import unittest
from utils import retrieve_cne_information_from_web


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.list_of_identity_document = [("V", "20975248"), ("E", "0")]
        self.cne_url = "http://www.cne.gob.ve/"

    def test_retrieve_cne_information(self):
        cne_information_by_identity_document = retrieve_cne_information_from_web(
            self.list_of_identity_document, self.cne_url)
        self.assertEqual(
            cne_information_by_identity_document,
            {"V-20975248": {'name': 'JOSUE SAMUEL BANEGA VASQUEZ', 'state': 'EDO. BOLIVAR', 'municipality': 'MP. CARONI', 'parish': 'PQ. UNARE'}}
            )

unittest.main()