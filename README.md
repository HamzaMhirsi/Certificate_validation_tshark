# Certificate_validation
In this project I will work to validate certificate

# youngerthan.py
Certificate younger than 1 month may be highly used in an attack. We need to block such traffic. 

# lessthan1day.py
Certificate recently created (less than 1 day from creation) may be highly used in an attack, better to block this traffic.

# printablestring.py
we can verify certificate chain when we extract the following filed from traffic using tshark command:
#tshark -i 1 -T field -e x509sat.printableString -e x509sat.printableString

# keyworlddetection.py
Such "word/subject/issuer/email @" if detected on certificate may indicate an abnormal activity in the traffic, we can get find those indicators  in Malware  and detect them with this code, I focus on Printable string, country name and UTF-8 string field in the certificate, that we can find them in subject and issuer section of the certificate. We can get those fields with the following tshark command:
#tshark -i  1 -T fields -e x509sat.uTF8String -e x509sat.CountryName -e x509sat.printableString

