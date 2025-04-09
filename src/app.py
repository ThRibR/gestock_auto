
#aula
usuarios = []

def soma(a,b):
    return a+b

def is_par(a):
    if a%2 == 0:
        return True
    else:
        return False

def cadastro_usuario(nome, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return "email ja existe"
       
    novo_usuario ={
        "nome":nome,
        "email":email
    }

    usuarios.append(novo_usuario)
    return "sucesso"

#controller
def cadastro(nome , cpf):
    new_user = {
        "nome":nome,
        "cpf":cpf
    }
    return save(new_user)

#service
def save(new_user):
    if new_user["nome"] and new_user["cpf"]:
        return True #salvo no DB
    return False #erro ao salvar no DB


'''
1. Teste de Função de Envio de Email
● Cenário: Você tem uma função que envia um email de boas-vindas a um usuário
utilizando um serviço externo de email.
'''
users = []
def user(nome, email):
    nUser = {
        "Nome":nome,
        "Email":email
    }
    for usuario in users:
        if usuario["email"] == email:
            return "email ja existe"
        users.append(nUser)
        return save(nUser)

def save(nUser):
    if nUser["nome"] and nUser["email"]:
        return True #salvo no DB
    return False #erro ao salvar no DB

def email_boas_vindas(email):
    for user in users:
        if users['email'] == email:
            return f"Seja bem vindo, {users['nome']}!"
'''
● Objetivo: Crie um mock para o serviço de envio de email e verifique se o método de
envio foi chamado com os parâmetros corretos.
● Dica: Simule o comportamento do serviço de email sem realmente enviar um email
durante o teste.
'''

'''
2. Teste de Requisição a API de Preço
● Cenário: Sua função get_product_price faz uma requisição HTTP a uma API
externa para obter o preço de um produto. Ela recebe um ID de produto e retorna o
preço.
● Objetivo: Use unittest.mock para simular a resposta da API sem realmente
fazer a requisição HTTP. Verifique se o preço retornado é o esperado.
● Dica: Crie um mock do método requests.get para simular a resposta de uma
API.
'''
def get_product_price(id):
    url = f"sla/{id}"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception
    d = r.json()
    return d
    
'''
4. Teste de Função de Processamento de Pagamento
● Cenário: Sua função processa um pagamento utilizando um serviço externo
(exemplo: Stripe ou PayPal).
'''
    
'''
3. Teste de Armazenamento em Banco de Dados
● Cenário: Você tem uma função que salva um registro de usuário no banco de dados
utilizando um ORM (exemplo: SQLAlchemy).
● Objetivo: Crie um mock do ORM (ou da função que interage com o banco) para
verificar se a função de persistência foi chamada corretamente sem acessar
realmente o banco de dados.
● Dica: Use um mock para o método session.add() e verifique se o método foi
chamado com o objeto correto.
4. Teste de Função de Processamento de Pagamento
● Cenário: Sua função processa um pagamento utilizando um serviço externo
(exemplo: Stripe ou PayPal).
● Objetivo: Crie um mock para o serviço de pagamento e verifique se a função de
pagamento é chamada com os parâmetros corretos. Simule um erro, como um
pagamento falho, e verifique como o código lida com ele.
● Dica: Simule uma resposta de falha (exemplo: pagamento recusado) usando o
mock.
5. Teste de Função de Notificação por SMS
● Cenário: Você tem uma função que envia notificações SMS usando um serviço
externo como Twilio.
● Objetivo: Crie um mock do serviço de SMS e verifique se a função de envio foi
chamada com o número de telefone correto e a mensagem esperada.

● Dica: Use assert_called_with para verificar os parâmetros passados para o
método de envio do SMS.
6. Teste de Leitura de Arquivo
● Cenário: Sua função lê dados de um arquivo local e processa essas informações.
● Objetivo: Use um mock para simular a leitura de um arquivo e testar se a função
está processando os dados corretamente.
● Dica: Crie um mock para a função open ou o método que lê o arquivo e simule o
conteúdo do arquivo.
7. Teste de Função de Registro de Log
● Cenário: Você tem uma função que grava logs em um arquivo ou serviço de log
(exemplo: Loguru, logging).
● Objetivo: Crie um mock para o objeto de logging e verifique se o log foi gravado
corretamente quando a função é chamada.
● Dica: Simule a gravação de log e verifique se o método de log foi chamado com a
mensagem certa.
8. Teste de Função de Autenticação
● Cenário: Você tem uma função que autentica um usuário contra um serviço de
autenticação externo (exemplo: OAuth, LDAP, etc.).
● Objetivo: Use mocks para simular a resposta de autenticação sem chamar o serviço
real e verifique se o comportamento da função de autenticação está correto.
● Dica: Simule respostas de sucesso e erro e verifique como a função se comporta.
9. Teste de Função de Agendamento de Tarefas
● Cenário: Sua aplicação possui uma função que agenda uma tarefa para ser
executada em um horário específico, utilizando um serviço de agendamento
(exemplo: Celery, APScheduler).
● Objetivo: Crie um mock para o serviço de agendamento e verifique se a tarefa foi
agendada corretamente.
● Dica: Verifique se o serviço de agendamento foi chamado com os parâmetros
corretos.
10. Teste de Função de Busca em Banco de Dados
● Cenário: Sua função realiza uma consulta em um banco de dados para buscar
usuários por nome.
● Objetivo: Crie um mock para a função de consulta ao banco de dados (exemplo:
session.query) e verifique se a função está retornando os dados esperados.
● Dica: Use side_effect para simular diferentes cenários de dados retornados
(exemplo: nenhum usuário encontrado, usuário encontrado).
11. Teste de Função de Processamento de Imagem

● Cenário: Sua função processa imagens utilizando uma API externa para
redimensionar ou transformar as imagens (exemplo: Pillow ou um serviço externo de
imagem).
● Objetivo: Crie um mock para a API de processamento de imagem e verifique se a
função está chamando a API com os parâmetros corretos e se o processamento é
realizado corretamente.
● Dica: Simule um erro de processamento de imagem e verifique se a função lida
corretamente com a falha.
12. Teste de Função de Geração de Relatórios
● Cenário: Sua aplicação gera relatórios em PDF ou Excel utilizando uma biblioteca
externa (exemplo: ReportLab, Pandas).
● Objetivo: Crie um mock para a biblioteca de geração de relatórios e verifique se os
métodos necessários para gerar o relatório estão sendo chamados corretamente.
● Dica: Verifique se a função de geração de relatório está sendo chamada com os
parâmetros corretos, sem realmente gerar o arquivo.
13. Teste de Função de Criação de Usuário
● Cenário: Sua função cria um novo usuário e envia uma notificação por email e SMS
após a criação.
● Objetivo: Crie mocks para o serviço de email e SMS e verifique se ambos são
chamados corretamente após a criação do usuário.
● Dica: Verifique se os serviços são chamados na ordem correta e com os parâmetros
corretos.
14. Teste de Função de Sincronização de Dados
● Cenário: Sua função sincroniza dados entre dois sistemas externos, por exemplo,
entre um banco de dados local e um banco de dados remoto.
● Objetivo: Use mocks para simular a sincronização de dados sem interagir com os
sistemas reais.
● Dica: Verifique se os dados foram sincronizados corretamente, garantindo que a
função de sincronização foi chamada para cada item de dados.
'''