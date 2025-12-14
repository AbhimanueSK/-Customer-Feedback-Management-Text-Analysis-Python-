# -Customer-Feedback-Management-Text-Analysis-Python-
This project demonstrates a menu-driven customer feedback management system implemented in Python, focusing on user input handling, text cleaning, word analysis, and summary insights. The program stores feedback in a structured dictionary format and performs basic text preprocessing and analytical operations without using advanced NLP libraries.
🎯 Project Objectives

The objective of this project is to:

Collect and manage customer feedback dynamically

Clean and normalize text data

Perform word-based analysis on feedback comments

Generate meaningful summaries and insights from textual data

📌 Project Workflow & Features
✍️ Step 2: Add More Feedbacks

Prompts the user to enter the number of additional feedback entries

Collects the following details for each feedback:

Customer Name

Written Feedback (text)

Rating (1–5 scale)

Automatically increments S_No starting from 11 onward

Appends all new records into the existing feedback_data dictionary

🧹 Step 3: Text Cleaning

All feedback comments are cleaned using basic Python string operations:

Removes punctuation marks (. , ! ?)

Replaces multiple spaces with a single space

Removes leading and trailing whitespaces

Converts all text to lowercase

💡 Text cleaning is implemented using .replace(), .split(), and ' '.join() methods.

🔁 Step 4: Word Count Insights

A reusable function count_word_in_feedbacks(word) is created to:

Accept a word as input

Count how many feedback comments contain the given word (case-insensitive)

The function is used to analyze:

Number of feedbacks containing "good"

Number of feedbacks containing "poor"

Number of feedbacks containing "excellent"

📊 Step 5: Final Summary & Insights

The program generates the following insights:

Displays the final cleaned feedback_data dictionary

Calculates and prints the average customer rating

Identifies and displays the feedback with the longest comment (based on word count)

Extracts and prints a list of unique words used across all feedbacks

(Optional) Sorts feedbacks by rating (highest to lowest) using zip() and sorted()

🛠️ Tools & Concepts Used

Python

Dictionaries & Lists

String manipulation

Functions

Loops & Conditional logic

zip() and sorted()

📈 Learning Outcomes

Improved understanding of text preprocessing techniques

Hands-on experience with dictionary-based data storage

Function-based analytical thinking

Real-world simulation of feedback analysis systems

📂 Use Cases

Beginner-friendly text analytics project

Academic assignment or lab exercise

Python portfolio project

Foundation for sentiment analysis systems
