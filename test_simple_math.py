"""Module de tests unitaires pour la classe SimpleMath."""

import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    """Classe de test pour SimpleMath."""

    def test_addition(self):
        """Teste la méthode addition."""
        self.assertEqual(SimpleMath.addition(2, 3), 5)

    def test_soustraction(self):
        """Teste la méthode soustraction."""
        self.assertEqual(SimpleMath.soustraction(5, 3), 2)

if __name__ == '__main__':
    unittest.main()
