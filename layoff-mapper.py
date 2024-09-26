# importing necessary modules
import io
import sys
import csv

from IPython.utils.sysinfo import encoding

# Defining the mapper function to filter data by date
def mapper_filterByDate(input_file):
  # Creating a CSV reader from the input file
  reader = csv.reader(io.StringIO(input_file))
  # Itirating through each line in the CSV file
  for line in reader:
    # Checking if the line has at least 4 elements
    if len(line) >3 :
      # Extracting industry, date, and layoff_count from the line
      industry = line[2]
      date = str(line[4])
      layoff_count = line[10]

    # Check if the date contains "2023"
      if "2023" in date:
    # Print the company name, date, and layoff count separated by a tab
        print(f"{industry}\t{date}\t{layoff_count}")
  
# Entry point of the program
if __name__ == '__main__':
  # Setting up input stream from standard input
  input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
  # Itirating through each line in the input stream
  for line in input_stream:
    # Calling the mapper function for each line
    mapper_filterByDate(line)