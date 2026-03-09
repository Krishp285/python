
print(df.assign(profit=df["revenue"]-df["budget"]).sort_values(by="profit",ascending=False).head(10))
# 10.Print the titles of the movies directed by Christopher Nolan. Also print their count
print(df[df["director_name"]=="Christopher Nolan"]["title"])
print(df[df["director_name"]=="Christopher Nolan"].shape[0])
# Print number of movies directed by each director
print(df.groupby("director_name").size())


# find total budget of movies released each year , show only year where total budget > 500 million
print(df.groupby("year")["budget"].sum().loc[lambda x: x > 500_000_000])