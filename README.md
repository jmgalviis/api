# Proyecto: API de Energía

Este proyecto es una API REST desarrollada con **FastAPI** que permite gestionar datos relacionados con el consumo y la inyección de energía, así como realizar cálculos de facturación y estadísticas para clientes y sistemas. La aplicación utiliza **SQLite** como base de datos durante el desarrollo y pruebas.

---

## Tabla de Contenidos
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración](#configuración)
- [Ejecutar la Aplicación](#ejecutar-la-aplicación)
- [Endpoints Principales](#endpoints-principales)
- [Documentación de Swagger](#documentación-de-swagger)
- [Ejecutar Pruebas](#ejecutar-pruebas)
- [Contribución](#contribución)

---

## Requisitos Previos
Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.9 o superior**
- **pip** (Administrador de paquetes de Python)
- **Git**

---

## Instalación
1. Clona este repositorio:
   ```bash
   git clone git@github.com:jmgalviis/api.git
   cd api
   ```

2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate   # Windows
   ```

3. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

4. Asegúrate de tener un archivo SQL para inicializar la base de datos (por defecto, **create_db.sql**). La configuración de la ruta se encuentra en `conftest.py`.

---

## Configuración
El proyecto utiliza un archivo SQLite para almacenar los datos. Por defecto, el archivo se crea localmente como `test.db` durante las pruebas o al ejecutar la API.

Puedes ajustar los parámetros de conexión en `conftest.py` o `app/infrastructure/database.py`.

---

## Ejecutar la Aplicación
1. Inicia la aplicación:
   ```bash
   python main.py
   ```

2. Ve a la documentación interactiva de la API en tu navegador:
   - [Swagger UI](http://127.0.0.1:8000/docs)

---

## Endpoints Principales
### 1. Facturación
- **POST** `/api/v1/calculate-invoice`
  - Calcula la factura de un cliente para un mes dado.
  - **Request Body**:
    ```json
    {
      "client_id": 2256,
      "month": "2023-09"
    }
    ```
  - **Response**:
    ```json
    {
      "EA": 150.0,
      "EC": 250.0,
      "EE1": 100.0,
      "EE2": 50.0
    }
    ```

### 2. Estadísticas de Cliente
- **GET** `/api/v1/client-statistics/{client_id}`
  - Devuelve estadísticas de consumo e inyección para un cliente específico.
  - **Response**:
    ```json
    {
      "total_consumption": 150.0,
      "total_injection": 100.0
    }
    ```

### 3. Carga del Sistema
- **GET** `/api/v1/system-load`
  - Devuelve la carga horaria del sistema.
  - **Response**:
    ```json
    {
      "hourly_load": [
        {
          "timestamp": "2025-01-01 00:00:00",
          "load": 50.0
        },
        {
          "timestamp": "2025-01-02 00:00:00",
          "load": 75.0
        }
      ]
    }
    ```

---

## Documentación de Swagger
Cada endpoint de la API está documentado con Swagger, y puedes acceder a su documentación interactiva en:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Los endpoints principales tienen los siguientes propósitos:

1. **/calculate-invoice**: Recibe un ID de cliente y un mes para calcular su factura.
2. **/client-statistics/{client_id}**: Proporciona el consumo total e inyección de energía de un cliente.
3. **/system-load**: Muestra las cargas horarias del sistema.

---

## Ejecutar Pruebas
El proyecto incluye pruebas unitarias y de integración con `pytest`. Para ejecutar las pruebas:

```bash
pytest test/
```

---

## Contribución
1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios:
   ```bash
   git checkout -b mi-nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Envía tus cambios:
   ```bash
   git push origin mi-nueva-funcionalidad
   ```
5. Abre un Pull Request.

---

## Licencia
Este proyecto está licenciado bajo la [MIT License](https://opensource.org/licenses/MIT).


## Resultado
![image](https://github.com/jmgalviis/api/blob/main/img_1.png)
---
![image](https://github.com/jmgalviis/api/blob/main/img_2.png)
---
![image](https://github.com/jmgalviis/api/blob/main/img_2.png)
