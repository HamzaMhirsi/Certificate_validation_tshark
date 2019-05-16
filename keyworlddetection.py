pstring='Arizona,Scottsdale,GoDaddy.com, Inc.,http://certs.godaddy.com/repository/,Go Daddy Secure Certificate Authority - G2,Domain Control Validated'
ustring='mitmproxy,mitmproxy,5.5.5.5,mitmproxy,mitmproxy,mitmproxy,mitmproxy'
key_world=['IOC','emails','word']
string=pstring+ustring
for i in key_world:
	if i in string:
		print 'we detected "' + i + '" the certificate is compromised'
		
