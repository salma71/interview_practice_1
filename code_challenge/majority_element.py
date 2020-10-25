def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([])
    []
    '''
    # find the majority element, use counter
    # if there is no majority return []
    # return the index of the majority element
    if lst == []: 
        return []
    else:
        from collections import Counter
        count = Counter(lst)
        major_element = sorted(
            count.keys(),
            key = lambda x: -count[x]
        )
        top_elem = major_element[0]
        if count[top_elem] > len(lst) // 2:
            return [
                i for i, ele in enumerate(lst)
                if ele == top_elem
            ]
        else:
            return []
    

