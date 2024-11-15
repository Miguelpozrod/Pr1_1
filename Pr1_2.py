import os
import sys

def hijo(pipe):
    # Cerrar el extremo de escritura de la pipe en el proceso hijo
    os.close(pipe[1])

    # Recibir mensaje del padre
    mensaje = os.read(pipe[0], 100).decode('utf-8')
    print(f"Hijo recibió: {mensaje}")

    # Modificar y enviar mensaje de vuelta
    mensaje_modificado = mensaje.upper()
    os.write(pipe[0], mensaje_modificado.encode('utf-8'))

    # Leer contenido del archivo
    contenido = os.read(pipe[0], 1000).decode('utf-8')

    # Contar líneas y palabras
    lineas = contenido.count('\n')
    palabras = len(contenido.split())

    # Preparar y enviar resultado
    resultado = f"Líneas: {lineas}, Palabras: {palabras}"
    os.write(pipe[0], resultado.encode('utf-8'))

    # Cerrar el extremo de lectura de la pipe
    os.close(pipe[0])

def padre(pipe):
    # Cerrar el extremo de lectura de la pipe en el proceso padre
    os.close(pipe[0])

    # Enviar mensaje al hijo
    mensaje = "Hola, proceso hijo!"
    os.write(pipe[1], mensaje.encode('utf-8'))

    # Leer mensaje modificado del hijo
    mensaje_modificado = os.read(pipe[1], 100).decode('utf-8')
    print(f"Padre recibió: {mensaje_modificado}")

    # Leer y enviar contenido del archivo
    try:
        with open("archivo.txt", "r") as f:
            contenido = f.read()
        os.write(pipe[1], contenido.encode('utf-8'))

        # Leer resultados del hijo
        resultado = os.read(pipe[1], 100).decode('utf-8')
        print(f"Resultados del archivo: {resultado}")

    except FileNotFoundError:
        print("Error: archivo.txt no encontrado")

    # Cerrar el extremo de escritura de la pipe
    os.close(pipe[1])

def main():
    # Crear una única pipe
    pipe = os.pipe()

    # Crear proceso hijo
    pid = os.fork()

    if pid == 0:  # Proceso hijo
        hijo(pipe)
    else:  # Proceso padre
        padre(pipe)
        # Esperar a que el proceso hijo termine
        os.waitpid(pid, 0)

if __name__ == "__main__":
    main()
