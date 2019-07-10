#baca1 = open('list1.txt','r').readlines()
#baca2 = open('list2.txt','r').readlines()
#print "LIST 1 : %s" % str(len(baca1))
#print "LIST 2 : %s" % str(len(baca2))
baca = open('anu.txt','r').readlines()
print "BEFORE : %s" % str(len(baca))
kumpulan = []
for a in baca:
	b = a.strip()
	if b not in kumpulan:
		kumpulan.append(b)
print "AFTER : %s" % str(len(kumpulan))