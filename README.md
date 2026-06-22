# 🔐 Generador Seguro de Contraseñas

Trabajo Autónomo — **Lógica de Programación** · UIDE
Autor: **Angel Rafael Parraga Zambrano**
Docente: Vizcaíno Imacaña Fernanda Paulina

---

## 📌 Descripción del proyecto

Aplicación de consola que genera contraseñas seguras de forma automatizada.
El usuario configura la **longitud** y los **tipos de caracteres** deseados, y el
programa produce una contraseña usando un generador **criptográficamente seguro
(CSPRNG)**, evaluando además su fortaleza por entropía.

Este repositorio corresponde a la **fase de desarrollo** del proyecto, partiendo del
diseño funcional y de arquitectura realizado en el Trabajo Autónomo N.º 1.

---

## 🚦 Estado del avance — **≈ 50 % completado**

| ID | Funcionalidad | Estado |
|------|----------------------------------|:------:|
| RF-01 | Configurar longitud (validación 8–128) | ✅ Implementado |
| RF-02 | Seleccionar tipos de caracteres | ✅ Implementado |
| RF-03 | Generar contraseña (CSPRNG) | ✅ Implementado |
| RF-04 | Evaluar fortaleza (entropía) | ✅ Implementado (versión inicial) |
| RF-05 | Copiar al portapapeles | ⬜ Pendiente |
| RF-06 | Ver historial de la sesión | ⬜ Pendiente |
| RF-07 | Limpiar historial | ⬜ Pendiente |
| — | Menú principal interactivo | ⬜ Pendiente |

---

## 🗂️ Estructura del repositorio

```
generador-contrasenas/
├── README.md                 ← este archivo
├── src/
│   └── generador.py          ← código fuente (avance del 50%)
├── diagramas/
│   ├── diagramas_mermaid.md  ← código fuente de los 3 diagramas (Mermaid)
│   ├── diagrama_casos_uso.png
│   ├── diagrama_flujo.png
│   └── diagrama_arquitectura.png
└── docs/
    └── logica_de_programacion_autonomo_1.pdf  ← documento de diseño (TA N.º 1)
```

---

## 🧩 Diagramas

Los diagramas elaborados en la fase de diseño guían la implementación:

- **Casos de uso** — funcionalidades observables por el usuario.
- **Diagrama de flujo** — secuencia lógica de la generación.
- **Diagrama de arquitectura** — estructura en 3 capas (Presentación · Lógica · Datos).

> El código fuente de los diagramas está en `diagramas/diagramas_mermaid.md`
> y las imágenes exportadas en la misma carpeta.

### Relación código ↔ diagrama de flujo

| Paso del diagrama de flujo | Función en `generador.py` |
|----------------------------|---------------------------|
| Definir parámetros | `solicitar_longitud()`, `solicitar_tipos_caracteres()` |
| Validar parámetros | condicionales dentro de las funciones anteriores |
| Construir conjunto de caracteres | `construir_conjunto()` |
| Seleccionar caracteres (CSPRNG) | `generar_contrasena()` |
| Evaluar fortaleza | `evaluar_fortaleza()` |
| Mostrar contraseña | `main()` |

---

## 🛠️ Entorno de desarrollo

- **Lenguaje:** Python 3.10+
- **IDE recomendado:** Visual Studio Code
- **Dependencias:** solo librería estándar (`secrets`, `string`, `math`) — sin instalaciones externas.

---

## ▶️ Cómo ejecutar

```bash
# Clonar el repositorio
git clone https://github.com/ThePowersr/trabajo-autonomo-2-logica-programacion.git
cd generador-contrasenas

# Ejecutar el programa
python3 src/generador.py
```

---

## 🧠 Conceptos de programación aplicados

- **Estructuras condicionales (`if / elif / else`)**: validación de longitud, tipos de
  caracteres y clasificación de fortaleza.
- **Estructuras repetitivas (`while`, `for`)**: re-pedir entradas inválidas y construir
  la contraseña carácter a carácter.
- **Funciones**: el código está modularizado siguiendo las capas de la arquitectura.
- **Comentarios**: cada bloque importante está documentado.

---

## 📅 Próximos pasos

1. Añadir menú principal interactivo.
2. Implementar copiado al portapapeles (RF-05).
3. Implementar historial de sesión y su limpieza (RF-06, RF-07).
4. Mejorar el evaluador de fortaleza con verificación de variedad de caracteres.
