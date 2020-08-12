import pandas as pd
import glob

facu="filo"
tipo="errores"

path = r'/home/jpvilla/src/csvutils/lotes/' # use your path
all_files = glob.glob(path + facu +"-?-" + tipo+ ".csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

df.to_csv(path + facu + "-consolidado-"+ tipo +".csv", index=False)

