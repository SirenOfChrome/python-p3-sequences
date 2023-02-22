def print_fibonacci(length):
    if length < 1:
        return []
    elif length == 1:
        return [0]
    elif length == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence

# example usage
fib_sequence = print_fibonacci(9)
print(fib_sequence)

#GDC