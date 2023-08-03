# Python program to display the Fibonacci sequence

def fibonacci_series(n, n1, n2):
    results = []
    # update n1, n2 (starting 2 numbers of the sequence)
    if n1 == 0 and n2 == 1:
        n1, n2 = n1, n2
    else:
        n1 = n1 + n2
        n2 = n1 + n2
    count = 0

    # check if the number of terms is valid
    if n <= 0:
        return "Please enter a positive integer"
    # if there is only one term, return n1
    elif n == 1:
        results.append(n1)
    # generate fibonacci sequence
    else:
        while count < n:
            results.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1
    return results
