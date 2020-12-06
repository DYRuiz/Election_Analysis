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

#Create filename variable for analysis output using indirect path
file_to_save=os.path.join("Analysis","election_analysis.txt")

#READ AND ANALYZE DATA HERE

#Variable and dictionary initialization
    #Initialize total vote counter
total_votes=0
    #Candidate options and candidate votes
candidate_options=[]
    #Declare empty dictionary
candidate_votes={}
    #Winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#Open the election results and read the file
with open(file_to_load) as election_data:

    #Read the file object using the reader function
    file_reader=csv.reader(election_data)
    #Read the header row
    headers=next(file_reader)    
    #Print each row in the csv file
    for row in file_reader:
        #Add to the total vote count
        total_votes+=1
        #Print candidate name from each row
        candidate_name=row[2]
        #Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #Begin tracking candidate vote count
            candidate_votes[candidate_name]=0
        #Add a vote to each candidate count
        candidate_votes[candidate_name]+=1

    #Save results to output text file
    with open(file_to_save,"w") as txt_file:
        #Print final vote count to terminal
        election_results=(
            f"\nElection Results\n"
            f"--------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------\n")
        print(election_results,end="")
        
        #Save final vote count to the text file
        txt_file.write(election_results)
        
        #Determine percentage of votes for each candidate
        #Iterate through candidate list
        for candidate_name in candidate_votes:
            #Retrieve vote count of candidate
            votes=candidate_votes[candidate_name]
            #Calculate percentage of votes
            vote_percentage=float(votes)/float(total_votes)*100
            
            #Print the each candidate's name, vote count and percentage of vote
            candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            #Save candidate results to text file
            txt_file.write(candidate_results)#Determine winning vote count and candidate
            
            #Determine if the votes is greater than the winning count
            if (votes>winning_count) and (vote_percentage>winning_percentage):
                #True: Set winning count equal to voting count and winning percentage equal to vote percentage
                winning_count=votes
                winning_percentage=vote_percentage
                #Set winning candidate equal to candidate's name
                winning_candidate=candidate_name   
   
        winning_candidate_summary=(
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
        print(winning_candidate_summary)
        #Save the winning candidate's summary to the text file
        txt_file.write(winning_candidate_summary)
        
            
        
