import pandas as pd
import numpy as np


df = pd.read_excel("base_latina.xlsx")
df["CedulaPasaporte"] = df["CedulaPasaporte"].astype(str)
df["Beca_Estimada"] = df["Beca_Estimada"].apply(lambda x: str(np.round(x*100, 2)) + " %")
df["upper.beca"] = df["upper.beca"].apply(lambda x: str(np.round(x*100, 2)) + " %")

df = df.rename(columns={"NOMBRE_CARRERA": "Carrera", 
                       "NOMBRE_ENFASIS": "Énfasis",
                       "NOMBRE_GRADO": "Grado",
                       "TOTAL_CURSOS": "Curso",
                       "Beca_Estimada": "Beca Media",
                       "upper.beca": "Máximo de Beca"})


def buscar(cedula):
    lts = ["MARCA", "SEDE", "NOMBRE_FACULTAD", "Carrera", "Énfasis", "Grado", "Curso", "Beca Media", "Máximo de Beca"]
    
    ff = df.loc[(df["CedulaPasaporte"] == cedula), lts]   
    
    
    
    return ff