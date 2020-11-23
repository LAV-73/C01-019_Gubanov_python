myset = set()
while True:
	x = int(input())
	if x == 0:
		break
	if x in myset:
		print("Аlready met")
	else:
		print("New digit")
		myset.add(x)
    
#Expaple with correct answer
#1
#New digit
#2
#New digit
#3
#New digit
#3
#Аlready met
#2
#Аlready met
#1
#Аlready met
#0
