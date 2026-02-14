# Student Performance Analysis Using Python
![](aiimage.PNG)

## Project Overview:
There are several factors which effect overall performance of students curriculum .This project aims to analyse effect of various such factors like Hours Studied,Sleep Hours,Question Papers Practiced etc. Comparing these factors with overall performance index of students in dataset Student_Performance.

## Problem Statement:
Q1: How does Hours Studied relate to Performance Index?
Q2: Will more Sleep Hours effects Performance Index in positive manner?
Q3: Solving how many Sample Question Papers are optimal for good Performance?
Q4: Is there any relations between Extracurricular Activites and Performance Index?

## Dataset Information:

RangeIndex: 10000 entries, 0 to 9999
Data columns (total 6 columns):

 -   Column                            Non-Null Count  Dtype  
---  ------                            --------------  -----  
 0   Hours Studied                     10000 non-null  int64  
 1   Previous Scores                   10000 non-null  int64  
 2   Extracurricular Activities        10000 non-null  object 
 3   Sleep Hours                       10000 non-null  int64  
 4   Sample Question Papers Practiced  10000 non-null  int64  
 5   Performance Index                 10000 non-null  float64

dtypes: float64(1), int64(4), object(1)

## Key Insights :
- Study hours show a strong positive association with performance.
- Sleep hours show improvement within observed range.
- Extracurricular participation correlates with slightly higher averages.

## Visualizations :
- Histogram / distribution
- Bar comparison
- line comparison
- scatter plot
- Correlation heatmap

## Tools & Tech Stack :
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Conclusion :
In raw data analysis higher the Sleep Hours,Hours Studied and participate in Extra Curricular Activites chance for getting good Performance Index is high.In aggregate analysis as Sleep Hours,Hours Studied goes higher and participate in Extra Curricular Activites average Performance increases steadily.