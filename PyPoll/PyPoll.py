import os
import csv

results = {}
total_votes = 0
candidates = []
counties = []
percents = []

election_data = os.path.join('Resources', 'election_data.csv')

with open(election_data) as CSV_file:
    readCSV = csv.reader(CSV_file, delimiter=',')
    first = next(readCSV)

    for row in readCSV:

        total_votes = total_votes + 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            results[candidate] = 0
        results[candidate] += 1
    winner = candidates[1]

    for candidate in candidates:
        if results[candidate] >= results[winner]:
            winner = candidate

    for candidate in candidates:
        percents.append(((results[candidate]/total_votes)*100))
        combined_data = zip(candidates, percents)
        combined_data = list(combined_data)

    print('Election Results')
    print('-----------------------------------------')
    print('Total Votes: ', total_votes)
    print('-----------------------------------------')
    print(combined_data)
    print('-----------------------------------------')
    print('Winner: ' + winner)
    print('-----------------------------------------')