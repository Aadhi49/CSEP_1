str1="Race"
str2="Care"
str1=str1.lower()
str2=str2.lower()
if (len(str1)) == (len(str2)):
	sorted_str1=sorted(str1)
	sorted_str2=sorted(str2)
	if (sorted_str1) == (sorted_str2):
		print( str1 + " and " + str1 + " are anagram " )
	else:
		print(str1+ " and " +str2+" are not anagram ")
else:
	print(str1+ " and " +str2+" are not anagram ")

'method 2'
'''
c='cool'
d='looc'
k=0
for i in c:
	if i in d:
		k+=1
if k==len(c):
	print('anagram')
else:
	print('not anangram')
'''
