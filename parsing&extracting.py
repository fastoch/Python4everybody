data = 'From stephen.marquard@uct.ac.za Sat Jan 5 9:14:16 2008'
atsign = data.find('@') # look for the @ sign
nxtspace = data.find(' ',atsign) # look for the nxt space after the @ sign
host = data[atsign+1:nxtspace]
print(host)