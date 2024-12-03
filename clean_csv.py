import csv

input_file = 'merged_roster.csv'
output_file = 'cleaned_merged_roster.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        cleaned_row = []
        for field in row:
            # Remove any extra characters after the closing quote
            if field.startswith('"') and field.endswith('"') and len(field) > 2:
                field = field.strip('"')
            cleaned_row.append(field)
        writer.writerow(cleaned_row)

print(f"The cleaned CSV file has been saved as '{output_file}'.")