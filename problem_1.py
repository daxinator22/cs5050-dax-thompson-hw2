A = [1, 2, 3, 4, 19]
B = [1, 2, 3, 4, 5]
x = 0

def find_sum(A, B, x, startA, startB):
    if startA >= len(A):
        print('No solution was found')
        return

    if A[startA] + B[startB] == x:
        print(f'Found solution at A[{startA}] and B[{startB}]')
        return

    elif startB + 1 == len(B):
        find_sum(A, B, x, startA + 1, 0)
        
    else:
        find_sum(A, B, x, startA, startB + 1)

find_sum(A, B, x, 0, 0)
