#Print "Hello World"
#print("Hello World")

#create counties list
#counties = ["Arapahoe", "Denver", "Jefferson"]
#if statement
#if counties[2] == 'Denver':
    #print(counties[2])
#else: 
    #print("try again")

#practice if-else statement
#temperature = int(input("What is the temperature outside? "))
#if temperature > 80:
    #print("Turn on the AC!")
#else:
    #print("Open the windows!")

#practice if statements with grades int and letter assigned
#What is the score?
#score = int(input("What is your test score? "))
#Determine the grade
#if score >= 90:
 #   print("Your grade is an A.")
#elif score >=80:
 #   print("Your grade is a B.")
#elif score >= 70:
 #   print("Your grade is a C.")
#elif score >= 60:
 #   print("Your grade is a D.")
#else:
 #   print("Your grade is an F.")

#counties code
#counties = ["Arapahoe", "Denver", "Jefferson"]
#if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")
# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")
# if "Arapahoe" or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties")
# else:
#     print("Arapahoe and El Paso are not in the list of counties")

#loop practice
#while loop
# x = 0
# while x<=5:
#     print(x)
#     x=x+1
# #for loops
# for county in counties:
#     print(county)

# #list
# # numbers = [0, 1, 2, 3, 4]
# # for num in numbers:
# #     print(num)
# #for num in range(5):
#     #print(num)
# #rewritten
# #for i in range(len(counties)):
#     #print(counties[i])

#counties dictionary
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#get keys
#for county in counties_dict:
    #print(county)
#for county in counties_dict.keys():
    #print(county)
#get values
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
#     print(counties_dict[county])
#     print(counties_dict.get(county))
#get key-value pair
# for county, voters in counties_dict.items():
#     print(county 'has' voters 'registered voters')


#print each dictionary in voting_data
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# #for county_dict in voting_data:
#     #print(county_dict)
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# for county_dict in voting_data:
#     print(county_dict['county'])

#print with original print statement
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes")
# #recode using f-strings
# print(f"I received {my_votes / total_votes * 100}% of the total votes")

#print each county and registered voters
counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
#f-strings to simplify
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#f-strings to print multiple strings or lines to screen
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes. ")
# print(message_to_candidate)
