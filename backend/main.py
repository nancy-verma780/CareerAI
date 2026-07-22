from CareerAI.backend.ai_models import roadmap
from fastapi import FastAPI, UploadFile, File
from app.resume import extract_text
from ai_models.skill_extractor import extract_skills
from ai_models.skill_gap import analyze_skill_gap
from ai_models.career_recommender import recommend_career
from ai_models.roadmap import get_roadmap
from ai_models.resume_score import calculate_resume_score
from ai_models.project_recommender import recommend_projects
from ai_models.github_analyzer import analyze_github
from ai_models.career_chat import ask_career_ai
from database.supabase_client import supabase
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    
    title="CareerAI API"
)
app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

@app.get("/history/{email}")
async def get_history(email:str):

    result = supabase.table(
        "resume_analysis"
    ).select("*").eq(
        "email",
        email
    ).execute()


    return result.data
@app.get("/")
def home():
    return {
        "message": "CareerAI Running"
    }
@app.get("/github-analysis/{username}")
async def github_analysis(username:str):

    result = await analyze_github(username)

    return result

@app.post("/career-chat")
async def career_chat(data:dict):

    answer = ask_career_ai(
        data["question"],
        data["profile"]
    )

    return {
        "answer":answer
    }

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    # Extract text from resume
    resume_text = extract_text(
        file.file,
        file.filename
    )

    # Extract skills
    skills = extract_skills(resume_text)
    career = recommend_career(skills)
    projects = recommend_projects(
    career["recommended_role"]
)
    resume_score = calculate_resume_score(skills)
    roadmap = get_roadmap(
    career["recommended_role"]
)

    # Analyze skill gap
    missing_skills = analyze_skill_gap(
        skills,
        "machine learning engineer"
    )
    supabase.table(
        "resume_analysis"
    ).insert(
        {
            "email": "student@gmail.com",
            "skills": skills,
            "career": career,
            "score": resume_score,
            "roadmap": roadmap,
            "projects": projects
        }
    ).execute()

    return {
        "filename": file.filename,
        "skills": skills,
        "career": career,
        "missing_skills": missing_skills,
        "resume_text": resume_text[:500],
        "resume_score": resume_score,
        "recommended_projects": projects,
        "roadmap": roadmap,
    }