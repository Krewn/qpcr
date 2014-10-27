#   ___             __         _            ___  _____                                          
#  / _ | ___  ___ _/ /_ _____ (_)__   ___  / _/ / _/ /_ _____  _______ ___ _______ ___  _______ 
# / __ |/ _ \/ _ `/ / // (_-</ (_-<  / _ \/ _/ / _/ / // / _ \/ __/ -_|_-</ __/ -_) _ \/ __/ -_)
#/_/ |_/_//_/\_,_/_/\_, /___/_/___/  \___/_/  /_//_/\_,_/\___/_/  \__/___/\__/\__/_//_/\__/\__/ 
#                  /___/__       __                                                             
#                     / _ \___ _/ /____ _                                                       
#                    / // / _ `/ __/ _ `/                                                       
#                   /____/\_,_/\__/\_,_/	    Author :: Kevin Nelson :: kpie314@gmail.com

from pylab import *
import sys
import os
import csv
import numpy

def readFile(n,delim):
	fileIN=n
	Data={}
	with open(fileIN) as csvfile:
		tableMain=csv.reader(csvfile,delimiter=delim)
		k=0
		for row in tableMain:
			Data[k]=row
			k+=1
	return(Data)

#data = readFile(sys.argv[1])

def RawParse(data):
	starts=[]
	ends=[]
	names=[]
	found=False
	for k in range(0,len(data)):
		if(len(data[k])==0):
			if(found):
				ends.append(k)
			found=False
			pass
		else:
			if(found==False):
				found=True
				names.append(data[k][0])
				starts.append(k+1)
	if(len(ends)<len(starts)):
		ends.append(k)
	ret={}
	print 'Making Data With'
	print names
	print 'starts'
	print starts
	print 'ends'
	print ends
	
	if(len(ends)==len(starts) and len(starts)==len(names)):
		for k in range(0,len(names)):
			ret[names[k]]={}
			k3=0
			for k2 in range(starts[k],ends[k]):
				ret[names[k]][k3]=data[k2]
				k3+=1
	return(ret,names)

def DictPrt2d(sdmB,delim):					# This is usful for printing 2 dimenstion dictionaries {{}} -> csv files.	
	op=''
	First=True
	for k in sdmB:
		if First:
			First= False
		else:
			if(op[len(op)-1]==delim):op=op[0:len(op)-1]+'\n'
		for k2 in sdmB[k]:				# Patched for {{}} or {[]}
			try:
				op += str(sdmB[k][k2])		#Dictionary Behavior	
			except(TypeError):
				op+=str(k2)			#List Behavior
			op += delim
	if(op[len(op)-1]==','):op=op[0:len(op)-1]+'\n'
	op+='\n'
	return(op)
		
def RoxPlot(Data,name):
	t=Data.keys()
	t2=Data[t[1]].keys()
	#print DictPrt2d(Data[t[1]],'\t')
	#print Data[t[1]].keys()
	#print t
	#print t2
	temp=Data[t[1]]
	#print(DictPrt2d(temp,'\t'))
	t = temp[0][1:-1]
	#print t
	s = temp[1][1:]
	#print s
	#print str(len(s))+' : '+str(len(t))
	close()
	plot(t, s)

	xlabel(temp[0][0])
	ylabel(temp[1][0])
	title('Rox :'+name)
	grid(True)
	formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
	ax = subplot(111)
	ax.yaxis.set_major_formatter(formatter)
	ax.xaxis.set_major_formatter(formatter)
	savefig('Rox :'+name+'.png')
	#show()
	pass

def FamMgbPlot(Data,name):
	t=Data.keys()
	t2=Data[t[1]].keys()
	#print DictPrt2d(Data[t[1]],'\t')
	#print Data[t[1]].keys()
	#print t
	#print t2
	temp=Data[t[1]]
	#print(DictPrt2d(temp,'\t'))
	t = temp[0][1:-1]
	#print t
	s = temp[2][1:]
	#print s
	#print str(len(s))+' : '+str(len(t))
	close()
	plot(t, s)

	xlabel(temp[0][0])
	ylabel(temp[2][0])
	title('FAM-MGB :'+name)
	grid(True)
	formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
	ax = subplot(111)
	ax.yaxis.set_major_formatter(formatter)
	ax.xaxis.set_major_formatter(formatter)
	savefig('FAM-MGB :'+name+'.png')
	pass

def qpcrPlot(Data,f,t,s,g):#Data container, file name, sample name, gene name
	
	T = Data[f][t][s][g][1:-1]#Fval
	S = range(1,len(T)+1,1)   #Cycle Number
	Fmax=max(T)
	k2=0	
	for k in T:
		T[k2] = int(k)
		k2+=1	
	print T 
	print ' len: ' + str(len(T))
	print S
	print ' len: ' + str(len(S))
	#print s
	#print str(len(s))+' : '+str(len(t))
	close()
	plot(S,T)

	xlabel('cycle')
	ylabel('fluorescence')
	print type(f)
	print type(t)
	print type(s)
	print type(g)
	title(t+':'+s+':'+g)
	grid(True)
	formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
	ax = subplot(111)
	ax.yaxis.set_major_formatter(formatter)
	ax.xaxis.set_major_formatter(formatter)
	savefig(t+'_'+s+'_'+g+'.png')
	pass

def askYesNo():
	print 'please anwser "Y" or "N"'
	ans = raw_input()
	if (ans == 'Y' or ans == 'y' or ans == 'Yes' or ans == 'yes'):
		return(True)
	elif (ans == 'N' or ans == 'n' or ans == 'No' or ans == 'no'):
		return(False)
	elif (True):
		return(askYesNo())

def QuickPlot(x,y):
	close()
	plot(x,y)

	xlabel('x')
	ylabel('y')
		
	grid(True)
	formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
	ax = subplot(111)
	ax.yaxis.set_major_formatter(formatter)
	ax.xaxis.set_major_formatter(formatter)
	show()
	print 'save image (Y/N):'
	ans = askYesNo()
	if(ans):
		print 'please enter file name:'
		ans = raw_input()
		savefig(ans+'.png')
	pass

def RoxPlots():
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	for f in files:
		if(f[-3:]=='csv'):
			Data , names = RawParse(readFile(f,','))
			if not os.path.exists('OutPut'):# Check if the folder 'OutPut' exists
				os.makedirs('OutPut')		# If not make it
			os.chdir('OutPut')
			RoxPlot(Data,f[:-4])
			os.chdir('..')
	pass

def FamMgbPlots():
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	for f in files:
		if(f[-3:]=='csv'):
			Data , names = RawParse(readFile(f,','))
			if not os.path.exists('OutPut'):
				os.makedirs('OutPut')	
			os.chdir('OutPut')
			FamMgbPlot(Data,f[:-4])
			os.chdir('..')
	pass

def GetAssayResults():
	keyErrorCount=0
	ret={}
	ret2={}
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	for f in files:
		if(f[-3:]=='csv'):
			print 'Reading file : ' + f
			ret[f]={}
			Data , names = RawParse(readFile(f,','))
			ret2[f]=Data
			keyNames={}
			for k in Data['Experiment Information']:
				#print k
				keyNames[Data['Experiment Information'][k][0]]=Data['Experiment Information'][k][1:]
			if not os.path.exists('OutPut'):# Check if the folder 'OutPut' exists
				os.makedirs('OutPut')		# If not make it
			os.chdir('OutPut')
			for k in Data:
				if(k[-7:]=='FAM-MGB'):
					ret[f][k]={}
					for k2 in Data[k]:
						try:
							works=True
							temp =[keyNames[Data[k][k2][0]][0],keyNames[Data[k][k2][0]][3],Data[k][k2]]
						except(KeyError):
							works=False
							keyErrorCount+=1
							#print '!--#KeyError#--!'
						if works:
							if((keyNames[Data[k][k2][0]][0] in ret[f][k].keys())==False):
								ret[f][k][keyNames[Data[k][k2][0]][0]]={}
							ret[f][k][keyNames[Data[k][k2][0]][0]][keyNames[Data[k][k2][0]][3]]=Data[k][k2]

							
			os.chdir('..')
	#print 'keyErrorCount='+str(keyErrorCount)
	return(ret,ret2)
	
def scf(Data,f,s,g):#Data container, file name, sample name, gene name
	
	d = Data[f]['Raw Data for Probe FAM-MGB'][s][g][1:-1]#Fval
	k2=0
	for k in d:
		d[k2]=float(k)
		k2+=1
	print Data[f]['Bkgd Data for Probe FAM-MGB'][s].keys()
	Bkgd = Data[f]['Bkgd Data for Probe FAM-MGB'][s][g][1:-1]
	k2=0
	for k in Bkgd:
		Bkgd[k2]=float(k)
		k2+=1
	fMax= float(max(d))
	k2=1
	for k in d:
		if(k>=(fMax/2)):
			break
		k2+=1
	if(d[k2]-d[k2-1])!=0.:		
		c = (k2 - 1)+((fMax/2)-d[k2-1])/(d[k2]-d[k2-1])
	else:
		return(0)
	b = d[k2]-d[k2-1]
	return(fMax/(1+numpy.e**(c/b)))

def getNormalization(Data,f,s,g):
#	try:
#		print 'file:'+str(f in Data.keys())
#		print 'table:'+str('Raw Data for Probe FAM-MGB' in Data[f].keys())
#		print 'sample:'+str(s in Data[f]['Raw Data for Probe FAM-MGB'].keys())
#		print 'gene:' + str(g in Data[f]['Raw Data for Probe FAM-MGB'][s].keys())
#	except(KeyError):
#		print 'RawError'
#	try:
#		print 'file:'+str(f in Data.keys())
#		print 'table:'+str('Bkgd Data for Probe FAM-MGB' in Data[f].keys())
#		print 'sample:'+str(s in Data[f]['Bkgd Data for Probe FAM-MGB'].keys())
#		print 'gene:' + str(g in Data[f]['Bkgd Data for Probe FAM-MGB'][s].keys())
#	except(KeyError):
#		print 'BkgdError'
	a = Data[f]['Raw Data for Probe FAM-MGB'][s][g][1:-1]
	#print a
	b = Data[f]['Bkgd Data for Probe FAM-MGB'][s][g][1:-1]
	#print b
	#print len(a)==len(b)
	c=[]
	n=[]
	for k in range(0,len(a)):
		c.append(int(a[k])-int(b[k]))
		n.append(int(k))
	return(c)

def getPolynomialFunc(xs,ys,i):
	z = np.polyfit(xs, ys, i)
	f = np.poly1d(z)
	return(f)

def logFit(xs,ys,i):
	print 'before'
	print xs
	logxs=[]
	for k in xs:
		logxs.append(numpy.log(k))
	print 'after'
	print logxs
	getPolynomialFunc(logxs,ys,i)
	


















