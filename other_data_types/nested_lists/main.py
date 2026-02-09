vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove ("onions")

#carrots
in_carrots = "carrots" in vegetables
if in_carrots == True:
   print ("Carrots are already in the list.")
else:
    vegetables.append("carrots")
print (vegetables)

#cucumbers
in_cucumbers ="cucumbers" in vegetables
if in_cucumbers == True:
   print ("Cucumbers are alerady in the list.")
else: 
    vegetables.append ("cucumbers")
vegetables.sort ()
print ("Updated Vegetable Inventory:", vegetables)
