def return_element(list1, element):
    """
    This function returns the index of the first occurrence of the given element in the list.

    Args:
        list1 (list): The list to search in.
        element (int): The element to search for.

    Returns:
        int: The index of the first occurrence of the element in the list.
    """

    for i in range(len(list1)):
        if list1[i] == element:
            return i

    return -1
