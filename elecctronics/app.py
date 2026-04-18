from flask import Flask, render_template, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) # Clave aleatoria para seguridad

# Catálogo de Electrónica
productos = [
    {"id": 1, "nombre": "Auriculares Pro Max", "categoria": "Audio", "precio": 299, "imagen": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500"},
    {"id": 2, "nombre": "Smartwatch V3", "categoria": "Relojes", "precio": 199, "imagen": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500"},
    {"id": 3, "nombre": "Cámara Mirrorless", "categoria": "Foto", "precio": 850, "imagen": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500"},
    {"id": 4, "nombre": "Teclado Mecánico RGB", "categoria": "Gaming", "precio": 120, "imagen": "https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=500"}
]

@app.route('/')
def index():
    if 'carrito' not in session:
        session['carrito'] = []
    return render_template('index.html', productos=productos, total=len(session['carrito']))

@app.route('/agregar/<int:id>')
def agregar(id):
    carrito = session.get('carrito', [])
    carrito.append(id)
    session['carrito'] = carrito
    return redirect(url_for('index'))

@app.route('/limpiar')
def limpiar():
    session.pop('carrito', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
