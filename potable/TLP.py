#!/usr/bin/env python
#TODO: MASKING at the beginning to reduce the array and the pairwise comp.
import os,sys,math

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
	print("TLP.exe crit1 weigt btter scren")
	print("\n\n")
	print("It will run with one criteria:") 
	print("\tcrit1: WA_AWAY (Compulsory, use 0)") 
	print("\tcrit2: WS_UNSAFE (Compulsory, use 0)") 
	print("\tcrit3: WT_UNTREAT (Compulsory, use 0)") 
	print("\tweigt: 1.0,1.0,0.0 [0.0-1.0]") 
	print("\tbtter: m,m,l [m (more) or l (less)]") 
	print("\tscren: POP,>,200 [ SEXR,<,0.5 [ ..]] (comma separated info)") 
	print("----------------------------------------------------------")
	print("\tscren is a set of screening columns thresholds")
	print("\tit tells the program to mask out using thresholds")
	print("\tUp to 8 screening criteria will be read, no warning if more")
	print("\tavailable types are:")
	print("\tTOPOZONE,INUNDATION,ELEVATION,DRYRAIN,SOIL_LOWP,SOIL_MEDP,SOIL_HIGHP,TAGAP_DRY,TAGAP_WET,CONZ_PROX,CONZ_PEOP,POP,SEXR,KW_UPTOSEC,KW_ILLIT,LF_RICE,LF_VEGE,LF_LSC,LF_WAGED,INDLIVELI,MIGRANTS,PL_P1HH,PL_P2HH,PL_NONPHH,RYLD_WET,RYLD_DRY,RYLD_DANDW,RYLD_RANDI,LA_RICE1HA,LA_CULT1HA,INDAGRIM,A_IRRIC,A_IRRIR,A_IRRIP,A_IRRIW")
	print("\t")
	print("\ti.e. TOPOZONE,le,3 (comma separators are compulsory)")
	print("\ti.e. ELEVATION,ge,5")
	print("\tge: >=\tle: <=")
	print("\tgt: >\tlt: <")
	print("\teq: ==\tne: !=")
	print("----------------------------------------------------------")
	os.system("tput setaf 3")
	print("Example 1:") 
	print("TL.py 0 0 0 1.0,1.0,1.0 m,m,l") 
	print("Means that:") 
	print("TL.py WA_AWAY WS_UNSAFE WT_UNTREAT 1.0,1.0,1.0 more,more,less") 
	print("----------------------------------------------------------")
	os.system("tput setaf 4")
	print("Example 2:") 
	print("TL.py 0 0 0 1.0,1.0,1.0 m,m,l TOPOZONE,le,3") 
	print("Means that:") 
	print("TL.py WA_AWAY WS_UNSAFE WT_UNTREAT 1.0,1.0,1.0 more,more,less with TOPOZONE less or equal to 3") 
	print("----------------------------------------------------------")
	print("\n") 
	os.system("tput setaf 9")

#import the csv file 
import numpy as np

data = np.genfromtxt("tablefile.csv", skip_header=1, delimiter=",")
#Clarify the table access order, TO BE CHANGED IF NEW tablefile.csv
#Access XCOORD Full Column with data[:,137]
#Access YCOORD Full Column with data[:,138]
XL=np.asarray(data[:,0])
YL=np.asarray(data[:,1])
#Create Village output list
VL=np.zeros(data.shape[0])
#Create Village MASK list
MK=np.ones(data.shape[0])
#Create outranking criteria column list
#Access WA_AWAY Full Column with data[:,36]
#Access WS_UNSAFE Full Column with data[:,37]
#Access WS_UNTREAT Full Column with data[:,38]

#set critcolno with any of the critno[index]
mastercritno=[36,37,38]

#------------------------
#PARSING ARGUMENTS
#------------------------

#Minimum number of input variables
#1 csv weights list
#1 csv better list (more is better="m")
if (len(sys.argv) < 5):
	os.system("tput setaf 1")
	print("\ninsufficient amount of input variables")
	os.system("tput setaf 9")
	usage()
	exit(1)

#Collect the user's choices for the criteria
crit1=sys.argv[1]
crit2=sys.argv[2]
crit3=sys.argv[3]

#Create column index of selected criteria 
critno=[]
#Access WA_AWAY Full Column with data[:,36]
critno.append(mastercritno[0])
#Access WS_UNSAFE Full Column with data[:,37]
critno.append(mastercritno[1])
#Access WS_UNTREAT Full Column with data[:,38]
critno.append(mastercritno[2])

#Collect the weight list
w=[]
w.extend(sys.argv[3].split(","))
if(len(w)<3):
	os.system("tput setaf 1")
	print("\nWeights list has less than 3 criteria members")
	os.system("tput setaf 9")
	usage()
	exit(1)

#Collect the "more/less is better" list
lmib=[]
lmib.append(sys.argv[4].split(","))
if(len(lmib)<3):
	os.system("tput setaf 1")
	print("\nList of 'more/less' has less than 3 criteria member")
	os.system("tput setaf 9")
	usage()
	exit(1)

if(len(sys.argv)>4):
	#Create the masking list
	screnlist=[]
	for i in range(5,len(sys.argv),1):
		if(i<=5):
			screnlist.append(sys.argv[i])

	scren={'TOPOZONE':4,'INUNDATION':5,'ELEVATION':6,'DRYRAINFALL':7,'SOIL_LOWP':8,'SOIL_MEDP':9,'SOIL_HIGHP':10,'TAGAP_DRY':11,'TAGAP_WET':12,'CONZ_PROX':13,'CONZ_PEOP':14,'POP':15,'SEXR':16,'KW_UPTOSEC':17,'KW_ILLIT':18,'LF_FISH':19,'LF_CROP':20,'LF_ANI':21,'LF_WAGED':22,'INDLIVELI':23,'MIGRANTS':24,'FP_WRK':25,'FP_FEMWRK':26,'PL_P1HH':27,'PL_P2HH':28,'PL_NONPHH':29,'RYLD_WET':30,'RYLD_DRY':31,'LA_RICE1HA':32,'LA_CULT1HA':33,'MA_INDACT':34,'MA_PROXROAD':35}

	for i in range(len(screnlist)):
		a=screnlist[i].split(',')
		print(a)
		try:
			b=int(scren[str(a[0])])#extract col number from dict
			print(b)
			c=str(a[1])#Get comparison symbol
			print(c)
			d=float(a[2])#Get threshold value
			print(d)
			#nullify the MK output multiplicator if applies
			#here we should mask the opposite of the threshold
			for i in range(data.shape[0]):
				if(c=='le'):
					if(data[i,b]>d):
						MK[i]=0	
				elif(c=='ge'):
					if(data[i,b]<d):
						MK[i]=0	
				elif(c=='eq'):
					if(data[i,b]!=d):
						MK[i]=0	
				elif(c=='ne'):
					if(data[i,b]==d):
						MK[i]=0	
				elif(c=='lt'):
					if(data[i,b]>=d):
						MK[i]=0	
				elif(c=='gt'):
					if(data[i,b]<=d):
						MK[i]=0	
				else:
					#do nothing
					print("Not understood %s, skipping" % b)
		except:
			print("screening name typo %s, will be ignored" % a[0])


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
	#print(vil1rowno,vil2rowno,critcolno,VL.shape[0])
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
	##return vil1out,vil2out
	return vil1out,vil2out

#set counter for weight and lmib user input forwarding
counter=0
for critcolno in critno:
	print("critcolno=%d" % critcolno)
	for vil1rowno in range(data.shape[0]):
		for vil2rowno in range(data.shape[0]):
			(a,b)=assignvpwc(vil1rowno,vil2rowno,critcolno,counter)
			if(False == math.isnan(a)):
				VL[vil1rowno]+=a
				#print(VL[vil1rowno])
			if(False == math.isnan(b)):
				VL[vil2rowno]+=b
				#print(VL[vil2rowno])
	counter+=1

#Remove negative values
VL=VL.clip(0)
#Rescale 0 to 1
VLM=np.max(VL)
VLm=np.min(VL)
VLr=VLM-VLm
VL=[(i-VLm)/VLr for i in VL]
#convert float array to string list
#vlfloat=VL.tolist()
#vl = ["%.2f" % x for x in vlfloat]
#Temporary stage: OUTPUT an XYZ text file
f=open("villages.csv","w")
for i in range(data.shape[0]-1):
	try:
		if(MK[i]!=0):
			strng=(str(XL[i])+","+str(YL[i])+","+str(VL[i])+"\n")
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
idField = osgeo.ogr.FieldDefn("ID_0", osgeo.ogr.OFTReal)
lyr.CreateField(idField)
fidx = 0
for i in range(len(XL)):
	#Apply data MASK
	if(MK[i]!=0):
		ftr = osgeo.ogr.Feature(lyrDef)
		pt = osgeo.ogr.Geometry(osgeo.ogr.wkbPoint)
		pt.SetPoint(0, XL[i], YL[i])
		ftr.SetGeometry(pt)
		ftr.SetFID(fidx)
		ftr.SetField(ftr.GetFieldIndex('ID_0'),VL[i])
		lyr.CreateFeature(ftr)
		fidx += 1

shpData.Destroy()


#create shapefile projection file
sr.MorphToESRI()
file = open('points.prj', 'w')
file.write(sr.ExportToWkt())
file.close()

