def print_fibonacci(length):
    if length < 1:
        print("[]")
    elif length == 1:
        print("[0]")
    elif length == 2:
        print("[0, 1]")
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        print(fib_sequence)
#gpt redo GDC#1