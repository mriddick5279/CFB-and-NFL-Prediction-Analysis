import argparse

import cfb, nfl

"""
Arguement parser for user to choose a league and season year

League Options: [cfb, nfl]
Year Options: [2024, present)
"""
parser = argparse.ArgumentParser(description="Load and analyze NFL/CFB season file.\n\n" \
"Default season year if not specified will be 2024.")

# Adding arguments and parsing them
parser.add_argument("league",type=str,default='2024',help="Select NFL or CFB as league you want")
parser.add_argument("--year",type=str,default='2024',required=False,help="NFL/CFB season year of file to analyze")

args = parser.parse_args()

# Checking if season year for either league exists
if int(args.year) >= 2024:
    if args.league.upper() == 'CFB': # CFB was selected. Run CFB analysis
        season_file = f"{args.year}regular_season.csv"
        cfb.run(season_file)
    if args.league.upper() == 'NFL': # NFL was selected. Run NFL analysis
        season_file = f"{args.year}regular_season.csv"
        nfl.run(season_file)
else:
    print("INVALID YEAR: Earliest season available for either league is 2024")