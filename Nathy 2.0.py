from os import system

def question():
    
    return (str(input('''Voce ja realizou todas as listas de exercicios para a prova
[S] - Sim
[N] - Não
Resp : ''')).strip().lower())

def exercicios():
    
    exer = question()
    print('\n')
    
    while exer not in 'sn':
        print('Digitou errado ! responda novamente')
        exer = question()
        print('\n')
        
    if exer == 'n':
        
        while (exer == 'n'):
            print("hummmm.... poxa vamos terminar a lista, let's go !!!")
            exer = question()
            print('\n')
            
            while exer not in 'sn': 
                print('Digitou errado ! responda navamente')
                exer = question()
                print('\n')
    return 0
        
def parabens():
    A = '<3'
    print('\t\t   Nathy você é especial pra mim')
    print(f'''
{A:>18} {A:.>10} {A:.>10} {A:.>10}

              |\\        * *************** *         /|" 
              | \\    *  ¨    Vc merece,    ¨ *     / |" 
              |..\\ *    ¨                  ¨   *  /..|" 
              |   O     ¨   Chocolate !!!  ¨     O   |" 
              |../  *   ¨                  ¨    * \\..|" 
              | /     * ¨   Chocolate !!!  ¨  *    \\ |" 
              |/         * *************** *        \\|"
              
{A:>18} {A:.>10} {A:.>10} {A:.>10}    
    ''')
    print('\n')
    
    return 0

#Começa aqui o programa
nome = str(input(''' 
Ola tudo bom, vamos a um pequeno teste
Digite nome completo: ''')).strip().lower()
system("cls")

print(f'\n{nome} !!!')
if 'nathaly' in nome: 
    exercicios()
    system("cls")
    parabens()
    parabens()
    parabens()
else:
    exercicios()
    print('Ooohhh , parabens, vc vai se dar muito bem nas provas !!!')
    
input('Digite algo para finalzar a execução....')