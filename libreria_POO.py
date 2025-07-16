import questionary as qs
from rich import print

class Menu:
    def __init__(self):
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        #El texto que te dice que debes hacer
    
    def seleccionar_opcion(self):
        respuesta = qs.select(
            "Que quieres hacer? (Use las flechas de ↑ ↓  y la tecla Enter.)",
            #opciones para el menu con teclado
            choices=[
                "Registrar un libro",
                "Registrar un socio",
                "Prestar libro",
                "Devolver libro",
                "Ver libros prestados",
                "Ver todos los libros",
                "Ver todos los socios",
                "Salir"
            ]
            
        ).ask()
        return respuesta
    
    def seleccionar_opcion(self):
        option = Menu()
        match option:
            case "Registrar un libro": Biblioteca.registrar_libro()
            case "Registrar un socio": Biblioteca.registrar_socio()
            case "Prestar libro": Biblioteca.prestar_libro()
            case "Devolver libro": Biblioteca.devoler_libro()
            case "Ver libros prestados": Biblioteca.ver_libros_prestados()
            case "Ver todos los libros": Biblioteca.ver_todos_libros()
            case "Ver todos los socios": Biblioteca.ver_todos_socios()
            case "Salir":
                print("[green]Gracias por usar La biblioteca de 8 bits[/green]")
                print("[green]Hasta luego 👋[/green]")
                return
            case _: print("Opcion no valida, seleccione una opcion valida")
                


class Libro:
    def __init__(self, isbn, titulo, autor):
        #Atributos
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.estado = "Disponible"
        self.socio_prestado = None
        
        #Metodos
    def prestado (self, socio_id):
        if self.prestado == "Disponible":
            self.prestado = "Prestado"
            self.socio_prestado = socio_id
            return True #todo salio bien 
        return False
    
    def devolver(self, socio_id):
        self.prestado = "Disponible"
        self.socio_prestado = None

class socio:
    #Atributos
    def __init__(self, id, nombre, apellido, email):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido 
        self.email = email
        self.libros_prestados = []
    
    #Metodos
    

class Biblioteca:
    #atributos 
    def __init__(self):
        self.libros = [] # lista de libros objetos
        self.socios = [] # listos de socios registrados 
        self.contador_socios = 1
    
    def registrar_libro(self):
        
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("                                               [red]Registrar un libro[/red]                                                            ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")

        titulo = input("Ingrese el nombre del libro o precione Enter para salir: ").strip().capitalize()
        if not titulo:
            respuesta = qs.select(
                "Desea salir del sistema?",
                choices=[
                    "Si",
                    "No"
                ]
            ).ask()
            if respuesta != "No":
                Menu
                return
                registrar_libro()
        
        print(f"Se va a ingresar el nombre [blue]{titulo}[/blue]")
        #Se coloco la opcion que confirme con las teclas si esta correcto el nombre que quiere registrar
        respuesta = qs.select(
            "Es correcto? Use las flechas de ↑ ↓  y la tecla Enter.",
            choices=[
                "Si",
                "No"
            ]
        ).ask()
        if respuesta != "Si":
            self.registrar_libro()
            return
        
        autor = input("Ingrese el nombre del autor: ").strip().title()
        if not autor:
            print("❌ El nombre del autor no puede estar vacio ❌")
            self.registrar_libro
            return
        #Se coloco la opcion que confirme con las teclas si esta correcto el nombre que quiere registrar
        print(f"Se va a ingresar el autor [blue]{autor}[/blue]")
        respuesta = qs.select(
                "Es correcto? Use las flechas de ↑ ↓  y la tecla Enter.",
                choices=[
                    "Si",
                    "No"
                ]
            ).ask()
        if respuesta != "Si":
            self.registrar_libro()
            return
        
        
        #Esto es una revision para que no registre dos veces el mismo nombre
        for libro in self.libros:
            if libro ['title'] == titulo:
                print("Ya existe un libro registrado con ese nombre")
                self.registrar_libro
                
        isbn = str(input("Ingrese el numero ISBN del libro: "))
            
        self.libros.append(Libro(isbn, titulo, autor))
        
        print("Libro creado exitosamente")
        print(f"\nSe ha registrado el libro llamado [blue]{titulo}[/blue] ✅")
        print(f"Autor: [green]{autor}[/green]")
        print(f"ISBN: {isbn}")
        
        respuesta = qs.select(
            "Quiere registrar un nuevo libro?",
            choices=[
                "Si",
                "No"
            ]
        ).ask()
        
        if respuesta == "Si":
            self.registrar_libro()
        else:
            Menu
        
        print("[bold blue]==========================================================================================================[/bold blue]")
     
     
    def ver_todos_libros(self):
    
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("                                               [red]Ver todos los libros[/red]                                                              ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("\nLa lista de libros de la biblioteca de 8 bits son:\n")
        for libro in self.libros:
            print(f"{libro[self.titulo]}")
            
        pregunta = qs.select(
            "\nQuiere salir al menu principal?",
            choices=[
                "Si",
                "No"
            ]
        ).ask()
        
        if pregunta == "Si":
           Menu
        else:
            self.ver_todos_libros()
    
    def registrar_socio(self):
    
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("                                               [red]Registrar un socio[/red]                                                            ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        
        nombre_socio = input("Ingrese el nombre del nuevo socio o precione Enter para salir: ").strip().capitalize()
        if not nombre_socio:
            respuesta = qs.select(
                "Desea salir del sistema?",
                choices=[
                    "Si",
                    "No"
                ]
            ).ask()
            if respuesta != "No":
                Menu()
                return
            self.registrar_socio()
        print(f"Se va a registral el nombre {nombre_socio}, es correcto? ")
        respuesta = qs.select(
            "Es correcto? Use las flechas de ↑ ↓  y la tecla Enter.",
            choices=[
                "Si",
                "No"
            ]
        ).ask()
        if respuesta != "Si":
            self.registrar_socio()
        
        apellido_socio = input("Ingrese el apellido del nuevo socio: ").strip().capitalize()
        if not apellido_socio:
            print("❌ Ingrese un apellido, este espacio no puede estar vacio ❌")
            self.registrar_socio()
            
        id_socio = input("Ingrese su iD: ")
        if not id_socio:
            print("❌ Este espacio no puede estar vacio ❌")
            self.registrar_socio
            return
        
        for id in self.socios:
            if id['id_socio'] == nombre_socio:
                print("Este usuario ya esta registrado")
        
        nuevo_socio = {
            'nombre': nombre_socio,
            'apellido': apellido_socio,
            'id_socio': id_socio
        }
        
        self.socios.append(nuevo_socio)
        
        print("Nuevo usuario creado exitosamente ✅")
        print(f"El nuevo socio es [green]{nombre_socio} {apellido_socio}[/green]")
        
        print("[bold blue]==========================================================================================================[/bold blue]")

        respuesta = qs.select(
            "Desea ingresar un nuevo socio?",
            choices=[
                "Si",
                "No"
            ]
        ).ask()
        
        if respuesta == "Si":
            self.contador_socios()
            return
        else:
            Menu()
            
        
    def prestar_libro(self):
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("                                               [red]Rentar un libro[/red]                                                              ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        
        isbn = input("Ingrese el ISBN del libro que quiere rentar: ").strip().lower()
        if not isbn:
            print("❌ El ISBN no puede estar vacio ❌")
            
        libro_encontrado = None
        for libro in self.libros:
            if libro['isbn'] == isbn:
                libro_encontrado = libro
                break
            
        if not libro_encontrado:
            print(f"No se encontro el libro con el ISBN {isbn}")
            self.prestar_libro
            return 
        
        id_socio = input("Ingrese el nombre del socio: ").strip().capitalize()
        if not id_socio:
            print("❌ El nombre del socio no puede estar vacio ❌")
            
        socio_encontrado = None
        for socio in self.socios:
            if socio['nombre'] == id_socio:
                socio_encontrado = socio
                print("[green]Socio encontrado exitosamente[/green]")
                break
            
        if not socio_encontrado:
            print("❌ Socio no encontrado ❌")
            
        if libro_encontrado['estado'] == "Disponible":
            libro_encontrado['estado'] = "Libro prestado"
            libro_encontrado['socio_prestado'] = id_socio
            print(f"Felicidades [blue]{id_socio}[/blue]")
            print(f"has adquirido con exito el libro [green]{libro_encontrado['title']}[/green]")
        else:
            print("No es posible rentar el libro.")
            print("Consulte con el equipo de libreria de 8 bits.")
    
    
    def devolver_libro(self):
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("                                               [red]Devoler un libro[/red]                                                              ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        
        usuario = input("Ingrese el nombre del usuario: ")
        if not usuario:
            print("El campo de usuario no puede estar vacio")
            self.devolver_libro
            return
        
        #Es un ciclo para buscar el nombre del socio en el diccionario, si si encuentra, entonces la variable socio_encontrado pasara a llamarse socio que es el nombre asignado en el ciclo
        
        socio_encontrado = False
        
        for socio in self.socios:
            if socio['nombre'] == usuario:
                socio_encontrado = socio
        
        # Se crea una variable llamda libro devolver. Esto con el fin de que si no encuentra el libro en el ciclo no me rompa el codigo.
        # Si lo encuentra, entonces socio_encontrado ahora se asiganara el valor de libro
        
        libro_devolver = False
        
        libro_devolver = input("Ingrese el ISBN del libro a devolver")
        if not libro_devolver:
            print("El ISBN no puede estar vacio, ingrese el ISBN correcto")
            self.devolver_libro()
            return
        
        for libro in self.libros:
            if libro['isbn'] == libro_devolver:
                libro_devolver = libro
                pregunta = qs.select(
                    f"Usted desea regresar el libro {libro_devolver[self.titulo]}",
                    choices=[
                        "Si",
                        "No"
                    ]
                ).ask()
                
                if pregunta == "Si":
                    libro_devolver[self.estado] = "Disponible"
                    libro_devolver['socio_prestado'] = None
                    print(f"Gracias {usuario}")
                    print(f"El libro {self.libros[self.titulo]}ha sido regresado exitosamente")
                else:
                    self.devoler_libro
                    return
        respuesta = qs.select(
            f"Quiere devolver otro libro {usuario}?",
            choices=[
                "Si",
                "No"
            ]
        ).ask()
        
        if respuesta == "Si":
            self.devolver_libro()
        else:
            Menu()


    def libros_disponibles(self):
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("                                               [red]Libros disponibles[/red]                                                              ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        
        libros_prestados = []
        for prestados in self.libros:
            if prestados['estado'] != "Disponible":
                libros_prestados.append(prestados)
        
        for self.libro in libros_prestados:
            print(f"{self.libro['title']} prestado")
            
        if libros_prestados == []:
            print("No hay libros actualmente prestados en la biblioteca")
            
        pregunta = qs.select(
            "Desea regresar al menu principal?",
            choices=[
                "Si",
                "No"
            ]
        ).ask()
        
        if pregunta == "Si":
            Menu()
        else:
            self.libros_disponibles()
            
    def ver_todos_libros(self):
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("                                               [red]Ver todos los libros[/red]                                                              ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("\nLa lista de libros de la biblioteca de 8 bits son:\n")
        for libro in self.libros:
            print(f"{libro[self.titulo]}")
            
        pregunta = qs.select(
            "\nQuiere salir al menu principal?",
            choices=[
                "Si",
                "No"
            ]
        ).ask()
        
        if pregunta == "Si":
            Menu()
        else:
            self.ver_todos_libros()


    def ver_todos_socios(self):

        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("                                               [red]Ver todos los socios[/red]                                                              ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("\nLa lista de socios en la libreria de 8 bits son:")
        
        for socio in self.socios:
            print(f"{socio['nombre']}")
        
        pregunta = qs.select(
            "Quieres volver al menu principal?",
            choices=[
                "Si",
                "No"
            ]
        ).ask()
        
        if pregunta == "Si":
            Menu()
        else:
            self.ver_todos_socios()
        
bibiloteca1 = Biblioteca()
menu1 = Menu()
menu1.seleccionar_opcion()
