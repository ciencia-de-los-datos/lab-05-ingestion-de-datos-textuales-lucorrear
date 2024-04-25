import os
import pandas as pd
import pyarrow.csv as pv
import pyarrow as pa
import zipfile

# Primero, descomprimimos el archivo data.zip si aún no está descomprimido
if not os.path.exists('data'):
    with zipfile.ZipFile('data.zip', 'r') as zip_ref:
        zip_ref.extractall('data')

# Función para leer los archivos de texto y obtener los datos
def read_files(folder, encoding='utf-8'):
    data = []
    for sentiment in os.listdir(folder):
        sentiment_path = os.path.join(folder, sentiment)
        if os.path.isdir(sentiment_path):
            for file in os.listdir(sentiment_path):
                file_path = os.path.join(sentiment_path, file)
                with open(file_path, 'r', encoding=encoding, errors='replace') as f:
                    content = f.read()
                    data.append({'phrase': content, 'sentiment': sentiment})
    return data

# Lectura de los datos de entrenamiento
train_data = read_files('data/train')

# Lectura de los datos de prueba
test_data = read_files('data/test')

# Convertimos los datos a DataFrames de pandas
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

# Convertimos los DataFrames de pandas a objetos Table de Arrow
train_table = pa.Table.from_pandas(train_df)
test_table = pa.Table.from_pandas(test_df)

# Guardamos los objetos Table en archivos CSV utilizando pyarrow
pv.write_csv(train_table, 'train_dataset.csv')
pv.write_csv(test_table, 'test_dataset.csv')    