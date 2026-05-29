import pandas as pd

import random

from mapping import *

df=pd.read_csv("../data/cleaned movies.csv")

def get_age_group(age) :

    if age < 18 :
        return "teen"
    elif age <=30 :
        return "young_adult"
    elif age <=50 :
        return "adult"
    return "senior"

def get_movie_era(Year) :

    if Year < 1980 :
        return "before_1980"
    elif Year < 1990 :
        return "1980_1990"
    elif Year < 2000 :
        return "1990_2000"
    return "after_2000"

def recommend(region,weather,age) :

    recommendations = []

    age_group = get_age_group(age)

    for _, movie in df.iterrows():

        score=0

        movie_era = get_movie_era(movie["Year"])

        # region score

        if movie["Language"] in region_map[region] :
            score += 5
        
        # weather score

        for w in weather_map[weather] :
            if w in movie["Genre"] :
                score += 5
                break

        # age score

        for g in age_map[age_group] :
            if g in movie["Genre"] :
                score +=5
                break
        
        # movie era score

        score += movie_era_map[age_group][movie_era]

        if (score > 0) :

            recommendations.append(
                {
                "name"     : movie["Movie Name"],
                "language" : movie["Language"],
                "genre"    : movie["Genre"],
                "year"     : movie["Year"],
                "rating"   : movie["Rating(10)"],
                "score"    : score/20,
                }
            )
            
    random.shuffle(recommendations)  

    recommendations = sorted(recommendations , key = lambda x:x["score"] , reverse=True)
        
    return recommendations[:10]

result = recommend("kerala","rainy",26)

for movie in result:

    print(movie)
