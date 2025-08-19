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

def enviar_notificacao(msg):
    print(f"Notificação enviada: {msg}")

def gerar_relatorio():
    print("Relatório gerado com sucesso!")

def atualizar_perfil(usuario):
    print(f"Perfil do usuário {usuario} atualizado.")

def main():
    print("Sistema iniciado")
    exibir_dashboard()
    cadastrar_usuario("Maria")
    login("Vitor", "123")
    enviar_notificacao("Bem-vindo!")
    gerar_relatorio()
    atualizar_perfil("Vitor")
