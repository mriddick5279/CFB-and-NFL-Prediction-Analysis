import pandas as pd
import matplotlib.pyplot as plt

def run(file):
    # Loading dataset
    df = pd.read_csv(f'NFL\\Seasons\\{file}')

    # print(df.info())

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
    plt.legend(["Correct", "Incorrect"])
    plt.savefig("NFL\\Outputs\\home_away_wins_and_losses_plot.png")
    plt.close()

    # Determining record among divisions
    nfc_records = {'North': [0,0], 'East': [0,0], 'South': [0,0], 'West': [0,0]}
    afc_records = {'North': [0,0], 'East': [0,0], 'South': [0,0], 'West': [0,0]}

    for item in df.itertuples():
        # print(item[10])
        if item[5] == item[7]:
            conf = item[5]

            temp = conf.split(" ")
            division = temp[1]

            if item[10] == 'W':
                if 'AFC' in conf:
                    curr_wins = afc_records[division][0]
                    afc_records[division][0] = curr_wins + 1
                elif 'NFC' in conf:
                    curr_wins = nfc_records[division][0]
                    nfc_records[division][0] = curr_wins + 1
            
            elif item[10] == 'L':
                if 'AFC' in conf:
                    curr_losses = afc_records[division][1]
                    afc_records[division][1] = curr_losses + 1
                elif 'NFC' in conf:
                    curr_losses = nfc_records[division][1]
                    nfc_records[division][1] = curr_losses + 1

    labels = []
    top = []
    bott = []
    for k, v in afc_records.items():
        print(f"AFC {k}: {v[0]}-{v[1]}")
        labels.append(k)
        top.append(v[1])
        bott.append(v[0])

    # Creating stacked bar plot for AFC W/L 
    plt.bar(labels, bott, color='g')
    plt.bar(labels, top, bottom=bott, color='r')
    plt.title("AFC Wins and Losses Breakdown")
    plt.ylabel("Games", fontsize=15)
    plt.yticks(fontsize=10)
    plt.legend(["Correct", "Incorrect"])
    plt.savefig("NFL\\Outputs\\afc_wins_and_losses_plot.png")
    plt.close()

    print()

    labels = []
    top = []
    bott = []
    for k, v in nfc_records.items():
        print(f"NFC {k}: {v[0]}-{v[1]}")
        labels.append(k)
        top.append(v[1])
        bott.append(v[0])

    # Creating stacked bar plot for NFC W/L 
    plt.bar(labels, bott, color='g')
    plt.bar(labels, top, bottom=bott, color='r')
    plt.title("NFC Wins and Losses Breakdown")
    plt.ylabel("Games", fontsize=15)
    plt.yticks(fontsize=10)
    plt.legend(["Correct", "Incorrect"])
    plt.savefig("NFL\\Outputs\\nfc_wins_and_losses_plot.png")
    plt.close()