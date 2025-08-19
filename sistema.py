def exibir_dashboard():
    print("Dashboard carregado!")

def cadastrar_usuario(nome):
    print(f"Usuário {nome} cadastrado com sucesso!")

# hotfix-login: corrige mensagem de login
def login(usuario, senha):
    print(f"Tentando logar usuário {usuario}...")
    if senha == "123":
        print("Login bem-sucedido! 🟢")
    else:
        print("Senha incorreta ❌")

# feature-notificacao-personalizada
def enviar_notificacao(msg):
    print(f"Notificação enviada: {msg.upper()}")  # garante que a mensagem seja maiúscula

# feature-relatorio-formatado
def gerar_relatorio():
    print("Relatório gerado com formatação avançada!")

def atualizar_perfil(usuario):
    print(f"Perfil do usuário {usuario} atualizado.")

def pesquisar_usuario(nome):
    print(f"Pesquisando usuário: {nome}")

def ajuda():
    print("Exibindo tela de ajuda...")

def configuracoes():
    print("Abrindo configurações do sistema...")

def gerar_relatorios_avancados():
    print("Relatórios avançados gerados!")

def chat_entre_usuarios(usuario1, usuario2):
    print(f"{usuario1} enviou mensagem para {usuario2}")

def mostrar_estatisticas():
    print("Exibindo estatísticas do sistema")

def main():
    print("Sistema iniciado")
    exibir_dashboard()
    cadastrar_usuario("Maria")
    login("Vitor", "123")
    enviar_notificacao("Bem-vindo!")
    gerar_relatorio()
    atualizar_perfil("Vitor")
    pesquisar_usuario("Maria")
    ajuda()
    configuracoes()
    gerar_relatorios_avancados()
    chat_entre_usuarios("Vitor", "Maria")
    mostrar_estatisticas()
