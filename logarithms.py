''' Binary Search - Logarithms '''
# total time cost of binary search is O(log n)

def binary_search(target, nums):
    """See if target appears in nums """
    # We think of floor_index and ceiling_index as "walls" around
    # the possible positions of our target, so by -1 below we mean
    # to start our wall "to the left" of the 0th index
    # (we *don't* mean the last index)

    floor_index = -1
    ceiling_index = len(nums)

    # If there isn't at least 1 index between floor and ceiling,
    # we've run out of guesses and the number must not be present

    while floor_index + 1 < ceiling_index:
        # Find the index ~halfway between the floor and ceiling
        # we use integer division, so we'll never get a "half index"
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance

        guess_value = nums[guess_index]
        if guess_value == target:
            return True
        
        if guess_value > target:
            # Target is to the left, so move ceiling to the left
            ceiling_index = guess_index
        else:
            # Target is to the right, so move floor to the right
            floor_index = guess_index
    
    return False

nums = [0,5,6,7,8,9,10,11,12,20,100]
print (binary_search(6, nums))

''' Merge Sort '''
# Total time cost is O(n log n)

def merge_sort(list_to_sort):
    # Base case: lists with fewer than 2 elements are sorted
    if len(list_to_sort) < 2:
        return list_to_sort
    
    # Step 1: divide the list in half
    # We use integer division, so we'll never get a "half index"
    mid_index = len(list_to_sort) // 2
    left = list_to_sort[:mid_index]
    right = list_to_sort[mid_index:]

    # Step 2: sort each half
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # Step 3: merge the sorted halves
    sorted_list = []
    current_index_left = 0
    current_index_right = 0

    while len(sorted_list) < len(left) + len(right):
        if ((current_index_left < len(left)) and