import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv", sep=",", decimal=",")
    # print(df.head(15))
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    # print(race_count)

    # What is the average age of men?
    average_age_men = (df.loc[df['sex'] == "Male", "age"].mean()).round(decimals=1)
    # print(average_age_men)
    

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (((df['education'] == 'Bachelors').sum()) / (df['education'].value_counts().sum())*100).round(decimals=1)
    # print((percentage_bachelors).round(decimals=1) * 100)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    degrees = ['Bachelors', 'Masters', 'Doctorate']
    educationDf = df['education']
    degreesMask = educationDf.isin(degrees)
    higher_education = round(df['education'].value_counts(normalize=True)[['Bachelors', 'Masters', 'Doctorate']].sum() * 100, 1)
    lower_education = df['education'].value_counts(normalize=True)[['Bachelors', 'Masters', 'Doctorate']].sum()

    # percentage with salary >50K
    salaryDf = df['salary']
    salaryMask = df['salary'] == '>50K'
    salaryDfCount = salaryMask.value_counts()
    higher_education_rich = round(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'].value_counts(normalize=True)['>50K'] * 100, 1)
    lower_education_rich = round(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['salary'].value_counts(normalize=True)['>50K'] * 100, 1)
    # print(lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    # print(min_work_hours.min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    rich_percentage = round(df[df['hours-per-week'] == 1]['salary'].value_counts(normalize=True)['>50K'] * 100, 1)
    # print(rich_percentage)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df.groupby('native-country')['salary'].value_counts(normalize=True).loc[:, ('>50K')].idxmax()
    highest_earning_country_percentage =  round(df.groupby('native-country')['salary'].value_counts(normalize=True).loc[:, ('>50K')].max() * 100, 1)
    # print(highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    country_mask = (df['native-country'] == "India")
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
