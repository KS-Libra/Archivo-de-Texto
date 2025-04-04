# Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Escribir al menos tres líneas de notas personales en el archivo
    file.write("Esta es mi primera nota personal.\n")
    file.write("Esta es mi segunda nota personal.\n")
    file.write("Esta es mi tercera nota personal.\n")

# Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt
with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea
    for line in file:
        # Mostrar cada línea leída en la consola
        print(line.strip())
# Cerrar archivo
