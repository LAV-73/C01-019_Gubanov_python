learners_french = input().split()
pianists = input().split()
swimmers = input().split()

A = set()
B = set()
C = set()

for x in learners_french:
	A.add(x)
for x in pianists:
	B.add(x)
for x in swimmers:
	C.add(x)
D = set()
D = (B.intersection(C)).difference(A)
result = []
for x in D:
	result.append(x)
print(*result)

#example
#Savior tywok LimberG
#tywok BryanChen The_Hedgehog
#tywok BryanChen The_Hedgehog
#
#correct answer: BryanChen The_Hedgehog
#my answer:BryanChen The_Hedgehog
