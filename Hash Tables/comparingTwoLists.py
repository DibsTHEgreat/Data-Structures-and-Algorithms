# In this file I am going to show a solution to a very common interview
# question that involves hash tables. This method can also be used for
# similar types of questions.

# Question: Compare 2 lists and figure out if these two lists have an
# item that matches.

def item_in_common(list1, list2):
    # first what we'll do is create a dictionary to contain all of our 
    # values from our first list. This can be our baseline on making a
    # hashtable.
    my_dict = {}
    # creating a for loop to go through the first list, and adding them
    # to the dictionary. We're gonna make list1 our baseline, as in all
    # values are equal to true. Than if any matches are found in list2,
    # we can return true for our answer.
    for i in list1:
        my_dict[i] = True
        
    for j in list2:
        # In this for loop we are using variable j to iterate through the
        # second list to find any matches, if a match is found we return true 
        if j in my_dict:
            return True
    
    return False  

# Note: For interview questions what is important is to write code in
# an efficient manner, the goal isn't simply to solve the question,
# but also in an efficient manner (time-complexity).

list1 = [1, 2, 5]
list2 = [3, 4, 5]

print(item_in_common(list1, list2))