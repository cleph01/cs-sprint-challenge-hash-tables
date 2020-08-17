def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}

    found = False

    for idx, value in enumerate(weights):
        
        target = limit - value

        if target in dict:

            found == True

            if target > value:

                return (dict.get(target), idx)
            
            elif target < value:

                return (idx, dict.get(target))

            else:

                return (idx, dict.get(target))
    
        elif target not in dict and found == False:

            dict[value] = idx

        else: 

            return None



    

weights_2 = [4, 4]

get_indices_of_item_weights(weights_2, 2, 8)