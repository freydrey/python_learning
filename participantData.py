# ParticipantNumber = 2
# ParticipantData = []
# registeredParticipants = 0

# outputFile = open("ParticipantData.txt","w")

# while registeredParticipants < ParticipantNumber:
#     tempPartData = []
#     name = input("Please enter your name: ")
#     tempPartData.append(name)

#     country = input("Please enter your country: ")
#     tempPartData.append(country)

#     age = input("Please enter your age: ")
#     tempPartData.append(age)

#     print(tempPartData)
#     ParticipantData.append(tempPartData)
#     print(ParticipantData)

#     registeredParticipants += 1

# for participant in ParticipantData:
#     for data in participant:
#         outputFile.write(str(data))
#         outputFile.write(" ")

#     outputFile.write("\n")

# outputFile.close
#ctrl + / block comment

inputFile = open("ParticipantData.txt","r")

inputList = []

for line in inputFile:
    tempParticipant = line.strip("\n").split()
    print(tempParticipant)
    inputList.append(tempParticipant)
    print(inputList)


Age = {}
for part in inputList:
    tempAge = int(part[-1])
    if tempAge in Age:
        Age[tempAge] +=1
    else:
        Age[tempAge] = 1


print(Age)

Oldest = 0
Youngest = 100
mostOccuringAge = 0
counter = 0

for tempAge in Age:
    if tempAge > Oldest:
        Oldest = tempAge
    if tempAge < Youngest:
        Youngest = tempAge
    if Age[tempAge] >= counter:
        counter = Age[tempAge]
        mostOccuringAge = tempAge

print(Oldest)
print(Youngest)
print("Most occuring age is:",mostOccuringAge,"with",counter,"participants")

inputFile.close