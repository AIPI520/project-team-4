![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Project Description


## Objective
The objective of the this project is to build a model to predict the number of utility asset power outages for each location (grid cell) within a utility's territory.

## Data
You have a data file (outage_data.parquet) available to you.  The file contains data on 488 locations (grid cells) across the utility's territory for 154 storm events.  There are 4108 features which contain useful data on weather conditions, asset concentration, location, and time.  The target we are predicting is "outage_count".

## Evaluating your model  
We will use all storms occuring after Nov 1 2018 (15 storms) as a test set to evaluate your final model's performance.  Since we will need to explain our results to a non-technical audience (our utility customer), we will use MAPE as the metric.  Your should develop a validation approach to use during modeling building (you should NOT use the test set for this).  Your grade will be impacted by your performance but there are no specific thresholds of performance you must meet - more important than your final performance is the soundness of your approach to the problem, your execution of it, and your ability to communicate it well.

## Project Deliverables
You will submit the following:  
1) Link to a 10-minute max video describing your approach to the problem.  You should use slides to explain your process.  Slides should NOT contain any code snippets but visualizations, diagrams, tables etc are great.  You should explain the final approach you settled on but also discuss your experimentation process and intermediate results (e.g. compare performance of different models you have tried).  You should include discussion of challenges you faced and how you overcame them.  You can have one presenter or all members of your team can present.
2) Code repo containing your project code.  You may use a notebook for data exploration / EDA and initial prototyping, but all of your "production" code for your data pipeline and modeling should be contained in Python scripts.  Below is an example structure for your repo.  Be sure that all code is contained in functions/classes and is documented at least with docstrings.  Your repo should include a readme file descripting your project and how to run it.

### Project repo structure
Your project repo should be organized similar to the below structure.  This is a suggested organization and you may deviate from the below structure if you wish, but make sure you have at least the main components (README, requirements.txt, main.py, helper scripts, model(s), data).


```
├── README.md               <- description of project and how to set up and run it
├── requirements.txt        <- requirements file to document dependencies
├── Makefile [OPTIONAL]     <- setup and run project from command line
├── main.py                 <- main script/notebook to run project 
├── scripts                 <- directory for pipeline scripts or utility scripts
    ├── make_dataset.py     <- script to get data
    ├── build_features.py   <- script to run pipeline to generate features 
    ├── model.py            <- script to train model and predict 
├── models                  <- directory for trained models
├── data                    <- directory for project data
    ├── raw                 <- directory for raw data or script to download
    ├── processed           <- directory to store processed data
    ├── outputs             <- directory to store any output data
├── notebooks               <- directory to store any exploration notebooks used
├── .gitignore              <- git ignore file
```

## Grading
Your project will be graded on the following criteria. 

- **80% project approach and presentation**
    - Clear explanation of your project approach
    - Verbal delivery is professional, understandable and clear
    - Slides are professional, good use of diagrams/tables/visualizations as needed  
    - Data pipeline and modeling approach are sound  
    - Model performance is reasonable

- **20% project code submission**  
    - Code organization - well organized and includes all necessary files to run the project
    - Code documentation - code is well commented and readable, and project contains descriptive readme file

## Teams
- Team 1: Jared, Shuaiming, Daniel, Nick S
- Team 2: Mrinoy, Mike, Abhishek, Jay
- Team 3: Dominique, Hongxuan, Suneel, Sri
- Team 4: Joao, Jingwei, Samyukta, Zihan
- Team 5: Nick C, Haoyang, Aryan
- Team 6: Katie, Thomas,  Rishabh

## Deadline
Wednesday November 22 8:30am

Have fun, and good luck!