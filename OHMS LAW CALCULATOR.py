
z = int(input(" Press (1) for vlotage (2) Current (3) Resistance:"))

if z == 1:
   print ("supply the missing values to calculate the voltage")
   a = float(input("CURRENT(I):"))
   b = float(input("RESISTANCE:"))
   
   V = a*b
   print ("Answer:", V, "Volts")
 
if z == 2:
   print ("supply the missing values to calculate the Current")
   a = float(input("Voltage:"))
   b = float(input("Resistance:"))
   
   I = a/b
   print ("Answer", I,"Amperes")
   
if z == 3:
   print ("supply the missing values to calculate the Resistance")
   a = float(input("Voltage:"))
   b = float(input("Current:"))
   
   I = a/b
   print ("Answer", I,"Ohms")
   
input('Press ENTER to exit')
   

