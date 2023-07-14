import os
from PIL import Image

def convert_to_webp(image_path):
    image = Image.open(image_path)
    new_image_path = os.path.splitext(image_path)[0] + '.webp'
    image.save(new_image_path, 'webp')
    print(f'{image_path} convertida para {new_image_path}')
    os.remove(image_path)
    print(f'{image_path} excluída')

def convert_folder_to_webp(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            convert_to_webp(image_path)

# Substitua 'caminho_da_pasta' pelo caminho da sua pasta contendo as imagens
convert_folder_to_webp(r'C:\Users\First Iformática\OneDrive\Área de Trabalho\site\Projeto-Setor-G\veiculos_gtav\assets\images\vans')