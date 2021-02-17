A = [1, 2, 3, 4, 4, 19]
B = [1, 2, 2, 4, 4, 5]
x = 20

def compare_ends(A, B, counter):
    a = 0
    b = len(B) - 1
    while a < len(A) or b > 0:
        counter += 1
        sum = A[a] + B[b]
        if sum == x:
            print(f'Solution found at A[{a}]={A[a]} and B[{b}]={B[b]}')
            break

        elif sum < x:
            a += 1

        else:
            b -= 1

    return counter

print(f'There were {compare_ends(A, B, 0)} comparisons')
