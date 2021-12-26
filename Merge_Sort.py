# Merge sort would break this list (5,4,7,1,3,2,8,6) down again and again until the only thing that is left is a list with only 1 item in them.  So 8 separate lists with 1 item in each one.  A list with 1 item in it, is by definition, "sorted".


# Merge function

# adding text for Github testing

def merge(list1, list2)
  # new list to combine list1 and list2
  combined = []
    i = 0
    j = 0
      while i < len(list1) and j < len(list2):
        if list[i] < list2[j]:
          combined.append(list1[i])
          i += 1
        else;
          combined.append(list2[j])
          j += 1