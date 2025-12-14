
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]}

n = int(input("How many more feedbacks do you want to add? "))
current_sno = len(feedback_data['S_No']) + 1
for i in range(n):
    print(f"\nEntering feedback {i+1}:")
    name = input("Enter Name: ")
    written_feedback = input("Enter Written Feedback: ")
    while True:
        rating = int(input("Enter Rating (1–5): "))
        if 1 <= rating <= 5:
            break
        print("Invalid rating! Please enter a number between 1 and 5.")
    feedback_data['S_No'].append(current_sno)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(written_feedback)
    feedback_data['Rating'].append(rating)
    current_sno += 1  
punctuations = ['.', ',', '!', '?']
for i in range(len(feedback_data['Feedback'])):
    feedback = feedback_data['Feedback'][i]
    for p in punctuations:
        feedback = feedback.replace(p, '')
    feedback = ' '.join(feedback.split())
    feedback = feedback.lower()
    feedback_data['Feedback'][i] = feedback
for fb in feedback_data['Feedback']:
    print(fb)
def count_word_in_feedbacks(word):
    word = word.lower()
    count = 0
    for fb in feedback_data['Feedback']:
        if word in fb.split():
            count += 1
    return count
print("Feedbacks containing 'good'     :", count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor'     :", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))
print("final cleaned feedback data:")
for i in range(len(feedback_data['S_No'])):
    print(f"{feedback_data['S_No'][i]}. {feedback_data['Name'][i]} — rating: {feedback_data['Rating'][i]}")
    print(f"   feedback: {feedback_data['Feedback'][i]}")
avg_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("average rating:", round(avg_rating, 2))
max_len = -1
longest_feedback = ""
for fb in feedback_data['Feedback']:
    word_count = len(fb.split())
    if word_count > max_len:
        max_len = word_count
        longest_feedback = fb
print("longest feedback comment:")
print(longest_feedback)
print("word count:", max_len)
unique_words = set()
for fb in feedback_data['Feedback']:
    for w in fb.split():
        unique_words.add(w)
print("unique words used in feedbacks:")
print(unique_words)
