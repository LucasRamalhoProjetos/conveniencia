import streamlit as st
from PIL import Image
import math

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
        {"nome": "Produto 7", "preco": 18.00, "descricao": "Chocolate", "imagem": "imagens/produto7.jpg"},
        {"nome": "Produto 8", "preco": 5.50, "descricao": "Refrigerante", "imagem": "imagens/produto8.jpg"},
    ]

    # Inicializa o estado da sessão para o carrinho de compras
    if 'carrinho' not in st.session_state:
        st.session_state.carrinho = []

    # Define o número mínimo de colunas (2) e o máximo (5)
    num_colunas = min(max(3, len(produtos) // 3), 5)  # Dividir por 3 para que os produtos caibam bem nas colunas

    # Cria as colunas
    colunas = st.columns(num_colunas)

    # Define o tamanho fixo da imagem
    largura_imagem = 300
    altura_imagem = 300

    # Distribui os produtos entre as colunas
    for i, produto in enumerate(produtos):
        coluna = colunas[i % num_colunas]
        with coluna:
            try:
                imagem = Image.open(produto["imagem"])
                imagem = imagem.resize((largura_imagem, altura_imagem))  # Redimensiona a imagem
                st.image(imagem, use_container_width=True)
            except FileNotFoundError:
                st.error(f"Imagem não encontrada: {produto['imagem']}")
            st.subheader(produto["nome"])
            st.write(f"Preço: R${produto['preco']:.2f}")
            st.write(produto["descricao"])
            if st.button(f"Adicionar {produto['nome']} ao carrinho", key=produto["nome"]):
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
