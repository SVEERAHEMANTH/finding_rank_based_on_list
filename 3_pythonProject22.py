noOfStudents = int(input("Enter the number of students: "))     # no of students

marksDict = {}                      # student name as key and marks as value

nameList = []                       # list to store student name
markList = []                       # list to store student mark



for i in range(0, noOfStudents):
    print("\nEnter the name of the student no", i + 1, ":")
    name = input()
    nameList.append(name)


    print("Enter the marks student no", i + 1, "has gotten:")
    mark = int(input())
    markList.append(mark)

    marksDict[name] = mark          # adding name and mark in dictionary


print("\nInitial dictionary", marksDict)                    # printing marks dictionary


markList.sort()
markList.reverse()

j = 1

print("\nInitia Rank")
for i in markList:
    print("Rank", j, "is: ", list(marksDict.keys())[list(marksDict.values()).index(i)])
    j = j + 1



# markNew = markList.copy()           # making a copy of marks list



while(1):
    print('\nType "1" if you want to update or type "exit" to exit updatation:')
    userWant = input()
    if userWant == "1":
        print("Whose marks you want to update? Enter student's name:")
        updateName = input()
        if updateName in nameList:
            print("Enter the marks: ")
            updateMarks = int(input())

            # index = nameList.index(updateName)
            # markNew[index] = updateMarks

            marksDict[updateName] = int(marksDict[updateName] + updateMarks)
        else:
            print("\nEntered name is invalid")
    else:
        print("\nYou exit the updation program.")
        break

markNew = list(marksDict.values())

print("\nName list:", nameList)
print("Marks list:", markList)
print("New marks:", markNew)

print("List after updation: ", marksDict)

# marksDict = {'nandy': 60, 'daiwik': 20, 'yash': 70}
# markList = [60, 20, 70]

print("The student who got the hightest marks is: ", list(marksDict.keys())[list(marksDict.values()).index(max(marksDict.values()))])




j = 1

markNew.sort()
markNew.reverse()

for i in markNew:
    print("Rank", j, "is: ", list(marksDict.keys())[list(marksDict.values()).index(i)])
    j = j + 1


# 26- 202 19
