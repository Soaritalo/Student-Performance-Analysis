
alunos = {
    'Victoria': [8, 7, 9, 6],
    'André': [5, 6, 7, 5],
    'Kaua': [9, 9, 8, 10],
    'Lucas': [6, 5, 6, 7]
}
medias = {}

for aluno, notas in alunos.items():
    soma = sum(notas)
    quantidade = len(notas)
    medias[aluno] = soma / quantidade
notas_total = []

for notas in alunos.values():
    notas_total.extend(notas)
soma_total = sum(notas_total)
quantidade_total = len(notas_total)
media_total = soma_total / quantidade_total

ranking = sorted(
    medias.items(), 
    key=lambda item: item[1],
    reverse=True
)
print("\n===== MÉDIAS=====")
for aluno, media in medias.items():
    print(f"{aluno} = {media:.2f}")
print("\n===== MÉDIA GERAL DA TURMA =====")
print(f"{media_total:.2f}")
print("\n===== RANKING =====")
for posicao, (aluno, media) in enumerate(ranking, start=1):
    print(f"{posicao}º lugar - {aluno} | Média: {media:.2f}")
