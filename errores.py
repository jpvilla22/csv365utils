import pandas as pd

facu="filo"
tipo="errores"
path = r'/home/jpvilla/src/csvutils/lotes/' # use your path
department = "Facultad de Filosofia y Letras"

def indf(df, row):
    insert_loc = df.index.max()

    if pd.isna(insert_loc):
        df.loc[0] = row
    else:
        df.loc[insert_loc + 1] = row

# Levanto el dataframe consolidado de errores
dfc = pd.read_csv(path + facu + "-consolidado-" + tipo + ".csv")

# Creo dos dataframes vacios para almacenar los resultados
dferr = pd.DataFrame(columns = ["Display name","Username","Error","Additional information"])
dfcreate = pd.DataFrame(columns = ["User Name","First Name","Last Name","Display Name","Job Title","Department","Office Number","Office Phone","Mobile Phone","Fax","Address","City","State or Province","ZIP or Postal Code","Country or Region"])

for j in range(3): #cambiar por len(dfc)
    nom=dfc.iat[j,0]
    usr=dfc.iat[j,1]
    erro=dfc.iat[j,2]

    print("\nNombre en " + facu + ": " + nom)
    print("Usuario pedido: " + usr)
    print("Error: " + erro)


    resp = input("\nIngrese 1 para cambiar usuario o cualquier otro caracter para indicar repetido: ")
    if resp == "1":
        resp3 = "0"
        while resp3 != "1":
            resp2 = input("\nIngrese nuevo nombre de usuario SIN @uba.ar: ")
            resp3 = input("\nIngrese 1 para confirmar usuario "+ resp2 +" cualquier otro caracter para reintentar: ") 
        print("Ud ingreso " + resp2)
        indf(dfcreate,[resp2+"@uba.ar","","",nom,"",department,"","","","","","","","","Argentina"])      
    else:
        print("Repetido")
        indf(dferr,[str(usr),str(nom),str(erro),"Creemos que puede ser el mismo usuario y no un homonimo"])

#dfcreate.to_csv(path + facu + "-crear.csv", index=False)
#dferr.to_csv(path + facu + "-repetidos.csv", index=False)
