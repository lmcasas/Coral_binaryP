def guardar_mensaje_en_txt(mensaje, nombre_archivo):
    try:
        # Abre el archivo en modo escritura
        with open(nombre_archivo, 'w') as archivo:
            # Escribe el mensaje en el archivo
            archivo.write(mensaje)
        print("Mensaje guardado exitosamente en", nombre_archivo)
    except IOError:
        print("Error al guardar el mensaje en el archivo", nombre_archivo)

# Ejemplo de uso
mensaje = "Este es un mensaje de ejemplo."
nombre_archivo = "prueba.txt"
guardar_mensaje_en_txt(mensaje, nombre_archivo)