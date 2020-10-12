def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}

    result = []

    for element in a:

        if (-1*element) in dict:

            if element not in result:
                
                result.append(abs(element))

        else: 

            dict[element] = None
      

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
