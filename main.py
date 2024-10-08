import tkinter as tk
from tkinter import messagebox, Toplevel, ttk, Listbox
from biblioteca import libros, usuarios, prestamos, morosidad
from datetime import datetime, timedelta

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Biblioteca")
        self.imagen = tk.PhotoImage(file="libro-removebg-preview.png")
        self.title_label = tk.Label(root, text="Biblioteca", font=("Times New Roman", 140, "bold italic"), bg="#E8DCBD",
                                    fg="white", compound="center", image=self.imagen)
        self.title_label.pack(pady=0)
        self.centrar_ventana(root, 1000, 700)

        self.create_main_menu()


    def centrar_ventana(self, ventana, ancho, altura):
        ancho_de_la_ventana = ventana.winfo_screenwidth()
        alto_de_la_ventana = ventana.winfo_screenheight()
        x = (ancho_de_la_ventana // 2) - (ancho // 2)
        y = (alto_de_la_ventana // 2) - (altura // 2)
        ventana.geometry(f"{ancho}x{altura}+{x}+{y}")

    def salir_del_programa(self):
        respuesta = messagebox.askokcancel("Salir", "¿Desea salir del programa?")
        if respuesta:
            root.quit()
        else:
            return self.root

    def create_main_menu(self):
        self.menu_bar = tk.Menu(self.root)

        self.menu_libros = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_libros.add_command(label="Agregar Libro", command=self.abrir_ventana_agregar_libro)
        self.menu_libros.add_command(label="Salir", command=self.salir_del_programa)
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

        self.imagen_libro = tk.PhotoImage(file=r"Iconos\libros.png")
        self.imagen_usuarios = tk.PhotoImage(file=r"Iconos\usuarios.png")
        self.imagen_prestamos = tk.PhotoImage(file=r"Iconos\prestamo.png")
        self.imagen_morosidad = tk.PhotoImage(file=r"Iconos\morosidad.png")
        self.imagen_salir = tk.PhotoImage(file=r"Iconos\salir.png")
        self.imagen_agregar_libro = tk.PhotoImage(file=r"Iconos\agregar-libro.png")
        self.imagen_agregar = tk.PhotoImage(file=r"Iconos\agregar.png")
        self.imagen_buscar_libros = tk.PhotoImage(file=r"Iconos\buscar-libro.png")
        self.imagen_eliminar = tk.PhotoImage(file=r"Iconos\eliminar.png")
        self.imagen_listar = tk.PhotoImage(file=r"Iconos\listar.png")
        self.imagen_registrar_usuario = tk.PhotoImage(file=r"Iconos\agregar-usuario.png")
        self.imagen_prestar_libro = tk.PhotoImage(file=r"Iconos\prestar-libro.png")
        self.imagen_devolver_libro = tk.PhotoImage(file=r"Iconos\devolver-libro.png")
        self.imagen_regresar = tk.PhotoImage(file=r"Iconos\regresar.png")

        button = tk.Button(root, text="  Libros", command=self.abrir_ventana_libros, bg="white", fg="#3C372B",
                           font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                           image=self.imagen_libro)
        button.pack(pady=10)
        buttonu = tk.Button(root, text="  Usuarios", command=self.abrir_ventana_usuarios, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_usuarios)
        buttonu.pack(pady=10)
        buttonp = tk.Button(root, text="  Prestamos", command=self.abrir_ventana_prestamos, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_prestamos)
        buttonp.pack(pady=10)
        buttonm = tk.Button(root, text="  Morosidad", command=self.abrir_ventana_morosidad, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_morosidad)
        buttonm.pack(pady=10)
        buttonm = tk.Button(root, text="  Salir", command=self.salir_del_programa, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_salir)
        buttonm.pack(pady=10)

    def abrir_ventana_libros(self):
        ventana = Toplevel(self.root)
        ventana.title("Opción Libro")
        ventana.config(bg="#E8DCBD")
        self.imagen_libro_titulo = tk.PhotoImage(file=r"Iconos\libros-titulo.png")
        label = tk.Label(ventana, text="Libros", font=("Times New Roman", 60, "bold italic"), fg="#3C372B",
                         bg="#E8DCBD", compound="center", image=self.imagen_libro_titulo)
        label.pack(pady=10)
        self.centrar_ventana(ventana, 600, 445)

        button1 = tk.Button(ventana, text="  Agregar Libro", command=self.abrir_ventana_agregar_libro, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=340, height=50,
                            compound="left", image=self.imagen_agregar)
        button2 = tk.Button(ventana, text="  Eliminar Libro", command=self.abrir_ventana_eliminar_libro, bg="white",
                            fg="#730B0B", font=("Times New Roman", 20, "bold italic"), width=340, height=50,
                            compound="left", image=self.imagen_eliminar)
        button3 = tk.Button(ventana, text="  Buscar Libro", command=self.abrir_ventana_buscar_libro, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=340, height=50,
                            compound="left", image=self.imagen_buscar_libros)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=35, height=35,
                            compound="center", image=self.imagen_regresar)

        button1.pack(pady=10)
        button3.pack(pady=10)
        button2.pack(pady=10)
        boton_regresar.pack(pady=10, padx=10, anchor="ne")


    def abrir_ventana_agregar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Agregar Libro")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 540,230)

        label_titulo = tk.Label(ventana, text="Título del Libro:", bg="#E8DCBD", fg="#3C372B",
                                font=("Times New Roman", 25, "bold italic"))
        label_titulo.grid(pady=5, padx=5, sticky="ne", row=0, column=0)

        entry_titulo = tk.Entry(ventana, width=27, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        entry_titulo.grid(row=0, column=1)

        label_autor = tk.Label(ventana, text="Autor:", bg="#E8DCBD", fg="#3C372B",
                               font=("Times New Roman", 25, "bold italic"))
        label_autor.grid(pady=5, padx=5, sticky="ne", row=1, column=0)

        entry_autor = tk.Entry(ventana, width=27, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        entry_autor.grid(row=1, column=1)

        label_isbn = tk.Label(ventana, text="ISBN:", bg="#E8DCBD", fg="#3C372B",
                              font=("Times New Roman", 25, "bold italic"))
        label_isbn.grid(pady=5, padx=5, sticky="ne", row=2, column=0)

        entry_isbn = tk.Entry(ventana, width=27, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        entry_isbn.grid(row=2, column=1)

        #NO TOCAR
        def agregar_libro():
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            isbn = entry_isbn.get()
            if titulo != "" and autor != "" and isbn != "":
                try:
                    if libros.agregar_libro(titulo, autor, isbn):
                        messagebox.showinfo("Éxito", "Libro agregado exitosamente")
                        ventana.destroy()
                    else:
                        messagebox.showwarning("Error", "ISBN Repetido, por favor inserte uno válido")
                        ventana.destroy()
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
            else:
                messagebox.showwarning("Error", "Debe completar todos los campos")


        boton_agregar = tk.Button(ventana, text="  Agregar Libro", command=agregar_libro, bg="white", fg="#3C372B",
                                  font=("Times New Roman", 20, "bold italic"), width=240, height=35, compound="left",
                                  image=self.imagen_agregar_libro)
        boton_agregar.grid(row=3, column=1, pady=5)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=3, column=0, pady=0, padx=10, sticky="sw")

    def abrir_ventana_eliminar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Libro")
        ventana.geometry("240x70")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 700, 500)


        label = tk.Label(ventana, text="Seleccione un libro:", bg="#E8DCBD", fg="#3C372B",
                                font=("Times New Roman", 25, "bold italic"))
        listbox = tk.Listbox(ventana, height=15, width=60, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        label.grid()
        listbox.grid(row=1, column=0, padx=10, sticky="n")
        datos = libros.listar_libros()

        if datos != []:
            for dato in datos:
                dato = f"Libro: {dato}"
                listbox.insert(tk.END, dato)
        else:
            listbox.insert(tk.END, "No hay datos para mostrar")

        def seleccion_eliminar():
            indices = listbox.curselection()
            if indices != ():
                if messagebox.askokcancel("Advertencia ¿Desea eliminar el libro?", message=", "
                        .join(listbox.get(i) for i in indices)):
                    datos = libros.listar_libros_()
                    datos.pop(indices[0])
                    libros.guardar_libro_(datos)
                    messagebox.showinfo("Exito!", "Eliminado exitosamente")
                    ventana.destroy()
                else:
                    ventana.destroy()
                    messagebox.showwarning("Error!", "Debe seleccionar un libro para eliminarlo")

        boton_eliminar = tk.Button(ventana, text="Eliminar Libro", command=seleccion_eliminar, bg="#FFB6B5")
        boton_eliminar.grid(row=2, column=1,  padx=10, sticky="se")
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=2, column=0, pady=0, padx=10, sticky="se")

    def abrir_ventana_buscar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Buscar Libro")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 885, 460)

        label_titulo = tk.Label(ventana, text="Título del Libro:", bg="#E8DCBD", fg="#3C372B",
                                font=("Times New Roman", 25, "bold italic"))
        label_titulo.grid(row=0, column=0)

        entry_titulo = tk.Entry(ventana, width=27, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat",
                                bd=2)
        entry_titulo.grid(row=0, column=1, padx=0)

        text_resultados = tk.Text(ventana, height=18, width=86, fg="#3C372B", font=("Times New Roman", 15, "italic"),
                                  relief="flat", bd=2)
        text_resultados.grid(row=2, column=0, columnspan=4, pady=0, padx=10, ipadx=0)
        def buscar_libro():
            titulo = entry_titulo.get()
            resultados = libros.buscar_libro(titulo)
            text_resultados.delete(1.0, tk.END)
            if resultados:
                for libro in resultados:
                    text_resultados.insert(tk.END, f"ISBN: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}")
            else:
                text_resultados.insert(tk.END, "No se encontraron libros.")

        boton_buscar = tk.Button(ventana, text="  Buscar Libro", command=buscar_libro, bg="white", fg="#3C372B",
                                 font=("Times New Roman", 15, "bold italic"), width=140, height=20, compound="left",
                                 image=self.imagen_buscar_libros)
        boton_buscar.grid(row=0, column=2, pady=0)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=0, column=3, pady=10, padx=10, sticky="ne")


    def abrir_ventana_usuarios(self):
        ventana = Toplevel(self.root)
        ventana.title("Opción Libro")
        ventana.config(bg="#E8DCBD")
        self.imagen_usuarios_titulo = tk.PhotoImage(file=r"Iconos\usuarios-titulo.png")
        label = tk.Label(ventana, text="Usuarios", font=("Times New Roman", 60, "bold italic"), fg="#3C372B",
                         bg="#E8DCBD", compound="center", image=self.imagen_usuarios_titulo)
        label.grid(row=0, column=0, pady=10, padx=110)
        self.centrar_ventana(ventana, 570, 430)


        button1 = tk.Button(ventana, text="  Agregar Usuario", command=self.abrir_ventana_registrar_usuario, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=340, height=50,
                            compound="left", image=self.imagen_agregar)
        button2 = tk.Button(ventana, text="  Eliminar Usuario", command=self.abrir_ventana_eliminar_usuario, bg="white",
                            fg="#730B0B", font=("Times New Roman", 20, "bold italic"), width=340, height=50,
                            compound="left", image=self.imagen_eliminar)
        button3 = tk.Button(ventana, text="  Listar Usuarios", command=self.abrir_ventana_listar_usuario, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=340, height=50,
                            compound="left", image=self.imagen_listar)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=4, column=0, pady=0, padx=10, sticky="ne")
        button1.grid(row=1, column=0, pady=10, padx=110)
        button3.grid(row=2, column=0, pady=10, padx=110)
        button2.grid(row=3, column=0, pady=10, padx=110)


    def abrir_ventana_registrar_usuario(self):
        ventana = Toplevel(self.root)
        ventana.title("Registrar Usuario")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 560, 150)

        label_nombre = tk.Label(ventana, text="Nombre del usuario:", bg="#E8DCBD", fg="#3C372B",
                                font=("Times New Roman", 25, "bold italic"))
        label_nombre.grid(row=0, column=0)

        entry_nombre = tk.Entry(ventana, width=27, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        entry_nombre.config(width=25)
        entry_nombre.grid(row=0, column=1, padx=5)

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

        boton_registrar = tk.Button(ventana, text="  Registrar Usuario", command=registrar_usuario, bg="white",
                            fg="#3C372B", font=("Times New Roman", 18, "bold italic"), width=225, height=25,
                            compound="left", image=self.imagen_registrar_usuario)
        boton_registrar.grid(row=2, column=1, pady=5)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=1, column=0, pady=10, padx=10, sticky="w")

    def abrir_ventana_eliminar_usuario(self):
        ventana = Toplevel(self.root)
        ventana.title("Eliminar Usuario")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 625, 520)

        listbox = tk.Listbox(ventana, height=15, width=60, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)

        listbox.grid(row=1, column=0, padx=10)
        datos = usuarios.listar_usuarios_()
        if datos != []:
            for dato in datos:
                dato = f"Usuario: {dato}"
                listbox.insert(tk.END, dato)
        else:
            listbox.insert(tk.END, "No hay datos para mostrar")
        def seleccion_eliminar():
            indices = listbox.curselection()
            if indices != ():
                if messagebox.askokcancel("Advertencia ¿Desea eliminar el usuario?", message=", "
                        .join(listbox.get(i) for i in indices)):
                    datos = usuarios.listar_usuarios_()
                    datos.pop(indices[0])
                    usuarios.guardar_usuarios_(datos)
                    messagebox.showinfo("Exito!", "Eliminado exitosamente")
                    ventana.destroy()
                else:
                    ventana.destroy()

            else:
                messagebox.showwarning("Error!", "Debe seleccionar un usuario para eliminar")
        boton_eliminar = tk.Button(ventana, text="Eliminar Usuario", command=seleccion_eliminar, bg="#FFB6B5")
        boton_eliminar.grid(row=1, column=1)
        boton_eliminar.grid(row=2, column=0, pady=10)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        boton_regresar.grid(pady=10, padx=10, sticky="se")

    def abrir_ventana_listar_usuario(self):
        ventana = Toplevel(self.root)
        ventana.title("Listar Usuarios")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 725, 455)
        text_resultados = tk.Text(ventana, height=18, width=70, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        text_resultados.grid(row=2, column=0, columnspan=2, padx=10)

        def listar_u():
            resultados = usuarios.listar_usuarios()
            text_resultados.delete(1.0, tk.END)
            if resultados:
                for i, user in enumerate(resultados, start=1):
                    text_resultados.insert(tk.END,
                                           f"Usuario: {user[0]}, ID Usuario: {user[1]}\n")
            else:
                text_resultados.insert(tk.END, "No se encontraron usuarios.")

        boton_listar = tk.Button(ventana, text="  Listar Usuario", command=listar_u, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=225, height=25,
                            compound="left", image=self.imagen_listar)
        boton_listar.grid(row=1, column=1, pady=5)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=1, column=0, pady=10, padx=10, sticky="w")

    def abrir_ventana_prestamos(self):
        ventana = Toplevel(self.root)
        ventana.title("Opción Prestamos")
        ventana.config(bg="#E8DCBD")
        self.imagen_prestamos_titulo = tk.PhotoImage(file=r"Iconos\prestamos-titulo.png")
        label = tk.Label(ventana, text="Prestamos", font=("Times New Roman", 60, "bold italic"), fg="#3C372B",
                         bg="#E8DCBD", compound="center", image=self.imagen_prestamos_titulo)
        label.pack(pady=10)
        self.centrar_ventana(ventana, 500, 368)


        button1 = tk.Button(ventana, text=" Prestar Libro", command=self.abrir_ventana_prestar_libro, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_prestar_libro)
        button2 = tk.Button(ventana, text="  Devolver Libro", command=self.abrir_ventana_devolver_libro, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_devolver_libro)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=35, height=35,
                                   compound="center", image=self.imagen_regresar)
        button1.pack(pady=10)
        button2.pack(pady=10)
        boton_regresar.pack(pady=10, padx=10, anchor="se")

    def abrir_ventana_prestar_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Prestar Libro")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 540, 140)

        label_isbn = tk.Label(ventana, text=" ISBN del Libro:", bg="#E8DCBD", fg="#3C372B",
                                font=("Times New Roman", 25, "bold italic"))
        label_isbn.grid(row=0, column=0)

        entry_combo = ttk.Combobox(ventana, state="readonly", values=libros.listar_libros_(), width=27, font=("Times New Roman", 15, "italic"))
        entry_combo.grid(row=0, column=1)

        label_id_usuario = tk.Label(ventana, text=" ID del Usuario:", bg="#E8DCBD", fg="#3C372B",
                                font=("Times New Roman", 25, "bold italic"))
        label_id_usuario.grid(row=1, column=0)

        entry_combo_u = ttk.Combobox(ventana, state="readonly", values=usuarios.listar_usuarios_(), width=27, font=("Times New Roman", 15, "italic"))
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

        boton_prestar = tk.Button(ventana, text="Prestar Libro", command=prestar_libro, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=225, height=30, compound="left",
                            image=self.imagen_prestar_libro)
        boton_prestar.grid(row=2, column=1)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        boton_regresar.grid(row=2, column=0, pady=10, padx=10, sticky="w")

    def abrir_ventana_devolver_libro(self):
        ventana = Toplevel(self.root)
        ventana.title("Devolver Libro")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 570, 537)

        listbox = tk.Listbox(ventana, height=15, width=60, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        label = tk.Label(ventana, text="Seleccione un libro:", bg="#E8DCBD", fg="#3C372B",
                         font = ("Times New Roman", 25, "bold italic"))
        label.pack(pady=0)
        listbox.pack(pady=10, padx=10)
        datos = prestamos.listar_prestamos_()
        if datos != []:
            for dato in datos:
                dato = f"Prestamo: {dato}"
                listbox.insert(tk.END, dato)
        else:
            listbox.insert(tk.END, "No hay datos para mostrar")
        def seleccion_eliminar():
            indices = listbox.curselection()
            if indices != ():
                if messagebox.askokcancel("Advertencia ¿Desea devolver el libro?", message=", "
                        .join(listbox.get(i) for i in indices)):
                    datos = prestamos.listar_prestamos_()
                    dat = datos[indices[0]]
                    dat = dat.split(", ")
                    dat = dat[1].split(" - ")
                    libros.agregar_libro(dat[1], dat[2], dat[0])
                    datos.pop(indices[0])
                    prestamos.guardar_prestamos_(datos)
                    messagebox.showinfo("Exito!", "Devuelto exitosamente")
                    ventana.destroy()
                else:
                    ventana.destroy()

        boton_devolver = tk.Button(ventana, text="Devolver Libro", command=seleccion_eliminar, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=340, height=50, compound="left",
                            image=self.imagen_devolver_libro)
        boton_devolver.pack(pady=10)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        boton_regresar.pack(pady=0, padx=10, anchor="se")


    def abrir_ventana_morosidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Opción Morosidad")
        ventana.config(bg="#E8DCBD")
        self.imagen_morosidad_titulo = tk.PhotoImage(file=r"Iconos\morosidad-titulo.png")
        label = tk.Label(ventana, text="Morosidad", font=("Times New Roman", 60, "bold italic"), fg="#3C372B",
                         bg="#E8DCBD", compound="center", image=self.imagen_morosidad_titulo)
        label.pack(pady=10)
        self.centrar_ventana(ventana, 660, 360)


        button1 = tk.Button(ventana, text="  Ver Morosidad", command=self.abrir_ventana_verificar_morosidad, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=400, height=50, compound="left",
                            image=self.imagen_morosidad)
        button2 = tk.Button(ventana, text="  Devolver Libro con Morosidad", command=self.abrir_ventana_devolver_libro_c_mora, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=400, height=50, compound="left",
                            image=self.imagen_devolver_libro)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white",
                            fg="#3C372B", font=("Times New Roman", 20, "bold italic"), width=25, height=25,
                            compound="center", image=self.imagen_regresar)
        button1.pack(pady=10, padx=10)
        button2.pack(pady=10, padx=10)
        boton_regresar.pack(pady=10, padx=10, anchor="se")
    def abrir_ventana_verificar_morosidad(self):
        ventana = Toplevel(self.root)
        ventana.title("Ver Prestamos Con Mora")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 1250, 380)

        listbox = tk.Listbox(ventana, height=15, width=130, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        listbox.pack(pady=10, padx=10)
        datos = morosidad.leer_prestamos_p_morosidad_rec()
        if datos != []:
            for dato in datos:
                dato = f"Prestamo: {dato}"
                listbox.insert(tk.END, dato)
        else:
            listbox.insert(tk.END, "No hay datos para mostrar")


    def abrir_ventana_devolver_libro_c_mora(self):
        ventana = Toplevel(self.root)
        ventana.title("Devolver Libro Con Mora")
        ventana.config(bg="#E8DCBD")
        self.centrar_ventana(ventana, 570, 537)

        listbox = tk.Listbox(ventana, height=15, width=60, fg="#3C372B", font=("Times New Roman", 15, "italic"), relief="flat", bd=2)
        label = tk.Label(ventana, text="Seleccione un libro:", bg="#E8DCBD", fg="#3C372B",
                         font = ("Times New Roman", 25, "bold italic"))
        label.pack(pady=0)
        listbox.pack(pady=10, padx=10)
        datos = prestamos.listar_prestamos_()
        if datos != []:
            for dato in datos:
                dato = f"Prestamo: {dato}"
                listbox.insert(tk.END, dato)
        else:
            listbox.insert(tk.END, "No hay datos para mostrar")
        def seleccion_eliminar():
            indices = listbox.curselection()
            if indices != ():
                if messagebox.askokcancel("Advertencia ¿Desea devolver con Mora?", message=", "
                        .join(listbox.get(i) for i in indices)):
                    datos = prestamos.listar_prestamos_()
                    dat = datos[indices[0]]
                    dat = dat.split(", ")
                    fecha_prestamo = dat[2]
                    dat = dat[1].split(" - ")
                    fecha_prestamo_dt = datetime.strptime(fecha_prestamo, '%Y-%m-%d')
                    fecha_limite = fecha_prestamo_dt + timedelta(days=15)
                    fecha_actual = datetime.today()
                    if fecha_actual > fecha_limite:
                        diferencia = fecha_actual - fecha_limite
                        dias_mora = diferencia.days
                        mora_total = dias_mora * 6
                        if messagebox.askokcancel("MORA",f"Tu mora es de: {dias_mora} días y debes pagar: {mora_total}.00 Qtz" ):
                            libros.agregar_libro(dat[1], dat[2], dat[0])
                            datos.pop(indices[0])
                            prestamos.guardar_prestamos_(datos)
                            messagebox.showinfo("Exito!", "Devuelto con mora exitosamente")
                            ventana.destroy()
                        else:
                            ventana.destroy()
                    else:
                        messagebox.showinfo("Sin Mora", "No hay mora para este préstamo.")
                else:
                    ventana.destroy()

        boton_devolver = tk.Button(ventana, text="Devolver Libro Con Mora", command=seleccion_eliminar, bg="white", fg="#3C372B",
                            font=("Times New Roman", 20, "bold italic"), width=360, height=50, compound="left",
                            image=self.imagen_devolver_libro)
        boton_devolver.pack(pady=10)
        boton_regresar = tk.Button(ventana, command=ventana.destroy, bg="white", width=25, height=25,
                                   compound="center", image=self.imagen_regresar)
        boton_regresar.pack(pady=0, padx=10, anchor="se")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")
    root.config(bg="#E8DCBD")
    app = BibliotecaApp(root)
    root.mainloop()
