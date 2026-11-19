# Social Media Engagement \& Content Performance Dashboard



An interactive data analysis and visualization project that explores social media post engagement across Instagram, YouTube, Facebook, LinkedIn, and X.

The project uses Python for data handling and analysis, Matplotlib for a correlation heatmap, and Plotly for an interactive dashboard.



## Project Highlights

* Creates a dataset of 50 social media posts.
* Examines likes, shares, comments, platforms, and post dates.
* Displays dataset shape, information, and descriptive statistics.
* Calculates a correlation matrix for likes, shares, and comments.
* Summarizes average engagement and post counts by platform.
* Builds an interactive four-chart dashboard:

  * Likes vs. comments scatter plot
  * Average likes by platform bar chart
  * Likes distribution histogram
  * Likes over time line chart
* Includes hover details to inspect individual data points.
* 

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Plotly
* Jupyter/IPython display utilities

## Repository Structure

```text
social-media-engagement-dashboard/
│
├── dashboard\_project.py
│   
├── dashboard/
│   └── social\\\_media\\\_engagement\\\_dashboard.html

|
├── screenshots.png

|
├── requirements.txt
|
└── README.md
```

## Dataset Information

The dataset is generated directly inside the Python script; a separate CSV file is not required.

|Attribute|Description|
|-|-|
|Likes|Number of likes received by a post|
|Shares|Number of times a post was shared|
|Comments|Number of comments on a post|
|Platform|Social media platform|
|Post\_Date|Date of the post|

* Number of records: 50
* Number of columns: 5
* Date range: January 1–February 19, 2026

**Note:** The project uses programmatically generated sample data for demonstration and learning. It should not be interpreted as real platform analytics.



## Key Analysis

The project explores:

1. How likes and comments vary together.
2. How average likes differ across social media platforms.
3. How likes are distributed across posts.
4. How post likes change across the generated date sequence.
5. How likes, shares, and comments are correlated.



## Future Improvements

* Add CSV upload support for user-provided social media data.
* Add platform and date filters.
* Include engagement-rate calculations.
* Add more KPIs and comparison views.
* Connect the dashboard to real social media analytics data where authorized.



## Author

**Divyanshi Sagal**
BCA – AI \& Data Science Student

K.R.Mangalam University, Haryana

LinkedIn link - www.linkedin.com/in/divyanshi-sagal-33b2bb432



