import tkinter as tk
from tkinter import messagebox, Toplevel
from biblioteca import libros, usuarios, prestamos, morosidad

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Biblioteca")
        self.create_main_menu()

    def create_main_menu(self):
        self.menu_bar = tk.Menu(self.root)

        self.menu_libros = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_libros.add_command(label="Agregar Libro", command=self.abrir_ventana_agregar_libro)
        self.menu_libros.add_command(label="Eliminar Libro", command=self.abrir_ventana_eliminar_libro)
        self.menu_libros.add_command(label="Buscar Libro", command=self.abrir_ventana_buscar_libro)
        self.menu_bar.add_cascade(label="Libros", menu=self.menu_libros)

        self.menu_usuarios = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_usuarios.add_command(label="Registrar Usuario", command=self.abrir_ventana_registrar_usuario)
        self.menu_usuarios.add_command(label="Eliminar Usuario", command=self.abrir_ventana_eliminar_usuario)
        self.menu_bar.add_cascade(label="Usuarios", menu=self.menu_usuarios)

        self.menu_prestamos = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_prestamos.add_command(label="Prestar Libro", command=self.abrir_ventana_prestar_libro)
        self.menu_prestamos.add_command(label="Devolver Libro", command=self.abrir_ventana_devolver_libro)
        self.menu_bar.add_cascade(label="Préstamos", menu=self.menu_prestamos)

        self.menu_morosidad = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_morosidad.add_command(label="Verificar Morosidad", command=self.abrir_ventana_verificar_morosidad)
        self.menu_bar.add_cascade(label="Morosidad", menu=self.menu_morosidad)

        self.root.config(menu=self.menu_bar)

    def abrir_ventana_agregar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Agregar Libro")

        label_titulo = tk.Label(ventana, text="Título del Libro:")
        label_titulo.grid(row=0, column=0)

        entry_titulo = tk.Entry(ventana)
        entry_titulo.grid(row=0, column=1)

        label_autor = tk.Label(ventana, text="Autor:")
        label_autor.grid(row=1, column=0)

        entry_autor = tk.Entry(ventana)
        entry_autor.grid(row=1, column=1)

        label_isbn = tk.Label(ventana, text="ISBN:")
        label_isbn.grid(row=2, column=0)

        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=2, column=1)

        def agregar_libro():
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            isbn = entry_isbn.get()

            try:
                libros.agregar_libro(titulo, autor, isbn)
                messagebox.showinfo("Éxito", "Libro agregado exitosamente")
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        boton_agregar = tk.Button(ventana, text="Agregar Libro", command=agregar_libro)
        boton_agregar.grid(row=3, column=1)

    def abrir_ventana_eliminar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Libro")

        label_isbn = tk.Label(ventana, text="ISBN del Libro:")
        label_isbn.grid(row=0, column=0)

        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=0, column=1)

        def eliminar_libro():
            isbn = entry_isbn.get()
            libros.eliminar_libro(isbn)
            messagebox.showinfo("Éxito", "Libro eliminado exitosamente")
            ventana.destroy()

        boton_eliminar = tk.Button(ventana, text="Eliminar Libro", command=eliminar_libro)
        boton_eliminar.grid(row=1, column=1)

    def abrir_ventana_buscar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Buscar Libro")

        label_titulo = tk.Label(ventana, text="Título del Libro:")
        label_titulo.grid(row=0, column=0)

        entry_titulo = tk.Entry(ventana)
        entry_titulo.grid(row=0, column=1)

        text_resultados = tk.Text(ventana, height=10, width=50)
        text_resultados.grid(row=2, column=0, columnspan=2)

        def buscar_libro():
            titulo = entry_titulo.get()
            resultados = libros.buscar_libro(titulo)
            text_resultados.delete(1.0, tk.END)
            if resultados:
                for libro in resultados:
                    text_resultados.insert(tk.END, f"Título: {libro['titulo']}, Autor: {libro['autor']}, ISBN: {libro['isbn']}\n")
            else:
                text_resultados.insert(tk.END, "No se encontraron libros.")

        boton_buscar = tk.Button(ventana, text="Buscar Libro", command=buscar_libro)
        boton_buscar.grid(row=1, column=1)


    def abrir_ventana_registrar_usuario(self):
        ventana = Toplevel(self.root)
        ventana.title("Registrar Usuario")

        label_nombre = tk.Label(ventana, text="Nombre del Usuario:")
        label_nombre.grid(row=0, column=0)

        entry_nombre = tk.Entry(ventana)
        entry_nombre.grid(row=0, column=1)

        label_id_usuario = tk.Label(ventana, text="ID del Usuario:")
        label_id_usuario.grid(row=1, column=0)

        entry_id_usuario = tk.Entry(ventana)
        entry_id_usuario.grid(row=1, column=1)

        def registrar_usuario():
            nombre = entry_nombre.get()
            id_usuario = entry_id_usuario.get()

            try:
                usuarios.registrar_usuario(nombre, id_usuario)
                messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        boton_registrar = tk.Button(ventana, text="Registrar Usuario", command=registrar_usuario)
        boton_registrar.grid(row=2, column=1)

    def abrir_ventana_eliminar_usuario(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Usuario")

        label_id_usuario = tk.Label(ventana, text="ID del Usuario:")
        label_id_usuario.grid(row=0, column=0)

        entry_id_usuario = tk.Entry(ventana)
        entry_id_usuario.grid(row=0, column=1)

        def eliminar_usuario():
            id_usuario = entry_id_usuario.get()
            usuarios.eliminar_usuario(id_usuario)
            messagebox.showinfo("Éxito", "Usuario eliminado exitosamente")
            ventana.destroy()

        boton_eliminar = tk.Button(ventana, text="Eliminar Usuario", command=eliminar_usuario)
        boton_eliminar.grid(row=1, column=1)

    def abrir_ventana_prestar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Prestar Libro")

        label_isbn = tk.Label(ventana, text="ISBN del Libro:")
        label_isbn.grid(row=0, column=0)

        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=0, column=1)

        label_id_usuario = tk.Label(ventana, text="ID del Usuario:")
        label_id_usuario.grid(row=1, column=0)

        entry_id_usuario = tk.Entry(ventana)
        entry_id_usuario.grid(row=1, column=1)

        def prestar_libro():
            isbn = entry_isbn.get()
            id_usuario = entry_id_usuario.get()

            try:
                prestamos.prestar_libro(isbn, id_usuario)
                messagebox.showinfo("Éxito", "Libro prestado exitosamente")
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        boton_prestar = tk.Button(ventana, text="Prestar Libro", command=prestar_libro)
        boton_prestar.grid(row=2, column=1)

    def abrir_ventana_devolver_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Devolver Libro")

        label_isbn = tk.Label(ventana, text="ISBN del Libro:")
        label_isbn.grid(row=0, column=0)

        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=0, column=1)

        label_id_usuario = tk.Label(ventana, text="ID del Usuario:")
        label_id_usuario.grid(row=1, column=0)

        entry_id_usuario = tk.Entry(ventana)
        entry_id_usuario.grid(row=1, column=1)

        def devolver_libro():
            isbn = entry_isbn.get()
            id_usuario = entry_id_usuario.get()

            prestamos.devolver_libro(isbn, id_usuario)
            messagebox.showinfo("Éxito", "Libro devuelto exitosamente")
            ventana.destroy()

        boton_devolver = tk.Button(ventana, text="Devolver Libro", command=devolver_libro)
        boton_devolver.grid(row=2, column=1)
    def abrir_ventana_verificar_morosidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Verificar Morosidad")

        label_isbn = tk.Label(ventana, text="ISBN del Libro:")
        label_isbn.grid(row=0, column=0)

        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=0, column=1)

        label_id_usuario = tk.Label(ventana, text="ID del Usuario:")
        label_id_usuario.grid(row=1, column=0)

        entry_id_usuario = tk.Entry(ventana)
        entry_id_usuario.grid(row=1, column=1)

        def verificar_morosidad():
            isbn = entry_isbn.get()
            id_usuario = entry_id_usuario.get()

            if morosidad.morosidad(isbn, id_usuario):
                messagebox.showwarning("Morosidad", "El usuario tiene morosidad con este libro")
            else:
                messagebox.showinfo("Sin Morosidad", "El usuario no tiene morosidad con este libro")

        boton_verificar = tk.Button(ventana, text="Verificar Morosidad", command=verificar_morosidad)
        boton_verificar.grid(row=2, column=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
