from dominio import Usuario, Lance, Leilao, Avaliador

well = Usuario('weliton')
val = Usuario('valderez')

lance_well = Lance(well,100.0)
lance_val = Lance(val,150.0)

leilao = Leilao('celular')

leilao.lances.append(lance_val)
leilao.lances.append(lance_well)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} e deu um lance {lance.valor} ')

avaliador = Avaliador()
avaliador.avalia(leilao)
print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')