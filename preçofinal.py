valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

valorTotalHamburgueres = valorHamburguer * quantidadeHamburguer
valorTotalBebidas = valorBebida * quantidadeBebida
precoTotalPedido = valorTotalHamburgueres + valorTotalBebidas
trocoNecessario = valorPago - precoTotalPedido

print(f"O preço final do pedido é R$ {precoTotalPedido:.2f}. Seu troco é R$ {trocoNecessario:.2f}.")
