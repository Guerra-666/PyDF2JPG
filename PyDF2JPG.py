from pdf2image import convert_from_path
from PIL import Image
import os

# Directorio de entrada donde se encuentran los archivos PDF
input_dir = '/Users/tu_usuario/Desktop/certificados_pdf/'  # Cambia 'directorio_de_entrada/' por tu carpeta de entrada
# Directorio de salida donde se guardarán las imágenes JPG
output_dir = '/Users/tu_usuario/Desktop/imagenes_certificados/'  # Cambia 'directorio_de_salida/' por tu carpeta de salida

# Crea el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Lista todos los archivos en el directorio de entrada
pdf_files = [file for file in os.listdir(input_dir) if file.endswith('.pdf')]

# Convierte cada archivo PDF en imágenes JPG
for pdf_file in pdf_files:
    pdf_path = os.path.join(input_dir, pdf_file)
    images = convert_from_path(pdf_path)
    
    # Guarda cada página como un archivo JPG en el directorio de salida
    for i, image in enumerate(images):
        jpg_path = os.path.join(output_dir, f'{os.path.splitext(pdf_file)[0]}_pagina_{i + 1}.jpg')
        image.save(jpg_path, 'JPEG')

    print(f'Se han convertido {len(images)} páginas de "{pdf_file}" a imágenes JPG.')

print('La conversión de PDF a JPG se ha completado.')
