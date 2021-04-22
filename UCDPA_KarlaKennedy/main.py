# ---------------------- Importing Data and Packages to Pycharm -------------
# Importing Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Importing Datasets & Printing Head to check correctly imported
df = pd.read_csv('summer_olympic_medals.csv')
print(df.head())
print(df.info())

my_dict = pd.read_csv('/Users/karlakennedy/Desktop/UCD_PAKarlaKennedy/dictionary.csv')
print(my_dict.head())
print(my_dict.info())

# ---------------------- Analyzing Data ----------------------------

# Cleaning Data & Checking for Null Values
print(df.isnull().any()) #Report Shows null value present in Country
print(my_dict.isnull().any()) #Report shows null value present in Population and GDP_per_Capita

# Drop rows where all data is the same
df = df.drop_duplicates()
my_dict =my_dict.drop_duplicates()

# Recheck the info of each
print(df.isnull().any())
print(my_dict.isnull().any())

# Cleaning Data by Grouping by Year then City
olympic_cities = df.groupby("Year").City.first()
print('Olympic Host Cities by Year ')
print(olympic_cities)

# Grouping by Gender
df['Gender_Code'] = pd.factorize(df.Gender)[0]
print(df.head())
print("Olympic Men and Women Medalists: ")
print(df.Gender.value_counts())
print(df.Gender_Code.value_counts())

# Joining/Merging DataFrames
result = pd.merge(df, my_dict, on='Country',  how='outer')
print('DataFrames Joined Head: ')
print(result.head())

# Indexing
twentieth_century_countries =  ["United States", "United Kingdom", "Sweeden", "Belgium", "France", "Netherlands",
                                "United States (2)", "Germany", "United Kingdom (2)", "Finland", "Australia", "Italy",
                                "Japan", "Mexico", "Germany (2)", "Canada", "Russia", "United States (3)",
                                "South Korea", "Spain", "United States (4)", "Australia (2)"]
twentieth_century_cities = ["St Louis", "London", "Stockholm", "Antwerp", "Paris", "Amsterdam", "Los Angeles",
                            "Berlin", "London", "Helsinki", "Melbourne", "Rome", "Tokyo", "Mexico", "Munich",
                            "Montreal", "Moscow", "Los Angeles (2)", "Seoul", "Barcelona", "Atlanta", "Sydney"]
ind_south_korea = twentieth_century_countries.index("South Korea")
print("South Korea Index Example: ", twentieth_century_cities[ind_south_korea])


# Slicing
olympic_cycle = [2000, 2004, 2008, 2012, 2016, 2021]
backward_olympic_cycle = olympic_cycle[::-1]
print("Reverse Chronological Olympic Cycles: ", backward_olympic_cycle)

# Sorting Data
olympic_cycle.sort(reverse = True)
print("Olympics (in descending): ", olympic_cycle)

# Sorting Data
mean_capita = np.mean(result["GDP_per_Capita"])
print("Mean GDP = ", mean_capita)

# Using loc or iloc
irish_medalist = result.loc[result['Country'] == 'IRL', ['Year', 'Athlete', "Medal"]]
print("Ireland Olympic Medalists: ")
print(irish_medalist)

# Looping -  Giving Countries an index number.
for Year, data in my_dict.items():
	print("Country:", Year, "\nCountry:", data)

#For Loop
olympic_cycle = [2000, 2004, 2008, 2012, 2016, 2021]
for year in olympic_cycle:
    print(year)
    if year == 2000 :
        print("Sydney Olympic Games")
    if year == 2004 :
        print("Athens Olympic Games")
    if year == 2008 :
        print("Beijing Olympic Games")
    if year == 2012 :
        print("London Olympic Games")
    if year == 2016 :
        print("Rio de Janeiro Olympic Games")
    if year == 2021 :
        print("Tokyo Olympic Games - will it go ahead this summer?")


# Itterrows
for i, row in my_dict.iterrows():
    print(i, row[0], row[1], row[3])

# Counting Medals by Gold, Silver, Bronze
labels = 'Gold', 'Silver', 'Bronze'
sizes = [10486, 10310, 10369]
df['Medal_Won'] = pd.factorize(df.Medal)[0]
print(df.head())
print(df.Medal.value_counts())
print(df.Medal_Won.value_counts())

# Top 10 Athletes
top_olympian = result.Athlete.value_counts().head(10)
print("Top 10 Olympians: ")
print(top_olympian)

# ------------------------------------- Python ------------------------

# Listing - Top 10 Teams for Medals
top_medal = result.Country.value_counts()
top_summer = top_medal.reset_index()
top_summer = top_summer.rename(columns={"index" : "Team"})
top_s = list(top_summer.Team.head(10))
print("Top 10 Countries Listed: ", top_s)

# Using Numpy to get the Total Population
total_population = my_dict["Population"].sum()
print("Total Population: ", total_population)

# Creating a dictionary of Olympic Cities
cities_dict = { 'Athens (1st)':1896, 'Paris':1900, 'St Louis':1904, 'London (1st)':1908, 'Stockholm':1912,
                'Antwerp':1920, 'Los Angeles (1st)':1932, 'Berlin':1936, 'London (2nd)':1948, 'Helsinki':1952,
                'Melbourne / Stockholm':1956, 'Rome':1960, 'Tokyo':1964, 'Mexico':1968, 'Munich':1972,
                'Montreal':1976, 'Moscow':1980, 'Los Angeles (2nd)':1984, 'Seoul':1988, 'Barcelona':1992,
                'Atlanta':1996, 'Sydney':2000, 'Athens (2nd)':2004, 'Beijing':2008, 'London (3rd)':2012 }
print('City Dictionary: ', cities_dict)
print('Year of Berlin Olympics: ', cities_dict['Berlin'])
cities_dict['Rio de Janeiro'] = 2016
print('City Dictionary (2016 added): ', cities_dict)

# Custom Function for Reusable Code
population = my_dict["Population"]
gdp_per_capita = my_dict["GDP_per_Capita"]
def real_gdp(population, gdp_per_capita):
    print('The real GPD is:', population, gdp_per_capita)
    return gdp_per_capita/population

# Custom Function Attempt Two - round() function
my_dict['GDP_rounded'] = my_dict['GDP_per_Capita'].round()
print(my_dict.head())

# Correlation between GDP and Medals Won
total_country_medals = result.groupby(['Country'])['Medal'].count().reset_index()
print("Total Country Medals")
print(type(total_country_medals))
print(total_country_medals)

print(my_dict.head())
medal_gdp = pd.merge(my_dict, total_country_medals, on='Country',  how='outer')
print('Medal/GDP Joined Head: ')
print(medal_gdp.head())
# ------------------------------------ Visualisations -------------------------

# Visualising Olympic Athletes % by Gender
label= 'Men', 'Women'
size = [22746, 8419]
my_colors = 'lightblue', 'pink'
fig1, ax1 = plt.subplots()
my_explode = (0, 0.1)
ax1.pie(size, labels=label, autopct='%1.1f%%', shadow=True, startangle=15, colors=my_colors, explode=my_explode)
plt.title('Summer Olympic Medallists by Gender')
ax1.axis('equal')
plt.show()

# Medals Won and GDP per Capita
sns.set_theme(style="whitegrid")
plt.title('Medals Won & GDP per Capita')
color = sns.color_palette(["#3498db", "#e74c3c"])
ax = sns.barplot(x="Medal", y="GDP_per_Capita", hue='Gender', data=result,
                 order=['Gold', 'Silver', 'Bronze'], palette=color)
plt.show()

# Top 10 Countries with Most Medals
df.Country.value_counts().head(10).plot(kind="bar",
                                        color=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r']);
plt.ylabel("Number of Medals Won")
plt.title("Top 10 Countries for Olympic Medals")
plt.xlabel("Country")
plt.show()

# Country Medals broken down to Gold, Silver, Bronze
medal_top=result[["Year", "Country", "Medal"]]
medal_top.groupby(["Country", "Medal"]).Year.count().reset_index().pivot("Country", "Medal", "Year").\
    fillna(0).sort_values("Gold", ascending=False).head(10).plot(kind="bar",
                                                                 color=['brown', 'gold', 'grey']);
plt.title('Medals Won per Country')
plt.xlabel("Country")
plt.ylabel("Number of Medals Won")
plt.show()

# Number of Male & Female Athletes Compared at each games
color = sns.color_palette(["#3498db", "#e74c3c"])
result.groupby(["Year", "Gender"]).Medal.count().reset_index().pivot("Year", "Gender", "Medal").fillna(0).plot\
    (color=color);
ax=plt.gcf()
ax.set_size_inches(8, 6)
plt.grid(b=None)
plt.title('Linegraph of Gender Winning Olympic Medals over Time')
plt.show()

# Participation in different Sports (Top 30)
matplotlib_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'r', 'b', 'g']
df.Discipline.value_counts().head(30).plot(kind="bar", color=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g'])
ax=plt.gcf()
ax.set_size_inches(13, 7)
plt.xlabel("Sport")
plt.ylabel("Participation Number")
plt.title('Top 30 Summer Olympic Sports by Participation')
plt.tight_layout()
plt.show()

# Medals Won by Country by Year
test1 = result.groupby(['Country', 'Year'])['Medal'].count().reset_index()
test1 = test1[test1['Country'].isin(result['Country'].value_counts()[:10].index)]
test1 = test1.pivot('Year', 'Country', 'Medal')
test1.plot()
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.grid(b=None)
plt.xlabel("Year")
plt.ylabel('Number of Medals Won')
plt.title('Medals Won by Country over Time')
plt.show()

# Visualising the correlation between GDP and Medals Won
fig, scatter = plt.subplots(figsize=(10, 6), dpi=100)
scatter = sns.scatterplot(x="GDP_rounded", y="Medal", hue="Country", size="Medal", legend=False, data=medal_gdp)
plt.title('Correlation between GDP and Medals Won by Country')
fig.set_size_inches(10, 8)
plt.show()

# Second Attempt at GDP and Medals
sns.set_theme(style="white")
g = sns.relplot(x="GDP_rounded", y="Medal", hue="Country", size="Medal",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=medal_gdp)
plt.title('Correlation between GDP and Medals Won by Country')
plt.show()
