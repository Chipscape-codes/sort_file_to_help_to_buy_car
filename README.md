Used Car Filtering Tool
This Python script helps users filter and analyze used car listings based on location and price range. It allows buyers to identify the best car options from a dataset using basic criteria like price and kilometers driven.

Features
Filter cars by city and price range

View cars within your specified budget

Identify:

Car with lowest price

Car with highest price

Car with lowest kilometers driven

Car with highest kilometers driven

View complete specifications of the top-matching cars

Requirements
Python 3.x

pandas

Install the required package:

bash
Copy
Edit
pip install pandas
Usage
Make sure the file used_cars_data.csv is in the same directory.

Run the script:

bash
Copy
Edit
python sort_to_help_buy_car.py
Input:

City name (e.g., chennai)

Maximum price limit (e.g., 600000)

Minimum price threshold to filter cheap listings (e.g., 100000)

The program will display filtered results and key insights.

Input File Format
The CSV file should contain the following columns:

Name

Price

Kilometers_Driven

Location

Ensure numeric fields like Price and Kilometers_Driven are clean and valid.

Output
A filtered table of matching cars

Details of:

Cheapest car

Costliest car

Least-driven car

Most-driven car

Full specs of the top-matching cars
