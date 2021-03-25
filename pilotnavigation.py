import random
name=["Vikram","Arun","Vignesh"]
print("Welcome back Pilot" +" "+ random.choice(name) + "!!\n\nThis is your navigation support how can we Help you-\n\n1.Check If you can land\n2.Check If you are on time.")
n=int(input("Enter Your choice: "))
if(n==1):
      H=int(input("\nInput you current height: \n"))
      if(H<3000):
            print("\n\nYou have to attain a height of atleast 3000ft to land. Cheer up Pilot")
      elif(H>3000 and H<6000):
            print("\n\nYou can land safely.\nAll the best!!")
      else:
            print("\n\nYou are not allowed to land at this height.\n"
            "You need to maintain a height between 300ft to 6000ft in order to land.")
else:
      print("\nYour are absolutely on time sir!!")