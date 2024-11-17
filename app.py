from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, Mundo! Esta es una aplicación de prueba desplegada en Docker y ECR."

if __name__ == '__main__':
    # Obtén el puerto desde la variable de entorno o usa 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
