import os   # Allow us to create file paths across op systems
import csv  # Module for reading CSV files

candidates = []
candidate_i = 0
votes = []

csvpath = os.path.join(".", "Resources", "election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)    # save and go past header
    for row in csvreader:
        if row[2] not in candidates :
            candidates.append(row[2])
            votes.append(0)
        candidate_i = candidates.index(row[2])
        votes[candidate_i] += 1

total_vote_count = sum(votes)
winner = candidates[votes.index(max(votes))]

print("'''text\nElection Results\n-------------------------\n\
Total Votes: %d\n-------------------------" % total_vote_count)
for i in range(len(candidates)):
    print("%s: %.3f%% (%d)" \
    % (candidates[i], votes[i]*100/total_vote_count, votes[i]))
print("-------------------------\nWinner: %s\n\
-------------------------\n'''" % winner)

output_path = os.path.join(".", "analysis", "Analysis.txt")

with open(output_path, 'w') as f:
    f.write("'''text\nElection Results\n-------------------------\n\
Total Votes: %d\n-------------------------\n" % total_vote_count)
    for i in range(len(candidates)):
        f.write("%s: %.3f%% (%d)\n" \
        % (candidates[i], votes[i]*100/total_vote_count, votes[i]))
    f.write("-------------------------\nWinner: %s\n\
-------------------------\n'''" % winner)