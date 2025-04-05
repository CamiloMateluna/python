###Solución taller 1 Camilo Mateluna

###Sección 1

#Ejercicio 1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#cargar el dataframe

df = pd.read_csv("Titanic-Dataset.csv")

print("\nPrimeras filas del DataFrame:")
print(df.head())

print("\nDescripción estadística:")
print(df.describe())


#Ejercicio 2

#Listar los nombres de las columnas
col = df.columns
print(col)

#Verificar los tipos
tipos = df.dtypes
print(tipos)


###Sección 2

#Ejercicio 3

 #Media
media=df.mean(numeric_only=True)
print(media)

#Mediana
mediana=df.median(numeric_only=True)
print(mediana)

#desviación estándar
ds=df.std(numeric_only=True)
print(ds)

#Conteo de valores únicos en columnas categóricas:

#Para la columna "Name"
conteo_name = df["Name"].value_counts
print(conteo_name)

#Para contar todas las columnas
conteo_col = df.nunique()
print(conteo_col)

#Ejercicio 4

#Ver cuantos faltantes hay por columna
num_faltantes = df.isnull().sum()

#Inspecciona si alguna columna (ej. Cabin, Age) tiene muchos valores nulos

#PROBANDO

