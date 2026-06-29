"""
=====================================================================
 GENERADOR SEGURO DE CONTRASEÑAS
 Proyecto Integrador - Lógica de Programación
 Autor: Angel Rafael Parraga Zambrano
 Universidad Internacional del Ecuador (UIDE)
---------------------------------------------------------------------
 Programa que genera contraseñas seguras usando un generador
 criptográficamente seguro (CSPRNG). El usuario configura la longitud
 y los tipos de caracteres, evalúa la fortaleza, copia al portapapeles
 y mantiene un historial de la sesión.

 FUNCIONALIDADES IMPLEMENTADAS (todos los requerimientos):
   RF-01  Configurar longitud (validación 8-128)
   RF-02  Seleccionar tipos de caracteres
   RF-03  Generar contraseña (módulo secrets = CSPRNG)
   RF-04  Evaluar fortaleza por entropía
   RF-05  Copiar al portapapeles
   RF-06  Ver historial de la sesión
   RF-07  Limpiar historial
=====================================================================
"""

import secrets   # CSPRNG: generador criptográficamente seguro
import string     # Conjuntos de caracteres predefinidos
import math       # Cálculo de entropía

# ---------------------------------------------------------------------
#  CAPA DE DATOS: Biblioteca de caracteres y constantes
# ---------------------------------------------------------------------
MINUSCULAS = string.ascii_lowercase          # a-z
MAYUSCULAS = string.ascii_uppercase          # A-Z
DIGITOS    = string.digits                   # 0-9
SIMBOLOS   = "!@#$%^&*()-_=+[]{};:,.<>?/"     # símbolos especiales

LONGITUD_MINIMA = 8     # RF-01
LONGITUD_MAXIMA = 128   # RF-01

# Historial de la sesión (CAPA DE DATOS: almacenamiento local)
historial = []   # lista que guarda las contraseñas generadas


# =====================================================================
#  RF-01: GESTOR DE CONFIGURACIÓN - longitud
# =====================================================================
def solicitar_longitud():
    """
    Pide la longitud y valida el rango permitido.
    BUCLE while: se repite hasta recibir un valor válido.
    """
    while True:  # estructura repetitiva
        entrada = input(f"Longitud de la contraseña ({LONGITUD_MINIMA}-{LONGITUD_MAXIMA}): ")

        if not entrada.isdigit():  # condicional: validar que sea número
            print("  [!] Error: debe ingresar un número entero.\n")
            continue

        longitud = int(entrada)

        # Condicionales para validar el rango (RF-01)
        if longitud < LONGITUD_MINIMA:
            print(f"  [!] El mínimo es {LONGITUD_MINIMA} caracteres.\n")
        elif longitud > LONGITUD_MAXIMA:
            print(f"  [!] El máximo es {LONGITUD_MAXIMA} caracteres.\n")
        else:
            return longitud  # valor válido


# =====================================================================
#  RF-02: GESTOR DE CONFIGURACIÓN - tipos de caracteres
# =====================================================================
def solicitar_tipos_caracteres():
    """
    Pregunta qué conjuntos de caracteres incluir (RF-02).
    Garantiza que se seleccione al menos un tipo.
    """
    print("\nSeleccione los tipos de caracteres a incluir (s/n):")

    while True:  # bucle hasta una selección válida
        usar_min = input("  ¿Incluir minúsculas (a-z)? ").strip().lower() == "s"
        usar_may = input("  ¿Incluir mayúsculas (A-Z)? ").strip().lower() == "s"
        usar_dig = input("  ¿Incluir dígitos (0-9)?    ").strip().lower() == "s"
        usar_sim = input("  ¿Incluir símbolos (!@#)?   ").strip().lower() == "s"

        # Condicional: al menos un tipo activo
        if usar_min or usar_may or usar_dig or usar_sim:
            return {
                "minusculas": usar_min,
                "mayusculas": usar_may,
                "digitos":    usar_dig,
                "simbolos":   usar_sim,
            }
        print("  [!] Debe seleccionar al menos un tipo de carácter.\n")


def construir_conjunto(tipos):
    """
    Construye el alfabeto uniendo los conjuntos seleccionados.
    Corresponde al paso 'Construir conjunto' del diagrama de flujo.
    """
    alfabeto = ""
    if tipos["minusculas"]:
        alfabeto += MINUSCULAS
    if tipos["mayusculas"]:
        alfabeto += MAYUSCULAS
    if tipos["digitos"]:
        alfabeto += DIGITOS
    if tipos["simbolos"]:
        alfabeto += SIMBOLOS
    return alfabeto


# =====================================================================
#  RF-03: MOTOR DE GENERACIÓN (CSPRNG)
# =====================================================================
def generar_contrasena(longitud, alfabeto):
    """
    Genera la contraseña con secrets.choice() (CSPRNG, NO random).
    BUCLE for: un carácter por cada posición.
    """
    contrasena = ""
    for _ in range(longitud):  # estructura repetitiva
        contrasena += secrets.choice(alfabeto)
    return contrasena


# =====================================================================
#  RF-04: EVALUADOR DE FORTALEZA
# =====================================================================
def evaluar_fortaleza(longitud, alfabeto):
    """
    Calcula la entropía: E = longitud * log2(tamaño_alfabeto)
    y clasifica la contraseña.
    """
    tamano = len(alfabeto)
    entropia = longitud * math.log2(tamano)

    # Condicionales de clasificación
    if entropia < 40:
        nivel = "Débil"
    elif entropia < 60:
        nivel = "Media"
    elif entropia < 80:
        nivel = "Fuerte"
    else:
        nivel = "Muy fuerte"

    return round(entropia, 1), nivel


# =====================================================================
#  RF-05: COPIAR AL PORTAPAPELES
# =====================================================================
def copiar_al_portapapeles(texto):
    """
    Copia la contraseña al portapapeles del sistema.
    Usa pyperclip si está disponible; si no, avisa al usuario.
    """
    try:
        import pyperclip
        pyperclip.copy(texto)
        print("  [OK] Contraseña copiada al portapapeles.")
    except ImportError:
        # Condicional de respaldo si la librería no está instalada
        print("  [!] Instale 'pyperclip' (pip install pyperclip) para copiar.")
        print(f"      Contraseña: {texto}")


# =====================================================================
#  RF-06 / RF-07: HISTORIAL
# =====================================================================
def ver_historial():
    """Muestra el historial recorriéndolo con un bucle for (RF-06)."""
    if len(historial) == 0:  # condicional: historial vacío
        print("\n  El historial está vacío.")
        return

    print("\n  --- HISTORIAL DE CONTRASEÑAS (sesión actual) ---")
    for i, item in enumerate(historial, start=1):  # bucle for
        print(f"  {i}. {item['contrasena']}  ({item['nivel']}, {item['entropia']} bits)")


def limpiar_historial():
    """Vacía el historial de la sesión (RF-07)."""
    historial.clear()
    print("\n  [OK] Historial limpiado.")


# =====================================================================
#  CAPA DE PRESENTACIÓN: flujo de generación completo
# =====================================================================
def flujo_generar():
    """Ejecuta el proceso completo del diagrama de flujo."""
    longitud = solicitar_longitud()                 # RF-01
    tipos = solicitar_tipos_caracteres()            # RF-02
    alfabeto = construir_conjunto(tipos)            # construir conjunto
    contrasena = generar_contrasena(longitud, alfabeto)  # RF-03
    entropia, nivel = evaluar_fortaleza(longitud, alfabeto)  # RF-04

    # Mostrar resultado
    print("\n" + "-" * 50)
    print(f"  Contraseña : {contrasena}")
    print(f"  Entropía   : {entropia} bits")
    print(f"  Fortaleza  : {nivel}")
    print("-" * 50)

    # Guardar en historial (RF-06)
    historial.append({"contrasena": contrasena, "nivel": nivel, "entropia": entropia})

    # Preguntar si desea copiar (RF-05)
    if input("  ¿Copiar al portapapeles? (s/n): ").strip().lower() == "s":
        copiar_al_portapapeles(contrasena)


# =====================================================================
#  MENÚ PRINCIPAL (une todas las funcionalidades)
# =====================================================================
def main():
    """Bucle principal que dirige al usuario según su elección."""
    print("=" * 50)
    print("       GENERADOR SEGURO DE CONTRASEÑAS")
    print("=" * 50)

    while True:  # BUCLE principal: el programa corre hasta que el usuario sale
        print("\n  MENÚ PRINCIPAL")
        print("  1. Generar nueva contraseña")
        print("  2. Ver historial")
        print("  3. Limpiar historial")
        print("  4. Salir")

        opcion = input("  Seleccione una opción: ").strip()

        # Condicionales que dirigen a cada funcionalidad
        if opcion == "1":
            flujo_generar()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            limpiar_historial()
        elif opcion == "4":
            print("\n  ¡Hasta pronto!")
            break  # sale del bucle -> termina el programa
        else:
            print("  [!] Opción no válida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
