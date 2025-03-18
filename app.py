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
    ]

    # Exibição dos produtos
    for produto in produtos:
        col1, col2 = st.columns([1, 2])
        with col1:
            imagem = Image.open(produto["imagem"])
            st.image(imagem, use_container_width=True)  # Substitua use_column_width por use_container_width
        with col2:
            st.subheader(produto["nome"])
            st.write(f"Preço: R${produto['preco']:.2f}")
            st.write(produto["descricao"])
            if st.button(f"Adicionar {produto['nome']} ao carrinho"):
                st.success(f"{produto['nome']} adicionado ao carrinho!")

if __name__ == "__main__":
    exibir_produtos()
