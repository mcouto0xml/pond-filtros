from PIL import Image
import io

"""
Essa função tem a responsabilidade de carregar as imagens em RGB
"""
def load_image(file):
    return Image.open(file).convert("RGB")

"""
Essa função tem a responsabilidade de transformar os objetos do PIL
em PNG, para o usuário baixar
""" 
def image_to_bytes(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf
