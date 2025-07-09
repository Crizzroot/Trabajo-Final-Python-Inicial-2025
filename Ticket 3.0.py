import random
import json
import os

# Archivo donde se almacenarán los tickets
ARCHIVO_TICKETS = "tickets.json"

# Verificamos si existe el archivo y lo cargamos
if os.path.exists(ARCHIVO_TICKETS):
    with open(ARCHIVO_TICKETS, 'r', encoding="utf-8") as archivo:
        tickets = json.load(archivo)
        # Convertimos las claves a enteros por seguridad
        tickets = {int(k): v for k, v in tickets.items()}
else:
    tickets = {}

def guardar_tickets():
    with open(ARCHIVO_TICKETS, 'w', encoding="utf-8") as archivo:
        json.dump(tickets, archivo, indent=4, ensure_ascii=False)

def alta_ticket():
    while True:
        print("\n" + "="*50)
        print("               ALTA DE TICKET")
        print("="*50)

        nombre = input("Nombre del usuario: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Descripción del problema: ")

        numero = random.randint(1000, 9999)
        while numero in tickets:
            numero = random.randint(1000, 9999)

        tickets[numero] = {
            "nombre": nombre,
            "sector": sector,
            "asunto": asunto,
            "problema": problema
        }

        guardar_tickets()  # Guarda el ticket en el archivo

        print("\n" + "-"*50)
        print(f"TICKET N°: {numero}")
        print("-"*50)
        print(f"NOMBRE   : {nombre}")
        print(f"SECTOR   : {sector}")
        print(f"ASUNTO   : {asunto}")
        print(f"PROBLEMA : {problema}")
        print("-"*50)
        print("IMPORTANTE: Recordá este número para futuras consultas.")
        print("-"*50)

        continuar = input("\n¿Deseás crear otro ticket? (s/n): ").lower()
        if continuar != "s":
            break

def leer_ticket():
    while True:
        print("\n" + "="*50)
        print("                LECTURA DE TICKET")
        print("="*50)

        nro = input("Ingresá el número de ticket (0 para volver): ")
        if nro == "0":
            break

        if nro.isdigit() and int(nro) in tickets:
            ticket = tickets[int(nro)]
            print("\n" + "-"*50)
            print(f"TICKET N°: {nro}")
            print("-"*50)
            print(f"NOMBRE   : {ticket['nombre']}")
            print(f"SECTOR   : {ticket['sector']}")
            print(f"ASUNTO   : {ticket['asunto']}")
            print(f"PROBLEMA : {ticket['problema']}")
            print("-"*50)
        else:
            print("\nTICKET INEXISTENTE O NÚMERO INVÁLIDO.")

        continuar = input("\n¿Deseás leer otro ticket? (s/n): ").lower()
        if continuar != "s":
            break

# Menú principal
while True:
    print("\n" + "*"*50)
    print("              SISTEMA DE TICKETS")
    print("*"*50)
    print("1) Alta ticket")
    print("2) Leer ticket")
    print("3) Salir")
    print("*"*50)

    opcion = input("Seleccioná una opción: ")

    match opcion:
        case "1":
            alta_ticket()
        case "2":
            leer_ticket()
        case "3":
            confirmar = input("¿Estás seguro que querés salir? (s/n): ").lower()
            if confirmar == "s":
                print("\nFinalizando el sistema... Hasta luego.")
                print("-"*50)
                break
        case _:
            print("\nOpción inválida. Intentá nuevamente.")
