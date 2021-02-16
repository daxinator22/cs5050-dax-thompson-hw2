A = [1, 2, 3, 4, 4, 19]
B = [1, 2, 2, 4, 4, 5]
x = 23

def find_B_sum(A, B, x):
    if len(B) == 0:
        return False
    
    if B[0] + A[0] == x:
        print(f'Found solution at {A[0]} and {B[0]}')
        return True

    else:
        midB = int(len(B) / 2)
        if midB == 0:
            midB = 1

        if midB < len(B) and B[midB] + A[0] > x:
            return find_B_sum(A, B[:midB], x)

        else:
            return find_B_sum(A, B[midB:], x)

def find_sum(A, B, x):

    if len(A) == 0:
        return False


    else:
        if find_B_sum(A, B, x):
            return True

        midA = int(len(A) / 2)
        if midA == 0:
            midA = 1

        if midA < len(A) and A[midA] + B[0] > x:
            find_sum(A[:midA], B, x)

        else:
            return find_sum(A[midA:], B,  x)
    


find_sum(B, A, x)
