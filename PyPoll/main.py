import csv

# File path
file_path = "/Users/muadrashid/Desktop/M3PythonChallenge/PyPoll/Resources/election_data.csv"

# Initialize a dictionary to store candidate votes
candidate_votes = {}

# Read the CSV file
with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    total_votes = 0
    
    # Count votes for each candidate
    for row in reader:
        total_votes += 1
        candidate = row['Candidate']
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
output_path = "/Users/muadrashid/Desktop/M3PythonChallenge/PyPoll/Resources/election_results.txt"
with open(output_path, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = candidate_percentages[candidate]
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")
