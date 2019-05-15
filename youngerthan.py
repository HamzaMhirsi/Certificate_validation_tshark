import arrow

sdate='17-11-07,16-05-20,19-01-09,'
edate='19-11-07,24-05-20,20-01-09,'
startdate=sdate.split(',')
enddate=edate.split(',')
del startdate[-1]
del enddate[-1]
i=0
while i < len(startdate):	
	a = arrow.get(enddate[i],'YY-MM-DD')
	b = arrow.get(startdate[i],'YY-MM-DD')
	diff = abs((b-a).days)
	if diff < 32 :
		print "error: This certificate is younger than 1 month"
	i+=1