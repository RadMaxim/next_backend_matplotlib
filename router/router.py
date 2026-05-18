
from fastapi import APIRouter

from services.services import create_chart, addNewData
from pydantic import BaseModel


class ChartPoint(BaseModel):
    x: int
    y: int
authApp = APIRouter(tags=["Home"])

@authApp.get("/home")
def get_home_page():
    return ""
@authApp.get("/chart")

async def get_chart():
    return create_chart()
@authApp.post("/chart/points")
async def add_chart_point(point: ChartPoint):
    return addNewData(point)