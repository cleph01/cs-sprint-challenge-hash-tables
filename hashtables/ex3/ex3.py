def intersection(arrays):
    """
    YOUR CODE HERE
    """
    dict = {}

    result = []

    for sub_array in arrays:

        for element in sub_array:

            if element in dict:

                if element not in result:
                    
                    result.append(element)

            else: 

                dict[element] = None
      

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
