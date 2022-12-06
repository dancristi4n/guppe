import unittest

from atividades import comer, dormir, eh_engracada, eh_admin, listar_usuarios


class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito."""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_eh_engracada(self):
        # self.assertEqual(eh_engracada('Sérgio Malandro'), False)
        self.assertFalse(eh_engracada('Sérgio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')

    def test_eh_admin(self):
        self.assertNotEqual(eh_admin('danilo'), 'Bem vindo admin')
        self.assertNotEqual(eh_admin('morpheus'), 'Acesso negado')

    def test_listar_usuarios(self):
        self.assertIn('u2', listar_usuarios())
        self.assertNotIn('u3', listar_usuarios())


if __name__ == '__main__':
    unittest.main()
