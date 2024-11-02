
from rembg import remove
# fornece ao interpretador Python recursos de edição de imagem
from PIL import Image
# Aqui editamos o nome da imagem de entrada.
img_entrada = 'original.jpeg'
# Aqui definimos o nome da imagem de saída.
img_saida = 'editado.png'

input = Image.open(img_entrada)
output = remove(input)

#salvando a imagem de saída
output.save(img_saida, 'PNG')
