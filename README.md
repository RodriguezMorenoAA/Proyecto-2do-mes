# Proyecto de Minería de Datos – Omega Centauri

## Descripción
En este proyecto se trabajó con datos del cúmulo globular Omega Centauri usando información del catálogo Gaia DR3. La idea fue descargar datos reales, limpiarlos y luego analizarlos para ver cómo se comportan las estrellas especialmente en el diagrama HR.

## Coordenadas
coordenadas de SIMBAD a grados decimales:

* RA: 201.697°
* Dec: −47.479°
## Pasos del proyecto

### 1. Descarga de datos

Se hizo una consulta ADQL (por cierto fue la parte más difícil y que
me sigue costando sinceramente) al catálogo Gaia DR3 en VizieR para obtener
estrellas en un radio de 0.5 grados alrededor de Omega Centauri.

Primero el bash 1_descarga_omega.sh

Esto genera el archivo:

'omega_bruto.csv'

### 2. Crear base de datos
Se cargó el CSV en Python y ya pues se eliminaron filas con datos
faltantes (en movimientos propios y magnitudes)
y luego se guardó todo en una base de datos SQLite.

en el bash se ejecuta un python3 2_crear_db.py

Esto genera:

arqueologia.db
tabla: "estrellas"

### 3. Análisis

ejecutando un bash python3 3_analisis.py


Esto genera:

movimiento_propio.png
diagrama_hr.png

## Qué se observa
### Movimiento propio
En la gráfica de pmRA vs pmDE se ve:

> una nube grande centrada cerca de (0,0), que corresponde a estrellas de la Vía Láctea
> un grupo más compacto desplazado, que corresponde a Omega Centauri

### Filtro
A partir de la gráfica se eligió un rango aproximado:

pmRA  entre -5 y 0
pmDE entre -7 y -2

Con esto se logra aislar bastante bien el cúmulo, todo se hizo a ojo

### Diagrama HR
Se usó:

Color: BP - RP
Magnitud: Gmag (invertida)

Antes del filtro el diagrama es más desordenado
pero después se ve más claro y con mejor estructura
porque ya no hay tantas estrellas que no pertenecen al cúmulo.

## Conclusión
El uso del movimiento propio permite separar
estrellas del cúmulo de las de la Vía Láctea.
Esto hace que el diagrama HR se vea más limpio y tenga más sentido físicamente.

## Dependencias

en el bash:
pip install pandas matplotlib

## Notas

	Los archivos se pueden volver a generar ejecutando los scripts
	
	El trabajo lo hice en Ubuntu usando bash, Python y SQLite obviamente
	con los demás recursos visto en los ejecutables, y claramente usé la ia	
	para que ese diagrama hr se viera bonito
	¿Por qué? Tenia que verse bonita esa cosa, por el curso de estelar también.

	Lo disfruté, aunque fue muy frustrante la parte de ADQL, es demasiado
	frustrante y no se por qué me cuesta tanto, sin embargo cuando se usa
	SQL y ADQL desde python como que no se hace tan complejo, supongo que
	porque todo se hace en el mismo entorno.

	Gracias por el proyecto y las clases de esta primera mitad
