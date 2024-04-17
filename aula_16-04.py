from datetime import datetime

with open('ex01.txt', 'w') as arquivo:
    arquivo.write('---------------------------------\n')
    arquivo.write('MAX RAYDEN DE SOUZA REBELO JUNIOR\n')
    hoje = datetime.now().strftime('%d/%m/%Y')
    arquivo.write(hoje)
    arquivo.write('\t')
    arquivo.write('MANAUAS-AM')
    arquivo.write('\n')
    arquivo.write('23\tJAPIIM')
    arquivo.write('\n---------------------------------\n')

    disciplina = input('Digite uma Matéria: ')
    nota = input('Digite uma nota: ')
    while disciplina != 'sair' and nota != 'sair':
        arquivo.write(disciplina+','+nota+'\n')
        disciplina = input('Digite uma Matéria: ')
        nota = input('Digite uma nota: ')