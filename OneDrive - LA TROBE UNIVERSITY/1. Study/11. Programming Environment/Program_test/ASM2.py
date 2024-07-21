#Enter inputs
Slices_num = int(input("Enter numbers of pizza slices: "))
People_num = int(input("Enter numbers of people: "))

#Calculation of number of people that get equal slices
Slices_per_person = Slices_num // People_num

#Print result
print("The number of people get equal slices: " + str(Slices_per_person))