#!/usr/bin/env python


def unduplify(source) :
	target = ''
	start  = source[0]
	for i in source[1:]:
		cur = i
		if cur != start :
			target = target + start
			start = cur

	target = target + source[-1]

	return target


def stripify (source) :
        target = ''
        print "Starting : ", source
        i = 0
        while True :
                print "In loop"
                i+=1
                if ( i >= len(source)) :
                        print "breaking"
                        break
                        print "Source a: ", source[0:i]
                        print "Source b: ", source[i:].lstrip(source[i-1])
                        target = source[0:i] + source[i:].lstrip(source[i-1])
                        #print target
                        source = target
                        print len(source), i

        return source

print stripify("bob")
print stripify("boooob")
print stripify("boobbb")
print stripify("boobbbobll")
