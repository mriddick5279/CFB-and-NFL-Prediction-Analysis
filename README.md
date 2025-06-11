# CFB-and-NFL-Prediction-Analysis
This repository hosts how I analyzed my prediction data for both College Football and the NFL for each I season I did predictions for. It's all written in Python and utilizes pandas and matplotlib for visualization of some parts of the data. CSV files are included.

>[!NOTE]
> Part of the analysis includes the "Slap Types" that I used for each game and the records associated with them (more of a visual thing found on my TikTok). Most are acronyms of sorts, so I have left a legend/key of sorts at the bottom of this README file to follow to tell what each one stands for. The record for each slap type essentially means, when I predicted a game using this slap type, was I right or wrong.

# Using any Analysis Script
There are few steps you'll need to setup and a couple of different ways you can choose to do this

## Setup
1. Download the latest version of [Miniconda]([https://www.python.org/downloads/](https://www.anaconda.com/download/success)). You will need to scroll down the page to see the Miniconda installers, and then choose the appropriate installer for your system (Windows, Mac, or Linux). When following the launcher, if it gives you the option to add it to your PATH variable, select yes.
2. Using you computer's search feature, find the **Anaconda Prompt**. Don't worry about the name of this prompt, it is still running Miniconda.
3. Download this repository by cliking on **Code > Download ZIP** at the top of the main page of the repository. Extract all files from the .zip file to wherever you want on your device when it is finished downloading.
4. Using the Anaconda Prompt, navigate to the location of the file/folder on your device that contains the **main.py** script. To do this, use the **cd** command. This command allows you to navigate through your file/folder system on your device. The Anaconda Prompt will typically start you at the location **C:\Users\your_device_username**. So, for example, if you downloaded and extracted the files to your Desktop, you would use the cd command as follows:
```
cd "Desktop\CFB-and-NFL-Prediction-Analysis"
```

> [!TIP]
> You can press **TAB** to autofill any folder/file names in the Anaconda Prompt for you. All you need to do is add the corresponding backslash **\\** to do another folder/file afterwards.

5. Create an environment using the Anaconda Prompt. This is where we will download the necessary package **pandas** that the python script uses. To do this, type **conda create -n ENV_NAME**, where **ENV_NAME** represents the name you personally choose to call this environment. While you can name the environment whatever you want, it's best convention to name is something relevant to what you are doing in the environment, so for example **analysis**, **football_analysis**, etc.
6. Once you have done this, use the python package installer **pip** to install **pandas** and **matplotlib**. pip should already be installed from when you installed Miniconda, so all you need to do is type **pip install pandas**, then **pip install matplotlib** in your Anaconda Prompt. It will then pull and download the necessary files. If you are in a preexisting conda environment that you've made and you already have it installed but forgot, it will tell you **Requirement Satisfied** for each download needed for the package.

## Running Analysis
Now that everything is set up properly, you should be able to run the main script that will let you analyze either a CFB or NFL season (if it exists). To do this you must run the following command in your Anaconda Prompt:
```
python main.py [league] [--year YEAR]
```

> [!TIP]
> Again, double check you are in the "CFB-and-NFL-Prediction-Analysis" folder. Otherwise you will receive an error about main.py not existing.

To break this down, here are what these pieces mean:

* **league**: This argument simply refers to either choosing the NFL or CFB. All that's required here is to type one of these after main.py (**capitilization does not matter**)
* **--year**: This argument is optional, but allows you to choose the year of the season you want to see the analysis of. Simply type the year you want after you type **--year**. If you do not choose to use this argument it will default to the 2024 season for either league

Here are some examples of what the full thing would look like once you have typed it out:

1. See analysis of NFL in default year 2024 season
```
python main.py nfl
```

2. See analysis of CFB in default year 2024 season
```
python main.py cfb
```

3. See analysis of NFL in 2025 season
```
python main.py nfl --year 2025
```

4. See analysis of CFB in 2025 season
```
python main.py cfb --year 2025
```

> [!NOTE]
> If you ever forget how to do this, you can type ```python main.py -h```. This will show instructions on what the command is supposed to do and how to use it.