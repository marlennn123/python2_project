san1 = int(input('томонку диапазон: '))
san2 = int(input('жогорку диапазон: '))
import random
secretnyi = random.randint(san1,san2)
kata = 0
joop = False
while not joop:
    kata += 1
    san3 = int(input(f'{san1} дон {san2} га чейин сан тап: '))
    if san3 < secretnyi:
        print('сан чонураак')
    elif san3 > secretnyi:
        print('сан кичирээк')
    else:
        joop = True
        print(f'Куттуктайбыз! {secretnyi} санын {kata} аракетте таптыныз')