import sys
fhand1 = open(sys.argv[1])
fhand2 = open(sys.argv[2])
for line1 in fhand1 :
    print line1.rstrip()
print "--------------------------"
for line2 in fhand2 :
    print line2.rstrip()
print "this is the end!"
