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

            if dict.get(target) > idx:

                return (dict.get(target), idx)
            
            elif dict.get(target) <= idx:

                return (idx, dict.get(target))
    
        elif target not in dict and found == False:

            dict[value] = idx

        else: 

            found = False

            return None



    

weights_2 = [4, 4]

get_indices_of_item_weights(weights_2, 2, 8)