# PyDF2JPG
---

# Convertidor de PDF a Imágenes JPG

Este script en Python te permite convertir archivos PDF en imágenes JPG de forma sencilla. Es útil cuando deseas extraer páginas de un PDF y guardarlas como imágenes individuales.

## Requisitos

Asegúrate de tener los siguientes requisitos antes de ejecutar este script:

1. Python 3.x (Se recomienda Python 3.6 o superior).
   - [Descargar Python](https://www.python.org/downloads/)

2. Poppler (pdftoppm) instalado en tu sistema.

   - **macOS**: Se puede instalar a través de Homebrew. Ejecuta el siguiente comando en la Terminal:

     ```shell
     brew install poppler
     ```

   - **Windows**: Descarga el [instalador de Poppler para Windows](http://blog.alivate.com.au/poppler-windows/).

   - **Linux**: En la mayoría de las distribuciones de Linux, puedes instalarlo desde el gestor de paquetes. Por ejemplo, en Ubuntu puedes usar:

     ```shell
     sudo apt-get install poppler-utils
     ```

3. Instala las bibliotecas de Python necesarias utilizando `pip`:

   ```shell
   pip install pdf2image pillow
   ```

## Uso

1. Clona o descarga este repositorio.

2. Abre una terminal y navega hasta el directorio donde se encuentra el script `pdf_to_jpg.py`.

3. Ejecuta el script proporcionando la ruta de la carpeta que contiene tus archivos PDF de entrada y la carpeta de salida donde se guardarán las imágenes JPG:

   ```shell
   python pdf_to_jpg.py
   ```

   - Para cambiar las rutas de entrada y salida, edita las variables `input_dir` y `output_dir` en el script con las rutas correctas.

4. El script procesará los archivos PDF en la carpeta de entrada y generará imágenes JPG en la carpeta de salida.

5. ¡Listo! Las imágenes JPG se generarán en la carpeta de salida que especificaste.

## Ejemplo

Supongamos que tienes una carpeta llamada `certificados_pdf` con archivos PDF en tu escritorio y deseas guardar las imágenes JPG en una carpeta llamada `imagenes_certificados`. Debes editar el script como sigue:

```python
# Directorio de entrada donde se encuentran los archivos PDF
input_dir = '/Users/tu_usuario/Desktop/certificados_pdf/' 

# Directorio de salida donde se guardarán las imágenes JPG
output_dir = '/Users/tu_usuario/Desktop/imagenes_certificados/' 
```

Luego, ejecuta el script como se indicó anteriormente.

## Soporte

- Para problemas con el script o preguntas relacionadas, puedes abrir un [issue](https://github.com/Guerra-666/PyDF2JPG/issues) en este repositorio.

---

¡Espero que esta herramienta te sea útil para convertir tus archivos PDF en imágenes JPG de manera sencilla!
