''' Binary Search - Logarithms '''

def binary_search(target, nums):
    """See if target appears in nums """
    # We think of floor_index and ceiling_index as "walls" around
    # the possible positions of our target, so by -1 below we mean
    # to start our wall "to the left" of the 0th index
    # (we *don't* mean the last index)

    floor_index = -1