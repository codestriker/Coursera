import MapReduce
import sys
import collections

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
    total = []
    unique =[]
    dups = []
    final = []
    for v in list_of_values:
        total.append(v)
#unique = list(set(total))
#dups = total - unique
#final = unique - dups 
    final = [x for x, y in collections.Counter(total).items() if y <= 1]
    for v in final:
        mr.emit((key, v))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
