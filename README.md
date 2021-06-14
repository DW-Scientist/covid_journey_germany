# covid_journey_germany

## Welcome to an Analysis of the Corona Journey in Germany

This repository prepares all the analysis for a written article on Medium. You can find it by using the following link:

--> Link

## Motivation
As you can read up tones of articles every day about numbers and figures of Corona, I decided to build my own picture of the situation in my Home Country Germany. Within the article I mapped my numeric result with public sources from the internet. The whole analysis gave me a better overview abouthe Journey of Corona in Germany. I would love to read stories about your countries as well :).  

## This repo contains the following elements

1. **A data directory:**
This directory is currently empty since the data I used is a bit to big for uploading. 
You can find the data on Kaggle using the following link: 
https://www.kaggle.com/headsortails/covid19-tracking-germany?select=covid_de_vaccines.csv

You can download this as a zip file. Basically you will have 3 different files:
  - covid_de.csv
  - covid_de_vaccines.csv
  - data/demographics_de.csv

Within the data directory is a file named `read_data.py`. You can use those lines of code to try if you can read the data.

2. **A Jupyter Notebook**

Within this Notebook I did all the analysis I used for the medium article. Since this follows the same structure as the article it will answer you the following questions:
  - Which were the worst times for Germany during Corona?
  - How did the virus hit Germany in total?
  - How is vaccination progressing in Germany?
  - Which vaccines are preferred in Germany?
  - How many cases will we have at the end of July?

Please make sure you install all the elements from element 4 `requirements.txt`. You need this to make the `plotly`charts visible.

3. **A pics directory**
This directory just contains the pictures which I extracted from the Jupyter Notebook to put them into the medium article.

4. **A `requirements.txt` file**
This file contains all the packages you need to run this Notebook on your local machine.
Just use the following `pip` to install the packages in you virtual in environment: `pip install -r requirements.txt`

## Key Findings of those German Corona Analysis
- Winter 2020 and March/April 2021 hit Germany the most
- 4.4 % of the population have been infected until today
- Moderna gets number 2 in Germany since Astrazeneca got influenced by bad news about side effects
- Due to an Regressor Estimation the rate of infected people could climb up to 4.6% until the end of July 2021

## I really hope you like the article and just send me any feedback you have
Have fun reading and exploring yourself :)!!!

