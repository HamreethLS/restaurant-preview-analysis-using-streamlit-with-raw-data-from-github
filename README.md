# restaurant preview analysis using streamlit with raw data from github
 
Restaurant Review Dashboard
This Streamlit application provides a dashboard for analyzing restaurant reviews. The application loads a dataset of restaurant reviews, cleans and processes the data, and provides interactive visualizations and filtering options to explore the data.

Features
Data Loading and Caching: The application loads review data from a CSV file hosted on GitHub and caches it for efficient performance.
Data Cleaning: The rating column is cleaned to extract numerical ratings, and the date column is converted to a datetime format to extract the month name.
Review and Follower Counts: The application extracts review and follower counts from the rev_count column.
Interactive Sidebar:
Text input for filtering reviews based on keywords.
Dropdown selection for filtering reviews by month.
Visualizations:
Bar chart displaying the top 5 restaurants based on average rating.
Bar chart displaying the top 5 restaurants based on total followers count.
Data Display: The filtered DataFrame of reviews is displayed below the visualizations.
Installation
To run this application, you need to have Python installed :
pip install -r requirements.txt
Usage
Clone this repository to your local machine.
Navigate to the directory containing the app.py file.
Run the application using Streamlit:

streamlit run app.py

This will launch the application in your default web browser.

Dataset
The application uses a dataset of restaurant reviews, which is loaded from a CSV file hosted on GitHub. The dataset includes the following columns:

rating: The rating given by the reviewer.
date: The date and time when the review was posted.
rev_count: A string containing the number of reviews and followers of the reviewer.
res_name: The name of the restaurant.
text: The text of the review.

License
This project is licensed under the MIT License.

This project was developed with dedication and care. We welcome feedback, suggestions, and contributions from the community to enhance its functionality and user experience.

Dataset Attribution
The tweet data used in this analysis is sourced from (https://github.com/skathirmani/datasets). We extend our gratitude to the providers of this valuable information.

Contact Information
For any queries, suggestions, or collaboration opportunities, please feel free to reach out:

Hamreeth L S
Email: hamreethls.bj@gmail.com
LinkedIn: www.linkedin.com/in/hamreeth-l-s-02471b293


Thank you for your interest in our Restaurant Preview Analysis Dashboard. We hope you find it insightful and useful!