import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def run(file):

    try:
        ### Loading dataset
        df = pd.read_csv(f'CFB\\Seasons\\{file}')

        ### Getting total win loss record

        wins = df.loc[df['Outcome'] == 'W', 'Outcome'].count()
        losses = df.loc[df['Outcome'] == 'L', 'Outcome'].count()
        print(f"\nFinal Regular Season Record: {wins}-{losses}")

        # Getting win-loss record for Home games

        home_wins_mask = (df['Prediction'] == 'Home') & (df['Outcome'] == 'W')
        home_losses_mask = (df['Prediction'] == 'Home') & (df['Outcome'] == 'L')

        home_wins = df.loc[home_wins_mask, 'Outcome'].count()
        home_losses = df.loc[home_losses_mask, 'Outcome'].count()
        print(f"\tHome Game Record: {home_wins}-{home_losses}")

        # Getting win-loss record for Away games

        away_wins_mask = (df['Prediction'] == 'Away') & (df['Outcome'] == 'W')
        away_losses_mask = (df['Prediction'] == 'Away') & (df['Outcome'] == 'L')

        away_wins = df.loc[away_wins_mask, 'Outcome'].count()
        away_losses = df.loc[away_losses_mask, 'Outcome'].count()
        print(f"\tAway Game Record: {away_wins}-{away_losses}\n")

        ### Creating stacked bar plot for overall W/L

        # Organizing labels and win-loss values
        labels = ['Home','Away']
        home_values = [home_wins, home_losses]
        away_values = [away_wins, away_losses]

        # Setting bar width and positions
        barWidth = 0.3

        bar1 = np.arange(len(labels))
        bar2 = [x + barWidth for x in bar1]

        # Creating and plotting values
        plt.figure(figsize=(15,12))
        plt.bar(bar1, home_values, width=barWidth, color='b', label='Home')
        plt.bar(bar2, away_values, width=barWidth, color='r', label='Away')
        plt.title("Home and Away Record Breakdown")
        plt.ylabel("Games", fontsize=15)
        plt.yticks(fontsize=10)
        plt.xticks([r + barWidth/2 for r in range(len(labels))], labels, fontsize=15)
        plt.legend(["Correct", "Incorrect"])
        plt.savefig("CFB\\Outputs\\home_away_wins_and_losses_plot.png")
        plt.close()

        ### Getting win-loss record of in-conference games for each Conference

        conferences = ['AAC', 'ACC', 'BIG10', 'BIG12', 'CUSA', 'MAC', 'MWC', 'PAC12', 'SBC', 'SEC']

        for conf in conferences:
            conf_wins_mask = ((df['Home Team Conference'] == conf) & (df['Away Team Conference'] == conf)) & (df['Outcome'] == 'W')
            conf_losses_mask = ((df['Home Team Conference'] == conf) & (df['Away Team Conference'] == conf)) & (df['Outcome'] == 'L')

            conf_wins = df.loc[conf_wins_mask, 'Outcome'].count()
            conf_losses = df.loc[conf_losses_mask, 'Outcome'].count()

            print(f"{conf} Record: {conf_wins}-{conf_losses}")

        ### Getting win-loss record for games involving at least one Ranked team

        # Matchup involves at least one ranked team

        one_team_ranked_wins_mask = ((df['Home Team Rank'].notna()) | (df['Away Team Rank'].notna())) & (df['Outcome'] == 'W')
        one_team_ranked_losses_mask = ((df['Home Team Rank'].notna()) | (df['Away Team Rank'].notna())) & (df['Outcome'] == 'L')

        one_team_ranked_wins = df.loc[one_team_ranked_wins_mask, 'Outcome'].count()
        one_team_ranked_losses = df.loc[one_team_ranked_losses_mask, 'Outcome'].count()
        print(f"\nGames w/ a Ranked Team: {one_team_ranked_wins}-{one_team_ranked_losses}")

        # Matchup involves both teams being ranked

        both_teams_ranked_wins_mask = (df['Home Team Rank'].notna()) & (df['Away Team Rank'].notna()) & (df['Outcome'] == 'W')
        both_teams_ranked_losses_mask = (df['Home Team Rank'].notna()) & (df['Away Team Rank'].notna()) & (df['Outcome'] == 'L')

        both_teams_ranked_wins = df.loc[both_teams_ranked_wins_mask, 'Outcome'].count()
        both_teams_ranked_losses = df.loc[both_teams_ranked_losses_mask, 'Outcome'].count()
        print(f"Games b/w Ranked Teams: {both_teams_ranked_wins}-{both_teams_ranked_losses}")

        # Getting win-loss record by Slap Type
        # Includes total overall record, home record, and away record for each slap type

        slap_types = ['LSSQ','RSSQ','LDQ','LSFS','RSFS','LDFS','LSWP','RSWP','LDWP','OBNL','OBL','OBNLF','OBLF','LSSF','LSSDF','RSSF','RSSDF','RSSQLS','LDF','LDS','LDDF','HB','FT','DIVING','FALLING','OUTRO']

        for slap in slap_types:
            slap_wins_mask = (df['Slap Type'] == slap) & (df['Outcome'] == 'W')
            slap_losses_mask = (df['Slap Type'] == slap) & (df['Outcome'] == 'L')

            slap_wins = df.loc[slap_wins_mask, 'Outcome'].count()
            slap_losses = df.loc[slap_losses_mask, 'Outcome'].count()

            print(f"\nTotal {slap} Record: {slap_wins}-{slap_losses}")

            slap_home_wins_mask = slap_wins_mask & (df['Prediction'] == 'Home')
            slap_home_losses_mask = slap_losses_mask & (df['Prediction'] == 'Home')

            slap_home_wins = df.loc[slap_home_wins_mask, 'Outcome'].count()
            slap_home_losses = df.loc[slap_home_losses_mask, 'Outcome'].count()

            print(f"\tHome Breakdown: {slap_home_wins}-{slap_home_losses}")

            slap_away_wins_mask = slap_wins_mask & (df['Prediction'] == 'Away')
            slap_away_losses_mask = slap_losses_mask & (df['Prediction'] == 'Away')

            slap_away_wins = df.loc[slap_away_wins_mask, 'Outcome'].count()
            slap_away_losses = df.loc[slap_away_losses_mask, 'Outcome'].count()

            print(f"\tAway Breakdown: {slap_away_wins}-{slap_away_losses}")

    except:
        print("ERROR: Season file most likely not available")