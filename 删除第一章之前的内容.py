import re
import linecache
file = '第一章.txt'
outfile = 'os.txt'
lineNumber = 1
with open(file,'r', encoding='utf-8') as f:
	number = []
	for line in f.readlines():
		m = re.findall(r"第一章 \w+",line)  #匹配含有字符'UINT32 O_'的行
		print(m)
		if m:
			number.append(lineNumber)
		n = re.findall(r"第1章 \w+",line) #假设只有一个OUT
		print(n)
		if n:
			number.append(lineNumber)
		lineNumber += 1


	with open(outfile, 'w+') as f_w:
		for j in range(len(number)):
			if j == 0:
				start = number[j]
				end = number[j+1]
				destlines = linecache.getlines(file)[start:end] #截取start-end行的字符，不包括start-1,但包含end行
				f_w.write('extern ')
				for i in range(len(destlines)):
					if i != len(destlines)-1:
						f_w.write(destlines[i])
					else:
						f_w.write(destlines[i].replace('\n',';\n'))
				f_w.write('\n')








