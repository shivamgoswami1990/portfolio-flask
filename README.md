# Portfolio Flask

# Setup environment variables
- export APP_SETTINGS="config.DevelopmentConfig"
- export DATABASE_URL="postgresql://localhost/portfolio"

# Create DB in Postgres
- psql
- create database portfolio;

# Migrate DB
- python3 manage.py db init
- python3 manage.py db migrate
- python3 manage.py db upgrade

# Run server
- python3 manage.py runserver
