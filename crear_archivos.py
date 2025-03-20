import os

# Configuración
folder_path = r"C:\Users\LENOVO\Documents\8vo semestre\proyecto-nuevo"  # Ruta de tu carpeta
num_files = 28  # Número de archivos a crear

os.makedirs(folder_path, exist_ok=True)  # Crea la carpeta si no existe

for i in range(1, num_files + 1):
    file_name = os.path.join(folder_path, f"ejercicio_{i}.py")
    with open(file_name, "w") as f:
        f.write(f"# Este es el archivo ejercicio_{i}.py\n")
    print(f"Archivo {file_name} creado.")
