method signatures

Raw.py
readFile(n,delim)		#Takes file name ( n ) & delimiter ( delim ) returns {[]}
RawParse(data)			#Reads subsheets from {[]} Data returns {{[]}}
DictPrt2d(sdmB,delim)		#Prints a 2d Dictionary as delim seperated file
RoxPlot(Data,name)		#Plots the rox curve for a given file
RoxPlots()			#Plots the rox curve for all files .csv in cwd
FamMgbPlot(Data,name)		#
FamMgbPlots()			#
qpcrPlot(Data,f,t,s,g)	#Data{{}}
askYesNo()
QuickPlot(x,y)
QuickerPlot(x)
GetAssayResults()	#returns (ret1,ret2) where  ret 1 = {{{{[]}}}}[file][table][sample][gene][cycle] & ret2 = {{{[]}}} [file][table][row][cycle] 
reading all csv in cwd

scf(Data,f,s,g)
getNormalization(Data,f,s,g)
getNormalizationMinusNegitive(Data,f,s,g)
getPolynomialFunc(xs,ys,i)
logFit(xs,ys,i)
