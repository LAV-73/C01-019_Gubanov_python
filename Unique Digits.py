array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

A = set()
B = set()
C = set()

for x in array1:
	A.add(x)
for x in array2:
	B.add(x)
C = A.union(B)

print(*A)
print("Count of unique digits in first list: ", len(A))

print(*B)
print("Count of unique digits in second list: ", len(B))

print(*C)
print("Count of unique digits in first and second list: ", len(C))
