#!/bin/bash

rm -f villages.csv
rm -f points.*

echo "self-test system for TonleSap mapping structure"

python TL.py

echo "First test: proxroad + wet + proxriv + dwell + irrhead + weigt=1.0,1.0,1.0,1.0,1.0 + better=m,l,l,m,m"
echo "TL.py 0 1 0 0 1 1.0,1.0,1.0,1.0,1.0 m,l,l,m,m"

python -i TL.py 0 1 0 0 1 1.0,1.0,1.0,1.0,1.0 m,l,l,m,m


