from unittest import TestCase, mock
from unittest.mock import patch
from run import consulta_api_viacep

class TestConsultaApiCep(TestCase):

    @patch('run.ApiCep.execute')
    @patch('run.print')
    @patch('run.input')
    def test_consulta_api_cep(self, mock_input, mock_print, mock_execute):
        # Arrange (organizar)
        mock_input.return_value_ = '89068060'
        mock_execute.return_value  = 'Retorno ApiCep'

        # Action (Ação)
        resultado = consulta_api_viacep()

        # Assertions (Afirmações)
        self.assertEqual(resultado, 'Cep consultado com sucesso!')
        mock_input.assert_called_once_with('Informe o cep para consulta: ')
        mock_print.assert_called_once_with('Retorno ApiCep')
        mock_print.assert_called_once_with('89068060')