from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
from flask import Flask, request, render_template_string
import threading

# --- Configuración del Servidor RPC ---
def hola_mundo(mensaje):
    return f"¡Servidor RPC recibió tu mensaje: {mensaje}!"

def start_rpc_server():
    rpc_server = SimpleXMLRPCServer(("0.0.0.0", 9000), allow_none=True)
    print("Servidor RPC escuchando en http://0.0.0.0:9000")
    
    # Registrar la función RPC
    rpc_server.register_function(hola_mundo, "hola_mundo")
    
    rpc_server.serve_forever()

# --- Configuración de Flask para Servir HTML ---
app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>RPC Servidor-Cliente</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        textarea { width: 100%; height: 100px; margin-bottom: 10px; }
        #response { margin-top: 20px; padding: 10px; border: 1px solid #ccc; background: #f9f9f9; }
    </style>
</head>
<body>
    <h1>RPC - Comunicación Cliente-Servidor</h1>
    <textarea id="message" placeholder="Escribe tu mensaje aquí"></textarea><br>
    <button onclick="sendMessage()">Enviar Mensaje</button>

    <div id="response">Respuesta del servidor aparecerá aquí...</div>

    <script>
        async function sendMessage() {
            const message = document.getElementById('message').value;
            const responseDiv = document.getElementById('response');

            const response = await fetch('/send_message', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            responseDiv.innerText = 'Servidor: ' + data.response;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/send_message', methods=['POST'])
def send_message():
    import json
    data = request.get_json()
    message = data.get("message", "")

    # Conectar al servidor RPC
    rpc_client = ServerProxy("http://localhost:9000")
    response = rpc_client.hola_mundo(message)

    return {"response": response}

# --- Ejecución del Servidor RPC y Flask ---
if __name__ == "__main__":
    # Iniciar el servidor RPC en un hilo separado
    threading.Thread(target=start_rpc_server, daemon=True).start()
    
    # Iniciar Flask
    print("Servidor Flask escuchando en http://localhost:5000")
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)

