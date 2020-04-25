#bubblesort
swapped =True
length = len(random_list)-1

while swapped is True:
  swapped = False
  
  for i in range(length):
    if random_list[i]>random_list[i+1]:
      temp = random_list[i]
      random_list[i] = random_list[i+1]
      random_list[i+1] = temp
      swapped = True
  length-=1
  

#mergesort

def mergeSort(random_list):
  sorted_list = []
  
  length = len(random_list)
  
  if len(random_list)<2:
    return random_list
  
  right_list = mergeSort(random_list[:length//2])
  left_list = mergeSort(random_list[length//2:])
  
  right_idx = 0
  left_idx = 0
  
  while right_idx<len(right_list) and left_idx<len(left_list):
    if right_list[right_idx]>left_list[left_idx]:
      sorted_list.append(left_list[left_idx])
      left_idx+=1
    else:
      sorted_list.append(right_list[right_idx])
      right_idx+=1
      
  sorted_list = sorted_list + left_list[left_idx:] + right_list[right_idx:]
  
  return sorted_list
