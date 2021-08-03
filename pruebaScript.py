import pandas as pd

#----------------------------------Script Lectura de datos----------------------------------------------
def abrirArchivos(ruta, letra, columnas):
    """ En esta función se abren los archivos con las columnas seleccionadas 
        ruta: es la ruta del archivo
        letra: es la identifiación del tipo de dato -> P=Precipitacion, T=Temperatura
        return df_datos: retorna los datos seleccionados
    """
    if letra == "P":
        df_datos = pd.read_csv(ruta, usecols = columnas)
        df_datos = df_datos.fillna(-1)
        #df_datos.fecha = pd.to_datetime(df_datos.fecha)



    else:
        df_datos = pd.read_csv(ruta, usecols = columnas)
        df_datos = df_datos.fillna(-99)
        #df_datos.fecha = pd.to_datetime(df_datos.fecha, usecols = columnas)

    return df_datos

ruta = 'C:/Users/Bender/Desktop/Mapas_ERA/Anexos_Final/Anexo A series IDEAM bruta/precipitacion_sup.csv'
precpGet = ['21210110', '21210120', '21210130']
df_precipSup = abrirArchivos(ruta, "P", precpGet)
print(df_precipSup.head(10))


        