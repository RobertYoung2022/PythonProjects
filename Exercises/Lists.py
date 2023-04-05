# 1. Create your own list of days of the week and print out each day of the week by individually accessing each item in the list.
daysOfWeek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
# print(daysOfWeek)

# 2. From your list of days of the week, print out the weekdays and weekend days.
weekdays = f"The weekdays are the following: {daysOfWeek[0].title()}, {daysOfWeek[1].title()}, {daysOfWeek[2].title()}, {daysOfWeek[3].title()} and {daysOfWeek[4].title()}." 
# print(weekdays)

weekend = f"The weekend days are the following: {daysOfWeek[5].title()} and {daysOfWeek[6].title()}." 
# print(weekend)

# NOTE: How to list the days of the week without print each individually.
# for x in range(len(daysOfWeek)):
#     if (x == daysOfWeek[4]):
#         continue
#     print(daysOfWeek, end = ' ')

# 3. From your list of days of the week, print a message containing comething relevant to you, for example, "On Monday I am going on my vacation." 
chillDay = f"I usually have a chill day to myself on {daysOfWeek[6].title()}."
# print(chillDay)
#-----------------------------------------------------------------------------------------------------------------------------------------

# 1. Create a list of friend or family. Print out each person from your list.
friendList = ['mike', 'xavier', 'luna', 'yun', 'darick']
print(friendList)

# NOTE: formatted statement for my friends list
# friendsMessage = f"The names of my friends are {friendList[0].title()}, {friendList[1].title()}, {friendList[2].title()}, {friendList[3].title()} and {friendList[4].title()}."
# print(friendsMessage)

# 2. You've just made a new friend, insert this person at the start of your list using the insert() method.
friendList.insert(0, 'derrick')
print(friendList)

# 3. Ust the append() method to add another friend to your list.
friendList.append('natu')
print(friendList)

# 4. You've misspelled a name on your list, update your list with the correct spelling.
friendList[6] = 'natsu'
print(friendList)

# 5. Use the del statement to remove a friend from your list.
del friendList[4]
print(friendList)

# 6. Use the pop() method to remove friends your list at different positions.
exFriendsList = friendList.pop()
print(friendList)
print(exFriendsList)
#------------------------------------------------------------------------------------------------------------------------------------------