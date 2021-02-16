A = [1, 2, 3, 4, 19]
B = [1, 2, 3, 4, 5]
x = 6
counter = 0

def find_B_sum(A, B, x):
    if len(B) == 0:
        return
    
    if B[0] + A[0] == x:
        print(f'Found solution at {A[0]} and {B[0]}')
        return

    else:
        find_B_sum(A, B[1:], x)

def find_sum(A, B, x):

    if len(A) == 0:
        return


    else:
        find_B_sum(A, B, x)
        find_sum(A[1:], B, x)
    


find_sum(B, A, x)
