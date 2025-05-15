"""
Essa função é responsável por rotacionar a imagem conforme parâmetros
"""
def rotate_image(img, angle):
    return img.rotate(angle, expand=True)
