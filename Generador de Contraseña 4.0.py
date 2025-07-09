import time
import sys
import os
import secrets 
import string

# ================================
# Efectos visuales y animación
# ================================

def escribir(texto, velocidad=0.05):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Calavera más realista estilo pirata
calavera = [
    "      ______",
    "   .-'      '-.",
    "  /            \\",
    " |              |",
    " |,  .-.  .-.  ,|",
    " | )(_o/  \\o_)( |",
    " |/     /\\     \\|",
    " (_     ^^     _)",
    "  \\__|IIIIII|__/",
    "   | \\IIIIII/ |",
    "   \\          /",
    "    `--------`",
    "     //    \\\\",
    "    ||      ||",
    "    ||      ||",
    "    []      []"
]

def mostrar_calavera():
    limpiar()
    for linea in calavera:
        print(linea)
        time.sleep(0.12)
    print()

def mensaje_final():
    escribir("\n>>> SISTEMA SEGURO ACTIVADO <<<", 0.07)
    escribir(">>> CONTRASEÑA SEGURA <<<", 0.07)

# ================================
# Generador de contraseñas
# ================================

diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}

def generar_contraseña(longitud, usar_letras, usar_numeros, usar_caracteres):
    tipo = ''
    if usar_letras == 's':
        tipo += diccionario['letras']
    if usar_numeros == 's':
        tipo += diccionario['numeros']
    if usar_caracteres == 's':
        tipo += diccionario['caracteres']

    if tipo == '':
        print("\nERROR: Debés seleccionar al menos un tipo de carácter.\n")
        return None

    contraseña = ''.join(secrets.choice(tipo) for _ in range(longitud))
    return contraseña

# ================================
# Validación de entrada 's' o 'n'
# ================================

def validar_sn(texto):
    while True:
        r = input(texto).lower()
        if r in ['s', 'n']:
            return r
        print("Respuesta inválida. Ingresá 's' o 'n'.")

# ================================
# Programa principal
# ================================

while True:
    print("\n" + "*" * 60)
    mostrar_calavera()
    mensaje_final()
    print("*" * 60)

    longitud_ingresada = input("¿Cuántos caracteres querés que tenga tu contraseña?: ")

    if not longitud_ingresada.isdigit():
        print("Error: Solo se aceptan números enteros positivos.")
        continue

    longitud = int(longitud_ingresada)

    if longitud <= 0:
        print("Error: La longitud debe ser mayor a cero.")
        continue

    letras = validar_sn("¿Querés incluir letras? (s/n): ")
    numeros = validar_sn("¿Querés incluir números? (s/n): ")
    caracteres = validar_sn("¿Querés incluir símbolos? (s/n): ")

    resultado = generar_contraseña(longitud, letras, numeros, caracteres)

    if resultado:
        print("\n" + "-" * 60)
        print(f"TU CONTRASEÑA SEGURA GENERADA ES:\n\n{resultado}")
        print("-" * 60)

    repetir = input("\n¿Generar otra contraseña? (s/n): ").lower()
    if repetir != 's':
        print("\nGracias por usar el generador de contraseñas seguras. Bye.")
        break