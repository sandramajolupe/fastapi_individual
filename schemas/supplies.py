from pydantic import BaseModel, Field
from typing import Optional

class Supplies(BaseModel):
    id : Optional[int] = None
    supplier_id: int = Field(ge=1, description="supplier id")
    product_id: int = Field(ge=1, description="product id ")
    purchase_price: int = Field(ge=1,le=50000,description="enter purchase price")
    class Config:
        schema_extra = {
            "example":{
                "supplier_id":0,
                "product_id":0,
                "purchase_price":50
            }
        }