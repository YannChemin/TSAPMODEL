#!/bin/bash

rm -f villages.csv
rm -f points.*

echo "self-test system for TonleSap mapping structure"

python TLA.py

#echo "First test: MA_INDACT + SW_PROXRIV + FISHPRO + weigt=1.0,1.0,1.0 + better=m,l,l"
#echo "TLA.py 0 0 0 1.0,1.0,1.0 m,l,l"

#python TLA.py 0 0 0 1.0,1.0,1.0 m,l,l

#echo "Second test: MA_INDACT + SW_PROXRIV + FISHPRO + weigt=1.0,1.0,1.0 + better=m,l,l + scren=TOPOZONE<=2"
#echo "TLA.py 0 0 0 1.0,1.0,1.0 m,l,l TOPOZONE,le,2"

#python TLA.py 0 0 0 1.0,1.0,1.0 m,l,l TOPOZONE,le,2

echo "Third test: MA_INDACT + SW_PROXRIV + FISHPRO + weigt=1.0,1.0,1.0 + better=m,l,l + scren=TOPOZONE<2,POP>120.0"
echo "TLA.py 0 0 0 1.0,1.0,1.0 m,l,l TOPOZONE,lt,2 POP,gt,120.0"

python TLA.py 0 0 0 1.0,1.0,1.0 m,l,l TOPOZONE,lt,2 POP,gt,120
