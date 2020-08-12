# splitcsv.py  - JPV 2020
#
# Este script toma un archivo .csv con usuarios de Office 365 de 
#  facultades y genera varios csv de 200 usuarios maximo, para cargar en 
#  Office 365 Admin. Esto es por una limitacion en la carga masiva de usuarios
#  de O365  

import pandas

facu="filo" #configurar facultad, esto lee un archivo csv con este nombre en dir actual
path = r'/home/jpvilla/src/csvutils/lotes/' # definir path de salida de los csv

df1 = pandas.read_csv(facu + ".csv")

# Rellenamos columnas comunes para todos los registros procesados
df1.Department = "Facultad de Filosofia y Letras"
df1["Country or Region"] = "Argentina"

# Funcion split dataframes adaptada de stack overflow
# entrada - df: un Dataframe, chunkSize: cantidad de registros del lote
# salida - una lista de DataFrames
#   (dividida en n lotes con la cantidad de registros indicada en chunkSize)
def s_df(df, chunk_size):
    chunks = list()
    num_chunks = len(df) // chunk_size + 1
    for i in range(num_chunks):
        chunks.append(df[i*chunk_size:(i+1)*chunk_size])
    return chunks

df2 = s_df(df1, 200)

subdfs=len(df2)

#recorre lista de DataFrames y manda cada DF spliteado a un csv
for j in range(subdfs):
     df2[j].to_csv(path + "filo-" + str(j) + ".csv", index=False)

