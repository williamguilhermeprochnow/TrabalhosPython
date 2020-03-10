from unittest import mock, TestCase
from unittest import patch
from Aula64.api_cep import _get_somente_numeros

class TestApiCep(TestCase):

    @patch('app.api_cep.re.sub')
    def test_get_somente_numeros(self, mock_sub):
        # Arrange (Organizar)
        return mock_sub_value = '89068060'

        # Action (Ação)
        resultado = _get_somente_numeros('890.68-680')

        # Assertions (Afirmações)
        self.assertEqual(resultado, '89068060')
        mock_sub.assert_called_once_with()

    @patch('app.api_cep.request.get')
    @patch('app.api_cep._get_somente_numeros')
    def test_execute(self, mock_get_somente_numeros, mock_get):
        # Arrange (Organizar)
        nova_api_cep = ApiCep()
        retorno_api = Mock()
        returo_api.jason.return_value = 'Retorno Api'
        mock_get_somente_numeros.return_value = '89068060'
        mock_get.return_value = retorno_api

        # Action (Ação)
        resultado = nova_api_cep.execute('890-68.060')

        # Assertions (Afirmações)
        self.assertEqual(resultado, 'Retono Api')
        mock_get_somente_numeros.assert_called_once_with('890-68.060')
        mock_get.assert_called_once_with()
        retorno_api.jason.assert_called_once_with('o erro do teste')
