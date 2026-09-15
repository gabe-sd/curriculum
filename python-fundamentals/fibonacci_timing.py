import time

def timer(function, param):
  start_time = time.time()
  result = function(param)
  stop_time = time.time()
  run_time = stop_time - start_time
  print("Your function ran with parameter {} and returned: {}\nin {} seconds".format(param, result, run_time))
  

def naive_fib(n):
  if n < 0:
    raise Exception("n must be non-negative")
  elif n in (0, 1):
    return n
  else:
    return naive_fib(n-1) + naive_fib(n-2)
    
    
def naive_fib_sequence(n):
  result = []
  for i in range(n+1):
    result.append(naive_fib(i))
  return result
    
    
cache = {
  0: 0,
  1: 1
}
def cache_fib(n):
  if n < 0:
    raise Exception("n must be non-negative")
  elif n in cache.keys():
    return cache[n]
  cache[n] = cache_fib(n-1) + cache_fib(n-2)
  return cache[n]
     
timer(naive_fib, 27)
timer(cache_fib, 27)







