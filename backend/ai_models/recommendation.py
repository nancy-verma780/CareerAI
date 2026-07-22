def recommend(skills):


    if "python" in skills and "statistics" in skills:

        return {

        "career":
        "Data Scientist",

        "roadmap":[

        "Machine Learning",

        "Deep Learning",

        "NLP",

        "Deployment"

        ]

        }



    elif "react" in skills:

        return {


        "career":
        "Frontend Engineer",

        "roadmap":[

        "Advanced React",

        "Next.js",

        "System Design"

        ]

        }


    else:

        return {

        "career":
        "Software Engineer"

        }