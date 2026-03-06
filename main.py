from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import asyncio

from scraper import get_ship_details

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/ship/{imo}")
async def ship_details(imo: str):

    try:
        result = await get_ship_details(imo)

        if result is None:
            return JSONResponse({"error": "Ship not found"})

        return result

    except Exception as e:
        return JSONResponse({"error": str(e)})