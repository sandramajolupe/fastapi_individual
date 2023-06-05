from pydantic import BaseModel, Field
from typing import Optional

class Supplies(BaseModel):
    id : Optional[int] = None
    supplier_id: int = Field(ge=1, description="Supplier id")
    product_id: int = Field(ge=1, description="Product id ")
    purchase_price: int = Field(ge=1,le=50000,description="Enter purchase price")
    class Config:
        schema_extra = {
            "example":{
                "supplier_id":1,
                "product_id":1,
                "purchase_price":40
            }
        }