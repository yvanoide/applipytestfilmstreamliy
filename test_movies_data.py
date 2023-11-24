import unittest
from models.movies_data import MoviesData

class TestMoviesData(unittest.TestCase):
    def setUp(self):
        # Initialisation des données de test si nécessaire
        pass

    def test_get_short_list(self):
        # Créez une instance de MoviesData avec des données spécifiques pour les tests
        # Assurez-vous que la méthode get_short_list retourne les résultats attendus

        # Exemple :
        test_data = MoviesData('/home/yves/iadev-python/stepro/py-testing-main/py-streamlit/sl-test/data/netflix_titles.csv')
        short_list = test_data.get_short_list(5)  # Obtenez une liste courte de 5 films

        # Vérifiez que la longueur de la liste courte est correcte
        self.assertEqual(len(short_list), 5)

    def test_get_realyse_years_array(self):
        # Créez une instance de MoviesData avec des données spécifiques pour les tests
        # Assurez-vous que la méthode get_realyse_years_array retourne les résultats attendus

        # Exemple :
        test_data = MoviesData('/home/yves/iadev-python/stepro/py-testing-main/py-streamlit/sl-test/data/netflix_titles.csv')
        years_array = test_data.get_realyse_years_array()

        # Vérifiez que la longueur de l'array est correcte
        self.assertEqual(len(years_array), 2000)  # Si vous avez limité à 2000 films dans votre classe MoviesData

# Si le fichier est exécuté directement, lancez les tests
if __name__ == '__main__':
    unittest.main()
