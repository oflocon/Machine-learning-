def stepgradient(curb,curm,pts,lrate):
	gradb=0
	gradm=0
	n=float(len(pts))
	for i in range(0,len(pts)):
	gradb+=-(2/n)*(pts[i].y-curm*pts[i].x+curb)
	gradm+=-(2/n)*pts[i].x*(pts[i].y-((curm*pts[i].x)+bcur))
	newb=bcur -(lrate*gradb)
	newm=mcur-(lrate*gradm)
	return [newb,newm]
	
#we can run the the gif by executing the complete file using numpy
#it has a inbuilt runner
