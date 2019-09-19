f = open("abcd.txt",'r')
while True:
	data  = f.read(2)
	print(data)
	if data == '':
		break