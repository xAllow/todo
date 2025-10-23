from app import app

# Vercel expects a callable named 'app' or 'application'. We export 'app' from app.py
application = app

# If you need a WSGI handler wrapper, Vercel's Python runtime will use 'application' automatically.
