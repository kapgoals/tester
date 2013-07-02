list = [3,4,5,4,7]

running_total = 0

for x in list:
	running_total = x + running_total
	print running_total
print running_total


others = [4,2,2]
for x in others:
	running_total = running_total - x
print running_total

#ENDFILE
