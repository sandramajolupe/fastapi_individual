from pydantic import BaseModel, Field
from typing import Optional 

class Product(BaseModel):
        id: Optional[int] = None
        name: str = Field(max_length=150,min_length=2, description="name")
        brand: str = Field(max_length=80,min_length=3, description="addres")
        description: str = Field(max_length=200,min_length=3, description="product description")
        price : int  = Field(ge=200, description="price")
        entry_date : str  = Field(max_length=200,min_length=3, description="entry_date")
        availability : str  = Field(max_length=300,min_length=3, description="availability")
        available_quantity: int  = Field(ge=50,le=5000, description="available_quantity")

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'name': 'sweater',
                    'brand': "zara",
                    'description':"of the best quality",
                    'price': 2000,
                    "entry_date": "enter the date",
                    "availability" :" yes",
                    "available_quantity" : 50
                }
            }