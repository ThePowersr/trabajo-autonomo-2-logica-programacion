# 🔐 Generador Seguro de Contraseñas

**Proyecto Integrador — Lógica de Programación**
Universidad Internacional del Ecuador (UIDE)

---

## 📌 Nombre del proyecto
El impacto de las nuevas tecnologías en la sociedad: **Generador Seguro de Contraseñas**.

## 👤 Estudiante
Angel Rafael Parraga Zambrano

## 🎯 Objetivo del sistema
Asistir al usuario en la creación de contraseñas robustas y seguras de forma rápida y
automatizada, empleando un generador criptográficamente seguro (CSPRNG), sin requerir
conocimientos técnicos.

## ⚙️ Descripción de funcionalidades

| ID | Funcionalidad |
|------|---------------------------------------------|
| RF-01 | Configurar la longitud de la contraseña (8 a 128) |
| RF-02 | Seleccionar tipos de caracteres (mayúsculas, minúsculas, dígitos, símbolos) |
| RF-03 | Generar la contraseña con aleatoriedad segura (módulo `secrets`) |
| RF-04 | Evaluar la fortaleza mediante el cálculo de entropía |
| RF-05 | Copiar la contraseña al portapapeles |
| RF-06 | Ver el historial de contraseñas de la sesión |
| RF-07 | Limpiar el historial |

## 📅 Fecha
Junio de 2026

---

## 🗂️ Estructura del repositorio

```
proyecto-integrador/
├── README.md
├── src/
│   └── generador.py            ← código completo del programa
├── diagramas/
│   ├── diagrama_casos_uso.png
│   ├── diagrama_flujo.png
│   └── diagrama_arquitectura.png
├── docs/
│   └── contenido_proyecto.tex  ← documento del proyecto (LaTeX)
└── presentacion/
    └── presentacion_generador.pptx
```

## 🛠️ Tecnologías
- **Lenguaje:** Python 3.10+
- **Librerías:** `secrets`, `string`, `math` (estándar) · `pyperclip` (opcional, para copiar)
- **Control de versiones:** Git + GitHub

## ▶️ Ejecución
```bash
# Clonar el repositorio
git clone https://github.com/ThePowersr/trabajo-autonomo-2-logica-programacion.git
cd generador-contrasenas

# Ejecutar el programa
python3 src/generador.py
```

> Para habilitar la copia al portapapeles: `pip install pyperclip`

---

## 🧠 Conceptos aplicados
- **Condicionales** (`if/elif/else`): validación, clasificación de fortaleza y menú.
- **Bucles** (`while`, `for`): re-solicitud de datos, generación y recorrido del historial.
- **Funciones**: código modular organizado según la arquitectura de tres capas.
- **Seguridad**: uso de CSPRNG en lugar de generadores pseudoaleatorios comunes.
