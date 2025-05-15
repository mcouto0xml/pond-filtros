from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import cv2
import numpy as np

"""
Essa função é responsável por filtrar a imagem em grayscale, que são as variações de cor do branco ao preto (0 a 255)
"""
def to_grayscale(img):
    return img.convert("L").convert("RGB")

"""
Essa função é responsável por filtrar a imagem para inverter seus valores RGB, pixel invertido = 255 - pixel original
"""
def invert_colors(img):
    return ImageOps.invert(img)

"""
Essa função é responsável por filtrar a imagem para aumentar o contraste do seus valores, isso é, deixar algo claro ainda mais claro e algo escuro ainda mais escuro
"""
def increase_contrast(img, factor=1.5):
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)

"""
Essa função é responsável por filtrar a imagem para borrar seus pixels, isto é, substituir um pixel pela média do valor dos vizinhos
"""
def blur_image(img):
    return img.filter(ImageFilter.GaussianBlur(radius=2))

"""
Essa função é responsável por filtrar a imagem para procurar suas diferenças maiores, no caso é aplicado uma operação matemática chamada convolução, que destaca grandes diferenças no números, mas mantém valores parecidos como estão. Assim disfarçando ruídos e mostrando bordas em preto e branco!
"""
def edge_detection(img):
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(img_cv, 100, 200)
    return Image.fromarray(edges).convert("RGB")

"""
A função de Nitidez tem princípios parecidos com a de detecção de bordas, porém possuem objetivos diferentes e máscaras diferentes para a convolução. O objetivo da Nitidez é aumentar a diferença entre pixels vizinhos, para conseguir realçar melhor diferenças, não destacar somente as grandes diferenças em preto e branco.
"""
def sharpen_image(img):
    return img.filter(ImageFilter.SHARPEN)
