#!/bin/bash

rm -f villages.csv
rm -f points.*

echo "self-test system for TonleSap mapping structure"

python TL.py

#echo "First test: proxroad + wet + proxriv + weigt=1.0,1.0,1.0 + better=m,l,l"
#echo "TL.py 0 1 0 1.0,1.0,1.0 m,l,l"

#python -i TL.py 0 1 0 1.0,1.0,1.0 m,l,l

#echo "Second test: proxroad + wet + proxriv + weigt=1.0,1.0,1.0 + better=m,l,l + scren=TOPOZONE<=2"
#echo "TL.py 0 1 0 1.0,1.0,1.0 m,l,l TOPOZONE,le,2"

#python -i TL.py 0 1 0 1.0,1.0,1.0 m,l,l TOPOZONE,le,2

echo "Third test: proxroad + wet + proxriv + weigt=1.0,1.0,1.0 + better=m,l,l + scren=TOPOZONE<2,POP>800"
echo "TL.py 0 1 0 1.0,1.0,1.0 m,l,l TOPOZONE,lt,2 POP,gt,800"

python -i TL.py 0 1 0 1.0,1.0,1.0 m,l,l TOPOZONE,lt,2 POP,gt,800


