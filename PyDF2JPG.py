import os
from tkinter import Tk, Label, Button, filedialog, Frame, ttk
from pdf2image import convert_from_path
from PIL import Image

class PDFConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("PyDF to JPG Converter")

        self.input_dir = ""
        self.output_dir = ""

        self.frame1 = Frame(master)
        self.frame1.pack()

        self.label1 = Label(self.frame1, text="Selecciona la carpeta de entrada:")
        self.label1.pack(side="left")

        self.input_button = Button(self.frame1, text="Seleccionar Carpeta", command=self.select_input_folder)
        self.input_button.pack(side="left", padx=(5, 0))

        self.frame2 = Frame(master)
        self.frame2.pack()

        self.label2 = Label(self.frame2, text="Selecciona la carpeta de salida:")
        self.label2.pack(side="left")

        self.output_button = Button(self.frame2, text="Seleccionar Carpeta", command=self.select_output_folder)
        self.output_button.pack(side="left", padx=(5, 0))

        self.convert_button = Button(master, text="Convertir PDFs", command=self.convert_pdfs)
        self.convert_button.pack(pady=(10, 0))

        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=(10, 0))

    def select_input_folder(self):
        self.input_dir = filedialog.askdirectory()
        print(f"Directorio de entrada seleccionado: {self.input_dir}")
        self.show_confirmation(self.frame1)

    def select_output_folder(self):
        self.output_dir = filedialog.askdirectory()
        print(f"Directorio de salida seleccionado: {self.output_dir}")
        self.show_confirmation(self.frame2)

    def convert_pdfs(self):
        if not self.input_dir or not self.output_dir:
            print("Selecciona directorios de entrada y salida antes de convertir.")
            return

        pdf_files = [file for file in os.listdir(self.input_dir) if file.lower().endswith('.pdf')]
        total_pages = sum(len(convert_from_path(os.path.join(self.input_dir, pdf_file))) for pdf_file in pdf_files)

        self.progress_bar["maximum"] = total_pages
        self.progress_bar["value"] = 0

        for pdf_file in pdf_files:
            pdf_path = os.path.join(self.input_dir, pdf_file)
            images = convert_from_path(pdf_path)

            for i, image in enumerate(images):
                jpg_path = os.path.join(self.output_dir, f'{os.path.splitext(pdf_file)[0]}_pagina_{i + 1}.jpg')
                image.save(jpg_path, 'JPEG')
                self.progress_bar["value"] += 1
                self.master.update_idletasks()  # Actualiza la interfaz gráfica

            print(f'Se han convertido {len(images)} páginas de "{pdf_file}" a imágenes JPG.')

        print('La conversión de PDF a JPG se ha completado.')

    def show_confirmation(self, frame):
        confirmation_label = Label(frame, text=" ✓ ", fg="green")
        confirmation_label.pack(side="left")

if __name__ == "__main__":
    root = Tk()
    app = PDFConverterApp(root)
    root.mainloop()
