import os
import csv

csv_path = os.path.join("..", "Resources", "election_data.csv")

Votes = 0

Cand_options = []
Cand_votes = {}

Winning_candidate = ""
Winning_count = 0

with open(csv_path, newline = '') as csvfile:
	csvread = csv.DictReader(csvfile)
    
    for row in csvread:

        Votes = Votes + 1
        Cand_name = row["Candidate"]

        if Cand_name not in Cand_options:
            Cand_options.append(Cand_name)

            Cand_votes[Cand_name] = 0

        Cand_votes[Cand_name] = Cand_votes[Cand_name] + 1


file_output = os.path.join("..", "Resources", "election_output.txt")

with open(file_output)