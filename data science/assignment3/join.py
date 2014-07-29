import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
    mr.emit_intermediate(key , value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = [] 
    for v in list_of_values:
      total.append(v)
    first = total[0]
    for tuple in total[1:]:
       mergedList = first + tuple 
       mr.emit((mergedList))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)