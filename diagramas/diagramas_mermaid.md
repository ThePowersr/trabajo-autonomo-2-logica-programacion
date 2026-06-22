# Diagramas Mermaid — Generador Seguro de Contraseñas

> Exporta cada diagrama como PNG y guárdalo en la carpeta `imagenes/`
> con el nombre exacto indicado. Luego compila el `.tex` normalmente.

---

## Diagrama 1: Casos de Uso
**Archivo destino:** `imagenes/diagrama_casos_uso.png`

```mermaid
graph LR
    Usuario(("👤 Usuario"))

    subgraph Sistema["  Sistema: Generador Seguro de Contraseñas  "]
        direction TB
        UC1("Configurar longitud\nde contraseña")
        UC2("Seleccionar tipos\nde caracteres")
        UC3("Generar contraseña")
        UC4("Copiar contraseña\nal portapapeles")
        UC5("Evaluar fortaleza\nde contraseña")
        UC6("Ver historial\nde contraseñas")
        UC7("Limpiar historial")
    end

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
    Usuario --> UC4
    Usuario --> UC6
    Usuario --> UC7

    UC1 -. "«include»" .-> UC3
    UC2 -. "«include»" .-> UC3
    UC3 -. "«include»" .-> UC5
```

---

## Diagrama 2: Flujo del Proceso
**Archivo destino:** `imagenes/diagrama_flujo.png`

```mermaid
flowchart TD
    A([🚀 Inicio])
    B["Definir parámetros\n· Longitud\n· Tipos de caracteres"]
    C{¿Parámetros\nválidos?}
    D["⚠️ Mostrar error\nde validación"]
    E["Construir conjunto\nde caracteres permitidos"]
    F["Seleccionar caracteres\naletoriamente\n(CSPRNG)"]
    G["Armar contraseña\ncompleta"]
    H["Evaluar fortaleza\n(entropía)"]
    I{¿Fortaleza\naceptable?}
    J["✅ Mostrar contraseña\ngenerada"]
    K{¿Acción\ndel usuario?}
    L["📋 Copiar al\nportapapeles"]
    M["💾 Guardar en\nhistorial"]
    N["🔄 Nueva\ncontraseña"]
    O([🏁 Fin])

    A --> B
    B --> C
    C -- No --> D
    D --> B
    C -- Sí --> E
    E --> F
    F --> G
    G --> H
    H --> I
    I -- No --> F
    I -- Sí --> J
    J --> K
    K -- Copiar --> L
    K -- Guardar --> M
    K -- Nueva --> B
    K -- Salir --> O
    L --> K
    M --> K
```

---

## Diagrama 3: Arquitectura del Sistema
**Archivo destino:** `imagenes/diagrama_arquitectura.png`

```mermaid
graph TB
    subgraph UI["🖥️  Capa de Presentación"]
        direction LR
        A["Panel de\nConfiguración"]
        B["Visualizador de\nContraseña"]
        C["Indicador de\nFortaleza"]
        D["Panel de\nHistorial"]
    end

    subgraph Logic["⚙️  Capa de Lógica de Negocio"]
        direction LR
        E["Motor de\nGeneración\n(CSPRNG)"]
        F["Evaluador de\nFortaleza"]
        G["Gestor de\nConfiguración"]
        H["Gestor de\nHistorial"]
    end

    subgraph Data["💾  Capa de Datos"]
        direction LR
        I["Almacenamiento\nLocal (sesión)"]
        J["Configuración\nde Usuario"]
        K["Biblioteca de\nCaracteres"]
    end

    A --> G
    B --> E
    C --> F
    D --> H

    G --> E
    E --> K
    E --> F
    F --> C
    H --> I
    G --> J

    style UI    fill:#dbeafe,stroke:#3b82f6,color:#1e3a5f
    style Logic fill:#dcfce7,stroke:#22c55e,color:#14532d
    style Data  fill:#fef9c3,stroke:#eab308,color:#713f12
```

---

## Instrucciones de exportación

1. Ve a [mermaid.live](https://mermaid.live) (editor online gratuito).
2. Pega el código de **cada diagrama** (sin los backticks ` ``` `).
3. Haz clic en **Download PNG** (esquina superior derecha).
4. Renombra el archivo con el nombre exacto indicado arriba.
5. Crea la carpeta `imagenes/` junto a tu archivo `.tex` y mueve los PNG ahí.
6. Compila con `pdflatex generador_contrasenas.tex`.
```
estructura de carpetas esperada:
├── generador_contrasenas.tex
└── imagenes/
    ├── diagrama_casos_uso.png
    ├── diagrama_flujo.png
    └── diagrama_arquitectura.png
```
