# Data Scraping and Analysis Project  

## Project Description  

This project involves scraping job vacancy data from a website, analyzing it, and visualizing various aspects  
such as salary distributions, experience requirements, and skill frequencies. The aim is to gain insights  
into the job market trends and requirements for Python-related roles.  


## To run this project, follow these steps to set up your environment:  

1. Clone the repository:
   ```bash
   git clone https://github.com/Irina17191/Scraping-DataAnalysis-project/tree/develop  
   cd Scraping-DataAnalysis-project  
   ```

2. Create a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Macos
   venv\Scripts\activate  # On Windows
   ```

3. Install the required packages:
    ```bash
   pip install -r requirements.txt
   ```

4. Download the Data:

Make sure you have access to the website from which data is being scraped  
or have the data available locally.


## Usage


1. Run the Scraping Script   
This script will scrape job vacancy data and save it to vacancies.csv.  
    ```bash
   python scraper/scraper.py
   ```

2. Run the Analysis Script:
This script will load the vacancies.csv file, 
perform data cleaning and analysis, and generate visualizations.
    ```bash
   cd data_analysis
   jupyter notebook
   ```
Open main.ipynb from the Jupyter interface and run the cells.  



## Examples:  
# Frequency of Skills in Job Vacancies  

![Application Screenshot]("preview_diagrams/1Frequency of Skills in Job Vacancies.png") 

# Experience Years vs Salary

![Application Screenshot](preview_diagrams/2Experience Years vs Salary.png)

# Experience Years vs Salary with Linear Regression

![Application Screenshot](preview_diagrams/3Experience Years vs Salary with Linear Regression.png)

# Experience Years vs Salary with Polynomial Regression

![Application Screenshot](preview_diagrams/4Experience Years vs Salary with Polynomial Regression.png)

# Heatmap of Skill Frequencies

![Application Screenshot](preview_diagrams/5Heatmap of Skill Frequencies.png)

# Salary Distribution by English Level

![Application Screenshot](preview_diagrams/6Salary Distribution by English Level.png)

# Correlation Matrix

![Application Screenshot](preview_diagrams/7Correlation Matrix.png)

