import sys
import json

def main():

    scores = {}
    dict = {}
    with open(sys.argv[1]) as sent_file:
	for line in sent_file:
	    term, score = line.split("\t")
	    scores[term] = int(score)

   # print scores.items()

    with open(sys.argv[2]) as tweet_file:
        for line in tweet_file:
            data = json.loads(line)
	    #print '---------------'
	    if data.has_key("text"):
                text = data["text"]
		#print text
		words = text.split()

		value = 0
		nofWords = 0
		avgSentiment = 0
		for word in words:
		    if '@' in word:
			continue	
		    word = word.replace(",", "")
                    word = word.replace(".", "")
                    word = word.replace("\'", "")
                    word = word.replace("\"", "")
                    word = word.replace(";", "")
                    word = word.replace(":", "")
                    word = word.replace("-", "")
                    word = word.replace("?", "")  
                    word = word.lower() 
		    if word in scores.keys():
		        #print (word, scores[word])
		        value += scores[word]
			nofWords += 1
		if nofWords != 0:
	   	    avgSentiment = (value / nofWords) * 0.7
		#print "Value:", value, " Average sentiment:", avgSentiment

		for word in words:
		    if '@' in word:
			continue
		    if 'http' in word:
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
                    word = word.lower(
)
		    if not word in scores.keys():
			if word in dict.keys():
				dict[word] = (dict[word] + avgSentiment)/2
			else:
				dict[word] = avgSentiment	
	
		for tuple in dict:
			print tuple, dict[tuple] 
if __name__ == '__main__':
    main()
