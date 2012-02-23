import inputdata

alldata = inputdata.raw_scores

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
binscores = numpy.zeros(shape=(len(readers),len(papers)))

for i in range(len(readers)):
    for j in range(len(papers)):
        if alldata[readers[i]].has_key(papers[j]):
            scores[i,j]=alldata[readers[i]][papers[j]]
            binscores[i,j]=1
print
print 'Scores matrix'
print scores
print
print 'Binary scores matrix'
print binscores

from math import sqrt
def my2norm(vec1,vec2):
    if (len(vec1)!=len(vec2)): 
        print 'error: unequal vector sizes'
    norm = 0
    for i in range(len(vec1)):
        if(vec1[i]!=0 and vec2[i]!=0):
            norm += pow((vec1[i]-vec2[i]),2)
    return sqrt(norm)

from scipy import stats
from scipy import spatial

dissimIndex = numpy.zeros(shape=(len(readers),len(readers)))
correlPearson = numpy.zeros(shape=(len(readers),len(readers)))
distRogTani = numpy.zeros(shape=(len(readers),len(readers)))
for i in range(len(readers)):
    bool
    for j in range(len(readers)):
        dissimIndex[i][j] = my2norm(scores[i],scores[j])
        correlPearson[i][j] = stats.pearsonr(scores[i],scores[j])[0]
        distRogTani[i][j] = spatial.distance.rogerstanimoto(binscores[i],binscores[j])
print
print "Reader's list: ",readers
print
print "Dissimilarity index matrix"
print dissimIndex     
print
print "Pearson correlation matrix"
print correlPearson     
print
print "Rogers-Tanimoto distance matrix"
print distRogTani     

