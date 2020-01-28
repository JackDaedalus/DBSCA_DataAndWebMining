##

## B8IT108 Data and Web Mining -  Machine Learning Workflow Program

## February 2020 

## Ciaran Finnegan - Student No. 10524150
## Dermot Madsen   - Student No. 10522567




## Main Python Program

##



## Module Imports for Machine Learning in Python
 
# Python version
import sys

import scipy
import numpy
import matplotlib
import pandas
import sklearn


# Load libraries

from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


## Module Imports for Python GUI widgets
from WineQuality_GUI import *

## Module Imports for custom Python code to read and analyse dataset
from WineQuality_LoadandAnalyseData import *

## Module Imports for custom Python code to pre-process dataset before modelling
#from WineQuality_DataPreProcessing import *

### Module Imports for custom Python code to evaluate and compare modelling algorithms
#from WineQuality_AlgorithmEvaluationAndComparison import *

### Module Imports for custom Python code to evaluate and compare modelling algorithms
#from WineQuality_PredictiveModelResults import *



def Main_WineML():


    # Set up file identifier for use in Console Print statements and graphical output
    sDatasetDescription = "Vinho Verde Red Wine Quality"
    sFilename = "winequality-red.csv"
    #sDatasetDescription = GetDatasetDescription()

    # Read CSV file and return dataset
    df_WineQuality, dfColNames, sDSClassCol = ReadDataframe(sFilename)

    # Display basic initial statistics about dataset
    # This data will be used to inform follow up data cleansing actions
    DisplayBasicDataFrameInfo(df_WineQuality, sDatasetDescription, sDSClassCol)

    # Display visual representations of the dataset attributes
    # These representations will also help with decisions on pre-modellling
    # data manipulation and algorithm selection / execution
    # DisplayVisualDataFrameInfo(df_Iris, sDatasetDescription)

    # Amend the Dataset so that modelling algorithms can be successfully applied
    #df_FinalWineQuality = PreSplitDataManipulation(df_WineQuality, sDatasetDescription, dfColNames, sDSClassCol)

    ## Divide dataset into label and feature sets (feature set is standardised)
    #X_Scaled, Y = CreateLableAndFeatureSet(df_FinalWineQuality, sDatasetDescription, sDSClassCol)

    ## Split dataset into training and test data
    #X_train, X_test, Y_train, Y_test= CreateTrainingAndTestData(X_Scaled, Y, sDatasetDescription)

    ## Evaluate different algorithm models
    #EvaluateAndCompareAlgorithms(X_train, Y_train, sDatasetDescription)

    ## Evaluate Predictive models againist test data
    #EvaluateAndPredictiveModel(X_train, Y_train, X_test, Y_test, sDatasetDescription)




Main_WineML()
