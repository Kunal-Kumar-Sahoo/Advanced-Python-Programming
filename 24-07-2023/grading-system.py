# Generate Grade Sheet of a student

def grade(score):
    '''
    Params: score(float)
    Returns: tuple(str, int)
    Description: This function inputs a score and
    returns the corresponding grade and grade point
    '''
    if score >= 80: 
        return 'O', 10
    elif score < 80 and score >= 70: 
        return 'A+', 9
    elif score < 70 and score >= 60:
        return 'A', 8
    elif score < 60  and score >= 50:
        return 'B', 7
    elif score < 50 and score >= 40:
        return 'C', 6
    return 'Fail', 0

def grade_sheet(name, semester, subjects, scores):
    '''
    Params: name(str), semester(int), subjects(list), scores(list)
    Returnn: None
    Description: This function generates the grade sheet of the student
    whose information is passed as function parameters
    '''

    # Check is number of subjects and number of scores are same
    assert len(subjects) == len(scores), "Subjects and Scores inconsistent"
    
    print(f'Name of the student: {name}')
    print(f'Semester: {semester}')

    # Map all the elements of the scores with the `grade()` function and store the result in a list
    grades = list(map(grade, scores))

    # Print the result and calculate CGPA
    print('Subject\t Score\t Grade\t Grade Point')
    GPA = 0
    for i in range(len(subjects)):
        print(f'{subjects[i]}\t {scores[i]}\t {grades[i][0]}\t {grades[i][1]}')
        GPA += grades[i][1]
    
    GPA /= len(subjects)
    
    print(f'CGPA: {GPA}')    
    

if __name__ == '__main__':
    name = input('Enter your name: ')
    semester = int(input('Enter your semester: '))

    number_of_subjects = int(input('Enter number of subjects: '))
    subjects, scores = [], []

    for i in range(number_of_subjects):
        prompt = input(f'Enter subject {i+1} and it\'s score: ').split()
        subjects.append(' '.join(prompt[0:-1]))
        scores.append(int(prompt[-1]))
    
    grade_sheet(name, semester, subjects, scores)