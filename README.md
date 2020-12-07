# Election Analysis

## Overview
A Colorado Board of Elections employee requested the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Calculate the total number of votes cast in each county.
3. Calculate the percentage of votes cast in each county.
4. Determine the largest county based on voter turnout.
5. Get a complete list of the candidates who received votes.
6. Calcuate the total number of votes each candidate received.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.51.1

## Election-Audit Results
The analysis of the election shows that:
-There were 369,711 votes cast in the election.
  - 38,885 votes (10.5% of the votes) were cast in Jefferson County
  - 306,055 votes (82.8% of the votes) were cast in Denver County
  - 24,801 votes (6.7% of the votes) were cast in Arapahoe County
- The county with the largest voter turnout was Denver

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.
  
## Election-Audit Summary
The script used to audit these election results can be modified and used for any election based on popular vote.  References to file locations and names will need to be updated to properly retrieve and read election results.  Likewise, reference to specific columns within the data should be modified as needed.  The script also assumes the source data has a header row.  If there is no header row, the script should be modified as to not omit that line of data.  
