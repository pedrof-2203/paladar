#/api/web_interface.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from db.neo4j_driver import get_driver
from models.restaurant_recommender import RestaurantRecommenderDB

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#app.mount("/static", StaticFiles(directory="static"), name="static")

driver = get_driver()
db = RestaurantRecommenderDB(driver)

@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "recommendations": None})

@app.post("/recommend", response_class=HTMLResponse)
def post_recommendation(request: Request, name: str = Form(...)):
    recommendations = db.recommend_restaurants(name)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "recommendations": recommendations,
        "name": name
    })
