import uvicorn, fastapi
from starlette.middleware.cors import CORSMiddleware

from router.router import authApp

app = fastapi.FastAPI()
app.include_router(authApp)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://192.168.77.79:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
