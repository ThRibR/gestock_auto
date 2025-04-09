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
2. Teste de Requisição a API de Preço
● Cenário: Sua função get_product_price faz uma requisição HTTP a uma API
externa para obter o preço de um produto. Ela recebe um ID de produto e retorna o
preço.
'''
def get_product_price(id):
    url = f"sla/{id}"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception
    d = r.json()
    return d