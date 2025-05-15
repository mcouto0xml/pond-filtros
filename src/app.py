import streamlit as st
import filters
import transforms
import utils
from PIL import Image


st.set_page_config(page_title="Visualizador de Imagens", layout="wide")
st.title("Visualizador de Imagens com Filtros")
background = Image.open("img/gato.png")
st.image(background, caption="Gato foda", use_container_width=True)

# Upload da imagem
uploaded_file = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

# Caso o upload tenha acontecido com sucesso
if uploaded_file:

    # Faz uma cópia da imagem do upload 
    image = utils.load_image(uploaded_file)
    processed_image = image.copy()

    # Separa as imagens em duas colunas/seções, mas apenas mostra a Imagem Original por enquanto
    col1, col2 = st.columns(2)
    col1.image(image, caption="Imagem Original", use_container_width=True)

    # Mostra a possibilidade de filtros em uma lista (função do Streamlite)
    st.subheader("Filtros")
    selected_filters = st.multiselect(
        "Selecione os filtros para aplicar",
        ["Escala de cinza", "Inversão de cores", "Aumento de contraste", "Desfoque", "Nitidez", "Detecção de bordas"]
    )

    # Para cada filtro selecionado aplicar um método da nossa classe de filtros
    for f in selected_filters:
        if f == "Escala de cinza":
            processed_image = filters.to_grayscale(processed_image)
        elif f == "Inversão de cores":
            processed_image = filters.invert_colors(processed_image)
        elif f == "Aumento de contraste":
            processed_image = filters.increase_contrast(processed_image)
        elif f == "Desfoque":
            processed_image = filters.blur_image(processed_image)
        elif f == "Nitidez":
            processed_image = filters.sharpen_image(processed_image)
        elif f == "Detecção de bordas":
            processed_image = filters.edge_detection(processed_image)

    # Aplica transformações de rotação, conforme um slider na visualização
    st.subheader("Transformações")
    angle = st.slider("Rotação (graus)", -180, 180, 0)
    if angle != 0:
        processed_image = transforms.rotate_image(processed_image, angle)

    # Agora sim mostra a segunda coluna/seção com a imagem já modificada
    col2.image(processed_image, caption="Imagem Modificada", use_container_width=True)

    # Aqui é feito o download da imagem
    st.subheader("Salvar imagem")
    img_bytes = utils.image_to_bytes(processed_image)
    st.download_button("Baixar imagem", data=img_bytes, file_name="imagem_editada.png", mime="image/png")
