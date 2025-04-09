# Task 1: Data Cleaning & Preprocessing

##  Internship: Elevate Labs – Data Analyst Role  
**Submitted by:** Vanshika Verma  
**Date:** April 9, 2025

---

##  Dataset
**Source:** Netflix Movies and TV Shows (Kaggle)  
The dataset contains metadata of movies and TV shows available on Netflix, including details like title, director, cast, country, release year, rating, duration, and genre.


##  Tools Used
- Python (Pandas)
- Git & GitHub

---

##  Cleaning Steps Performed

1. **Removed duplicates**  
2. **Filled missing values** in columns like `director`, `cast`, `country`, `date_added`, `rating`, and `duration` with `"Unknown"`  
3. **Standardized column names** to lowercase and snake_case  
4. **Converted `date_added`** to proper datetime format  
5. **Formatted text fields** (like `country`, `type`, and `rating`) to be consistent (e.g., title case)

---

##  Files Included

| File Name | Description |
|-----------|-------------|
| `netflix_titles_original.csv` | Raw dataset from Kaggle |
| `cleaned_netflix_titles.csv` | Final cleaned version after preprocessing |
| `clean_netflix_data.py` | Python script used to clean the dataset |

---

##  Outcome
A fully cleaned dataset ready for further analysis, visualization, or modeling.

---

##  Submission Link
[GitHub Repo Link](https://github.com/UncoolW/task-1-data-cleaning)

