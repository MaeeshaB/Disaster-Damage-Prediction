# Minimizing Severity of Natural Disasters in Business Expansion 

### How can we use historical meteorological information and economic conditions to decide where to expand a business in the United States?

## Table of Contents

- [Motivation and Goal](#motivation-and-goal)
- [Data Sources](#data-sources)
- [Requirements](#requirements)
- [Repository Structure](#repository-structure)
- [Results](#results)
- [Contributors](#contributors)

## Motivation and Goal

Natural disasters have increased by 500% in the last 50 years [[World Meteorological Organization](https://public.wmo.int/en/about-us), [World Bank Blogs](https://blogs.worldbank.org/latinamerica/so-called-natural-disasters-are-not-unpredictable)]. Improving disaster preparation is crucial by predicting risks and severity, represented by the financial cost, to minimize costs for business expansion.

The goal of this project was to create a model that predicts the cost of a natural disaster in the United States of America given a specific state, which can then be used to determine the optimal number of branches a theoretical business would open in each state in order to minimize economic loss. 

## Data Sources

Both economic and meteorological data from 1980 to 2021 was explored as they are key factors that impact the cost of a natural disaster. Meteorological features were provided by the [National Oceanic and Atmospheric Administration ’s National Centers for Environmental Information](https://www.ncdc.noaa.gov/cag/) and the features selected were:
- minimum temperature
- maximum temperature
- average temperature
- precipitation 
- average elevation 

The economy-related features were adjusted for inflation and include: 
- the cost of disaster (by type)
- unemployment rate
- population
- land area
- gross domestic product 
- inflation rate
- personal income

Economic data points were found through a subsidiary organization of the [Urban-Brookings Tax Policy Center](https://apps.urban.org/features/state-economic-monitor/) and weather-related disaster costs were found through the [National Centres for Environmental Informtion](https://www.ncei.noaa.gov/access/billions/).

## Requirements

- Python 3.x
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- CVXPY

## Repository Structure


```
Storm-Damage-Prediction/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── src/
│   ├── data_preparation/
│   ├── feature_engineering/
│   ├── modeling/
│   └── evaluation/
├── models/
├── notebooks/
├── results/
├── utils/
└── README.md
```

## Methods

After testing multiple regression models including linear, lasso, and ridge regression both with and without cross validation, the optimal model was found to be a random forest regression model. The model uses a 90/10 train test split and the optimal parameters were determined through cross validated grid search. This results in a Mean Absolute Percentage Error of 86.57%,  R2 score of 0.556 on the training set and a test score of 0.309. Across all state predictions, the average cost of a natural disaster will be $681 million. As the model score does not allow us to confidently use the cost predictions, the team must add additional features, which can be benchmarked from existing literature, or data points to increase performance. When attempting to increase performance, it was noted that increasing the train/test split increased model performance without appearing to overfit the data, however there is a tradeoff of decreasing available testing data. Once the prediction model performance has been improved, the team can move to implement the expected cost in a cost-minimization model that can help determine the number of branches to be opened in a specific state. 


## Results

(Present a summary of the results and any relevant visualizations. This can be updated as the project progresses.)

## Contributors

- [Maeesha Biswas](https://maeeshabiswas.com)
- [Dalya Mirlas](https://www.linkedin.com/in/dalya-mirlas/?originalSubdomain=ca)
- [Magdalene Choy](https://www.linkedin.com/in/magdalenechoy/?originalSubdomain=ca)
- [Michael Simunec](https://www.linkedin.com/in/michael-simunec-65105421b/)
