from typing import List


digits      = [i for i in range(20)] 
tens        = [10*i for i in range(2, 10)] 
hundreds    = [100*i for i in range(1, 10)]
terminate_number_list = digits + tens + hundreds

def is_list_same(in1: int, in2: int) -> bool:
    """check if two argument exists in the same list

    Args:
        in1 (int): first input
        in2 (int): second input

    Returns:
        bool: if two argument exists in the same list
    """
    is_in_digits    = in1 in digits   and in2 in digits
    is_in_tens      = in1 in tens     and in2 in tens
    is_in_hundreds  = in1 in hundreds and in2 in hundreds
    return any([is_in_digits, is_in_tens, is_in_hundreds])

def is_dependent(in1: int, in2: int) -> bool:
    """check if in2 is dependent to in1

    Args:
        in1 (int): first input
        in2 (int): second input

    Returns:
        bool: if in2 is dependent to in1
    """
    if in1 == -1 or in2 == -1:
        return False

    result = False
    if in1 in tens:
        if in2 in digits:
            result = True

    elif in1 in hundreds:
        if in2 in tens + digits:
            result = True

    elif in1 == 1e3:
        if in2 in terminate_number_list:
            result = True

    elif in1 == 1e6:
        if in2 in terminate_number_list + [1e3]:
            result = True
    
    elif in1 == 1e9:
        if in2 in terminate_number_list + [1e3, 1e6]:
            result = True

    elif in1 == 1e12:
        if in2 in terminate_number_list + [1e3, 1e6, 1e12]:
            result = True

    return result


def split_by_terminate_number(number_list: List[int]) -> List[List[int]]:
    """Split list when number in the same level are close to each other or
    when the descending order breaks.

    Args:
        number_list (List[int]): list of numbers

    Returns:
        List[List[int]]: list of sublist of numbers
    """
    splitted_list = []
    split_idx_list = []
    length = len(number_list)

    for idx in range(1, length):
        curr_value = number_list[idx]
        prev_value = number_list[idx - 1]
        if curr_value > prev_value or (is_list_same(curr_value, prev_value)):
            split_idx_list.append(idx)

    split_idx_list = [0] + split_idx_list + [length]
    pair_list = list(zip(split_idx_list[:-1], split_idx_list[1:]))
    for pair in pair_list:
        splitted_list.append(number_list[pair[0]: pair[1]])

    return splitted_list    