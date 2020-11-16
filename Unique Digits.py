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

# Example:
#1 2 3 4 5 5 4 3 2 1
#6 7 6 5 4 2 1 9
#correct answer
#1 2 3 4 5
#Count of unique digits in first list:  5
#1 2 4 5 6 7 9
#Count of unique digits in second list:  7
#1 2 3 4 5 6 7 9
#Count of unique digits in first and second list:  8
