from io import BytesIO

from fastapi import APIRouter
import random
import base64
import matplotlib.pyplot as plt
authApp = APIRouter(tags=["Home"])

@authApp.get("/home")
def get_home_page():
    return ""
@authApp.get("/chart")

async def get_chart():
    # random data
    x = list(range(10))
    y = [random.randint(10, 100) for _ in range(10)]

    # matplotlib chart
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(x, y, marker="o")

    ax.set_title("Random Chart")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # save to memory buffer
    buffer = BytesIO()

    plt.savefig(buffer, format="png", bbox_inches="tight")

    plt.close(fig)

    # move cursor to start
    buffer.seek(0)

    # convert to base64
    image_base64 = base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")

    return {
        "mimeType": "image/png",
        "data": image_base64,
    }
