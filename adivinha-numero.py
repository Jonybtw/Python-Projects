import random

def adivinha_o_numero():
    numero_a_toa = random.randint(1, 20)
    tentativas = 0

    while True:
        print(numero_a_toa)
        adivinha = int(input("Adivinha o numero de 1-20: "))
        tentativas += 1

        if adivinha < numero_a_toa:
            print("Muito baixo!")
        elif adivinha > numero_a_toa:
            print("Muito alto!")
        else:
            if tentativas == 1:
                print(f"Parabéns! Acertaste o número {numero_a_toa} em {tentativas} tentativa.")
            else:
                print(f"Parabéns! Acertaste o número {numero_a_toa} em {tentativas} tentativas.")
            break


    jogar_denovo = input("Queres jogar denovo? (s/n): ")
    if jogar_denovo.lower() == "s":
        adivinha_o_numero()
    else:
        print("\n")
        print("Adeus, obrigado por jogar!")
        print("Pressione Enter para continuar...")
        input()  # Aguarda o usuário pressionar a tecla "Enter"

# comecar o jogo
adivinha_o_numero()
