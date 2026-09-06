# 🧮 Calculadora Python

<p align="center">
  <strong>Aplicación de escritorio desarrollada en Python con Tkinter</strong>
</p>

<p align="center">
  Una calculadora interactiva diseñada para aplicar principios de programación, diseño de interfaces y manejo de estados en una aplicación de escritorio.
</p>

---

## 📌 Descripción

**Calculadora Python** es una aplicación de escritorio desarrollada utilizando **Python** y la biblioteca gráfica **Tkinter**.

El proyecto implementa una calculadora interactiva capaz de realizar operaciones aritméticas básicas mediante una interfaz gráfica sencilla e intuitiva. Además de resolver operaciones matemáticas, el proyecto permite poner en práctica conceptos fundamentales de ingeniería de software y programación, como:

* Manejo de eventos.
* Variables y estructuras de control.
* Funciones.
* Gestión del estado de la aplicación.
* Validación de entradas.
* Manejo de errores.
* Diseño de interfaces gráficas.
* Organización y control de versiones mediante Git.

El proyecto fue desarrollado como una práctica académica orientada al desarrollo de software y al fortalecimiento de habilidades de programación en Python.

---

## 🎯 Objetivo

Desarrollar una aplicación de escritorio funcional que permita al usuario realizar operaciones matemáticas básicas mediante una interfaz gráfica, aplicando principios fundamentales de programación y desarrollo de software.

### Objetivos específicos

* Implementar operaciones aritméticas básicas.
* Diseñar una interfaz gráfica funcional e intuitiva.
* Gestionar correctamente la entrada de datos del usuario.
* Implementar validaciones para evitar operaciones inválidas.
* Controlar el estado de la calculadora durante las operaciones.
* Aplicar buenas prácticas de programación.
* Utilizar Git y GitHub como herramientas de control de versiones y documentación.

---

## ⚙️ Funcionalidades

La aplicación cuenta con las siguientes funcionalidades:

| Funcionalidad              | Descripción                                                     |
| -------------------------- | --------------------------------------------------------------- |
| ➕ Suma                     | Permite sumar dos o más valores.                                |
| ➖ Resta                    | Permite realizar operaciones de resta.                          |
| ✖️ Multiplicación          | Permite multiplicar valores numéricos.                          |
| ➗ División                 | Permite realizar divisiones entre valores.                      |
| 🔢 Entrada numérica        | Permite introducir números mediante botones.                    |
| 🧹 C                       | Limpia el valor u operación actual.                             |
| 🗑️ AC                     | Reinicia completamente el estado de la calculadora.             |
| ⚠️ Validaciones            | Controla entradas y operaciones no válidas.                     |
| 🔄 Operaciones encadenadas | Permite continuar operaciones utilizando resultados anteriores. |

---

## 🛠️ Tecnologías utilizadas

### Lenguaje

* **Python 3**

### Interfaz gráfica

* **Tkinter**

### Control de versiones

* **Git**
* **GitHub**

### Desarrollo

* Programación orientada a eventos.
* Manejo de funciones.
* Estructuras condicionales.
* Gestión de variables de estado.
* Manejo de excepciones y validaciones.

---

## 🏗️ Arquitectura lógica

La aplicación puede entenderse mediante tres componentes principales:

```text
┌─────────────────────────────┐
│       INTERFAZ GRÁFICA      │
│           Tkinter           │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       GESTIÓN DE EVENTOS    │
│      Botones / Entradas     │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      LÓGICA DE NEGOCIO      │
│   Operaciones aritméticas   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│          RESULTADO          │
│     Display de pantalla     │
└─────────────────────────────┘
```

La interacción del usuario comienza en la interfaz gráfica. Los eventos generados por los botones son procesados por la lógica de la aplicación, que determina la operación correspondiente y actualiza el resultado mostrado.

---

## 📂 Estructura del proyecto

```text
Calculadora-Python/
│
├── Calculadora_V_2.0.py
├── LICENSE
├── README.md
└── .gitignore
```

### Descripción de archivos

**`Calculadora_V_2.0.py`**

Contiene la implementación principal de la aplicación, incluyendo la interfaz gráfica, gestión de eventos y lógica de las operaciones.

**`README.md`**

Documentación técnica y funcional del proyecto.

**`LICENSE`**

Define los términos bajo los cuales se distribuye el código fuente.

**`.gitignore`**

Especifica los archivos y directorios que Git debe ignorar durante el desarrollo.

---

## 💻 Requisitos

Para ejecutar el proyecto se requiere:

* Python **3.8 o superior**.
* Tkinter.

En la mayoría de las instalaciones estándar de Python, Tkinter se incluye junto con Python.

Puedes comprobar que Python está instalado ejecutando:

```bash
python --version
```

o:

```bash
python3 --version
```

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Javiersan237/Calculadora-Python.git
```

### 2. Entrar al directorio

```bash
cd Calculadora-Python
```

### 3. Ejecutar la aplicación

```bash
python Calculadora_V_2.0.py
```

En sistemas donde Python se ejecuta mediante `python3`:

```bash
python3 Calculadora_V_2.0.py
```

---

## 🖥️ Uso

Una vez ejecutada la aplicación, se mostrará la interfaz gráfica de la calculadora.

El flujo general de utilización es:

```text
Inicio
  │
  ▼
Ingresar número
  │
  ▼
Seleccionar operación
  │
  ▼
Ingresar segundo número
  │
  ▼
Ejecutar operación
  │
  ▼
Mostrar resultado
  │
  ├───────────────┐
  │               │
  ▼               ▼
Continuar       Reiniciar
operación       calculadora
```

La interfaz permite realizar operaciones de manera interactiva sin necesidad de introducir comandos directamente en la terminal.

---

## 🧠 Conceptos de programación aplicados

Este proyecto permite aplicar diferentes conceptos fundamentales de programación:

### Variables de estado

Se utilizan variables para mantener información relacionada con el estado actual de la calculadora, como el número introducido, la operación seleccionada y el resultado.

### Programación orientada a eventos

La aplicación responde a eventos generados por el usuario, principalmente mediante la interacción con los botones de la interfaz.

### Estructuras condicionales

Las condiciones permiten determinar qué operación debe realizarse dependiendo de la acción seleccionada.

### Funciones

La lógica se organiza mediante funciones para facilitar la reutilización del código y mejorar su legibilidad.

### Validación

Se contemplan situaciones que podrían provocar resultados incorrectos o comportamientos inesperados.

### Manejo de errores

La aplicación contempla operaciones que pueden generar errores, como intentar realizar una división entre cero.

---

## 🔐 Manejo de errores

Una aplicación de software debe considerar entradas y situaciones que no necesariamente representan un flujo válido.

Entre los escenarios contemplados se encuentran:

* División entre cero.
* Operaciones incompletas.
* Entradas no válidas.
* Reinicio del estado de la calculadora.
* Resultados que excedan las condiciones establecidas por la aplicación.

El objetivo es evitar que una entrada incorrecta provoque el cierre inesperado del programa.

---

## 📋 Historias de usuario

### HU-01 — Visualizar información

> Como usuario, quiero visualizar el número introducido y el resultado de las operaciones para conocer el estado actual de la calculadora.

### HU-02 — Realizar operaciones

> Como usuario, quiero seleccionar una operación matemática para obtener el resultado correspondiente.

### HU-03 — Limpiar entrada

> Como usuario, quiero poder eliminar la entrada actual para corregir un dato incorrecto.

### HU-04 — Reiniciar calculadora

> Como usuario, quiero reiniciar completamente la calculadora para comenzar una nueva operación.

### HU-05 — Control de errores

> Como usuario, quiero recibir una respuesta adecuada cuando intento realizar una operación inválida.

---

## 🔄 Metodología de desarrollo

Para la organización del proyecto se puede utilizar una metodología **Kanban**, dividiendo el desarrollo en diferentes estados:

```text
┌──────────────┐
│    TO DO     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ IN PROGRESS  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    TESTING   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     DONE     │
└──────────────┘
```

Este enfoque permite dividir el desarrollo en tareas pequeñas, visualizar el progreso y detectar funcionalidades pendientes.

---

## 🧪 Pruebas recomendadas

Para verificar el funcionamiento de la aplicación se pueden realizar pruebas como:

| Prueba               | Entrada      | Resultado esperado        |
| -------------------- | ------------ | ------------------------- |
| Suma                 | `10 + 5`     | `15`                      |
| Resta                | `10 - 5`     | `5`                       |
| Multiplicación       | `10 × 5`     | `50`                      |
| División             | `10 ÷ 5`     | `2`                       |
| División inválida    | `10 ÷ 0`     | Manejo de error           |
| Limpieza             | `C`          | Limpia entrada actual     |
| Reinicio             | `AC`         | Restablece el estado      |
| Operación encadenada | `10 + 5 - 2` | Resultado correspondiente |

---

## 📈 Mejoras futuras

El proyecto puede evolucionar incorporando nuevas funcionalidades, por ejemplo:

* [ ] Historial de operaciones.
* [ ] Operaciones con porcentajes.
* [ ] Potencias y raíces.
* [ ] Soporte para números decimales avanzado.
* [ ] Atajos de teclado.
* [ ] Tema claro / oscuro.
* [ ] Personalización de la interfaz.
* [ ] Registro de operaciones.
* [ ] Pruebas automatizadas con `pytest`.
* [ ] Empaquetado como aplicación ejecutable.
* [ ] Separación de la interfaz y lógica de negocio.
* [ ] Arquitectura modular.
* [ ] Documentación técnica ampliada.

---

## 📌 Estado del proyecto

**Estado:** 🟢 Funcional

**Versión:** `2.0`

El proyecto se encuentra en desarrollo académico y puede recibir nuevas funcionalidades y mejoras conforme avance su ciclo de desarrollo.

---

## 👨‍💻 Autor

**Javier Aram Ortega Cortez**

Estudiante de **Ingeniería en Sistemas Computacionales**

GitHub:

**[@JavierAramOC](https://github.com/JavierAramOC)**

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

Consulta el archivo [`LICENSE`](LICENSE) para conocer los términos completos de la licencia.

---

## ⭐ Contribuciones

Las sugerencias y mejoras son bienvenidas.

Si deseas contribuir:

1. Realiza un fork del repositorio.
2. Crea una nueva rama:

```bash
git checkout -b feature/nueva-funcionalidad
```

3. Realiza tus cambios.
4. Guarda los cambios:

```bash
git add .
git commit -m "feat: agregar nueva funcionalidad"
```

5. Envía tus cambios:

```bash
git push origin feature/nueva-funcionalidad
```

6. Abre un **Pull Request**.

---

<p align="center">
  Desarrollado con Python 🐍
</p>

<p align="center">
  <strong>Ingeniería en Sistemas Computacionales</strong>
</p>
