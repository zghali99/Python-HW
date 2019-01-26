import os
import csv

total_votes = 0
cand = ["Khan", "Correy", "Li", "O'Tooley"]
county = ["Bamoo", "Marsh", "Queen", "Raffah", "Trandee"]
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0
votes_each = [votes_khan, votes_correy, votes_li, votes_otooley]
khan_percent = 1
correy_percent = 1
li_percent = 1
otooley_percent = 1
percent_each = [khan_percent, correy_percent, li_percent, otooley_percent]

with open(election_date.csv) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        data = list(readCSV)
        total_votes = len(data) - 1
        if cand[i] == "Khan":
            votes_khan = total + 1
        khan_percent = (votes_khan/len(votes_khan))*100
        total = 0
        elif cand[i] == "Correy":
            votes_correy = total + 1
        correy_percent = (votes_correy/len(votes_correy))*100
        total = 0
        elif cand[i] == "Li":
            votes_li = total + 1
        li_percent = (votes_li/len(votes_li))*100
        total = 0
        else:
            votes_otooley = total + 1
        otooley_percent = (votes_otooley/len(votes_otooley))*100

        print("Election Results")
        print("----------------------------")
        print("Total votes: " + total_votes)
        print("----------------------------")
        print(cand[0] + ": "+ khan_percent + "% (" + votes_khan + ")" )
        print(cand[1] + ": "+ correy_percent + "% (" + votes_correy + ")" )
        print(cand[2] + ": "+ li_percent + "% (" + votes_li + ")")
        print(cand[3] + ": "+ otooley_percent + "% (" + votes_otooley + ")" )
        print("----------------------------")
        winner = max(percent_each)
        print("Winner: " + cand[0] )