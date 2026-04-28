import matplotlib
matplotlib.use('Agg') #Esto lo consulté por un error (estaría bien una retroalimentacion para saber cómo de pronto no usar esto, lo agradecería para aprender más)

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
conn = sqlite3.connect("arqueologia.db")

df = pd.read_sql_query("SELECT * FROM estrellas", conn)

plt.style.use("dark_background")

fig1, ax1 = plt.subplots(figsize=(6,6))
fig1.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.9)

ax1.scatter(df["pmRA"], df["pmDE"], s=1, color="white")

ax1.set_xlabel("pmRA (mas/yr)")
ax1.set_ylabel("pmDE (mas/yr)")
ax1.set_title("Movimiento propio")

ax1.grid(alpha=0.2)

fig1.savefig("movimiento_propio.png", dpi=300, bbox_inches=None)
plt.close(fig1)

query_cluster = """
SELECT * FROM estrellas
WHERE pmRA BETWEEN -5 AND 0
AND pmDE BETWEEN -7 AND -2
"""

df_cluster = pd.read_sql_query(query_cluster, conn)

#---------------
# Ya para el diagrama HR
# -------------------------------------------------------

color = df_cluster["BPmag"] - df_cluster["RPmag"]
gmag = df_cluster["Gmag"]

# Filtro físico básico
mask = (
    (color > -0.5) & (color < 3.0) &
    (gmag > 0) & (gmag < 18)
)

color = color[mask]
gmag = gmag[mask]

fig2, ax2 = plt.subplots(figsize=(7,9))
fig2.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.9) # Tocó hacer un ajuste

# Scatter con colores tipo HR real (este sc fue hecho por ia, la verdad lo hace)
sc = ax2.scatter(                 #(más bonito que yo, entonces lo dejo así)
    color,
    gmag,
    c=color,
    cmap="RdYlBu_r",
    s=3,
    alpha=0.8
)

ax2.set_xlabel("Índice de color (BP - RP)")
ax2.set_ylabel("Magnitud G")
ax2.set_title("Diagrama HR - Omega Centauri")

# Aqui invierto el eje para que quede la forma final
ax2.invert_yaxis()

# Mero ajuste   de limites para verla mejor y centrada (a ojo)
ax2.set_xlim(-0.5, 3)
ax2.set_ylim(18, 0)

ax2.grid(alpha=0.15)

# Ajuste de la barra de color
cbar = fig2.colorbar(sc, ax=ax2, pad=0.02)
cbar.set_label("Color estelar (BP - RP)")

fig2.savefig("diagrama_hr.png", dpi=300, bbox_inches=None) # "bbox_inches me solucionaba un error de ploteo"
plt.close(fig2)

# -------------------------------------------------------
conn.close()

print("Gráficas generadas correctamente.")
