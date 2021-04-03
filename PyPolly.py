# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Creating the with statement open the file as a text file
    with open(file_to_save, "w") as txt_file:
        file_reader = csv.reader(election_data)

        #Read and print the header row
        headers = next(file_reader)
        


# #The data we need to retreive

# 1. The total number of votes cast
    #Open data file
    #Write down the names of all candidates
    #Add a vote count for each candidate
    #Get the total votes for each candidate
    #Get the total votes cast for the election
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote