codigo = input("Digite o código do produto: ")
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço unitário do produto: R$ "))

valor_total = quantidade * preco

print("\n--- Informações do Produto Cadastrado ---")
print(f"Código: {codigo}")
print(f"Nome: {nome}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Valor total da compra: R$ {valor_total:.2f}")