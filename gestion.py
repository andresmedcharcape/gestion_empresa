
"""
Created on Fri Aug 27 22:01:47 2021
@author: Charcape
"""


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


filename = 'data_gestion.txt'
delimiter = '\t'


def preparar_datos(filename,delimiter):
    pd.options.display.max_rows = None
    pd.options.display.max_columns = None
    df = pd.read_csv(filename, delimiter=delimiter)
    df.isnull().sum()
    df.nunique()
    df.columns = ['CONTACTO', 'FECHA', 'HORA', 'AGENTE', 'GES_VTA', 'GES_VAL',
       'GES_NOVAL', 'GES_NOCON', 'GES_TER', 'CODIGO_CAMPANIA', 'Usuario',
       'NOMMES', 'AÑO', 'TIPOGESTION', 'gestion', 'SUBGESTION', 'SUPERVISOR',
       'Sub_Campaña']
    df = df.replace(np.nan,'ninguno')
    df['FECHA'] = pd.to_datetime(df['FECHA']).dt.strftime('%Y-%d-%m')
    return df
    

def evolutivo_ventas(fechas,ventas):
    plt.figure(figsize=(20,20))
    fig = plt.bar(x=fechas,height=ventas)
    plt.xlabel('Fechas')
    plt.ylabel('Ventas')
    plt.title('Evolutivo de Ventas')
    for i in range(len(ventas)):
        plt.annotate(str(ventas[i]), xy=(fechas[i],ventas[i]), ha='center', va='bottom')
    plt.savefig('evolutivo_ventas.jpg')
    plt.show()

def evolutivo_efectividad(fechas,efectividad):
    plt.figure(figsize=(20,20))
    fig = plt.plot(efectividad)
    plt.xlabel('Fechas')
    plt.ylabel('Efectividad')
    plt.title('Evolutivo de Efectividad')
    plt.savefig('evolutivo_ventas.jpg')
    plt.show()
    

df = preparar_datos(filename,delimiter)
fechas = df['FECHA'].unique()
ventas = df.groupby(df['FECHA'])['GES_VTA'].sum()
valida = df.groupby(df['FECHA'])['GES_VAL'].sum()
efectividad = (ventas / valida).apply(lambda x: x * 100)
evolutivo_ventas(fechas, ventas)
evolutivo_efectividad(fechas, efectividad)
