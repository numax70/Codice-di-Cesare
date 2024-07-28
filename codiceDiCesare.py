from art import logo
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)   
risposta=True
def caesar(start_text, ciper_direction, shift_amount):
    end_text=""
    for char in start_text:
        if char in alfabeto:
            position=alfabeto.index(char)
            if ciper_direction=="codifica":
                new_position=position+shift_amount
                if new_position >=26:
                    new_position=shift_amount-1
            elif ciper_direction=="decodifica":
                new_position=position-shift_amount         
            end_text+=alfabeto[new_position]
        else:
            end_text+=char             
    print(f"La {direzione} del testo è: {end_text}\n")
    
while risposta:
    direzione=input("Scegli: codifica o decodifica: \n")
    text=input(f"inserisci parola da {direzione}re: \n").lower()
    shift=int(input("Inserisci lo shift: \n"))
    #impedisce l'errore nel calcolo formattando lo shift al massimo fino a 26
    #nel caso in cui l'utente inserisca uno shift maggiore e fuori dunque dall'intervallo
    #compreso tra le lettere dell'alfabeto che sono appunto 26
    shift=shift%26 
    #Se inserissi 45 ad esempio: 45 % 26 il irsultato è 1 con il resto di 19. 
    #quest'ultimo numero è dentro l'intervallo dell'alfabeto e utilizzabile per
    #spostarmi all'interno fra le lettere. Se mettessi 77 % 26 il resto è 25.
    #Mentre 475%26 verrebbe 1,8 con resto di 7, per cui sarei sempre dentro l'intervallo
    #per cui con questo modulo % ottengo comunque sempre un risultato che mi consente di
    #non andare out of range. Cioè comunque l'intervallo sarà sempre da 0 a 26, se avessi messo
    #45 % 20, l'intervallo sarebbe da 0 a 20 e così via. Una sorta di formattatore di intervalli
    caesar(start_text=text, ciper_direction=direzione, shift_amount=shift)
    domanda=input("Vuoi continuare - Si o No ? ").lower()
    if domanda=="no" or domanda=="n":
        risposta=False
        print("Grazie per aver utilizzato il programma, Arrivederci !!")
        