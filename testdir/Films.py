mydict = dict()
while True:
	x = input()
	if x == "#":
		break
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
	print('"', films[i][1], '" has ', films[i][0], ' voices')

#example with correct answer
#s
#s
#s
#2
#2
#1
##
#" s " has  3  voices
#" 2 " has  2  voices
#" 1 " has  1  voices

