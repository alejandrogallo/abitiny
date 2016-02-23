import abitiny


import unittest


class TestBasis(unittest.TestCase):
    def test_parse_He(self):
        basis = abitiny.Basis(fileName = "abitiny/test/he.basis")
        basis.parseFile()
