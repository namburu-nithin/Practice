'''a python function  that takes a sequence of integer  values and determines if there is a distinct pair of numbers in the sequence whose product is odd'''
def odd_no(seq, N):
  b=[]
  c=0
  for i in seq:
    if i not in b:
      b.append(i)
    for i in b:
      if i%2==1:
        c+=1
  if c>1:
    return "yes"
  else:
    return "no"
N=int(input())
seq=[]
for i in range(N):
  seq.append(int(input()))
print(odd_no(seq, N))
