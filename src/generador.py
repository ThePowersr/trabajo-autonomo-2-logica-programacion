"""
=====================================================================
 Generador Seguro de Contraseñas
 Trabajo Autónomo - Lógica de Programación
 Autor: Angel Rafael Parraga Zambrano
---------------------------------------------------------------------
 ESTADO DEL AVANCE: ~50% completado
 Implementado en este avance:
   [OK] RF-01  Configurar longitud (con validación 8-128)
   [OK] RF-02  Seleccionar tipos de caracteres
   [OK] RF-03  Generar contraseña (usando CSPRNG: módulo secrets)
   [OK] RF-04  Evaluar fortaleza (versión inicial por entropía)
 Pendiente para el siguiente avance:
   [  ] RF-05  Copiar al portapapeles
   [  ] RF-06  Ver historial de la sesión
   [  ] RF-07  Limpiar historial
   [  ] Menú principal interactivo completo
=====================================================================
"""

import secrets   # CSPRNG: generador criptográficamente seguro (requerimiento de seguridad)
import string     # Conjuntos de caracteres predefinidos
import math       # Para el cálculo de entropía

# ---------------------------------------------------------------------
#  BIBLIOTECA DE CARACTERES  (Capa de Datos del diagrama de arquitectura)
# ---------------------------------------------------------------------
MINUSCULAS = string.ascii_lowercase          # a-z
MAYUSCULAS = string.ascii_uppercase          # A-Z
DIGITOS    = string.digits                   # 0-9
SIMBOLOS   = "!@#$%^&*()-_=+[]{};:,.<>?/"     # símbolos especiales

# Límites definidos en el requerimiento RF-01
LONGITUD_MINIMA = 8
LONGITUD_MAXIMA = 128


# =====================================================================
#  RF-01 / RF-02 : GESTOR DE CONFIGURACIÓN
#  Validación de parámetros usando estructuras condicionales y bucles
# =====================================================================
def solicitar_longitud():
    """
    Pide al usuario la longitud y valida que esté en el rango permitido.
    Usa un bucle 'while' (estructura repetitiva) que no termina hasta
    recibir un valor válido.
    """
    while True:  # BUCLE: se repite hasta que la entrada sea correcta
        entrada = input(f"Longitud de la contraseña ({LONGITUD_MINIMA}-{LONGITUD_MAXIMA}): ")

        # CONDICIONAL: verificar que sea un número
        if not entrada.isdigit():
            print("  [!] Error: debe ingresar un número entero.")
            continue  # vuelve al inicio del bucle

        longitud = int(entrada)

        # CONDICIONAL: verificar el rango (RF-01)
        if longitud < LONGITUD_MINIMA:
            print(f"  [!] Error: el mínimo es {LONGITUD_MINIMA} caracteres.")
        elif longitud > LONGITUD_MAXIMA:
            print(f"  [!] Error: el máximo es {LONGITUD_MAXIMA} caracteres.")
        else:
            return longitud  # valor válido -> salimos del bucle


def solicitar_tipos_caracteres():
    """
    Pregunta al usuario qué conjuntos de caracteres incluir (RF-02).
    Devuelve un diccionario con las opciones seleccionadas.
    Garantiza que al menos un tipo quede activado.
    """
    print("\nSeleccione los tipos de caracteres a incluir (s/n):")

    while True:  # BUCLE para asegurar al menos una selección válida
        usar_min = input("  ¿Incluir minúsculas (a-z)? ").strip().lower() == "s"
        usar_may = input("  ¿Incluir mayúsculas (A-Z)? ").strip().lower() == "s"
        usar_dig = input("  ¿Incluir dígitos (0-9)?    ").strip().lower() == "s"
        usar_sim = input("  ¿Incluir símbolos (!@#)?   ").strip().lower() == "s"

        # CONDICIONAL: al menos un tipo debe estar activo
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
    Construye el alfabeto disponible uniendo los conjuntos seleccionados.
    Corresponde al paso 'Construir conjunto de caracteres' del diagrama de flujo.
    """
    alfabeto = ""
    # Varios CONDICIONALES que van sumando conjuntos
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
#  RF-03 : MOTOR DE GENERACIÓN  (Capa de Lógica de Negocio)
# =====================================================================
def generar_contrasena(longitud, alfabeto):
    """
    Genera la contraseña seleccionando caracteres al azar del alfabeto.
    Usa secrets.choice() -> CSPRNG (NO usa random, que no es seguro).
    Emplea un bucle 'for' (estructura repetitiva).
    """
    contrasena = ""
    for _ in range(longitud):  # BUCLE: un carácter por cada posición
        contrasena += secrets.choice(alfabeto)
    return contrasena


# =====================================================================
#  RF-04 : EVALUADOR DE FORTALEZA  (versión inicial - se mejorará)
# =====================================================================
def evaluar_fortaleza(longitud, alfabeto):
    """
    Calcula la entropía aproximada en bits: E = longitud * log2(tamaño_alfabeto)
    y clasifica la contraseña. Es un cálculo inicial del avance.
    """
    tamano = len(alfabeto)
    entropia = longitud * math.log2(tamano)  # fórmula de entropía

    # CONDICIONALES que clasifican según la entropía
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
#  PROGRAMA PRINCIPAL (avance: flujo básico sin menú completo)
# =====================================================================
def main():
    print("=" * 55)
    print("     GENERADOR SEGURO DE CONTRASEÑAS  (avance)")
    print("=" * 55)

    # Paso 1 y 2 del diagrama de flujo: configurar parámetros
    longitud = solicitar_longitud()
    tipos = solicitar_tipos_caracteres()

    # Paso 3: construir el alfabeto
    alfabeto = construir_conjunto(tipos)

    # Paso 4: generar
    contrasena = generar_contrasena(longitud, alfabeto)

    # Paso 5: evaluar fortaleza
    entropia, nivel = evaluar_fortaleza(longitud, alfabeto)

    # Paso 6: mostrar resultado
    print("\n" + "-" * 55)
    print(f"  Contraseña generada : {contrasena}")
    print(f"  Entropía            : {entropia} bits")
    print(f"  Fortaleza           : {nivel}")
    print("-" * 55)

    # NOTA: las opciones de copiar/historial/menú se añaden en el próximo avance.


if __name__ == "__main__":
    main()
