dist = float(input('Qual a distancia da viagem em Km?'))
if dist <= 200:
    preco = dist*0.50
else:
    preco = dist*0.45
print('Para essa viagem de {}Km, você ira pagar R$ {} de passagem'. format(dist, preco))