salario=float(input("Salario: "))
prest=float(input("Prestação: "))

if prest>(salario*0.2):
  print("Emprestimo não Concedido")
else:
  print("Emprestimo Concedido")