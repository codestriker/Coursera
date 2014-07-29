import sys
import json

def main():

    scores = {}
    states = {}
    with open(sys.argv[1]) as sent_file:
        for line in sent_file:
            term, score = line.split("\t")
            #print type(term)
            scores[term] = int(score)


#print scores.items()
    with open(sys.argv[2]) as tweet_file:
        for line in tweet_file:
            data = json.loads(line)
            if data.has_key('place'):
                place = data['place']
                if place==None:
                    continue
                if place.has_key('country_code'):
                    country_code =  place['country_code']
                    if country_code==None:
                        continue
                    if country_code != 'US':
                        continue
                    name = place['full_name']
                    name = name[-2:]
                    #print '-------------------'
                    #print "found", name

                    # calculate sentiment
                    if data.has_key('text'):
                        text = data['text']
                        text = text.encode('utf-8')
                        #print text
                        words = text.split()
                        value = 0
                        for word in words:
                		    #if '@' in word:
                             #   continue
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
                                #print word, scores[word]
                                value += scores[word]
                        #if name == 'TX':
                        #    print value
                        if name in states.keys():
                            states[name] = states[name] + value
                        else:
                            states[name] = value

                        #print name, value
    #print states.items()
    if not states.items():
        return
    happy_state = max(states, key=states.get)
    print happy_state

    
if __name__ == '__main__':
    main()
