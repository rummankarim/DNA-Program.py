#Rumman-Al-Karim
#November 3,2017
#This program allows the user to enter a dna string 


DNA = str(input("Enter a DNA string: "))

comp = ""

for i in DNA:
  
  if (i == "A"):
    
    comp += "T"
  elif (i == "C"):
    
    comp += "G"
  elif (i == "G"):
    
    comp += "C"
  elif (i == "T"):
    
    comp += "A"
    
  else:
    print("Please input  valid DNA string")
  
  

    
print("The com..", comp)