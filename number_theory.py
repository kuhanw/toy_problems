#basic sieve
from collections import defaultdict
def create_list(): return []
cmps = defaultdict(create_list)

def generate_primes():

  v=2
  while True:
    yield v
    cmps[v*v].append(v)
    v+=1
    
    while v in cmps:
      for f in cmps[v]:
        cmps[v+f].append(f)
        
      del cmps[v]
      v+=1
