A = [1, 2, 3, 4, 4, 19]
B = [1, 2, 2, 4, 4, 5]
x = 24

def compare_divide(A, B):
    if len(A) == 0:
        return
    
    midA = int(len(A) / 2)
    if midA == 0:
        if B[0] + A[0] == x:
            print(f'A:{A[0]} B:{B[0]}')
        else:
            return

    else:
        compare_divide(A[:midA], B[:midA])
        compare_divide(A[midA:], B[midA:])

compare_divide(A, B)
