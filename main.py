import pandas as pd
import numpy as np

skills_weight = 0.4
qualification_weight = 0.2
experience_weight = 0.3
certification_weight = 0.1

data = pd.DataFrame({
    'applicant_name': ['sohel', 'shivu', 'priyanshu'],
    'skillsMatched': [6, 3, 7],
    'no_of_skills_required': [10, 5, 8],
    'qualificationMatched': [1, 0, 1],
    'experience': [5, 2, 10],
    'certificationMatched': [2, 0, 3],
    'no_of_certification_required': [4, 2, 5],
})

for index, row in data.iterrows():
    skills_matched = row['skillsMatched']
    no_of_skills_required = row['no_of_skills_required']
    qualification_matched = row['qualificationMatched']
    experience = row['experience']
    normalized_experience = experience / 10 
    certification_matched = row['certificationMatched']
    no_of_certification_required = row['no_of_certification_required']

    score = (skills_matched / no_of_skills_required * skills_weight) + \
            (qualification_matched * qualification_weight) + \
            (normalized_experience * experience_weight) + \
            (certification_matched / no_of_certification_required * certification_weight)
    
    score_percent = round(score * 100)
    data.at[index, 'score'] = f"{score_percent}%"

data = data.sort_values(by='score', ascending=False)

print(data)
