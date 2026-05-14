class cliente():
    def __init__(self,data):
        self.update_information(data)
        self._purchase_history={}
      
        
    def update_information(self,data):
        self._name=data.get("name", None)        
        self._customer_id=data.get("customer_id", None) 
        self._document=data.get("document", None) 
        self._email=data.get("email", None) 
        self._phone=data.get("phone", None) 
        self._address=data.get("address", None) 
        self._state=data.get("state", None) 
        self._membership=data.get("membership", None) 

    def add_purchase_history(self, new_value):
        self._purchase_history.update(new_value)  

    def calculate_total_spend(self):
        pass
        
   # --- getters ---    
    @property 
    def name(self):
        return self._name  

    @property   
    def customer_id(self):
        return self._customer_id 

    @property     
    def document(self):
        return self._document

    @property 
    def email(self):
        return self._email

    @property 
    def phone(self):
        return self._phone

    @property 
    def address(self):
        return self._address

    @property 
    def state(self):
        return self._state

    @property 
    def purchase_history(self):
        return self._purchase_history

    @property 
    def membership(self):
        return self._membership

    # --- setters ---  

    @name.setter
    def name(self, new_value):
        self._name =new_value

    @customer_id.setter
    def customer_id(self, new_value):
        self._customer_id=new_value

    @document.setter
    def document(self, new_value):
        self._document =new_value

    @email.setter
    def email(self, new_value):
        self._email=new_value

    @phone.setter
    def phone(self, new_value):
        self._phone=new_value

    @address.setter
    def address(self, new_value):
        self._address=new_value

    @state.setter
    def state(self, new_value):
        self._state=new_value
      
    @purchase_history.setter
    def purchase_history(self, new_value):
        self._purchase_history=new_value

    @membership.setter
    def membership(self, new_value):
        self._membership=new_value
