#Data needed
# 1) Total number of votes cast
# 2) List of candidates that received votes
# 3) Percentage of votes for each candidate
# 4) Total number of votes for each candidate
# 5) Winner based on popular vote

#Add dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load=os.path.join("Resources","election_results.csv")

#Open the elction results and read the file
with open(file_to_load) as election_data:

    #READ AND ANALYZE DATA HERE
    #Read the file object using the reader function
    file_reader=csv.reader(election_data)
    #Print the header row
    headers=next(file_reader)    
    print(headers)

#Create filename variable for analysis output using indirect path
file_to_save=os.path.join("Analysis","election_analysis.txt")

#Use with statement to open file as a text file
#with open(file_to_save,"w") as txt_file:
    #Write test data to file
    #txt_file.write("Counties in the Election\n---------\nArapahoe\nDenver\nJefferson")


