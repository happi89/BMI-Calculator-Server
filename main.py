from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

origins = [
    "https://bmi-calculator-fawn.vercel.app",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/calculate-bmi")
def update_item(weight: float, height: float):
  print(height, weight)
  BMI = round((weight / (height * height)), 1)
  Category = '';
  
  if(BMI > 30):
    Category = 'Obesity'
  elif(BMI > 25):
    Category = 'Overweight'
  elif(BMI > 18.5):
    Category = 'Normal weight'
  else:
    Category = 'Underweight'
  
  return {"BMI": BMI, "category": Category}
