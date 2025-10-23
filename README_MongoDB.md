# Configuración para MongoDB Atlas (Nube)

## Configuración inicial

1. **Instalar dependencias de Python:**
   ```bash
   pip install pymongo
   ```

2. **Configurar la conexión:**
   - Abre el archivo `config.py`
   - Reemplaza `TU_CONTRASEÑA_AQUI` con tu contraseña real de MongoDB Atlas
   
   ```python
   MONGO_PASSWORD = "tu_contraseña_real"
   ```

3. **Tu cadena de conexión:**
   ```
   mongodb+srv://alvaro:<db_password>@cluster0.e83jfyl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
   ```

## Configuración de la aplicación

- **Servicio:** MongoDB Atlas (Nube)
- **Base de datos:** `todo_app`
- **Colección:** `todos`
- **Usuario:** `alvaro`
- **Cluster:** `cluster0.e83jfyl.mongodb.net`

## Estructura de documentos en MongoDB

```json
{
  "_id": ObjectId("..."),
  "tarea": "Texto de la tarea",
  "day_added": "2024-01-01",
  "created_at": ISODate("2024-01-01T10:00:00.000Z")
}
```

## Comandos útiles de MongoDB

```javascript
// Conectar a la base de datos
use todo_app

// Ver todas las tareas
db.todos.find()

// Limpiar todas las tareas
db.todos.deleteMany({})

// Insertar tarea de ejemplo
db.todos.insertOne({
  "tarea": "Tarea de ejemplo",
  "day_added": "2024-01-01",
  "created_at": new Date()
})
```