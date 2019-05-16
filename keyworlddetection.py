pstring='Arizona,Scottsdale,GoDaddy.com, Inc.,http://certs.godaddy.com/repository/,Go Daddy Secure Certificate Authority - G2,Domain Control Validated'
ustring='miNKtmproxy,mitmproxy,217.29.220.255,mitmproxy,mitmproxy,mitmproxy,mitmproxy'
key_world=['NK','IRN','RU']
string=pstring+ustring
for i in key_world:
	if i in string:
		print 'we detected "' + i + '" the certificate is from North-Korea, Iran or Russia'
		