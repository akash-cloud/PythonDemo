def fun(file):
	f = open(file,'r')
	word_count = 0
	for i in f:
		word_count+=len(i.split())
	print("Number of words: ",word_count)
	f.close()
	

file=input("Enter File name: ")
fun(file)