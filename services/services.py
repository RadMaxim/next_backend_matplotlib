
import base64
import matplotlib.pyplot as plt
from io import BytesIO

from pydantic import BaseModel


class ChartPoint(BaseModel):
    x: int
    y: int
x_data: list[int] = []
y_data: list[int] = []
def create_chart():
    fig, ax = plt.subplots(figsize=(8, 4))

    if x_data and y_data:
        ax.plot(x_data, y_data, marker="o")
    else:
        ax.plot([], [])
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 100)

    ax.set_title("Dynamic Chart")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    buffer = BytesIO()

    plt.savefig(buffer, format="png", bbox_inches="tight")
    plt.close(fig)

    buffer.seek(0)

    return ({
        "mimeType": "image/png",

        "data": base64.b64encode(buffer.getvalue()).decode("utf-8"),


    })



def addNewData(point: ChartPoint):
    x_data.append(point.x)
    y_data.append(point.y)
    image_base64 = create_chart()
    return ({
        "mimeType": "image/png",

        "data": image_base64,
    })