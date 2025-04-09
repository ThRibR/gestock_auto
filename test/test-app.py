import unittest
from unittest.mock import patch
from src.app import cadastro, cadastro_usuario, email_boas_vindas, get_product_price

class TestApp(unittest.TestCase): # o que é o testcase? Olhar a documentação
    #teste aula
    @patch("src.app.save", return_value="ola")
    def test_cadastrar_usuario_valido(self, mock_salvar):
        nome = "Carlos"
        cpf = "213471283"
        resultado = cadastro(nome, cpf)
        self.assertTrue(resultado)
        mock_salvar.assert_called_once_with({'nome':nome, 'cpf':cpf})
    #teste 1
    @patch("src.app.save", return_value = True)
    def test_email_boas_vindas(self,m_s):
        nome = "Luis"
        email = "luis.torres@gamil.com"
        r = email_boas_vindas(nUser)
        self.assertTrue(r)
        m_s.assert_called_once_with({'nome':nome, 'email':email})
    #teste 2
    def test_get_product_price(self,mock):
        id = 3
        r = get_product_price(id)
        self.assertTrue(r)
        mock.assert
'''    
teste 1:
● Objetivo: Crie um mock para o serviço de envio de email e verifique se o método de
envio foi chamado com os parâmetros corretos.
● Dica: Simule o comportamento do serviço de email sem realmente enviar um email
durante o teste.
'''  
    
    
''' 
    def testSoma_positivo(self):
        resultado = soma(2,5)
        self.assertEqual(resultado, 7)
    
    def testPar(self):
        resultado = eh_par(2)
        self.assertEqual(resultado, True)

    def testPar(self):
        resultado1 = eh_par(7)
        self.assertEqual(resultado1, False)

    def testFatoral(self):
        resultado = fatoral(5)
        self.assertEqual(resultado, 120)

    def testContarVogais(self):
        resultado = contar_vogais('paralelepipedo')
        self.assertEqual(resultado, 120)
'''
    
'''
teste 2:
● Objetivo: Use unittest.mock para simular a resposta da API sem realmente
fazer a requisição HTTP. Verifique se o preço retornado é o esperado.
● Dica: Crie um mock do método requests.get para simular a resposta de uma
API.
'''
    
'''
teste 3:
● Objetivo: Crie um mock do ORM (ou da função que interage com o banco) para
verificar se a função de persistência foi chamada corretamente sem acessar
realmente o banco de dados.
● Dica: Use um mock para o método session.add() e verifique se o método foi
chamado com o objeto correto.
'''

'''
teste 4
'''

'''
teste 5
'''

if __name__=='__main__':#usa o principal
    unittest.main()