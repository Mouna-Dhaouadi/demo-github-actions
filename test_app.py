"""Tester le module qui fait la somme ou le produit"""
import unittest
import app

class TestApp(unittest.TestCase):
    """Classe pour les cas des tests"""
    def test_somme(self):
        """Tester la fonction de la somme"""
        self.assertEqual(app.somme(3, 7), 10)
        self.assertEqual(app.somme(-2, 2), 0)
        self.assertEqual(app.somme(-2, -2), -4)

    def test_produit(self):
        """Tester la fonction du produit"""
        self.assertEqual(app.produit(3, 5), 15)
        self.assertEqual(app.produit(3, 0), 0)
        self.assertEqual(app.produit(-3, -1), 3)


if __name__ == '__main__':
    unittest.main()
