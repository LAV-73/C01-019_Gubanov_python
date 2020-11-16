mydict = dict()
while True:
	s = input()
	if s == "#":
		break
	for x in s.split():
		x = x.lower()
		try:
			mydict[x] += 1
		except:
			mydict[x] = 1
#mydict.sort()
films = []
for k, v in mydict.items():
	films.append([v, k])
films.sort(key = lambda x : x, reverse = True)

for i in range(len(mydict)):
	print('"', films[i][1], '" has ', films[i][0])

#example with correct answer
#slovar
#SloVar
#MAp
#map
#m/-\p 
#romap
#parom
#slovnik 
#novii god?
##
# Correct answer
#" slovar " has  2
#" map " has  2
#" slovnik " has  1
#" romap " has  1
#" parom " has  1
#" novii " has  1
#" m/-\p " has  1
