Prior to running any of the Jupyter Notbooks or data in this download the neccesary files and create the environments found within them.

# General Setup Guide:

Download [Andaconda](https://docs.anaconda.com/anaconda/install/) to be able to install the environment and use your preference of commandline options or Editor to view the data.
Also go to this [Census Link](https://www2.census.gov/programs-surveys/acs/data/pums/2018/5-Year/) to acquires the data used in this data frame.

### From the list options below choose the environments within this neccesary envrionment for your operating system.

[`Capstone.yml`]

To utilize Geopandas:

[`geopandas.yml`]

All files are located in the main directory and src folder.
Run these two lines of code after the download to apply the kernals to your IDE.

`python -m ipykernel install --user --name geopandas --display-name "Python 3 (geopandas)"` 

`python -m ipykernel install --user --name Capstone --display-name "Python 3 (Capstone)"`  

# Directories of Project

### [Data](): A directory that contains all of the data used for exploration and analysis.

### [Notebooks](): Directory that holds all of the notebooks used for data exploration and analysis.

### [References](): This directory has all of the outside resources and helpful information [pertaining] to models and over all data analysis methodology.

### [Report](): Final notebook of the data analysis and PDF presentaion of the overall project.

### [Src](): The modules/functions creater to aid in the data cleaning and analaysis process.


 # Overview of Project
 This project aims to utilize Illinois 2018 American Community Survey data to create an imcome predicitor to aid Illinois and governmental programs with their allocation of the programs. This will allow allow for a faster application process due to better accuracy. 

 
# Methodoly of the Project and Data Analysis:
This project followed the CRISP-DM model of data science. The business understanding of this project is in aiding the the state of Illinois and allow the  government allocate resources where needed in Illinois.

## Data gathering 
This Data was acquired from the American Community Survery via a csv. 



## Data understanding 
A [data dictionary](https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2014-2018.pdf?#) was found for the data to better understand the column values. The overall income of the data set lie within the fairly equally when binned into:Poverty,Middle, and Uppder classses based on this [study](https://www.investopedia.com/financial-edge/0912/which-income-class-are-you.aspx#:~:text=The%202018%20piece%20from%20Pew,a%20three%2Dperson%20household). There was a lack of representation for the upper class which was expected, but it was not signigicant enough to require any sort of correction or manipulation of the data for this particular reason.

 ![](./Income_plot.png)

# Data Preparation
It was then filterd to remove all of the null values of our target varibale(HINCP). The data was then furhter cleaned and split into a train, val and test set. The data was then scaled and ready to begin modeling.




## Modeling & Evaluation
When beginning the modeling process it was first initated with a Linear regression model and from that FSM chose to try the data on other models such as a Neural network, Random forest Regressor and K-Nearest Neighbors regresor. These models were evalues on the R-squared value.


## Final Results
After further iterations and hyperparameter tuning the final model selcted is a random forest model. With a R-squared score of ***.

# Deployment
I would like to deploy this in Dash or Flask setting. When this is deployed the idea is indivuals can check how much income they will be perceived to make or are though to make given what ever parameter they are able to provide. The app would then report to them the predicted income and the income class they are predicted to be in. Possibly show the client the R-squared of the model for confidence sake once I get the value higher.

# Next steps
Furture iteration of this project would be to acquire more recent census data and provide better insight into the income fluctiation through the years. I would also like to come by data representing the dispersion of Illinois funds to its programs such as SNAP. Lastly, I would delver deper into the data and parse the data into counties and create more specified neural networks per county to ensure accurate representaion of the county and its income.