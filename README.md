# Quantified Self (QS) Ledger

## A Personal Data Aggregator and Dashboard for Self-Trackers and Quantified Self Enthusiasts

[Quantfied Self (QS) Ledger](https://github.com/markwk/qs_ledger) aggregates and visualizes your personal data. 

The project has two primary goals: 

1. **download all of your personal data** from various tracking services (see below for list of integration services) and store locally. 
2. provide the starting point for **personal data analysis, data visualization and a personal data dashboard** 

At present, the main objective is to provide working data downloaders and simple data analysis for each of the integrated services. 

Some initial work has been started on using these data streams for predictive analytics and forecasting using Machine Learning and Artificial Intelligence, and the intention to increasingly focus on modeling in future iterations. .

### Code / Dependencies: 

* The code is written in Python 3. 
* Shared and distributed via Jupyter Notebooks. 
* Most services depend on Pandas and NumPy for data manipulation and Matplot and Seaborn for data analysis and visualization. 
* To get started, we recommend downloading and using the [Anaconda Distribution](https://www.anaconda.com/download/#macos).
* For initial installation and setup help, see documentation below. 
* For setup and usage of individual services, see documentation provided by each integration.  

### Current Integrations: 

* [Apple Health](https://github.com/markwk/qs_ledger/tree/master/apple_health): fitness and health tracking, data analysis and dashboard from iPhone or Apple Watch (includes example of Elastic Search integration and Kibana Health Dashboard).
* [AutoSleep](https://github.com/markwk/qs_ledger/tree/master/autosleep/autosleep_data_analysis.ipynb): iOS sleep tracking data analysis of sleep per night and rolling averages. 
* [Fitbit](https://github.com/markwk/qs_ledger/tree/master/fitbit): fitness and health tracking and analysis of Steps, Sleep, and Heart Rate from a Fitbit wearable.
* [GoodReads](https://github.com/markwk/qs_ledger/tree/master/goodreads ): book reading tracking and data analysis for GoodReads.
* [Google Calendar](https://github.com/markwk/qs_ledger/tree/master/google_calendar/): past events, meetings and times for Google Calendar.
* [Google Sheets](https://github.com/markwk/qs_ledger/tree/master/google_sheets/): get data from any Google Sheet which can be useful for pulling data from IFTTT integrations that add data. 
* [Habitica](https://github.com/markwk/qs_ledger/tree/master/habitica/habitica_downloader.ipynb): habit and task tracking with Habitica's gamified approach to task management.
* [Instapaper](https://github.com/markwk/qs_ledger/tree/master/instapaper/instapaper_downloader.ipynb): articles read and highlighted passages from Instapaper.
* [Kindle Highlights](https://github.com/markwk/qs_ledger/tree/master/kindle/kindle_clippings_parser.ipynb): Parser and Highlight Extract from Kindle clippings, along with a sample data analysis and tool to export highlights to separate markdown files.  
* [Last.fm](https://github.com/markwk/qs_ledger/tree/master/last_fm): music tracking and analysis of music listening history from Last.fm.
* [Oura](https://github.com/markwk/qs_ledger/tree/master/oura): oura ring activity, sleep and wellness data. 
* [RescueTime](https://github.com/markwk/qs_ledger/tree/master/rescuetime): track computer usage and analysis of computer activities and time with RescueTime. 
* [Pocket](https://github.com/markwk/qs_ledger/tree/master/pocket/pocket_downloader.ipynb): articles read and read count from Pocket. 
* [Strava](https://github.com/markwk/qs_ledger/tree/master/strava): activities downloader (runs, cycling, swimming, etc.) and analysis from Strava. 
* [Todoist](https://github.com/markwk/qs_ledger/tree/master/todoist): task tracking and analysis of todo's and tasks completed history from Todoist app. 
* [Toggl](https://github.com/markwk/qs_ledger/tree/master/toggl): time tracking and analysis of manual timelog entries from Toggl. 
* [WordCounter](https://github.com/markwk/qs_ledger/tree/master/wordcounter): extract wordcounter app history and visualize recent periods of word counts.

### EXAMPLES: 

* [Combine and Merge Personal Data into Unified Data Frame](https://github.com/markwk/qs_ledger/blob/master/Example_Combined_Personal_Data.ipynb): This example notebook provides a step-by-step walkthrough about how to combine multiple data points into a unified daily CSV of personal metrics. 
* [Simple QS Correlation Explorer with Plot.ly and Dash](https://github.com/markwk/qs_ledger/blob/master/example_correlation_explorer_with_plotly.py): This example code uses combined data frame to generate a simple way to view data, visualize correlation and test for linear regression relationship. Requires Dash and Plot.ly. 
* [Import Apple Health Data into Elastic Search and Create a Dashboard](https://github.com/markwk/qs_ledger/blob/master/apple_health/apple_health_data2elastic.ipynb): This example code shows how to import data from a panda's dataframe into Elastic Search and then how create necessary indexes, objects and finally a working dynamic dashboard. See [Apple Health readme](https://github.com/markwk/qs_ledger/tree/master/apple_health) for specific instructions. 

### How to use this project: Installation and Setup Locally

Until we provide a working version for Google's Collab or other online jupyter notebook setups, we recommend to get started by downloading and using the [Anaconda Distribution](https://www.anaconda.com/download/), which is free and open source. This will give you a local working version of Numpy, Pandas, Jupyter Notebook and other Python Data Science tools. 

After installation, we recommend create and activating a virtual environment using [Anaconda](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/) or manually:  

`python3 -m venv ~/.virtualenvs/qs_ledger`

`source ~/.virtualenvs/qs_ledger/bin/activate`

Then clone the current github repo: 

`git clone https://github.com/markwk/qs_ledger.git`

Using your activate virtual environment, install dependencies: 

`pip install -r requirements.txt`

Then navigate into your directory and launch an individual notebook or the full project with jupyter notebook or jupyter lab: 

`jupyter lab`

### Code Organization 

Best practices and organization are still a work-in-progresss, but in general: 

* Each project has a NAME_downloader and NAME_data_analysis. 
* Some projects include a helper function for data pulling. 
* Optionally, some projects have useful notebooks for specific use cases, like weekly reviews. 

### Useful Shortcuts

You can use command line to run jupyter notebooks directly and, in the case of papermill, you can pass parameters: 

With [nbconvert](https://nbconvert.readthedocs.io/en/latest/index.html):

- `pip install nbconvert`
- `jupyter nbconvert --to notebook --execute --inplace rescuetime/rescuetime_downloader.ipynb`

With [Papermill](https://github.com/nteract/papermill):

- `pip install papermill`

- `papermill rescuetime_downloader.ipynb data/output.ipynb -p start_date '2019-08-14' -p end_date '2019-10-14'`
- **NOTE**: You first need to [parameterize your notebook](https://github.com/nteract/papermill#parameterizing-a-notebook) in order pass parameters into commands. 

#### Creators and Contributors: 

* [Mark Koester](https://github.com/markwk/)

**Want to help?** Fork the project and provide your own data analysis, integration, etc.   

## Questions? Bugs? Feature Requests? Need Support?

Post a ticket in the [QS Ledger Issue Queue](https://github.com/markwk/qs_ledger/issues) 
