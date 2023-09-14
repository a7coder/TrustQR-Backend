# from brownie import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routes.qr import qr
# from routes.product import product
# from routes.signup import user_router
# from routes.login import login_router
# from routes.decode_qr import qr_router
# import os
# import brownie.project as project

app = FastAPI()

# p = project.load(os.getcwd()+'/'+'blockchain')
# p.load_config()
# network.connect('sepolia')

# app.state.Authentication = p.Authentication.at('0xC141c4227573f0f9591cf71d96F224a867351E51')

# app.state.product_contract=p.Products.at('0x91D4eF7a60c7A29079Edbba7B6A73d77CD10Fa88')

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(qr)
# app.include_router(product)

# app.include_router(user_router)
# app.include_router(login_router)
# app.include_router(qr_router)

@app.get("/api/hello")
async def root():
    return {"message": "Hello World"}
