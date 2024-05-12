from fastapi import FastAPI , status
from fastapi.middleware.cors import CORSMiddleware
from .routers import users , auth , cancellation , token_access


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/" , status_code=status.HTTP_302_FOUND)
def welcomescreen():
    return "Welcome to the interactive mess management system"


app.include_router(users.router)
app.include_router(auth.router)
app.include_router(cancellation.router)
app.include_router(token_access.router)



