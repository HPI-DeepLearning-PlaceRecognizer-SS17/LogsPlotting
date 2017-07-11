import matplotlib.pyplot as plt 
import sys
import os


dic = {}
files = []
for i in range(len(sys.argv)):
	if "snet" in sys.argv[i]: #wont work for all files, but works for me. too lazy to filter out args
		files.append(open(sys.argv[i], 'r'))
for inpfile in files:
	dic[inpfile.name] = []
	for line in inpfile:
		if 'Validation-mAP' in line:
			split = line.split('=')
			print(line)
			print(str(split[0]))
			dic[inpfile.name].append(float(split[1]))

for logfile in dic:
	plt.plot(dic[logfile], label=logfile)

plt.legend(loc='best')
plt.ylabel("mAP")
plt.xlabel("Epoch")
plt.title("Comparison of Resnets as SSD base networks")
plt.show()
