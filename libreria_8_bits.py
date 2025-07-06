# El proyecto debe cumplir con los siguientes parametros:
# iniciar sesion
# Poder registrar un libro
# Registrar un socio
# Te vise si un libro esta prestado 
# Devolver un libro 
# Ver que libros estan prestados

#.strip para que no quede un espacio despues de que el usuario escriba en su imput


#libreria rich and questionary para mejorar la usabilidad y los colores en la terminal
from rich import print
import questionary as qs 

#base de datos de memoria
libros = []
socios = []
contador_isbn = 0

#Muestra el menu en la terminal
def mostrar_menu():
    while True:
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        print("                                            [green]La libreria de 8 bits[/green]                                                        ")
        print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
        #El texto que te dice que debes hacer
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

#Funcion para registrar un nuevo libro - terminado
def registrar_libro():
    global libros, contador_isbn
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
            main()
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
        registrar_libro()
        return
    
    autor = input("Ingrese el nombre del autor: ").strip().title()
    if not autor:
        print("❌ El nombre del autor no puede estar vacio ❌")
        registrar_libro()
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
        registrar_libro()
        return
    
    
    #Esto es una revision para que no registre dos veces el mismo nombre
    for libro in libros:
        if libro ['title'] == titulo:
            print("Ya existe un libro registrado con ese nombre")
            registrar_libro
            
    contador_isbn += 1
        
    nuevo_libro = {
        'isbn': str(contador_isbn),
        'title': titulo,
        'autor': autor,
        'estado': "Disponible",
        'socio_prestado': None 
    }
    
    libros.append(nuevo_libro)
    print("Libro creado exitosamente")
    print(f"\nSe ha registrado el libro llamado [blue]{titulo}[/blue] ✅")
    print(f"Autor: [green]{autor}[/green]")
    print(f"ISBN: {contador_isbn}")
    
    respuesta = qs.select(
        "Quiere registrar un nuevo libro?",
        choices=[
            "Si",
            "No"
        ]
    ).ask()
    
    if respuesta == "Si":
        registrar_libro()
    else:
        main()
    
    print("[bold blue]==========================================================================================================[/bold blue]")
        

#Funcion para registrar un nuevo socio - terminado
def registrar_socio():
    global socios
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
            main()
            return
        registrar_socio()
    print(f"Se va a registral el nombre {nombre_socio}, es correcto? ")
    respuesta = qs.select(
        "Es correcto? Use las flechas de ↑ ↓  y la tecla Enter.",
        choices=[
            "Si",
            "No"
        ]
    ).ask()
    if respuesta != "Si":
        registrar_socio()
    
    apellido_socio = input("Ingrese el apellido del nuevo socio: ").strip().capitalize()
    if not apellido_socio:
        print("❌ Ingrese un apellido, este espacio no puede estar vacio ❌")
        registrar_socio()
        
    id_socio = input("Ingrese su iD: ")
    if not id_socio:
        print("❌ Este espacio no puede estar vacio ❌")
        registrar_socio
        return
    
    for id in socios:
        if id['id_socio'] == nombre_socio:
            print("Este usuario ya esta registrado")
    
    nuevo_socio = {
        'nombre': nombre_socio,
        'apellido': apellido_socio,
        'id_socio': id_socio
    }
    
    socios.append(nuevo_socio)
    
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
        registrar_socio()
        return
    else:
        main()
        
    

#Funcion para prestar un libro -  terminado
def prestar_libro():
    global libros, socios
    
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    print("                                            [green]La libreria de 8 bits[/green]                                                        ")
    print("                                               [red]Prestar un libro[/red]                                                              ")
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    
    isbn = input("Ingrese el ISBN del libro que quiere rentar: ").strip().lower()
    if not isbn:
        print("❌ El ISBN no puede estar vacio ❌")
        
    libro_encontrado = None
    for libro in libros:
        if libro['isbn'] == isbn:
            libro_encontrado = libro
            break
        
    if not libro_encontrado:
        print(f"No se encontro el libro con el ISBN {isbn}")
        prestar_libro
        return 
    
    id_socio = input("Ingrese el nombre del socio: ").strip().capitalize()
    if not id_socio:
        print("❌ El nombre del socio no puede estar vacio ❌")
        
    socio_encontrado = None
    for socio in socios:
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
    
        

#Funcion para devolver el libro
#Se necesita saber el nombre del socio
def devoler_libro():
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    print("                                            [green]La libreria de 8 bits[/green]                                                        ")
    print("                                               [red]Prestar un libro[/red]                                                              ")
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    
    global socios, libros
    usuario = input("Ingrese el nombre del usuario: ")
    if not usuario:
        print("El campo de usuario no puede estar vacio")
        devoler_libro
        return
    
    
    #Es un ciclo para buscar el nombre del socio en el diccionario, si si encuentra, entonces la variable socio_encontrado pasara a llamarse socio que es el nombre asignado en el ciclo
    
    socio_encontrado = False
    
    for socio in socios:
        if socio['nombre'] == usuario:
            socio_encontrado = socio
    
    # Se crea una variable llamda libro devolver. Esto con el fin de que si no encuentra el libro en el ciclo no me rompa el codigo.
    # Si lo encuentra, entonces socio_encontrado ahora se asiganara el valor de libro
    
    libro_devolver = False
    
    libro_devolver = input("Ingrese el ISBN del libro a devolver")
    if not libro_devolver:
        print("El ISBN no puede estar vacio, ingrese el ISBN correcto")
        devoler_libro()
        return
    
    for libro in libros:
        if libro['isbn'] == libro_devolver:
            libro_devolver = libro
            pregunta = qs.select(
                f"Usted desea regresar el libro {libro_devolver['title']}",
                choices=[
                    "Si",
                    "No"
                ]
            ).ask()
            
            if pregunta == "Si":
                libro_devolver['estado'] = "Disponible"
                libro_devolver['socio_prestado'] = None
                print(f"Gracias {usuario}")
                print(f"El libro {libros['title']}ha sido regresado exitosamente")
            else:
                devoler_libro
                return
    respuesta = qs.select(
        f"Quiere devolver otro libro {usuario}?",
        choices=[
            "Si",
            "No"
        ]
    ).ask()
    
    if respuesta == "Si":
        devoler_libro()
    else:
        main()


#Funcion para ver cuantos libros se prestaron - terminado
def ver_libros_prestados():
    global libros
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    print("                                            [green]La libreria de 8 bits[/green]                                                        ")
    print("                                               [red]Prestar un libro[/red]                                                              ")
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    
    libros_prestados = []
    for prestados in libros:
        if prestados['estado'] != "Disponible":
            libros_prestados.append(prestados)
    
    for libro in libros_prestados:
        print(f"{libro['title']} prestado")
        
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
        main()
    else:
        ver_libros_prestados()

#Funcion para ver todos los libros, prestados o no - terminado  
def ver_todos_libros():
    global libros
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    print("                                            [green]La libreria de 8 bits[/green]                                                        ")
    print("                                               [red]Prestar un libro[/red]                                                              ")
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    print("\nLa lista de libros de la biblioteca de 8 bits son:\n")
    for libro in libros:
        print(f"{libro['title']}")
        
    pregunta = qs.select(
        "\nQuiere salir al menu principal?",
        choices=[
            "Si",
            "No"
        ]
    ).ask()
    
    if pregunta == "Si":
        main()
    else:
        ver_todos_libros()
    

#Funcion para ver todos los socios registrados
def ver_todos_socios():
    global socios
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    print("                                            [green]La libreria de 8 bits[/green]                                                        ")
    print("                                               [red]Prestar un libro[/red]                                                              ")
    print("[bold blue]---------------------------------------------------------------------------------------------------------------- [/bold blue]")
    print("\nLa lista de socios en la libreria de 8 bits son:")
    
    for socio in socios:
        print(f"{socio['nombre']}")
    
    pregunta = qs.select(
        "Quieres volver al menu principal?",
        choices=[
            "Si",
            "No"
        ]
    ).ask()
    
    if pregunta == "Si":
        main()
    else:
        ver_todos_socios

def main():
    while True:
        option = mostrar_menu()
        match option:
            case "Registrar un libro":
                registrar_libro()
            case "Registrar un socio":
                registrar_socio()
            case "Prestar libro":
                prestar_libro()
            case "Devolver libro":
                devoler_libro()
            case "Ver libros prestados":
                ver_libros_prestados()
            case "Ver todos los libros":
                ver_todos_libros()
            case "Ver todos los socios":
                ver_todos_socios()
            case "Salir":
                print("[green]Gracias por usar La biblioteca de 8 bits[/green]")
                print("[green]Hasta luego 👋[/green]")
                break 
            case _:
                print("Opcion no valida, seleccione una opcion valida")
                
main()