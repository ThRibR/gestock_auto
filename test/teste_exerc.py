import unittest
from unittest.mock import patch
from src.app import email_boas_vindas, get_product_price, 

class TestApp(unittest.TestCase): # o que é o testcase? Olhar a documentação
    #teste 1
    @patch("src.app.save", return_value = True)
    def test_email_boas_vindas(self,m_s):
        nome = "Luis"
        email = "luis.torres@gamil.com"
        r = email_boas_vindas(nUser)
        self.assertTrue(r)
        m_s.assert_called_once_with({'nome':nome, 'email':email})
    #teste 2
    @patch("requests.get")
    
    def test_get_product_price(self,mock):
        id = 3
        r = get_product_price(id)
        self.assertTrue(r)
        mock.assert_called_once_with({'id': id})
    #teste 3
        
'''
teste 1:
● Objetivo: Crie um mock para o serviço de envio de email e verifique se o método de
envio foi chamado com os parâmetros corretos.
● Dica: Simule o comportamento do serviço de email sem realmente enviar um email
durante o teste.

teste 2:
● Objetivo: Use unittest.mock para simular a resposta da API sem realmente
fazer a requisição HTTP. Verifique se o preço retornado é o esperado.
● Dica: Crie um mock do método requests.get para simular a resposta de uma
API.

teste 3:
● Objetivo: Crie um mock do ORM (ou da função que interage com o banco) para
verificar se a função de persistência foi chamada corretamente sem acessar
realmente o banco de dados.
● Dica: Use um mock para o método session.add() e verifique se o método foi
chamado com o objeto correto.

teste 4:
● Objetivo: Crie um mock para o serviço de pagamento e verifique se a função de
pagamento é chamada com os parâmetros corretos. Simule um erro, como um
pagamento falho, e verifique como o código lida com ele.
● Dica: Simule uma resposta de falha (exemplo: pagamento recusado) usando o
mock.
'''

