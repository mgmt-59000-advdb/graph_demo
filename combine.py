import pandas as pd

# Define the file names and corresponding course names
files_courses = {
    'advdb_roster.csv': 'advdb',
    'cloud_roster.csv': 'cloud',
    'devops_roster.csv': 'devops'
}

# Initialize an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

# Iterate over each file and course
for file, course in files_courses.items():
    # Read the CSV file into a DataFrame, ignoring the OrgDefinedId column
    df = pd.read_csv(file, usecols=['Last Name', 'First Name', 'Email'])
    
    # Add a new column for the course name
    df['Course'] = course
    
    # Append the DataFrame to the merged DataFrame
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_roster.csv', index=False)

print("The CSV files have been successfully merged into 'merged_roster.csv'.")