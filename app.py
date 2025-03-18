import streamlit as st
from PIL import Image

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

if __name__ == "__main__":
    exibir_produtos()
