# 🚀 Práctica: Integración Continua (CI) con Flask y GitHub Actions

Este repositorio contiene la resolución de la práctica de Introducción a CI/CD, basada en el repositorio original de [josejuansanchez/ci-cd-flask](https://github.com/josejuansanchez/ci-cd-flask).

El objetivo principal de esta práctica es implementar un flujo de **Integración Continua (CI)** utilizando **GitHub Actions** para una aplicación web sencilla desarrollada con Python y Flask.

> **⚠️ Nota sobre el Despliegue (CD):** Debido a las restricciones de permisos de las cuentas de estudiante de AWS Academy, esta práctica se centra exclusivamente en la fase de Integración Continua (CI). El despliegue automático (Continuous Deployment) hacia AWS ha sido omitido por seguridad de la plataforma.

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Framework Web:** Flask
* **Testing:** Pytest
* **Automatización CI:** GitHub Actions
* **Control de Versiones:** Git y GitHub

---

## 📝 Guía Paso a Paso de la Práctica

A continuación se detallan los pasos realizados para completar la práctica y configurar la automatización:

### Paso 1: Fork y Clonado del Repositorio
Para poder modificar el código y configurar nuestros propios flujos de GitHub Actions, primero creamos una copia del proyecto:

1. Se realizó un **Fork** del repositorio original del profesor hacia la cuenta personal de GitHub.

2. Se clonó el repositorio en el entorno de desarrollo local (instancia de Ubuntu en AWS conectada mediante VS Code):
   ```bash
   git clone [https://github.com/cnvt26/ci-cd-flask.git](https://github.com/cnvt26/ci-cd-flask.git)
   cd ci-cd-flask
   ```

### Paso 2: Preparación del Entorno Local

Para no instalar dependencias de forma global y mantener el sistema limpio, trabajamos con un entorno virtual de Python:

#### Creación y activación del entorno virtual:

```
python3 -m venv venv
source venv/bin/activate
```

#### Instalación de las dependencias necesarias (Flask, pytest, etc.) definidas en el proyecto:

```
pip install -r requirements.txt
```

### Paso 3: Ejecución y Pruebas Locales

Antes de automatizar nada, comprobamos que el código base funciona correctamente en nuestra máquina.

#### Para levantar la aplicación web de Flask y comprobar que responde:

```
python src/app.py
```

#### Para ejecutar las pruebas unitarias localmente:

```
pytest tests/test_app.py
```

### Paso 4: Creación de Nuevos Tests (Ampliación)

Siguiendo los requisitos de la práctica, se añadieron tests adicionales al archivo tests/test_app.py para ampliar la cobertura del código. Se añadieron comprobaciones para asegurar que la aplicación responde correctamente ante diferentes escenarios, verificando códigos de estado HTTP (200 OK, 404 Not Found) y el contenido de las respuestas.

### Paso 5: Automatización con GitHub Actions (CI)

La magia de la Integración Continua reside en la carpeta **.github/workflows/**. Ahí se encuentra el archivo .yml que dicta las órdenes al "robot" de GitHub.

- El flujo está configurado para activarse cada vez que se hace un git push a la rama main.

- Cuando detecta un cambio, GitHub levanta una máquina virtual (un Runner), instala Python, instala las dependencias de nuestro requirements.txt y ejecuta el comando pytest de forma automática.

Subimos nuestros cambios (con los nuevos tests) al repositorio:

```
git add .
git commit -m "Añadidos nuevos tests unitarios para CI"
git push
```

En la pestaña Actions de este repositorio en GitHub, podemos observar cómo el flujo se ejecuta automáticamente. Si nuestro código es correcto y pasa todos los tests, obtenemos el check verde (✅) de éxito.