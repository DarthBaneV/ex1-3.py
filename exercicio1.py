print("Valor do volume do tronco da pirâmide!")

h = float(input("Qual a altura do tronco?"))

Bmenor = float(input("Qual o valor da base menor?"))

Bmaior = float(input("Qual o valor da base maior?"))

volume = h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print("O volume do tronco da pirâmide é:", volume , "Metros")