import re
import pandas as pd
import joblib
import os

class EstandaresCarros:
    def __init__(self) -> None:
        self.modelo_carro = None
        self._load_model()
   
    def predecir_precio(self, year, mileage, state, make, model):   
        self.validar_entrada_year(year, mileage, state, make, model)    
        price = self.modelo_carro.predict(year, mileage, state, make, model)
        return price
    
    def _load_model(self):
        self.__model = joblib.load(os.path.dirname(__file__) + '\\training\\predictor_precios_model.pkl')  
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
