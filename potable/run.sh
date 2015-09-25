#!/bin/bash

rm -f villages.csv
rm -f points.*

echo "self-test system for TonleSap mapping structure"

python TLP.py

#echo "First test: WA_AWAY + WS_UNSAFE + WT_UNTREAT + weight=1.0,1.0,1.0 + better=m,m,l"
#echo "TLP.py 0 0 0 1.0,1.0,1.0 m,m,l"

#python TLP.py 0 0 0 1.0,1.0,1.0 m,m,l

#echo "Second test: WA_AWAY + WS_UNSAFE + WT_UNTREAT + weight=1.0,1.0,1.0 + better=m,m,l + scren=TOPOZONE<=2"
#echo "TLP.py 0 0 0 1.0,1.0,1.0 m,m,l TOPOZONE,le,2"

#python TLP.py 0 0 0 1.0,1.0,1.0 m,m,l TOPOZONE,le,2

echo "Third test: WA_AWAY + WS_UNSAFE + WT_UNTREAT + weight=1.0,1.0,1.0 + better=m,m,l + scren=TOPOZONE<2,POP>120.0"
echo "TLP.py 0 0 0 1.0,1.0,1.0 m,m,l TOPOZONE,lt,2 POP,gt,120"

python TLP.py 0 0 0 1.0,1.0,1.0 m,m,l TOPOZONE,lt,2 POP,gt,120.0

