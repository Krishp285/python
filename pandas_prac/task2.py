import pandas as pd

movies = pd.read_csv("pandas_prac\movies.csv")

movies.drop(columns= "Unnamed: 0" ,inplace=True)
directors=pd.read_csv("pandas_prac\directors.csv")
directors.drop(columns= "Unnamed: 0" ,inplace=True)


# print(movies.head())
# print(directors.head())

df =movies.merge(directors,left_on="director_id",right_on="id")
df.rename(columns={"id_x":"movie_id"},inplace=True)
df.drop(columns=["id_y"],inplace=True)

# print(df.head())


# task  :1 vote_average >7   ==> select * from movies where vote_average >7
# task  :2 select title , revenue , director_name from movies where vote_average >7 . 
# task :3 Get me the movies which were released in or after 2015 and having vote_average more than 7
"""vote_avg_greater = df.loc[df["vote_average"]>7]
print(vote_avg_greater.head(50))"""

vote = df.loc[df["vote_average"]>7,["title","revenue","director_name"]]
print(vote.head(20))

print("***********************")
movie_2015 = df.loc[(df["year"]>=2015) & (df["vote_average"]>7)] 
print(movie_2015.head(20))

# 1.Top 10 popular movies
print(df.sort_values(by="popularity",ascending=False).head(10))
# 2.Highest rated (vote_average) movies
print(df.sort_values(by="vote_average",ascending=False).head(10))
# 3.Number of movies released in a year
print(df.groupby("year").size())
# 4.Movie with the highest budget in a year
print(df.groupby("year")["budget"].max())
# 5.Most popular director
print(df.groupby("director_name")["popularity"].mean().sort_values(ascending=False).head(10))
# 6.Director producing high budget movies
print(df.groupby("director_name")["budget"].mean().sort_values(ascending=False).head(10))
# 7.Highest & lowest budget movies every month
print(df.groupby("month")["budget"].max())
print(df.groupby("month")["budget"].min())
# 8.Directors who did not directed any movie
print("--------------------------------------------")
print(directors[~directors["id"].isin(df["director_id"])]["director_name"])
# 9.Top 10 most profitable movies
print(df.assign(profit=df["revenue"]-df["budget"]).sort_values(by="profit",ascending=False).head(10))
# 10.Print the titles of the movies directed by Christopher Nolan. Also print their count
print(df[df["director_name"]=="Christopher Nolan"]["title"])
print(df[df["director_name"]=="Christopher Nolan"].shape[0])
# Print number of movies directed by each director
print(df.groupby("director_name").size())

# find total budget of movies released each year , show only year where total budget > 500 million
print(df.groupby("year")["budget"].sum().reset_index().loc[lambda x: x["budget"] > 500_000_000])

print("***********************")
# find numbers of movies released each month .show only months with more than 5 movies
print(df.groupby("month").size().reset_index(name="movie_count").loc[lambda x: x["movie_count"] > 5])   


# find number of movies directed by each director and show only directors with more than 2 movies
print(df.groupby("director_name").size().reset_index(name="movie_count").loc[lambda x: x["movie_count"] > 2])   

# find average budget of movies directed by each director and show only directors with average budget more than 150 million
print(df.groupby("director_name")["budget"].mean().reset_index().loc[lambda x: x["budget"] > 150_000_000])