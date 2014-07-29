from collections import Counter
import sys
import json

def main():

    hashlist = []
    #print 'Opening tweet file..'
    with open(sys.argv[1]) as tweet_file:
        #print 'Processing tweet file..'
        for line in tweet_file:
                data = json.loads(line)
                if data.has_key('entities'):
                    entities = data['entities']
                    if entities ==None:
                        continue
                    hashtags = entities['hashtags']
                    if not hashtags:
                        continue
                    for hash in hashtags:
                        text = hash['text']
                        text = text.encode('utf-8')
                        if not text: 
                           continue
                        hashlist.append(text)

    counts = Counter(hashlist)
    freqList =  counts.most_common(10)
    #print '\n------ Top 10 ------\n'
    for items in freqList:
        print items[0], items[1]
    #print '------------------'
if __name__ == '__main__':
    main()
