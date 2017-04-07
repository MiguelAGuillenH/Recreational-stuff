def A(m,n):
  print("\tCalculating A("+str(m)+","+str(n)+")")
  if m==0 and n>=0:
    return n+1
  if m>0 and n==0:
    return A(m-1,1)
  if m>0 and n>0:
    return A(m-1,A(m,n-1))
  else:
    return "ERROR!"
    
for i in range(0,5):
  for j in range(0,5):
    print("A("+str(i)+","+str(j)+") = ")
    print(A(i,j))
    input()
