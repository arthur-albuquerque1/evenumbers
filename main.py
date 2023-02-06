def even_numbers():
    exit = False
    while not exit:
        print('Bem vindo ao nosso contador de números ímpares')
        print('1. Números ímpares')
        print('2. Números pares')
        print('3. Sair')

        choice = int(input(''))
        if choice == 1:
           init_number = int(input('Digite o primeiro número: '))
           final_number = int(input('Digite o último número: '))
           numbers_list = list(range(init_number,final_number, 2))
           print('Sua lista de números ímpares é:')
           for n in numbers_list:
               print(n)
        elif choice == 2:
           init_number = int(input('Digite o primeiro número par: '))
           final_number = int(input('Digite o último número: '))
           numbers_list = list(range(init_number,final_number + 2, 2))
           print('Sua lista de números pares é:')
           for n in numbers_list:
               print(n)
        elif choice == 3:
            exit = True
            print('Até a próxima!')
        else: 
            print('Opção inválida, tente novamente')
        
even_numbers()
