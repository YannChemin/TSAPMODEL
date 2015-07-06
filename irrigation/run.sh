#!/bin/bash

rm -f villages.csv
rm -f points.*

echo "self-test system for TonleSap mapping structure"

python TL.py

#echo "First test: proxroad + wet + proxriv + weigt=1.0,1.0,1.0 + better=m,l,l"
#echo "TL.py 0 1 0 1.0,1.0,1.0 m,l,l"

#python -i TL.py 0 1 0 1.0,1.0,1.0 m,l,l

echo "Second test: proxroad + wet + proxriv + weigt=1.0,1.0,1.0 + better=m,l,l + scren=TOPOZONE<=2"
echo "TL.py 0 1 0 1.0,1.0,1.0 m,l,l TOPOZONE,ge,2"

python -i TL.py 0 1 0 1.0,1.0,1.0 m,l,l TOPOZONE,ge,2


