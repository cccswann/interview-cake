''' this function runs in constant time O(1) - The input could be 1 or 1000
but it will only require one step '''

def print_first_item(items):
    print(items[0])

''' this function runs in linear time O(n) where n is the number of items
in the list

if it prints 10 items, it has to run 10 times. If it prints 1,000 items,
we have to print 1,000 times'''

def print_all_items(items):
    for item in items:
        print(item)

''' Quadratic time O(n^2)'''

def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)

print_all_possible_ordered_pairs([0,6,8,9])


