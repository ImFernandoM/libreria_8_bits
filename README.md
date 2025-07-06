# 📚 La Librería de 8 Bits

Un mini sistema de gestión de biblioteca desarrollado en Python, diseñado para ejecutarse desde la terminal de manera interactiva y amigable, gracias a las librerías `rich` y `questionary`.

## 🎯 Funcionalidades

Este proyecto permite:

- ✅ Iniciar sesión en el sistema (menú principal)
- 📖 Registrar libros con título, autor y un identificador único (ISBN)
- 🧑‍💼 Registrar socios con nombre, apellido e ID
- 📕 Prestar libros a los socios registrados
- 📗 Devolver libros previamente prestados
- 📋 Ver los libros que se encuentran actualmente prestados
- 📚 Ver todos los libros registrados
- 🧾 Ver todos los socios registrados

## 🧠 Detalles técnicos

- Se utiliza `.strip()` para evitar espacios en blanco al inicio o final de las entradas del usuario.
- Todo se gestiona en memoria, no hay base de datos persistente.
- Uso de `questionary` para mejorar la interacción del usuario con menús amigables.
- Uso de `rich` para dar color y formato a la salida en terminal.

## 🧰 Requisitos

Asegúrate de tener instalado:

- Python 3.8 o superior
- Las siguientes librerías (pueden instalarse con pip):

```bash
pip install rich
```
```bash
pip install questionary 
```

## 🚀 Ejecución
Clona el repositorio o descarga el archivo .py.

Ejecuta el script principal:

bash
Copiar
Editar
python biblioteca.py
Usa las teclas ↑ ↓ y Enter para navegar por el menú.

## 📝 Notas adicionales
Los datos no se guardan entre sesiones, ya que no hay uso de archivos ni bases de datos.

Ideal como práctica para principiantes que desean aplicar estructuras como listas, diccionarios, condicionales, funciones y bucles en Python.

El menú principal se ejecuta en bucle hasta que el usuario seleccione “Salir”.

### Desarrollado por: Fernando Martinez
Versión: 1.0
Licencia: MIT
