from __future__ import division
import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():

    dict = {}
    nofWords = 0

    with open(sys.argv[1]) as tweet_file:
        for line in tweet_file:
            data = json.loads(line)
	    #pprint(data)
	    if data.has_key("text"):
                text = data["text"]
		#print text
		words = text.split()

		for word in words:
		    if '@' in word:
			continue	
		    word = word.replace(",", "") 
                    word = word.replace(".", "") 
                    word = word.replace("#", "") 
                    word = word.replace("\'", "") 
                    word = word.replace("\"", "") 
                    word = word.replace(";", "") 
                    word = word.replace(":", "") 
                    word = word.replace("-", "") 
                    word = word.replace("?", "")  
                    word = word.replace("\n", "")
		    word = word.replace("\t", "") 
		    word = word.lower()

	  	    if word in dict.keys():
			dict[word] = float( dict[word] + 1) 
	  	    else:
			dict[word] = float(1)	
		
		    nofWords = nofWords+1	
	
        if nofWords == 0:
            return
        #print '=================================================='
        max = 0	
        for tuple in dict:
            print  tuple, float(dict[tuple] / nofWords)

if __name__ == '__main__':
    main()
