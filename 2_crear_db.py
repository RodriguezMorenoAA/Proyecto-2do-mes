import pandas as pd
import sqlite3

df = pd.read_csv("omega_bruto.csv")
df.columns = df.columns.str.strip()
columnas_clave = ["pmRA", "pmDE", "Gmag", "BPmag", "RPmag"]

df_limpio = df.dropna(subset=columnas_clave)
df_limpio = df_limpio.reset_index(drop=True)

conn = sqlite3.connect("arqueologia.db")

df_limpio.to_sql("estrellas", conn, if_exists="replace", index=False)

conn.close()

print("Base de datos creada correctamente: arqueologia.db")
