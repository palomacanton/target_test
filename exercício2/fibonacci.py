a = 0
b = 1
ant = 1
res = 0


num = int(input("Digite um número da sequência Fibonacci: "))
seq = []

for x in range(num):
  res = a + b
  seq.insert(num, res)
  a = b
  b = res
  
if num in seq:
  print("\nAcertou!")
else:
  print("\nEsse número não está na sequência!")