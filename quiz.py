print('Seja muito bem vindo ao meu quiz! ')
answer_user =input('Quer começar? (s/n) ').upper()

print('Ótimo!As regras são bem simples, são duas perguntas de multipla escolha, cada resposta certa você ganha 1 ponto.\nEntão, vamos começar!')


if answer_user != 'S':
    quit()
score = 0

print('Carregando...')

print('Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n A) Activision \n B) Rockstar Games \n C) Ubisoft \n D) EA \n')

# Pergunta 2
answer_1 =input('Resposta:').upper()


if answer_1 == "B":
    print('Correct!')
    score = score +1

else:
    print('Wrong!')

# Pergunta dois
print('Qual o nome do protagonista do jogo GTA San Andreas?\n A) Carlos John \n B) Carl Jonhson \n C) Carl Jaqueline \n D) Carlos Jonhson \n')

answer_2 = input('Resposta:').upper()

if answer_2 == 'B':
    print('Correct!')
    score = score + 1
else:
    print('Wrong!')
# Mensagem de fim de jogo e 
print(f'O quiz acabou... Sua pontuação foi de {score} pontos.')