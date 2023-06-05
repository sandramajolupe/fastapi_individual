from pydantic import BaseModel, Field
from typing import Optional 

class Supplier(BaseModel):
        id: Optional[int] = None
        Name: str = Field(max_length=15,min_length=3, description="Name")
        Address: str = Field(max_length=80,min_length=10, description="Addres")
        Phone: int = Field(ge=15, description="Phone")
        Email : str  = Field(max_length=15,min_length=8, description="Email")

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'Name': 'zara',
                    'Address': "carrera 91b no. 42-65",
                    'Phone':12345676960,
                    'Email': "sami@gmail.com"
                }
            }