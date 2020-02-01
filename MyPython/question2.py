L = ['how', 'why', 'however', 'where', 'never']
for x in L:
    print "* " +x[0]+x[1] + " " + x


for x in L:
    if (x[0]+x[1]== "wh"):
        print "* " +x[0]+x[1] + " " + x
    else :
        print "- " +x[0]+x[1] + " " + x
