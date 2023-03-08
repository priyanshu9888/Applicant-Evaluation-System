Applicant Evaluation System

This Python script uses pandas and numpy libraries to calculate the score of job applicants based on their skills, qualification, experience, and certification.
How it works

The script creates a pandas DataFrame with the following columns:

    applicant_name: the name of the applicant
    skillsMatched: the number of skills matched with the required skills
    no_of_skills_required: the total number of skills required
    qualificationMatched: 1 if the applicant's qualification matches the required qualification, 0 otherwise
    experience: the number of years of experience of the applicant
    certificationMatched: the number of certifications matched with the required certifications
    no_of_certification_required: the total number of certifications required

The script then iterates over each row of the DataFrame, calculates the score of the applicant using the following weights:

    skills_weight: 40%
    qualification_weight: 20%
    experience_weight: 30%
    certification_weight: 10%

The final score is a weighted average of the applicant's skills, qualification, experience, and certification.

The script then sorts the DataFrame by score in descending order and prints the result.
How to use it

To use this script, you need to have pandas and numpy libraries installed. You can install them using pip:

pip install pandas numpy

Once you have installed the required libraries, you can run the script using any Python environment or IDE of your choice.

The script takes no input from the user and uses the data provided in the script itself. If you want to use your own data, you can modify the DataFrame accordingly.
Output

The output of the script is a pandas DataFrame with the following columns:

    applicant_name: the name of the applicant
    skillsMatched: the number of skills matched with the required skills
    no_of_skills_required: the total number of skills required
    qualificationMatched: 1 if the applicant's qualification matches the required qualification, 0 otherwise
    experience: the number of years of experience of the applicant
    certificationMatched: the number of certifications matched with the required certifications
    no_of_certification_required: the total number of certifications required
    score: the final score of the applicant in percentage.

The DataFrame is sorted by score in descending order.
License

This script is licensed under the MIT License. Feel free to use, modify, and distribute it as per your requirement.
