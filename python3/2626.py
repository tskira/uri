from sys import stdin
vencedor = {('papel', 'pedra', 'pedra') : 0, ('tesoura', 'papel', 'papel') : 0, ('pedra', 'tesoura', 'tesoura') : 0,
            ('pedra', 'papel', 'pedra'): 1, ('papel', 'tesoura', 'papel') : 1, ('tesoura', 'pedra', 'tesoura'): 1,
            ('pedra', 'pedra', 'papel'): 2, ('papel', 'papel', 'tesoura') : 2, ('tesoura', 'tesoura', 'pedra') : 2}
mensagem = {0 : 'Os atributos dos monstros vao ser inteligencia, sabedoria...', 1 : "Iron Maiden's gonna get you, no matter how far!", 2 : 'Urano perdeu algo muito precioso...'}
for line in stdin:
    jogada = tuple(line.split())
    if jogada in vencedor.keys():
        print(mensagem[vencedor[jogada]])
    else:
        print('Putz vei, o Leo ta demorando muito pra jogar...')