import streamlit as st
import sqlite3
from PIL import Image
import hashlib

# Função para conectar ao banco de dados SQLite
def conectar_banco():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome_usuario TEXT UNIQUE,
                  email TEXT,
                  senha TEXT)''')
    conn.commit()
    return conn, c

# Função para verificar as credenciais de login
def verificar_login(nome_usuario, senha):
    conn, c = conectar_banco()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    c.execute("SELECT * FROM usuarios WHERE nome_usuario = ? AND senha = ?",
              (nome_usuario, senha_hash))
    usuario = c.fetchone()
    conn.close()
    return usuario

# Função para exibir os produtos
def exibir_produtos():
    st.title("Bem-vindo à Nossa Conveniência Online!")
    st.write("Explore nossos produtos e faça suas compras online com comodidade. Entregamos diretamente na sua casa!")

    # Lista de produtos com categorias
    produtos = [
        {"nome": "Cerveja", "preco": 35.00, "descricao": "Caixa de cerveja", "imagem": "imagens/produto1.jpg", "categoria": "Bebidas"},
        {"nome": "Cigarro", "preco": 12.50, "descricao": "Cigarro", "imagem": "imagens/produto2.jpg", "categoria": "Tabaco"},
        {"nome": "Coca Cola", "preco": 7.25, "descricao": "Coca Cola", "imagem": "imagens/produto3.jpg", "categoria": "Bebidas"},
        {"nome": "Água", "preco": 15.00, "descricao": "Água Mineral", "imagem": "imagens/produto4.jpg", "categoria": "Bebidas"},
        {"nome": "Suco", "preco": 22.30, "descricao": "Suco de Laranja", "imagem": "imagens/produto5.jpg", "categoria": "Bebidas"},
        {"nome": "Biscoito", "preco": 10.00, "descricao": "Biscoitos", "imagem": "imagens/produto6.jpg", "categoria": "Alimentos"},
    ]

    # Inicializa o estado da sessão para o carrinho de compras
    if 'carrinho' not in st.session_state:
        st.session_state.carrinho = []

    # Exibe as informações do usuário logado no sidebar
    if 'usuario_autenticado' in st.session_state and st.session_state.usuario_autenticado:
        st.sidebar.header("Informações do Usuário")
        st.sidebar.write(f"**Usuário:** {st.session_state.nome_usuario}")
        # Adicione mais informações do usuário aqui, se necessário
        # Exemplo: st.sidebar.write(f"**Email:** {st.session_state.email}")

    # Filtro de categoria
    categorias_disponiveis = sorted(set([produto['categoria'] for produto in produtos]))
    categoria_selecionada = st.selectbox(
        'Selecione a categoria',
        options=['Todas'] + categorias_disponiveis,
        index=0
    )

    # Define as proporções das colunas
    colunas = st.columns([1, 1, 1])  # 3 colunas com largura igual

    # Define o tamanho fixo das imagens
    largura_imagem = 150  # Largura
    altura_imagem = 150   # Altura

    # Filtra os produtos pela categoria selecionada
    produtos_filtrados = [produto for produto in produtos if categoria_selecionada == 'Todas' or produto['categoria'] == categoria_selecionada]

    # Distribui os produtos entre as colunas
    for i, produto in enumerate(produtos_filtrados):
        coluna = colunas[i % 3]
        with coluna:
            try:
                imagem = Image.open(produto["imagem"])
                imagem = imagem.resize((largura_imagem, altura_imagem))  # Redimensiona a imagem
                st.image(imagem)  # Exibe a imagem com o tamanho redimensionado
            except FileNotFoundError:
                st.error(f"Imagem não encontrada: {produto['imagem']}")
            st.subheader(produto["nome"])
            st.write(f"Preço: R${produto['preco']:.2f}")
            st.write(produto["descricao"])
            if st.button(f"Adicionar ao carrinho: {produto['nome']}", key=produto["nome"]):
                st.session_state.carrinho.append(produto)
                st.success(f"{produto['nome']} adicionado ao carrinho!")

    # Exibe o carrinho de compras
    st.sidebar.header("Carrinho de Compras")
    if st.session_state.carrinho:
        total = 0.0
        for item in st.session_state.carrinho:
            st.sidebar.write(f"{item['nome']} - R${item['preco']:.2f}")
            total += item['preco']
        st.sidebar.write(f"**Total: R${total:.2f}**")
    else:
        st.sidebar.write("Seu carrinho está vazio.")

# Função para exibir o formulário de login
def exibir_login():
    st.title("Login")
    nome_usuario = st.text_input("Nome de Usuário")
    senha = st.text_input("Senha", type='password')
    if st.button("Entrar"):
        usuario = verificar_login(nome_usuario, senha)
        if usuario:
            st.session_state.usuario_autenticado = True
            st.session_state.nome_usuario = nome_usuario
            # Armazene mais informações do usuário, se necessário
            # Exemplo: st.session_state.email = usuario[2]
            # Define o parâmetro na URL
            st.query_params["logged_in"] = "true"
            # Recarrega a aplicação para exibir os produtos
            st.rerun()
        else:
            st.error("Nome de usuário ou senha inválidos.")

# Função principal que controla a navegação entre login e produtos
def main():
    if 'usuario_autenticado' not in st.session_state or not st.session_state.usuario_autenticado:
        exibir_login()
    else:
        exibir_produtos()

if __name__ == "__main__":
    main()