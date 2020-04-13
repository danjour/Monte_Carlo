import random 
def estimativa_pi(n):
  num_ponto_circulo=0
  num_ponto_total=0
  for _ in range(n):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    distancia=x**2+y**2
    if distancia <=1:
      num_ponto_circulo +=1
    num_ponto_total +=1
  return 4*num_ponto_circulo/num_ponto_total

n=int(input("Digite um número: "))
print(estimativa_pi(n))
