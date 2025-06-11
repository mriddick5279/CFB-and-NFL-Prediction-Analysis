import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset
df = pd.read_csv('regular_season.csv')

print(df.info())

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