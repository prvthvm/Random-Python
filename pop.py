#Pops the mentioned element and removes from the array

list = [0,1,2,3,4]

def pop(list, index = -1):
  if not list:
    raise ValueError("Please enter a list!")
  if index < 0:
    index += len(list)
  if index >= len(list):
    raise IndexError("Out of List range!")

  removed = list[index]

  for num in range(index,len(list)-1):
    list[num] = list[num+1]

  list[:] = list[:-1]

  print(f"Element {removed} has been popped!")
  print(f"Updated List:{list}")

  


pop(list)
