def calculate_resume_score(skills):

    score = 40

    score += len(skills) * 5

    if score > 100:
        score = 100

    return score