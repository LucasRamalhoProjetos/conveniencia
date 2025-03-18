import streamlit as st
from PIL import Image

# Função para exibir os produtos
def exibir_produtos():
    st.title("Bem-vindo à Nossa Conveniência Online!")
    st.write("Explore nossos produtos e faça suas compras online com comodidade. Entregamos diretamente na sua casa!")

    # Lista de produtos
    produtos = [
        {"nome": "Produto 1", "preco": 35.00, "descricao": "Caixa de cerveja", "imagem": "imagens/produto1.jpg"},
        {"nome": "Produto 2", "preco": 12.50, "descricao": "Cigarro", "imagem": "imagens/produto2.jpg"},
        {"nome": "Produto 3", "preco": 7.25, "descricao": "Coca Cola", "imagem": "imagens/produto3.jpg"},
        {"nome": "Produto 4", "preco": 15.00, "descricao": "Água Mineral", "imagem": "imagens/produto4.jpg"},
        {"nome": "Produto 5", "preco": 22.30, "descricao": "Suco de Laranja", "imagem": "imagens/produto5.jpg"},
        {"nome": "Produto 6", "preco": 10.00, "descricao": "Biscoitos", "imagem": "imagens/produto6.jpg"},
    ]

    # Inicializa o estado da sessão para o carrinho de compras
    if 'carrinho' not in st.session_state:
        st.session_state.carrinho = []

    # Define 3 colunas fixas
    num_colunas = 3
    colunas = st.columns(num_colunas)

    # Define o tamanho fixo das imagens
    largura_imagem = 150  # Largura
    altura_imagem = 150   # Altura

    # Estilos CSS para o botão e a mensagem de sucesso
    st.markdown("""
        <style>
            .small-button {
                font-size: 12px;  /* Tamanho da fonte */
                padding: 5px 15px;  /* Ajusta o tamanho do botão */
                border-radius: 5px;  /* Arredonda os cantos */
                background-color: #4CAF50;  /* Cor de fundo */
                color: white;  /* Cor do texto */
                border: none;  /* Sem borda */
            }
            .small-button:hover {
                background-color: #45a049;  /* Cor de fundo ao passar o mouse */
            }
            .small-message {
                font-size: 10px;  /* Tamanho da fonte da mensagem */
                color: green;  /* Cor da mensagem */
            }
        </style>
    """, unsafe_allow_html=True)

    # Distribui os produtos entre as 3 colunas fixas
    for i, produto in enumerate(produtos):
        coluna = colunas[i % num_colunas]
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
            if st.button(f"Adicionar {produto['nome']} ao carrinho", key=produto["nome"]):
                st.session_state.carrinho.append(produto)
                # Mensagem de sucesso com estilo personalizado
                st.markdown(f'<p class="small-message">{produto["nome"]} adicionado ao carrinho!</p>', unsafe_allow_html=True)

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
