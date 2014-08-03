import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):

    person = record[0]
    friend = record[1]

    mr.emit_intermediate(person, 1)

def reducer(key, list_of_values):
    
    total = 0
    for v in list_of_values:      
        total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  result = open('mr_result.txt','w')
  result.write(mr.execute(inputdata, mapper, reducer))
  result.close()
  
