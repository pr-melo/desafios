numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = False
    
    resposta_status_vegano = input()
    
    if resposta_status_vegano.lower() == "s":
        ehVegano = True
        
    status_vegano = "Vegano" if ehVegano else "Nao-vegano"

    print(f"Pedido {i}: {prato} ({status_vegano}) - {calorias} calorias")
