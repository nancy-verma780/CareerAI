PROJECTS = {
    "Machine Learning Engineer": [
        "Plant Disease Detection",
        "Resume ATS Analyzer",
        "AI Interview Assistant"
    ],
    "Frontend Engineer": [
        "Portfolio Website",
        "E-commerce Store",
        "Chat Application"
    ],
    "Backend Engineer": [
        "URL Shortener",
        "Blog API",
        "Authentication System"
    ]
}


def recommend_projects(role):
    return PROJECTS.get(role, [])