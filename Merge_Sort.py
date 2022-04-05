# Merge sort would break this list (5,4,7,1,3,2,8,6) down again and again until the only thing that is left is a list with only 1 item in them.  So 8 separate lists with 1 item in each one.  A list with 1 item in it, is by definition, "sorted".



# Notes next to the lines of code are from OpenAI - translating Python to natural language

def merge(list1, list2)
  
  combined = [] #create an empty list to store the combined lists
    i = 0 # create two variables, i and j, to keep track of the index of list1 and list2
    j = 0
      while i < len(list1) and j < len(list2): # while the index of list1 is less than the length of list1 and the index of list2 is less than the length of list2:
        if list[i] < list2[j]: # if the item at index i of list1 is less than the item of index j of list2:
          combined.append(list1[i]) # add the item at index i of list1 to the empty list and increment i by 1
          i += 1
        else; # otherwise:
          combined.append(list2[j]) # add the item at index j of list2 to the empty list and increment j by 1
          j += 1
          
          # while the index of list1 is less than the length of list1:
          # add the item at index i of list1 to the empty list and increment i by 1
