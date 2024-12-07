# Proyecto RPC Flask - Comunicación Cliente-Servidor

Este proyecto implementa un servidor **RPC (Remote Procedure Call)** en Python usando **XML-RPC** y una interfaz web servida con **Flask**. Permite la comunicación entre un cliente web y un servidor RPC para enviar y recibir mensajes.

## Características

- Servidor RPC expone el método `hola_mundo` que recibe un mensaje y devuelve una respuesta
- Cliente web interactúa con el servidor RPC a través de Flask y una interfaz HTML
- Totalmente **dockerizado** para facilitar el despliegue y ejecución

## Tecnologías Utilizadas

- **Python 3.9**
- **Flask** (servidor web)
- **XML-RPC** (para comunicación RPC)
- **HTML + JavaScript** (interfaz cliente)
- **Docker** (contenedorización)

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:
- Python 3.9+
- Docker
- Git

## Instalación Local

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/<tu-usuario>/rpc-flask.git
   cd rpc-flask
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta el servidor**:
   ```bash
   python rpc_server_flask.py
   ```

4. **Prueba la aplicación**:
   - Abre tu navegador en `http://localhost:5000`
   - Escribe un mensaje y verifica la respuesta del servidor

## Estructura del Proyecto

```
rpc-flask/
├── rpc_server_flask.py    # Código principal del servidor RPC y Flask
├── requirements.txt       # Dependencias necesarias
├── Dockerfile             # Archivo para construir la imagen Docker
└── README.md             # Documentación del proyecto
```

## Uso con Docker

### 1. Construir la imagen Docker
```bash
docker build -t rpc-flask .
```

### 2. Ejecutar el contenedor
```bash
docker run -p 5000:5000 -p 9000:9000 --name rpc-flask-container rpc-flask
```

### 3. Acceder a la aplicación
- **Interfaz Web**: http://localhost:5000
- **Servidor RPC**: Disponible en `localhost:9000` para pruebas directas

## Cómo Funciona

1. El **servidor RPC** (en el puerto 9000) expone el método `hola_mundo` que acepta un mensaje como parámetro.
2. El **servidor Flask** (en el puerto 5000) actúa como intermediario entre el cliente web y el servidor RPC.
3. La **interfaz HTML** permite enviar un mensaje al servidor Flask, que a su vez invoca el método RPC `hola_mundo`.
4. La respuesta del servidor RPC se devuelve al cliente web y se muestra en la interfaz.

## Pruebas y Ejemplo de Uso

1. Accede a la página principal del proyecto en el navegador: `http://localhost:5000`
2. Escribe un mensaje en la caja de texto y presiona **Enviar**
3. Verás una respuesta como esta:
   ```
   Servidor: ¡Servidor RPC recibió tu mensaje: Hola Mundo!
   ```

