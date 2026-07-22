CAREER_SKILLS = {


"machine learning engineer":[

"python",
"machine learning",
"statistics",
"numpy",
"pandas",
"scikit-learn",
"deep learning",
"tensorflow",
"pytorch"

],


"data scientist":[

"python",
"statistics",
"sql",
"pandas",
"numpy",
"machine learning",
"data visualization"

],


"frontend engineer":[

"html",
"css",
"javascript",
"react",
"next.js",
"typescript"

],


"software engineer":[

"python",
"java",
"data structures",
"algorithms",
"system design"

]


}
def analyze_skill_gap(user_skills, target_role):


    target_role = target_role.lower()


    required_skills = CAREER_SKILLS.get(
        target_role,
        []
    )


    missing = []


    for skill in required_skills:

        if skill not in user_skills:

            missing.append(skill)


    return missing

    if __name__ == "__main__":


    my_skills = [

        "python",
        "react",
        "sql"

    ]


    result = analyze_skill_gap(
        my_skills,
        "machine learning engineer"
    )


    print(result)