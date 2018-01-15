d = {'vertebrado' : { 'ave' : {'carnivoro' : 'aguia', 'onivoro' : 'pomba' },
                     'mamifero' : {'onivoro' : 'homem', 'herbivoro' : 'vaca'}},
     'invertebrado' : {'inseto' : {'hematofago' : 'pulga', 'herbivoro' : 'lagarta'},
                        'anelideo' : { 'hematofago' : 'sanguessuga', 'onivoro' : 'minhoca'}}}
a = [input() for i in range(3)]
print(d[a[0]][a[1]][a[2]])
