amount = int(input("Insert Coin: "))
while(True):
    amount = int(input("Insert Coin: "))
    print(f"Amount due: {amount}")

    amount -= int(input("Insert Coin: "))
    print("Amount due: ", amount)
    # if(amount == 0 or amount<0):
    #     break;
          
