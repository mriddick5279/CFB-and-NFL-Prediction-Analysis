import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading dataset
df = pd.read_csv('regular_season.csv')

# Getting total win loss record
wins = len(df[df['Outcome'] == 'W'])
losses = len(df[df['Outcome'] == 'L'])
print(f"\nFinal Regular Season Record: {wins}-{losses}")

# Getting win loss records for Home and Away games
home_predictions = df[df['Prediction'] == 'Home']
away_predictions = df[df['Prediction'] == 'Away']

home_wins = len(home_predictions[home_predictions['Outcome'] == 'W'])
home_losses = len(home_predictions[home_predictions['Outcome'] == 'L'])
print(f"Home Game Record: {home_wins}-{home_losses}")

away_wins = len(away_predictions[away_predictions['Outcome'] == 'W'])
away_losses = len(away_predictions[away_predictions['Outcome'] == 'L'])
print(f"Away Game Record: {away_wins}-{away_losses}\n")

# Creating stacked bar plot for overall W/L
labels = ['Home','Away']
top = [home_losses, away_losses]
bott = [home_wins, away_wins]

plt.bar(labels, bott, color='g')
plt.bar(labels, top, bottom=bott, color='r')
plt.title("Home and Away Record Breakdown")
plt.ylabel("Games", fontsize=15)
plt.yticks(fontsize=10)
plt.legend(["Wins", "Losses"])
plt.savefig("Outputs\\home_away_wins_and_losses_plot.png")
plt.close()

# Determining record among conferences
conference_records = {'AAC': [0,0], 'ACC': [0,0], 'BIG10': [0,0], 'BIG12': [0,0], 'CUSA': [0,0],'MAC': [0,0], 'MWC': [0,0], 'PAC12': [0,0], 'SBC': [0,0], 'SEC': [0,0]}

yes = 0; no = 0
for item in df.itertuples():

    if item[6] == item[9]:
        conf = item[6]

        if item[12] == 'W':
            curr_wins = conference_records[conf][0]
            conference_records[conf][0] = curr_wins + 1

        elif item[12] == 'L':
            curr_losses = conference_records[conf][1]
            conference_records[conf][1] = curr_losses + 1

    elif item[6] == 'PAC12' or item[9] == 'PAC12':
        if item[12] == 'W':
            curr_wins = conference_records['PAC12'][0]
            conference_records['PAC12'][0] = curr_wins + 1

        elif item[12] == 'L':
            curr_losses = conference_records['PAC12'][1]
            conference_records['PAC12'][1] = curr_losses + 1

labels = []
top = []
bott = []
for key, value in conference_records.items():
    print(f"{key} Record: {value[0]}-{value[1]}")
    labels.append(key)
    top.append(value[1])
    bott.append(value[0])
print()

# Creating stacked bar plot for conference W/L 
plt.bar(labels, bott, color='g')
plt.bar(labels, top, bottom=bott, color='r')
plt.title("Conference Wins and Losses Breakdown")
plt.ylabel("Games", fontsize=15)
plt.yticks(fontsize=10)
plt.legend(["Wins", "Losses"])
plt.savefig("Outputs\\conf_wins_and_losses_plot.png")
plt.close()

# Determining record for games involving ranked teams
ranked_record = {'One': [0,0], 'Both': [0,0]}
for item in df.itertuples():

    if item[5] <= 25 or item[8] <= 25:
        if item[5] <= 25 and item[8] <= 25:
            if item[12] == 'W':
                curr_wins = ranked_record['One'][0]
                ranked_record['One'][0] = curr_wins + 1

                curr_wins = ranked_record['Both'][0]
                ranked_record['Both'][0] = curr_wins + 1

            elif item[12] == 'L':
                curr_losses = ranked_record['One'][1]
                ranked_record['One'][1] = curr_losses + 1

                curr_losses = ranked_record['Both'][1]
                ranked_record['Both'][1] = curr_losses + 1

        else:
            if item[12] == 'W':
                curr_wins = ranked_record['One'][0]
                ranked_record['One'][0] = curr_wins + 1

            elif item[12] == 'L':
                curr_losses = ranked_record['One'][1]
                ranked_record['One'][1] = curr_losses + 1

for key, value in ranked_record.items():
    if key == 'One':
        print(f"Games w/ a Ranked Team: {value[0]}-{value[1]}")
    elif key == 'Both':
        print(f"Games b/w Ranked Teams: {value[0]}-{value[1]}")
print()

# Record breakdown for each slap type
# Includes total overall record, home record, and away record for each slap type
slap_types = ['LSSQ','RSSQ','LDQ','LSFS','RSFS','LDFS','LSWP','RSWP','LDWP','OBNL','OBL','OBNLF','OBLF','LSSF','LSSDF','RSSF','RSSDF','RSSQLS','LDF','LDS','LDDF','HB','FT','DIVING','FALLING','OUTRO']

for st in slap_types:
    stDF = df[df['Slap Type'] == st]
    slap_wins = len(stDF[stDF['Outcome'] == 'W'])
    slap_losses = len(stDF[stDF['Outcome'] == 'L'])

    print(f"Total {st} Record: {slap_wins}-{slap_losses}")

    sthomeDF = stDF[stDF['Prediction'] == 'Home']
    stawayDF = stDF[stDF['Prediction'] == 'Away']

    slap_wins_home = len(sthomeDF[sthomeDF['Outcome'] == 'W'])
    slap_losses_home = len(sthomeDF[sthomeDF['Outcome'] == 'L'])

    slap_wins_away = len(stawayDF[stawayDF['Outcome'] == 'W'])
    slap_losses_away = len(stawayDF[stawayDF['Outcome'] == 'L'])

    print(f"\tHome Breakdown: {slap_wins_home}-{slap_losses_home}")
    print(f"\tAway Breakdown: {slap_wins_away}-{slap_losses_away}\n")