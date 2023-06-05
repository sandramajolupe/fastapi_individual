from models.supplier import Supplier as SupplierModel
from schemas.supplier import Supplier
class SupplierService():
    def _init_(self, db):
        self.db = db
        
    def get_supplier(self):
        result = self.db.query(SupplierModel).all()
        return result
    
    def  create_supplier(self,supplier:SupplierModel):
        new_supplier= SupplierModel(
            Name = supplier.Name.upper(),
            Address = supplier.Address.upper(),
            Phone = supplier.Phone,
            Email= supplier.Email.upper()
            
        )
        self.db.add(new_supplier)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(SupplierModel).filter(SupplierModel.id == id). first()
        return result
    
    def update_supplier(self,data:Supplier):
        supplier = self.db.query(SupplierModel).filter(SupplierModel.id ==data.id).first()
        supplier.Name = data.Name
        supplier.Address = data.Address
        supplier.Phone = data.Phone
        supplier.Email = data.Email