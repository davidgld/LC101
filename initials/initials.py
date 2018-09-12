def get_initials(fullname):

     #""" Given a person's name, returns the person's initials (uppercase) """
     #TODO your code here
  get = (fullname)
  name_list = get.split()

  initials = ""

  for name in name_list: 
    initials += name[0].upper()  

  return initials

def main():
  letters = get_initials(input("What is your full name?\n"))
  print(letters)
  



if __name__ ==  '__main__':
  main()




#letters = get_initials("Ozzie Smith")
#print("The initials of 'Ozzie Smith' are", letters) 
#letters = get_initials("Bonnie blair")
#print("The initials of 'Bonnie blair' are", letters) 
#letters = get_initials("George")
#print("The initials of 'George' are", letters) 
#letters = get_initials("Daniel Day Lewis")
#print("The initials of 'Daniel Day Lewis' are", letters) 


 