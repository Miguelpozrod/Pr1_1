import psutil


def listar_procesos(palabra_clave):
    procesos_encontrados = []
    for proceso in psutil.process_iter(['name', 'pid', 'memory_info']):
        try:
            if palabra_clave.lower() in proceso.info['name'].lower():
                procesos_encontrados.append({
                    'nombre': proceso.info['name'],
                    'pid': proceso.info['pid'],
                    'memoria': proceso.info['memory_info'].rss // (1024 * 1024)  # Convertir a MB
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procesos_encontrados


def finalizar_proceso(nombre_proceso):
    for proceso in psutil.process_iter(['name', 'pid']):
        if proceso.info['name'] == nombre_proceso:
            try:
                proceso.terminate()
                proceso.wait(timeout=3)
                return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                return False
    return False


def main():
    palabra_clave = input("Ingrese una palabra clave para filtrar los procesos: ")

    procesos_activos = listar_procesos(palabra_clave)

    if procesos_activos:
        print("\nProcesos activos encontrados:")
        for proceso in procesos_activos:
            print(f"Nombre: {proceso['nombre']}, PID: {proceso['pid']}, Memoria: {proceso['memoria']} MB")
    else:
        print("\nNo se encontraron procesos activos que coincidan con la palabra clave.")

    if input("\n¿Desea finalizar algún proceso? (s/n): ").lower() == 's':
        nombre_finalizar = input("Ingrese el nombre del proceso a finalizar: ")
        if finalizar_proceso(nombre_finalizar):
            print(f"El proceso {nombre_finalizar} ha sido finalizado correctamente.")
        else:
            print(f"No se pudo finalizar el proceso {nombre_finalizar}.")


if __name__ == "__main__":
    main()
