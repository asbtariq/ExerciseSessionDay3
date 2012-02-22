import inputdata

alldata = inputdata.raw_scores
print alldata

readers = []
for ir in alldata.iterkeys(): 
    readers.append(ir)

papers_scores = []
for ips in alldata.itervalues(): 
    papers_scores.append(ips) 

papers = []
for ir in range(6):
    for ip in papers_scores[ir].iterkeys(): 
        papers.append(ip)
papers = list(set(papers))

import numpy
scores = numpy.zeros(shape=(len(readers),len(papers)))
print scores

for i in range(len(readers)):
    for j in range(len(papers)):
        if alldata[readers[i]].has_key(papers[j]):
            scores[i,j]=alldata[readers[i]][papers[j]]

'''
for i in range(len(readers)):
    score_vector[i] = alldata[readers[i]]

def two-norm(vec1,vec2)
'''
'''
print alldata['Mehrdad Mapping']['Chen 2002']
print int(alldata['Mehrdad Mapping'].has_key('Chen 2002'))
print int(alldata['Mehrdad Mapping'].has_key('Jackson 1999'))
print alldata['Mehrdad Mapping']['Jackson 1999']
'''




'''
infile = open('inputdata','r')
data = infile.readlines()
print data

datastr = open('inputdata').read()
eval(datastr)
print datastr
datastr1 = datastr.replace('\n','')
datastr2 = datastr1.lstrip('raw scores = ')
print datastr2
data = eval(datastr2)
print data
'''    
