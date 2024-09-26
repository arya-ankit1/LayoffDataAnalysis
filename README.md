# Layoff Data Analysis using Hadoop MapReduce

### Project Overview
This project aims to analyze industry layoffs using a distributed analytical technique with Hadoop MapReduce and HDFS. The analysis focuses on identifying layoff trends across different industries in 2023. Python programming language is utilized for the implementation of the map and reduce programs.

## Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Implementation](#implementation)
- [Results](#results)
- [Usage](#usage)
- [Critical Reflection](#critical-reflection)
- [Contributing](#contributing)

### Introduction
In today's data-driven world, large-scale data processing is crucial for extracting meaningful insights. This project utilizes Hadoop MapReduce to analyze layoff data, providing insights into industry-specific layoff trends in 2023.

### Problem Statement
The project aims to analyze layoffs across different industries in 2023. Understanding the layoff patterns helps stakeholders identify economic trends, market demands, and workforce dynamics.

### Dataset
The dataset is sourced from Layoff.csv, which contains layoff information for major companies from 2020 to 2024. The dataset includes variables such as company name, location, industry, percentage of layoffs, date, funding raised, and others.

### Project Structure
LayoffDataAnalysis

- layoff-reducer.py              # Reducer code for the MapReduce job
- layoff-mapper.py               # Mapper code for the MapReduce job
- layoffs_data.csv               # Input dataset
- README.md                      # Project description and usage guide
- HPCI_ReportFinal.pdf           # Project report explaining the methodology and results

### Installation and Setup
#### Requirements
- Python 3.x
- Hadoop installed and configured (or use Google Colab)
- Brunel Remote Access Services (VPN) for implementation (if using Brunel server)

### Steps to Set Up the Environment
1. Clone the Repository:
- git clone https://github.com/arya-ankit1/LayoffDataAnalysis.git
2. Upload the Files to the Hadoop Distributed File System (HDFS):
- Use the hadoop fs -copyFromLocal command to upload layoffs_data.csv, layoff-mapper.py, and layoff-reducer.py to HDFS.
3. Running on Google Colab (Optional):
- Open Google Colab and set up the Hadoop environment.
- Upload the necessary files (layoffs_data.csv, layoff-mapper.py, layoff-reducer.py) to the Colab environment.

### Implementation
#### 1.Map Phase:
- The mapper script (layoff-mapper.py) processes the dataset, extracting relevant fields like industry and date to shuffle and sort records for the year 2023.
#### 2.Reduce Phase:
- The reducer script (layoff-reducer.py) receives the key-value pairs from the mapper and calculates the total layoffs for each industry.

### Results
- The analysis identifies key layoff trends in consumer sectors, finance, healthcare, IT, and others for 2023.
- The results provide insights into economic conditions, workforce dynamics, and industry health.

### Usage
#### 1. Running the MapReduce Job on Hadoop:
hadoop jar /path/to/hadoop-streaming.jar \
-input /path/to/input/layoffs_data.csv \
-mapper layoff-mapper.py \
-reducer layoff-reducer.py \
-output /path/to/output/directory

#### 2. Retrieve the Results:
Copy the output from HDFS to your local system using:
hadoop fs -copyToLocal /path/to/output /local/destination

### Critical Reflection
The project demonstrates the power of Hadoop MapReduce for large-scale data analysis. Although the setup and implementation can be complex, especially for beginners, the framework's ability to process big data makes it a valuable tool for analyzing workforce trends.

### Contributing
If you want to contribute to this project, please fork the repository and submit a pull request with your changes.
