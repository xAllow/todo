from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)


try:
    if os.getenv('VERCEL'):
        MONGO_URI = os.getenv('MONGODB_URI')
        if not MONGO_URI:
            raise Exception("MONGODB_URI environment variable not set")
    else:
        from config import MONGO_URI
    
    client = MongoClient(MONGO_URI)
    db = client['todo_app']
    collection = db['todos']
    # Verificar conexión
    client.admin.command('ping')
    print("Conectado a MongoDB Atlas exitosamente!")
except Exception as e:
    print(f"Error conectando a MongoDB Atlas: {e}")
    # En caso de error, usar una lista vacía como fallback
    collection = None

@app.route('/')
def index():
    if collection is None:
        # Fallback si no hay conexión a MongoDB
        todos = []
    else:
        # Obtener todas las tareas de MongoDB
        todos = list(collection.find())
        
        # Convertir ObjectId a string para el template
        for todo in todos:
            todo['_id'] = str(todo['_id'])

    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    tarea = request.form.get('tarea')
    
    if tarea and collection is not None:
        new_todo = {
            'tarea': tarea,
            'day_added': datetime.now().strftime('%Y-%m-%d'),
            'created_at': datetime.now()
        }
        # Insertar en MongoDB
        collection.insert_one(new_todo)
    
    return redirect(url_for('index'))

@app.route('/delete/<todo_id>')
def delete_todo(todo_id):
    if collection is not None:
        # Eliminar de MongoDB usando ObjectId
        collection.delete_one({'_id': ObjectId(todo_id)})
    return redirect(url_for('index'))

@app.route('/update/<todo_id>', methods=['GET', 'POST'])
def update_todo(todo_id):
    if collection is None:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        tarea = request.form.get('tarea')
        if tarea:
            # Actualizar en MongoDB
            collection.update_one(
                {'_id': ObjectId(todo_id)}, 
                {'$set': {'tarea': tarea}}
            )
        return redirect(url_for('index'))
    
    # GET: Mostrar formulario de edición
    todo = collection.find_one({'_id': ObjectId(todo_id)})
    if not todo:
        return redirect(url_for('index'))
    
    todo['_id'] = str(todo['_id'])
    return render_template('update.html', todo=todo)

if __name__ == '__main__':
    app.run(debug=True)
