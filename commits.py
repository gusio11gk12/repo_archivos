import subprocess
from datetime import datetime, timedelta
import os

# Configuración
repo_dir = r"C:\Users\LENOVO\Documents\8vo semestre\proyecto-nuevo"  # Ruta a tu repositorio
start_date = datetime(2025, 2, 1)  # Fecha de inicio para los commits
days = 28  # Número de archivos/días
branch = "master"  # Rama en la que estás trabajando

os.chdir(repo_dir)

for i in range(days):
    file_name = f"ejercicio_{i+1}.py"
    
    if os.path.exists(file_name):
        subprocess.run(["git", "add", file_name])
        commit_date = (start_date + timedelta(days=i)).strftime("%Y-%m-%dT12:00:00")

        # Variables de entorno para fechas falsas
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = commit_date
        env["GIT_COMMITTER_DATE"] = commit_date

        subprocess.run(["git", "commit", "-m", f"Añadir {file_name} en {commit_date}"], env=env)
    else:
        print(f"Archivo {file_name} no encontrado, saltando...")

subprocess.run(["git", "push", "origin", branch])
