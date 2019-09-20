f = open("abcd.txt",'a')
s = "abcdefghijklmnopqrstuvwxyz"
i = 0
while i<len(s):
	f.write(s[i]+s[i+1]+"\n")
	i += 2
f.close()