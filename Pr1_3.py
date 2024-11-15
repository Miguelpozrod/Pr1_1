import subprocess
import asyncio
import time


async def ejecutar_asincrono():
    print("Iniciando ejecución asíncrona...")
    inicio = time.time()

    proceso = await asyncio.create_subprocess_exec(
        'notepad.exe',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    await proceso.communicate()

    fin = time.time()
    tiempo_total = fin - inicio
    print(f"Tiempo de ejecución asíncrona: {tiempo_total:.4f} segundos")


def ejecutar_sincrono():
    print("Iniciando ejecución síncrona...")
    inicio = time.time()

    subprocess.run(['notepad.exe'], check=True)

    fin = time.time()
    tiempo_total = fin - inicio
    print(f"Tiempo de ejecución síncrona: {tiempo_total:.4f} segundos")


async def main():
    while True:
        opcion = input("Seleccione el tipo de ejecución (s: síncrona, a: asíncrona, q: salir): ").lower()

        if opcion == 's':
            ejecutar_sincrono()
        elif opcion == 'a':
            await ejecutar_asincrono()
        elif opcion == 'q':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    asyncio.run(main())
