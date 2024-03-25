import re
class EstandaresCarros:
    def __init__(self) -> None:
        self.modelo_carro = None
        self.cargar_modelo()
   
    def predecir_precio(self, year, mileage, state, make, model):   
        self.validar_entrada_year(year, mileage, state, make, model)    
        price = self.modelo_carro.predict(year, mileage, state, make, model)
        return price
    
    def cargar_modelo(self):  
        pass
    
    def validar_entrada_year(self, year, mileage, state, make, model):
        if not isinstance(year, int) or year < 1900 or year > 2024:
            raise ValueError("ERROR_YEAR")
        if not isinstance(mileage, int) or mileage < 100 or mileage > 100000:
            raise ValueError("ERROR_MILEAGE")
        if not isinstance(state, str)or not re.match("^[a-zA-Z]+$", state):
            raise ValueError("ERROR_STATE")
        if not isinstance(make, str) or not re.match("^[a-zA-Z]+$", make):  
            raise ValueError("ERROR_MAKE")
        if not isinstance(model, str) or not re.match("^[a-zA-Z]+$", model):
            raise ValueError("ERROR_MODEL")
