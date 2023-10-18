def sum_of_items(lst: list) -> int:
    total = 0
    for i in lst:
        total += i
    return total
    """
    Given a list of integers, return the sum of these integers.
    If the list is empty, return 0.
    ex. [5, 6, 2, 1] --> 5+6+2+1=14
    ex. [0, 0] --> 0+0=0
    """
    pass

def dict_of_num_type_lsts(lst: list) -> dict:
    pos_lst = []
    neg_lst = []
    zero_lst = []
    dic = {}
    for i in lst:
        if i > 0:
            pos_lst.append(i)
        elif i < 0:
            neg_lst.append(i)
        else:
            zero_lst.append(i)
    dic["pos_lst"] = pos_lst
    dic["neg_lst"] = neg_lst
    dic["zero_lst"] = zero_lst
    return dic
    """
    Given a list of integers, create a dictionary with three keys: "pos_lst", "zero_lst", and "neg_lst".
    The value of key "pos_lst" should be the list of all positive integers in the argument.
    The value of key "zero_lst" should be the list of all zeroes in the argument.
    The value of key "neg_lst" should be the list of all negative integers in the argument.
    ex. [4, 2, 5, 0, 2, 1, 0, -1] -->
        {"pos_lst": [4, 2, 5, 2, 1], "zero_lst": [0, 0], "neg_lst": [-1]}
    """
    pass

def ratings_adjustment(ratings):
    backend_rating = ratings["backend"]
    lst = []
    for i in ratings:
        if i != "backend" and ratings[i] > backend_rating:
            lst.append(i)
    for i in lst:
        ratings.pop(i)
    return ratings
    """
    Given a dictionary containing the overall student ratings of the AppDev courses,
    with course names as keys and ratings as values, ensure that the results are correct.

    Naturally, any courses with a higher rating than 'backend' must have cheated,
    so they should be removed from the dictionary entirely.

    Return the corrected dictionary.
    """
    pass

class Counter:
    def __init__(self):
        self.value = 0  
    def getVal(self):
        return self.value
    def inc(self):
        self.value += 1
    def dec(self):
        self.value-=1
        
    """
    Implement a function 'getVal' that gets the value of an object. 
    On creation, this value should be 0.
    Implement a function called "inc" that increases the value of the object
    by 1.
    Implement a function called "dec" that decreases the value of the obejct
    by 1.
    """
    pass

if __name__ == "__main__":
    empty_lst = []
    big_lst = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    small_lst = [-1, 0, 1]
    lst_with_only_zeroes = [0, 0, 0]

    print("sum_of_items results:")
    print(f"sum_of_items({empty_lst}): {sum_of_items(empty_lst)}")
    print(f"sum_of_items({big_lst}): {sum_of_items(big_lst)}")
    print(f"sum_of_items({small_lst}): {sum_of_items(small_lst)}")
    print(
        f"sum_of_items({lst_with_only_zeroes}): {sum_of_items(lst_with_only_zeroes)}"
    )
    print()

    print("dict_of_num_type_lsts results:")
    print(
        f"dict_of_num_type_lsts({empty_lst}): {dict_of_num_type_lsts(empty_lst)}"
    )
    print(f"dict_of_num_type_lsts({big_lst}): {dict_of_num_type_lsts(big_lst)}")
    print(
        f"dict_of_num_type_lsts({small_lst}): {dict_of_num_type_lsts(small_lst)}"
    )
    print(
        f"dict_of_num_type_lsts({lst_with_only_zeroes}): {dict_of_num_type_lsts(lst_with_only_zeroes)}"
    )
    print()

    test_ratings = {'backend': 5, 'ios': 3, 'android': 7}
    print("ratings_adjustment results:")
    print(f"ratings_adjustment({test_ratings}): {ratings_adjustment(test_ratings)}")
    print()

    print("Counter results:")
    counter = Counter()
    print(f"counter.getVal(): {counter.getVal()}")
    counter.inc()
    counter.inc()
    print(f"counter.inc(), counter.inc(): {counter.getVal()}")
    counter.dec()
    print(f"counter.dec(): {counter.getVal()}")
    print()


