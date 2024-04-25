import os
import zipfile
import pandas as pd

# Descomprimir el archivo data.zip
with zipfile.ZipFile("data.zip", "r") as zip_ref:
    zip_ref.extractall("data")

# Definir la función para leer los archivos de texto y crear el DataFrame
def create_dataset(folder):
    data = []
    for sentiment in os.listdir(folder):
        sentiment_path = os.path.join(folder, sentiment)
        if os.path.isdir(sentiment_path):  # Verificar si es un directorio
            for file_name in os.listdir(sentiment_path):
                file_path = os.path.join(sentiment_path, file_name)
                if file_name.endswith(".txt"):  # Verificar si es un archivo de texto
                    with open(file_path, "r", encoding="utf-8") as file:
                        phrase = file.read().strip()
                    data.append({"phrase": phrase, "sentiment": sentiment})
    return pd.DataFrame(data)

# Crear el DataFrame para el conjunto de entrenamiento
train_dataset = create_dataset("data/train")

# Crear el DataFrame para el conjunto de pruebas
test_dataset = create_dataset("data/test")

# Guardar los DataFrames en archivos CSV
train_dataset.to_csv("train_dataset.csv", index=False)
test_dataset.to_csv("test_dataset.csv", index=False)
