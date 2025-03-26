# my-grade-book
Objective
Create a grade book program that manages student scores using functions and a dictionary.
The program should allow users to:
● Add scores
● Calculate averages
● Determine letter grades
● Continue managing the same student's grades
Instructions
Create Four Functions:
1. add_score(scores, score) – Adds a numeric score to a list and returns the
updated list.
2. get_average(scores) – Takes a list of scores and returns the average.
3. get_letter_grade(average) – Takes an average and returns a letter grade:
○ A: 90-100
○ B: 80-89
○ C: 70-79
○ D: 60-69
○ F: Below 60
4. view_grades(scores) – Returns a string listing all scores in the list.
Additional Steps:
● Create a dictionary actions that maps menu options (e.g., "1" for add score, "2"
for view average, etc.) to their corresponding functions.
● Define a function grade_book() that:
○ Initializes an empty list student_scores to store scores.
○ Prompts the user to enter a student name.
○ Displays the available menu options:
1. Add Score
2. View Scores
3. Get Average
4. Get Letter Grade
5. Quit
○ Uses a while loop that continues until the user chooses to quit.
Inside the While Loop:
● Prompt the user to select a menu option.
● Perform the corresponding action based on the user’s choice:
○ If "1" (Add Score): Prompt for a score (0-100), call add_score(), and
display "Score added."
○ If "2" (View Scores): Call view_grades() and display the result.
○ If "3" (Get Average): Call get_average() and display the result.
○ If "4" (Get Letter Grade): Call get_average(), then
get_letter_grade(), and display the result.
○ If "5" (Quit): Ask if they want to start a new student.
■ If yes, call grade_book() again.
■ If no, end the program.
Error Handling & Testing:
● Handle invalid inputs with an error message.
● Test the program with:
○ Multiple scores
○ Different students
○ Edge cases (e.g., empty score list, scores outside 0-100)
This exercise reinforces function creation, dictionary usage, loops, and conditional logic
while providing a practical application similar to a calculator program.
