def comp():
    while True:
        try:
            deg = int(input("enter degree you are at: "))
        except ValueError:
            print("pleas enter a number")
        else:
            break
    
    return deg