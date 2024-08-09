import tkinter as tk
from tkinter import messagebox, Toplevel, ttk, Listbox
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

        button = tk.Button(root, text="Libros", command=self.abrir_ventana_libros, bg="#E0D7BF")
        button.pack(pady=10)
        buttonu = tk.Button(root, text="Usuarios", command=self.abrir_ventana_usuarios, bg="#E0D7BF")
        buttonu.pack(pady=10)
        buttonp = tk.Button(root, text="Prestamos", command=self.abrir_ventana_prestamos, bg="#E0D7BF")
        buttonp.pack(pady=10)
        buttonm = tk.Button(root, text="Morosidad", command=self.abrir_ventana_morosidad, bg="#E0D7BF")
        buttonm.pack(pady=10)

        self.root.config(menu=self.menu_bar)

    def abrir_ventana_libros(self):
        ventana = Toplevel(self.root)
        ventana.title("Opción Libro")
        ventana.config(bg="#EFEBDF")

        button1 = tk.Button(ventana, text="Agregar Libro", command=self.abrir_ventana_agregar_libro, bg="#E0D7BF")
        button2 = tk.Button(ventana, text="Eliminar Libro", command=self.abrir_ventana_eliminar_libro, bg="#FFB6B5")
        button3 = tk.Button(ventana, text="Buscar Libro", command=self.abrir_ventana_buscar_libro, bg="#E0D7BF")
        button1.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)

    def abrir_ventana_agregar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Agregar Libro")
        ventana.config(bg="#EFEBDF")

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

        #NO TOCAR
        def agregar_libro():
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            isbn = entry_isbn.get()
            if titulo != "" and autor != "" and isbn != "":
                try:
                    libros.agregar_libro(titulo, autor, isbn)
                    messagebox.showinfo("Éxito", "Libro agregado exitosamente")
                    ventana.destroy()
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showwarning("Error", "Debe completar todos los campos")

        boton_agregar = tk.Button(ventana, text="Agregar Libro", command=agregar_libro, bg="#E0D7BF")
        boton_agregar.grid(row=3, column=1)

    def abrir_ventana_eliminar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Libro")
        ventana.config(bg="#EFEBDF")

        label_isbn = tk.Label(ventana, text="ISBN del Libro:")
        label_isbn.grid(row=0, column=0)

        entry_isbn = tk.Entry(ventana)
        entry_isbn.grid(row=0, column=1)

        def eliminar_libro():
            isbn = entry_isbn.get()
            if isbn != "":
                libros.eliminar_libro(isbn)
                messagebox.showinfo("Éxito", "Libro eliminado exitosamente")
                ventana.destroy()
            else:
                messagebox.showwarning("Advertencia!", "Debe agregar un dato válido")
        boton_eliminar = tk.Button(ventana, text="Eliminar Libro", command=eliminar_libro, bg="#FFB6B5")
        boton_eliminar.grid(row=1, column=1)

    def abrir_ventana_buscar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Buscar Libro")
        ventana.config(bg="#EFEBDF")

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
                    text_resultados.insert(tk.END, f"Título: {libro[0]}, Autor: {libro[1]}, ISBN: {libro[2]}\n")
            else:
                text_resultados.insert(tk.END, "No se encontraron libros.")

        boton_buscar = tk.Button(ventana, text="Buscar Libro", command=buscar_libro, bg="#E0D7BF")
        boton_buscar.grid(row=1, column=1)

    def abrir_ventana_usuarios(self):
        ventana = Toplevel(self.root)
        ventana.title("Opción Libro")
        ventana.config(bg="#EFEBDF")

        button1 = tk.Button(ventana, text="Agregar Usuario", command=self.abrir_ventana_registrar_usuario, bg="#E0D7BF")
        button2 = tk.Button(ventana, text="Eliminar Usuario", command=self.abrir_ventana_eliminar_usuario, bg="#FFB6B5")
        button3 = tk.Button(ventana, text="Listar usuarios", command=self.abrir_ventana_listar_usuario, bg="#E0D7BF")
        button1.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)

    def abrir_ventana_registrar_usuario(self):
        ventana = Toplevel(self.root)
        ventana.title("Registrar Usuario")
        ventana.config(bg="#EFEBDF")

        label_nombre = tk.Label(ventana, text="Nombre del Usuario:")
        label_nombre.grid(row=0, column=0)

        entry_nombre = tk.Entry(ventana)
        entry_nombre.grid(row=0, column=1)

        def registrar_usuario():
            nombre = entry_nombre.get()

            if nombre != "":
                try:
                    usuarios.registrar_usuario(nombre)
                    messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
                    ventana.destroy()
                except ValueError as e:
                    messagebox.showerror("Error", str(e))

            else:
                messagebox.showwarning("Advertencia", "Debe completar los campos")

        boton_registrar = tk.Button(ventana, text="Registrar Usuario", command=registrar_usuario, bg="#E0D7BF")
        boton_registrar.grid(row=2, column=1)

    def abrir_ventana_eliminar_usuario(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Usuario")
        ventana.config(bg="#EFEBDF")

        label_id_usuario = tk.Label(ventana, text="ID del Usuario:")
        label_id_usuario.grid(row=0, column=0)

        entry_id_usuario = tk.Entry(ventana)
        entry_id_usuario.grid(row=0, column=1)

        def eliminar_usuario():

            id_usuario = entry_id_usuario.get()
            if id_usuario == "":
                try:
                    usuarios.eliminar_usuario(id_usuario)
                    messagebox.showinfo("Éxito", "Usuario eliminado exitosamente")
                    ventana.destroy()
                except ValueError:
                    messagebox.showwarning("Info", "Escriba un dato válido")
        boton_eliminar = tk.Button(ventana, text="Eliminar Usuario", command=eliminar_usuario, bg="#FFB6B5")
        boton_eliminar.grid(row=1, column=1)

    def abrir_ventana_listar_usuario(self):
        ventana = Toplevel(self.root)
        ventana.title("Listar Usuarios")
        ventana.config(bg="#EFEBDF")

        text_resultados = tk.Text(ventana, height=10, width=50)
        text_resultados.grid(row=2, column=0, columnspan=2)
        def listar_u():
            resultados = usuarios.listar_usuarios()
            text_resultados.delete(1.0, tk.END)
            if resultados:
                for i, user in enumerate(resultados, start=1):
                   text_resultados.insert(tk.END,
                         f"Usuario: {user[0]}, ID Usuario: {user[1]}\n")
            else:
                text_resultados.insert(tk.END, "No se encontraron usuarios.")

        boton_eliminar = tk.Button(ventana, text="Listar Usuario", command=listar_u, bg="#E0D7BF")
        boton_eliminar.grid(row=1, column=1)

    def abrir_ventana_prestamos(self):
        ventana = Toplevel(self.root)
        ventana.title("Opción Prestamos")
        ventana.config(bg="#EFEBDF")

        button1 = tk.Button(ventana, text="Prestar Libro", command=self.abrir_ventana_prestar_libro, bg="#E0D7BF")
        button2 = tk.Button(ventana, text="Devolver Libro", command=self.abrir_ventana_devolver_libro, bg="#E0D7BF")
        button1.pack(pady=10)
        button2.pack(pady=10)
    def abrir_ventana_prestar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Prestar Libro")
        ventana.config(bg="#EFEBDF")
        ventana.geometry("300x300")

        label_isbn = tk.Label(ventana, text="ISBN del Libro:")
        label_isbn.grid(row=0, column=0)

        entry_combo = ttk.Combobox(ventana, state="readonly", values=libros.listar_libros_())
        entry_combo.grid(row=0, column=1)

        label_id_usuario = tk.Label(ventana, text="ID del Usuario:")
        label_id_usuario.grid(row=1, column=0)

        entry_combo_u = ttk.Combobox(ventana, state="readonly", values=usuarios.listar_usuarios_())
        entry_combo_u.grid(row=1, column=1)

        def prestar_libro():
            isbn = entry_combo.get()
            id_usuario = entry_combo_u.get()

            try:
                prestamos.prestar_libro(isbn, id_usuario)
                messagebox.showinfo("Éxito", "Libro prestado exitosamente")
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        boton_prestar = tk.Button(ventana, text="Prestar Libro", command=prestar_libro, bg="#E0D7BF")
        boton_prestar.grid(row=2, column=1)

    def abrir_ventana_devolver_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Devolver Libro")
        ventana.config(bg="#EFEBDF")

        label_isbn = tk.Label(ventana, text="Selecciona el Libro para Devolver:")
        label_isbn.grid(row=0, column=0, padx=10, pady=10)

        listbox_libros = Listbox(ventana, selectmode=tk.SINGLE, width=50, height=10)
        listbox_libros.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Leer los datos de prestamos.txt y llenar el Listbox
        with open("PRESTAMOS.txt", "r") as prestamos_file:
            prestamos = prestamos_file.readlines()

        for prestamo in prestamos:
            listbox_libros.insert(tk.END, prestamo.strip())

        def devolver_libro():
            # Obtener la selección del Listbox
            seleccion = listbox_libros.curselection()
            if seleccion:
                libro_seleccionado = listbox_libros.get(seleccion[0])
                # Separar la parte del libro y el usuario
                parte_libro, parte_usuario = libro_seleccionado.split(",")

                # Extraer el ISBN, título y autor
                isbn_titulo_autor = parte_libro.strip()

                # Devolver el libro y actualizar los archivos
                devolver_libro_a_biblioteca(isbn_titulo_autor, libro_seleccionado)

                messagebox.showinfo("Éxito", "Libro devuelto exitosamente")
                ventana.destroy()
            else:
                messagebox.showwarning("Advertencia", "Por favor, selecciona un libro para devolver")

        def devolver_libro_a_biblioteca(isbn_titulo_autor, libro_seleccionado):
            # Añadir el libro de nuevo a LIBROS.txt
            with open("LIBROS.txt", "a") as libros_file:
                libros_file.write(f"{isbn_titulo_autor}\n")

            # Eliminar el préstamo de PRESTAMOS.txt
            with open("PRESTAMOS.txt", "r") as prestamos_file:
                prestamos = prestamos_file.readlines()

            with open("PRESTAMOS.txt", "w") as prestamos_file:
                for prestamo in prestamos:
                    if prestamo.strip() != libro_seleccionado:
                        prestamos_file.write(prestamo)

        boton_devolver = tk.Button(ventana, text="Devolver Libro", command=devolver_libro, bg="#E0D7BF")
        boton_devolver.grid(row=2, column=0, columnspan=2, pady=10)


    def abrir_ventana_morosidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Opción Morosidad")
        ventana.config(bg="#EFEBDF")

        button1 = tk.Button(ventana, text="Morosidad", command=self.abrir_ventana_prestar_libro,bg="#E0D7BF")
        button2 = tk.Button(ventana, text="Devolver Libro con Morosidad", command=self.abrir_ventana_devolver_libro,bg="#E0D7BF")
        button1.pack(pady=10)
        button2.pack(pady=10)

    def abrir_ventana_verificar_morosidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Verificar Morosidad")
        ventana.config(bg="#EFEBDF")

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

        boton_verificar = tk.Button(ventana, text="Verificar Morosidad", command=verificar_morosidad, bg="#E0D7BF")
        boton_verificar.grid(row=2, column=1)

if __name__ == "__main__":
    root = tk.Tk()
    #tamaño de la pantalla principal
    root.geometry("300x200")
    root.config(bg="#EFEBDF")
    app = BibliotecaApp(root)
    root.mainloop()
