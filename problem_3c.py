A = [4, 2, 9, 1, 7]

def count_inversions(A, i, k):
    if i == k:
        return [A[i]]

    mid = int((i + k) / 2)
    right = count_inversions(A, i, mid)
    left = count_inversions(A, mid + 1, k)

def merge(right, left):
    r = 0
    l = 0
    while r < len(right) or l < len(left):
        if right[r] > left[l]:


