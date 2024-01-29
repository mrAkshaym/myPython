
# list = ["CAT", 4, -1.2, "RAT", "Hello"]
# 
# print("Print list each item in a newline")
# for item in list:
#     print(item)
# 
# print("Append DOG to list")
# list.append("DOG")
# print(list)
# 
# print("Insert HORSE at index 2")
# list.insert(2, "HORSE")
# print(list)
# 
# print("Remove CAT from list")
# list.remove("CAT")
# print(list)

#for i in range (7):
#    print(i)

#for i in range (3, 12,2):
#    print(i)   

breakfast  = ["Bread", "Jam", "Butter"]
lunch = ["Rice", "Dal", "Sabji"]
dinner = ["Salad", "Poha", "Bati choka"]

#menu = [breakfast, lunch, dinner] 
    # output: [['Bread', 'Jam', 'Butter'], ['Rice', 'Dal', 'Sabji'], ['Salad', 'Poha', 'Bati choka']]

#menu = []
#menu.append(breakfast) #output : [['Bread', 'Jam', 'Butter']]

menu = {'breakfast' : breakfast, 'lunch':lunch, 'dinner':dinner}
#output : {'breakfast': ['Bread', 'Jam', 'Butter'], 'lunch': ['Rice', 'Dal', 'Sabji'], 'dinner': ['Salad', 'Poha', 'Bati choka']}

#print(menu)
print(menu['breakfast']) #['Bread', 'Jam', 'Butter']