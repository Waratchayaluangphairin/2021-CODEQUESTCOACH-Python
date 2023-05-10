friends = ["Kevin", "Karen", "Jim", "Jim", "Jim",  "Oscar", "Toby"]

lucky_numbers = [4,5,3,21,46.55]

friends.extend(lucky_numbers) #adds two lists together
friends.append("Sarah") #adding another item to the end of the list
friends.insert(1,"Keller") #adds another item to index 1, pushing everything else to the right
friends.remove("Kevin") #removes item from the list
#friends.clear() #clears the list
friends.pop() #removes the last element of the list

print(friends.index("Jim")) #tells the index of Kevin
print(friends.count("Jim")) #tells how many times jim is in the list
lucky_numbers.sort()
print(lucky_numbers) #organizes the list from least to greatest
lucky_numbers.reverse() #reverses the list order
print(lucky_numbers)

friends2 = friends.copy() #copies a list into another list
print(friends2)