CAREERS = {

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "tensorflow",
        "pytorch",
        "numpy",
        "pandas"
    ],

    "Data Scientist": [
        "python",
        "sql",
        "statistics",
        "pandas",
        "numpy"
    ],

    "Frontend Engineer": [
        "html",
        "css",
        "javascript",
        "react",
        "typescript"
    ],

    "Backend Engineer": [
        "python",
        "fastapi",
        "sql",
        "mongodb"
    ]

}


def recommend_career(user_skills):

    best_role = None
    best_score = 0


    for role, skills in CAREERS.items():

        score = 0

        for skill in skills:

            if skill in user_skills:
                score += 1


        if score > best_score:

            best_score = score
            best_role = role


    return {

        "recommended_role": best_role,

        "match_score": best_score

    }