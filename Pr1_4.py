import ftplib
import pyperclip
import time

def descargar_archivo_ftp():
    try:
        # Conectarse al servidor FTP público
        ftp = ftplib.FTP('ftp.dlptest.com')
        ftp.login('dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')

        # Descargar el archivo README
        with open('README', 'wb') as file:
            ftp.retrbinary('RETR README', file.write)

        ftp.quit()
        print("Archivo descargado exitosamente.")
    except ftplib.all_errors as e:
        print(f"Error al conectarse o descargar archivo: {e}")

def copiar_a_portapapeles():
    try:
        with open('README', 'r') as file:
            contenido = file.read()
        pyperclip.copy(contenido)
        print("Contenido copiado al portapapeles.")
        return contenido
    except FileNotFoundError:
        print("El archivo README no se encontró.")
        return None

def verificar_portapapeles(contenido_original):
    try:
        while True:
            contenido_actual = pyperclip.paste()
            if contenido_actual != contenido_original:
                print("El contenido del portapapeles ha cambiado.")
                print("Nuevo contenido:", contenido_actual)
                contenido_original = contenido_actual
            time.sleep(2)  # Esperar 2 segundos antes de la siguiente verificación
    except KeyboardInterrupt:
        print("\nVerificación del portapapeles detenida.")

def main():
    descargar_archivo_ftp()
    contenido_original = copiar_a_portapapeles()

    if contenido_original:
        print("Iniciando verificación del portapapeles...")
        verificar_portapapeles(contenido_original)

if __name__ == "__main__":
    main()
