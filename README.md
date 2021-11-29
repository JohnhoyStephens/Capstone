Prior to running any of the Jupyter Notbooks or data download the neccesary files and create the environments to run with them.

# General Setup Guide:

Download [Andaconda](https://docs.anaconda.com/anaconda/install/) to be able to install the environment and use your preference of commandline options or Editor to view the data.
To access the data go to the [Census website](https://www2.census.gov/programs-surveys/acs/data/pums/2018/5-Year/) and download the csv_hil.zip for your own experimentation. Then place the download in the data folder to allow for a smooth utilization of the prewritten code.

### Use the YAML files below to create the environments to run the data.

[`Capstone.yml`]

To utilize Geopandas:

[`geopandas.yml`]

All files are located in the main directory and src folder.
Run these two lines of code after the download to apply the kernals to your IDE.

`python -m ipykernel install --user --name tens --display-name "Python 3 (Capstone)"`

`python -m ipykernel install --user --name Capstone --display-name "Python 3 (visuals)"`

# Directories of Project

### [Data](https://github.com/jstephens1196/Johnhoy-Stephens-Flat-Iron-Capstone/tree/master/Data/csv_hil): A directory that contains all of the data used for exploration and analysis.

### [Notebooks](https://github.com/jstephens1196/Johnhoy-Stephens-Flat-Iron-Capstone/tree/master/Notebooks/Explortatory): Directory that holds all of the notebooks used for data exploration and analysis.

### [References](https://github.com/jstephens1196/Johnhoy-Stephens-Flat-Iron-Capstone/tree/master/References): This directory has all of the outside resources and helpful information [pertaining] to models and over all data analysis methodology.

### [Report](https://github.com/jstephens1196/Johnhoy-Stephens-Flat-Iron-Capstone/tree/master/Reports/Presentation): Final notebook of the data analysis and PDF presentaion of the overall project.

### [Src](https://github.com/jstephens1196/Johnhoy-Stephens-Flat-Iron-Capstone/tree/master/src): The functions created for analysis process.

# Overview of Project

This project aims to utilize Illinois 2018 American Community Survey data to create an imcome predicitor to aid Illinois benefit programs such as SNAP and unemployment with their allocation of resources. This will allow for a faster application process due for the Illinois Department of Human Services(IDHS) due to better accuracy. It will also lead to faster deploymenty of benefit for an Illinois citzen.This is very crucial in especially when looking at unemployment. This has been one of the most vital neccesities of this COVID-19 age due to the massive amount of layoff and furloughs done by organizations. In creating a better system to assess the income of an individual we can better deploy these state services to the citizens that need them. More information on this topic can be found [here](https://www.nytimes.com/2020/04/16/upshot/coronavirus-prediction-rise-poverty.html)

![](Reports/Figures/Map.png)

# Project Workflow and Data Analysis:

This project followed the CRISP-DM model of data science exploration. The business understanding of this project is in aiding the the Illinois benefit offices such as the IDHS and Illinois Department of Employment services and allow the government allocate resources where needed in Illinois. A better system will help with Illinois funded programs such as IDHS and IDES. Very popular topics of conversation due to the current economic environment caused by COVID-19. Creating this algorithm to better predict and invidiual's income will aid with processing applicants and giving them their benifits in a more timely manner.

## Data Gathering & understanding

Firstly, this Data was acquired from the American Community Survery via a csv. The the lastest CSV avaliable at this point in time is the 2018 American Community Survey. In utilizing the 2018 data the hope is to identify factors that will help provide better insight into the income an individual is cable of produciing given they live in Illinois. Utilizing this algorithim will allow for more accurate delivery on the SNAP and unemployment benifit type programs as well as quicker processing of the application to allow for a more rapid deployment of the benifits.

![](Reports/Figures/Income_plot.png)
The income values of the data were binned into:Poverty, Middle, and Upper classses based on this. The the classes were binned based on these follow income descriptions. Poverty class were individuals with income less than 48500 United Steates dollar(USD). Middleclass was individuals with income greater than 48500 but less than 145000 USD. Lastly, Upper Class was filled with people who has income greater than 145,500 USD.

Upon looking at his graph it is clear there is a lack of representation for the upper class which was expected, but it was not significant enough to require any sort of correction or manipulation of the data for this particular reason. For more information on the binning of the groups read this [study](https://www.investopedia.com/financial-edge/0912/which-income-class-are-you.aspx#:~:text=The%202018%20piece%20from%20Pew,a%20three%2Dperson%20household).

# Data Preparation

To being the data prepartion process for modeling we loaded in the csv_hil file. The next step is to filter out all of our missing values. To do this we removed all zero income values from out data set due to them not providing information on household income. The idea here is to try an use all the columns asisde from our target column to try and predicit income. We then went through out columns to find which one shared a strong pearson correlation coefficient with the target variable and took those witha .05 correlation value and higher into our filtered data fram. Any columns what had more thant 70,000 missing values were dropp from the data frame due to not want to adding to many artificial values to the data. Numeric features were analyzed by dropping there zero valued rows and running a histogram plot to see how the values were distributed. The numerical columns of choice were all right skewed so the median of the columns were used to impute missing values. When it came to our categorical columns the most common value of that column was used to fill in the missin values. Now having a filled data frame we can now move on to modeling.

## Modeling & Evaluation

When beginning the modeling process we took a filtered data set and put it thorugh the train_test_split module. The trainning split was then fed into the initial Linear regression mode. We then ran the score attribute of the model to see how it performed on the trainning data. I then did as cross validation score and adjusted R-sqaured function to assess the R-squared value more accurately. This process was then repeated however we scaled the features via Standard Scalar method as well as a MinMax Scalar. These different scalars were utilized to help provide some more standardization to the data and allow it to be accesed more concretely. The same over all process was conducted with a Neural network, Random forest Regressor and K-Nearest Neighbors regresor.

![](Reports/Figures/model_values.png)

From the above image we can see that the Linear Regresison model and the Random Forest regressor preform the best of the four algorithms used. From this I chose to move forward with the Random foresr model due to it performing slighlty better than the Linear regrression model as well as it is hase more hyperparamerters to tune.

## Final Results

After further iterations and hyperparameter tuning the final model selected is a Random Forest Regressor model with a R-squared score of .41.

![](Reports/Figures/modelavg_values.png)
From this graph we can see the model predicts average income fairly accurately with about a 70 USD discrepency.
![](Reports/Figures/model_predictions.png)
Now when looking at individual points and their predictions it has about a 30,000 USD discrepency. This is due to the model using all the data possible to predict income across the state. The problem with this that certain locations have different standards of living leading to less or more income within an area.

# Deployment

I would like to deploy this in a Dash or Flask setting. When this is deployed Illinois residents can check how much income they will be perceived to make given the parameters of the model. The app would then report to them the predicted income and the income class they are predicted to be in. Possibly show the client the R-squared of the model for confidence sake once I get the value higher.

# Next steps

Furture iteration of this project would be to acquire more recent census data and provide better insight into the income fluctiation through the years. I would also like to find a betting imputing method for the categorical and numerical featuets to potentially get more justifiable values. Lastly, I would like to create accurate models for each county so counties with over all lower income are help to reasonable standards support for this is found [here](https://en.wikipedia.org/wiki/List_of_Illinois_locations_by_per_capita_income).
