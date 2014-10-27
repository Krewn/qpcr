import Raw as ra # a Tool set specifically for the biomark fluorescense out put files.
import os
print('imports complete')

#print len(Data)
#for k in Data:
#	print k
#	print len(Data[k]) 
#	print(len(Data[k][Data[k].keys()[0]]))


ra.RoxPlots()
ra.FamMgbPlots()
ra.GetAssayResults()
Data , WholeData = ra.GetAssayResults()
print Data.keys()
for k in Data:
	print Data[k].keys() 
if not os.path.exists('OutPut'):
	os.makedirs('OutPut')	
os.chdir('OutPut')

for k in Data:
	#print Data[k]['Bkgd Data for Probe FAM-MGB']
	for k3 in Data[k]['Raw Data for Probe FAM-MGB']:
		for k4 in Data[k]['Raw Data for Probe FAM-MGB'][k3]:
			print k,k3,k4
			try:
				c = ra.getNormalization(Data,k,k3,k4)
				n = []
				for k2 in range(1,len(c)+1):
					n.append(k2)
				ra.QuickPlot(n,c)
			except(KeyError):
				print '>'









