import pandas as pd
import matplotlib.pyplot as plt

#Load the Spreadsheet
df = pd.read_csv('bestsellers.csv')

#Explore the Data
# Get the first 5 rows of the spreadsheet
print(df.head())
# Get the shape of the spreadsheet
print(df.shape)
# Get the column names of the spreadsheet
print(df.columns)
# Get summary statistics for each column
print(df.describe())
#Clean the Data
df.drop_duplicates(inplace=True)
#Renaming Columns
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#Converting Data Types
df["Price"] = df["Price"].astype(float)

#Analysis
author_counts = df['Author'].value_counts()
print(author_counts)
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)
print("Top Author:", author_counts.index[0])
print("Highest Rated Genre:", avg_rating_by_genre.idxmax())

# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")
# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
##visualizations

# Top 10 authors bar chart
author_counts.head(10).plot(kind='bar', title='Top 10 Authors by Number of Bestsellers')
plt.xlabel('Author')
plt.ylabel('Number of Books')
plt.tight_layout()
plt.show()

# Average rating by genre
avg_rating_by_genre.plot(kind='bar', color='skyblue', title='Average Rating by Genre')
plt.ylabel('Average Rating')
plt.tight_layout()
plt.show()
avg_rating_by_year = df.groupby("Publication Year")["Rating"].mean()
avg_rating_by_year.plot(kind='line', marker='o', title='Average Rating Over Time')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.show()

