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
    print("🔔 Nova notificação recebida!")
    print(f"Notificação enviada com sucesso: {msg.upper()}")  # garante que a mensagem seja maiúscula

# feature-relatorio-detalhado
def gerar_relatorio():
    print("Relatório gerado com formatação avançada! ✅")  # corrige bug de símbolos
    print("Incluindo detalhes de vendas e usuários 📊")

def atualizar_perfil(usuario):
    if not usuario:
        print("Erro: usuário inválido!")
    else:
        print(f"Perfil do usuário {usuario} atualizado.")
    print("Avatar atualizado com sucesso! 🎨")

def pesquisar_usuario(nome):
    # Corrige bug: exibe mensagem se usuário não for encontrado
    usuarios_cadastrados = ["Maria", "Vitor"]
    if nome in usuarios_cadastrados:
        print(f"Pesquisando usuário: {nome}")
    else:
        print(f"Usuário {nome} não encontrado!")

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
