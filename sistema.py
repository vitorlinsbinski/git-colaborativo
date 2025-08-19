def exibir_dashboard():
    print("Dashboard carregado!")

def cadastrar_usuario(nome):
    print(f"Usuário {nome} cadastrado com sucesso!")

def login(usuario, senha):
    print(f"Tentando logar usuário {usuario}...")
    if senha == "123":
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta.")

def gerar_relatorio():
    print("Relatório gerado com sucesso!")

def main():
    print("Sistema iniciado")
    exibir_dashboard()
    cadastrar_usuario("Maria")
    login("Vitor", "123")
    gerar_relatorio()
