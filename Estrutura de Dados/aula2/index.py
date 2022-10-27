import timeit

def um(n):
  print(sum(range(1,n+1)))

def dois(n):
  print((n*(n+1))/2)

def tres1(n):
  print(range(0,n+1))


start = timeit.default_timer()
tres1(999)
end = timeit.default_timer()
print('Time:', end-start)