A = [1, 2, 3, 4, 19]
B = [1, 2, 3, 4, 5]
x = 20

def find_sum(A, B, x):
    for eleA in A:
        for eleB in B:
            if eleA + eleB == x:
                print(f'Found solution of {eleA} and {eleB}')
                break

find_sum(A, B, x)
