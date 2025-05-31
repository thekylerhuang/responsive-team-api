from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base
from models import Member
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 開發階段可以先設 *
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 自動建立資料表（只會在第一次時執行）
Base.metadata.create_all(bind=engine)
@app.get("/")
def home():
    return{"message":"Hello FastAPI"}

@app.get("/api/members")
def get_members():
    return[
          {
            "name": "Kevin Samson",
            "title": "Founder",
            "description": "Turning clean code into beautiful experiences.",
            "image": "/images/team1.jpg",
            "email": "kevinsamson@gmail.com"
        },
        {
            "name": "Rebecca Williams",
            "title": "Designer",
            "description": "I design with empathy and detail in every pixel.",
            "image": "/images/team2.jpg",
            "email": "rebeccawilliams@gmail.com"
        },
        {
            "name": "Ben Markson",
            "title": "Designer/Developer",
            "description": "I love solving complex problems with simple logic.",
            "image": "/images/team3.jpg",
            "email": "benmarkson@gmail.com"
        },
        {
        "name": "Sophia Lin",
        "title": "UX Strategist",
        "description": "Designing experiences that actually solve user pain.",
        "image": "/images/team4.jpg",
        "email": "sophialin@gmail.com"
        },
        {
        "name": "Noah Wu",
        "title": "Cloud Architect",
        "description": "Building scalable systems from the ground up.",
        "image": "/images/team5.jpg",
        "email": "noahwu@gmail.com"
        },
        { 
        "name": "Leo Chen",
        "title": "AI Researcher",
        "description": "Passionate about machine learning.",
        "image": "/images/team6.jpg",
        "email": "leochen@gmail.com"
        },        
    ]