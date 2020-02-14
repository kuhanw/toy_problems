#Bubble sort
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
  

