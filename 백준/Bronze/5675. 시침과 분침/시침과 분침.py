while True:
    try:
        input_angle = int(input())

        if input_angle % 6:
            print("N")
        else:
            print("Y")
            
    except EOFError:
        break

