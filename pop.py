#Re-coding python's pop() function :

def pop(list, index = -1):
  
  removed = list[index]
  for num in range(index,len(list)-1):
    list[num] = list[num+1]

  list[:] = list[:-1]
  print(f"Element {removed} has been popped!")
  print(f"Updated List:{list}")
  

def main():

  my_list = list(map(int, input("Enter list elements: ").split()))
  index = input("Enter Index to pop:")
  
  if index == "":
    pop(my_list)
    return
    
  else:
    index = int(index)
    
    if index < 0:
        index += len(my_list)

    if index < 0 or index >= len(my_list):
        print("Index out of List range!\nTry again!")
        exit()

  pop(my_list, index)


main()
