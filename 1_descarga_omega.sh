#!/bin/bash

ADQL="SELECT Source,RA_ICRS,DE_ICRS,pmRA,pmDE,Gmag,BPmag,RPmag FROM \"I/355/gaiadr3\" WHERE 1=CONTAINS(POINT('ICRS',RA_ICRS,DE_ICRS),CIRCLE('ICRS',201.697,-47.479,0.5))"

URL_ADQL=$(echo $ADQL | sed 's/ /+/g')

TAP_URL="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="

echo "Descargando datos de Omega Centauri..."

# Descarga
wget -q -O omega_bruto.csv "$TAP_URL$URL_ADQL"

echo "Descarga finalizada: omega_bruto.csv"
