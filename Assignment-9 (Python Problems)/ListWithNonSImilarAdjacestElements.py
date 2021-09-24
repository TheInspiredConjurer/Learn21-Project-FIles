def originalListWithNonSimilarAdjEle(originalList):
	index=0
	next=index+1
	temporaryList=originalList
	l=len(temporaryList)
	finalOriginalList=[]
	maxI=len(temporaryList)-1

	for i,v in enumerate(temporaryList):
		next=i+1
		if next>maxI:
			finalOriginalList.append(v)
			break

		if v != temporaryList[next]:
			finalOriginalList.append(v)
		
	return finalOriginalList

originalList=[1, 2, 2, 3]

print ("Original List: ",originalList,"-->",originalListWithNonSimilarAdjEle(originalList),"(Final List)\n\n")