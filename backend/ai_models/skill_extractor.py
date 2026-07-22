import spacy


nlp = spacy.load(
"en_core_web_sm"
)



skills = [

"python",
"java",
"react",
"machine learning",
"sql",
"tensorflow",
"pandas",
"numpy",
"fastapi"

]



def extract_skills(text):

    text=text.lower()

    found=[]


    for skill in skills:

        if skill in text:

            found.append(skill)


    return found