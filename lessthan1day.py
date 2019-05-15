import arrow

sdate='17-11-07,16-05-20,19-01-09,'
startdate=sdate.split(',')
del startdate[-1]
utc = arrow.utcnow()
now = arrow.get(utc.format('YY-MM-DD'),'YY-MM-DD')
i=0
while i < len(startdate):	
	b = arrow.get(startdate[i],'YY-MM-DD')
	diff = abs((now-b).days)
	if diff < 2 :
		print "error: This certificate is been created in less than 1 day"
	i+=1 
