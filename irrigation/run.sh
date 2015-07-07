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

#echo "Third test: proxroad + wet + proxriv + weigt=1.0,1.0,1.0 + better=m,l,l + scren=TOPOZONE<2,POP>800"
#echo "TL.py 0 1 0 1.0,1.0,1.0 m,l,l TOPOZONE,lt,2 POP,gt,800"

#python -i TL.py 0 1 0 1.0,1.0,1.0 m,l,l TOPOZONE,lt,2 POP,gt,800


#Scenario 1
#Screening:
#Criteria 1: LA_RICE1HA (26)[29] - 2.5 < LA_RICE1HA =<3.0
#Criteria 2: INDLIVELI (20)[23] <1.02
#Criteria 3: PL_P1HH (22)[25] <144.6
#Outranking:
#Criteria 1: MA_PROXROAD (37)[40] – lower the better
#Criteria 2: TAGAP_DRY (38)[41] – higher the better
#Criteria 3: SW_PROXRIV (40)[43] – lower the better

echo "Scenario 1"
python -i TL.py 1 0 0 1.0,1.0,1.0 l,m,l INDLIVELI,lt,1.02 PL_P1HH,lt,144.6
 

#Scenario 2 (same as above except for the last step in outranking)
#Screening:
#Criteria 1: LA_RICE1HA (26) - 2.5 < LA_RICE1HA =<3.0
#Criteria 2: INDLIVELI (20) <1.02
#Criteria 3: PL_P1HH (22) <144.6
#Outranking:
#Criteria 1: MA_PROXROAD (37) – lower the better
#Criteria 2: TAGAP_DRY (38) – higher the better
#Criteria 3: GW_BOREW (43) –  higher the better
 
#echo "Scenario 2"
#python -i TL.py 1 0 0 1.0,1.0,1.0 l,m,l INDLIVELI,lt,1.02 PL_P1HH,lt,144.6
 

#Scenario 3 (same as above except for the last step in outranking)
#Screening:
#Criteria 1: LA_RICE1HA (26) - 2.5 < LA_RICE1HA =<3.0
#Criteria 2: INDLIVELI (20) <1.02
#Criteria 3: PL_P1HH (22) <144.6
#Outranking:
#Criteria 1: MA_PROXROAD (37) – lower the better
#Criteria 2: TAGAP_DRY (38) – higher the better
#Criteria 3: IRRI_HEAD (45) –  yes the better


#echo "Scenario 3"
#python -i TL.py 1 0 0 1.0,1.0,1.0 l,m,l INDLIVELI,lt,1.02 PL_P1HH,lt,144.6
 
#Scenario 4 (same as above except for the last step in outranking)
#Screening:
#Criteria 1: LA_RICE1HA (26) - 2.5 < LA_RICE1HA =<3.0
#Criteria 2: INDLIVELI (20) <1.02
#Criteria 3: PL_P1HH (22) <144.6
#Criteria 4: INUNDATION (2) < 1.89
#Criteria 5: SOIL_LOWP (5) = 0 
#Outranking:
#Criteria 1: MA_PROXROAD (37) – lower the better
#Criteria 2: TAGAP_DRY (38) – higher the better
#Criteria 3: GW_BOREW (43) –  higher the better
