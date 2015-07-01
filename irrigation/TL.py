#!/usr/bin/env python

import os,sys

def usage():
	"""
	This program is implementing a pairwise comparison for a selected
	number of criteria for villages of Tonle Sap.
	"""
	os.system("tput setaf 2")
	print("\n----------------------------------------------------------")
	print("Usage:")
	print("----------------------------------------------------------")
	print("This program needs the tablefile.csv in the same directory\n")
	print("TL.exe crit1 crit2 crit3 crit4 crit5 weigt btter")
	print("\n[subsetcol1=Value [subs...]]\n")
	print("It will run with five criteria:") 
	print("\tcrit1: MA_INDACT, MA_PROXROAD (1 choice)") 
	print("\tcrit2: TAGAP_DRY, TAGAP_WET (1 choice)") 
	print("\tcrit3: SW_PROXRIV, SW_PONDS (1 choice)") 
	print("\tcrit4: GW_DWELL, GW_BOREW (1 choice)") 
	print("\tcrit5: IRRI_SCH, IRRI_HEAD (1 choice)") 
	print("\tweigt: 0.0[,0.0[,..]] (comma separated float vals)") 
	print("\tbtter: m[,m[,..]] (comma separated [m;l], i.e. more or less)") 
	print("----------------------------------------------------------")
	os.system("tput setaf 3")
	print("Example 1:") 
	print("TL.py 0 0 0 0 0 1.0,1.0,1.0,1.0,1.0 m,l,l,m,m") 
	print("Means that:") 
	print("TL.py MA_INDACT TAGAP_DRY SW_PROXRIV GW_DWELL IRRI_SCH 1.0,1.0,1.0 more,less,less") 
	print("----------------------------------------------------------")
	os.system("tput setaf 4")
	print("Example 2:") 
	print("TL.py 0 0 1 0 0 1.0,1.0,1.0,1.0,1.0 m,l,l,l,l") 
	print("Means that:") 
	print("TL.py MA_INDACT TAGAP_DRY SW_PONDS GW_DWELL IRRI_SCH 1.0,1.0,1.0,1.0,1.0 more,less,more,less,less") 
	print("----------------------------------------------------------")
	print("\n") 
	os.system("tput setaf 9")

#import the csv file 
import numpy as np

data = np.genfromtxt("tablefile.csv", skip_header=1, delimiter=",")
#Clarify the table access order, TO BE CHANGED IF NEW tablefile.csv
#Access XCOORD Full Column with data[:,137]
#Access YCOORD Full Column with data[:,138]
XCOORDLIST=np.asarray(data[:,0])
YCOORDLIST=np.asarray(data[:,1])
#Create Village output list
villagelist=np.zeros(data.shape[0])
#Create outranking criteria column list
#Access MA_INDACT Full Column with data[:,39]
#Access MA_PROXROAD Full Column with data[:,40]

#Access TAGAP_DRY Full Column with data[:,41]
#Access TAGAP_WET Full Column with data[:,42]

#Access SW_PROXRIV Full Column with data[:,43]
#Access SW_PONDS Full Column with data[:,44]

#Access GW_DWELL Full Column with data[:,45]
#Access GW_BOREW Full Column with data[:,46]

#Access IRRI_SCH Full Column with data[:,47]
#Access IRRI_HEAD Full Column with data[:,48]

#set critcolno with any of the critno[index]
mastercritno=[39,40,41,42,43,44,45,46,47,48]

#------------------------
#PARSING ARGUMENTS
#------------------------

#Minimum number of input variables
#1 csv weights list
#1 csv better list (more is better="m")
if (len(sys.argv) < 6):
	os.system("tput setaf 1")
	print("\ninsufficient amount of input variables")
	os.system("tput setaf 9")
	usage()
	exit(1)

#Collect the user's choices for the criteria
crit1=sys.argv[1]
crit2=sys.argv[2]
crit3=sys.argv[3]
crit4=sys.argv[4]
crit5=sys.argv[5]

#Create column index of selected criteria 
critno=[]
#Access MA_INDACT Full Column with data[:,39]
#Access MA_PROXROAD Full Column with data[:,40]
if(int(crit1)==0):
	critno.append(39)
else:
	critno.append(40)
#Access TAGAP_DRY Full Column with data[:,41]
#Access TAGAP_WET Full Column with data[:,42]
if(int(crit2)==0):
	critno.append(41)
else:
	critno.append(42)
#Access SW_PROXRIV Full Column with data[:,43]
#Access SW_PONDS Full Column with data[:,44]
if(int(crit3)==0):
	critno.append(43)
else:
	critno.append(44)
#Access GW_DWELL Full Column with data[:,45]
#Access GW_BOREW Full Column with data[:,46]
if(int(crit4)==0):
	critno.append(45)
else:
	critno.append(46)
#Access IRRI_SCH Full Column with data[:,47]
#Access IRRI_HEAD Full Column with data[:,48]
if(int(crit5)==0):
	critno.append(47)
else:
	critno.append(48)


#Collect the weight list
w=[]
w.extend(sys.argv[6].split(","))
if(len(w)<5):
	os.system("tput setaf 1")
	print("\nWeights list has less than 5 criteria members")
	os.system("tput setaf 9")
	usage()
	exit(1)

#Collect the "more/less is better" list
lmib=[]
lmib.extend(sys.argv[7].split(','))
if(len(lmib)<5):
	os.system("tput setaf 1")
	print("\nList of 'more/less' has less than 5 criteria members")
	os.system("tput setaf 9")
	usage()
	exit(1)

#------------------------
#END OF PARSING ARGUMENTS
#------------------------

def mkvalrange(datacol):
	"""
	Create range data for a criterium data column
	"""
	return(np.max(datacol)-np.min(datacol))

def vpwc(val1,val2,valrange):
	"""
	Village pairwise Comparison for a given criterium
	"""
	return((val1-val2)/valrange)

def assignvpwc(vil1rowno,vil2rowno,critcolno,counter):
	#print(vil1rowno,vil2rowno,critcolno,villagelist.shape[0])
	#Compute value range for a given criterium
	#HINT: use stats range for column or row data table
	datacol=data[:,critcolno]
	valrange=mkvalrange(datacol)
	#get value from each village for a given criterium
	val1=data[vil1rowno,critcolno]
	val2=data[vil2rowno,critcolno]
	#compute pairwise comparison for a given criterion
	value=vpwc(val1,val2,valrange)
	#Assign given weight to value
	value*=float(w[counter])
	#Adjust the LessIsBetter parameter from User input
	if(lmib[counter]=="m"):
		LessIsBetter=False
	elif(lmib[counter]=="l"):
		LessIsBetter=True
	else:
		print("list of more/less has a typo, use 'm' or 'l'")
		usage()
		exit(1)

	if(LessIsBetter==True):
		if(value > 0):
			vil1out=float(value)
			vil2out=0.0
		elif(value == 0):
			vil1out=0.0
			vil2out=0.0
		else:
			vil2out=float(value)
			vil1out=0.0
	else:#MoreIsBetter
		if(value < 0):
			vil1out=float(value)
			vil2out=0.0
		elif(value == 0):
			vil1out=0.0
			vil2out=0.0
		else:
			vil2out=float(value)
			vil1out=0.0
	return vil1out,vil2out

#set counter for weight and lmib user input forwarding
counter=0
for critcolno in critno:
	print("critcolno=%d" % critcolno)
	for vil1rowno in range(data.shape[0]):
		for vil2rowno in range(data.shape[0]):
			villagelist[vil1rowno],villagelist[vil2rowno]=assignvpwc(vil1rowno,vil2rowno,critcolno,counter)
	counter+=1

#Temporary stage: OUTPUT an XYZ text file
f=open("villages.csv","w")
for i in range(data.shape[0]-1):
	try:
		strng=(str(XCOORDLIST[i])+","+str(YCOORDLIST[i])+","+str(villagelist[i])+"\n")
		f.write(strng)
	except:
		print("Error writing csv file, skipping row")
f.close()

#Final stage: Create a new shapefile directly
import osgeo.ogr, osgeo.osr
sr = osgeo.osr.SpatialReference()
sr.ImportFromEPSG(3148)
driver = osgeo.ogr.GetDriverByName('ESRI Shapefile')
if os.path.exists('points.shp'):
	driver.DeleteDataSource('points.shp')
shpData = driver.CreateDataSource('points.shp')
if shpData is None:
	print ' Could not create file'
	sys.exit(1)
lyr = shpData.CreateLayer('layer1', sr, osgeo.ogr.wkbPoint)
lyrDef = lyr.GetLayerDefn()
idField = osgeo.ogr.FieldDefn("ID_0", osgeo.ogr.OFTInteger)
lyr.CreateField(idField)
fidx = 0
for i in range(len(XCOORDLIST)):
	ftr = osgeo.ogr.Feature(lyrDef)
	pt = osgeo.ogr.Geometry(osgeo.ogr.wkbPoint)
	pt.SetPoint(0, XCOORDLIST[i], YCOORDLIST[i])
	ftr.SetGeometry(pt)
	ftr.SetFID(fidx)
	ftr.SetField(ftr.GetFieldIndex('ID_0'),villagelist[i])
	lyr.CreateFeature(ftr)
	fidx += 1

shpData.Destroy()


#create shapefile projection file
sr.MorphToESRI()
file = open('points.prj', 'w')
file.write(sr.ExportToWkt())
file.close()

