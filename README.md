# Certificate_validation
In this project I will work to validate certificate

# youngerthan.py
Certificate younger than 1 month may be highly used in an attack. We need to block such traffic. 

# lessthan1day.py
Certificate recently created (less than 1 day from creation) may be highly used in an attack, better to block this traffic.

# printablestring.py
we can verify certificate chain when we extract the following filed from traffic using tshark command:
#tshark -i 1 -T field -e x509sat.printableString -e x509sat.printableString


