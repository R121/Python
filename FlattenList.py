
# Function definition that takes in a list of integers and/or nested lists of integer, and flattens it
def flattenNestedList(nested_list):
    
    # List variable where we'll store our flattened results
    final_list = []

    #### NOTE:  If you wanted to do this iteratively instead of recursively (for example, because the input 
    #  lists are so long/complex that you might hit the recursion limit defined), there are several options.
    #  One  would be to use a While loop instead of the For loop I use below.  The While loop would terminate
    #  iterated through each object in the list.  During each iteration, you could use list methods such as 
    # .append(), .extend() and .pop() (amongst others) to append Integers and extend sub-lists from the  
    #  original list to your new flattened list, based on the what type the item is for the current 
    #  iteration of the While loop.  
    ####

    # Loop through our main list
    for item in nested_list:

        # If it's another list (sub-list), recursively call our flattenNestedList function for each element of the sub-list
        # Using recursion, it will eventually get to the most "inner" element of our sub-list - an Integer 
        # Once it reachs an Integer, it appends it to our fina list, then continues working "outwards" 
        #   until that process has completed for all sub-lists (and Integers) in the original list
        if isinstance(item, list):
            for sub_list in flattenNestedList(item):
                final_list.append(sub_list)
        else:    
        # If element of nested_list is not another list, it's an integer (for this particular problem)
        # Add the integer to our final list
            final_list.append(item)
    
    # Return our final list - the flattened results of our original list
    return final_list

# In Python, this line is used to invoke a "main" type function/section (I won't go into a more thorough explanation here)
# Execute our "main" code here: set the nested list to be used, call our function passing our nested list to it, then print results
if __name__ == "__main__":

    # Variable to store nested list of Integers and sub-lists to be sent to function
    # I used a number of lists here to test the function based on varying input lists
    # I uncommented the one I used for a given execution
    #test_list = []
    #test_list = [1,2,3,4,5,6,7,8,9,10]
    #test_list = [1,2,[11],5,6,7,8,9,10]   
    #test_list = [1,2,[3,4],5,6,7,8,9,10]         
    #test_list = [2,4,3,[4,9],3,[2,6],3,[3,6,34,3],2] 
    #test_list = [2,4,3,[4,9],3,[2,6],3,[],[3,6,34,3],2]  
    test_list = [2,4,[5,[34,9,[4,8]],3],3,[],[2,[1],[],6],3,[3,6,34,3],2]

    # Call function passing in flattened list; save results
    results_list = flattenNestedList(test_list)

    # Print out flattened list
    print("Flattened list is: " + str(results_list))






