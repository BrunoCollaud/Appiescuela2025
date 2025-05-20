from fastapi import FastAPI
from routes.userdetail import userDetail
from routes.user import user
from routes.materias import materia
from fastapi.middleware.cors import CORSMiddleware



api_escu = FastAPI()


api_escu.include_router(user)
api_escu.include_router(userDetail)
api_escu.include_router(materia)

api_escu.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["GET", "POST", "PUT", "DELETE"],
   allow_headers=["*"],
)

