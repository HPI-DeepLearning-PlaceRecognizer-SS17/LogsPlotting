import matplotlib.pyplot as plt 
import sys
import os


dic = {}
inpfile = open(sys.argv[1], 'r')
for line in inpfile:
	if 'Validation' in line:
		split = line.split('-')
		split = split[1].split('=')
		#print(float(split[1]))
		if not split[0] in dic:
			dic[split[0]] = []
		dic[split[0]].append(float(split[1]))

for classname in dic:
	plt.plot(dic[classname], label=classname)

plt.legend(loc='best')
plt.ylabel("mAP")
plt.xlabel("Epoch")
plt.title(str(inpfile.name))
plt.show()
