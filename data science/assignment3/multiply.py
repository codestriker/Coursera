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
    matrix  = record[0]
    row = record[1]
    col = record[2]
    value = record
    for w in range(0, 5):
       if "a" in matrix:
           key = row * 5 +  w 
       if "b" in matrix:
           key = w * 5 +  col
       mr.emit_intermediate(key, value)   

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = [] 
    for v in list_of_values:
      total.append(v)

    val = 0
    for v in total:
       if "a" in v[0]:
           col = v[2]
           for u in total:
               if "b" in u[0] and col  == u[1]:
                  val = val + v[3]*u[3]
    
    row = key / 5
    col = key % 5
    mr.emit((row, col, val))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
