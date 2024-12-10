from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"Salom ": "Dunyo"}  # Bu yerda asosiy endpoint mavjud

@app.get("/current_time")
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}
