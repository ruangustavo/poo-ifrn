alunos_notas = {}


def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_aprovacao(media):
    return "aprovado" if media >= 7 else "reprovado"


def imprimir_relatorio(alunos_notas):
    media_geral = 0
    for aluno, notas in alunos_notas.items():
        media_aluno = calcular_media(notas)
        situacao = verificar_aprovacao(media_aluno)
        media_geral += media_aluno
        print(
            f"Aluno: {aluno}, Notas: {notas}, Média: {media_aluno}, Situação: {situacao}"
        )

    media_geral /= len(alunos_notas)
    print(f"Média Geral da Turma: {media_geral}")


for _ in range(3):
    nome = input("Digite o nome do aluno: ")
    notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(3)]
    alunos_notas[nome] = notas

imprimir_relatorio(alunos_notas)
