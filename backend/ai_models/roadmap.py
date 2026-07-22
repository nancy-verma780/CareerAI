ROADMAPS = {
    "Machine Learning Engineer": [
        "Python Advanced",
        "NumPy",
        "Pandas",
        "Statistics",
        "Machine Learning",
        "Scikit-learn",
        "Deep Learning",
        "TensorFlow",
        "MLOps"
    ],
    "Data Scientist": [
        "Python",
        "SQL",
        "Statistics",
        "Pandas",
        "Data Visualization",
        "Machine Learning"
    ],
    "Frontend Engineer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Next.js",
        "TypeScript"
    ]
}


def get_roadmap(role):
    return ROADMAPS.get(role, [])