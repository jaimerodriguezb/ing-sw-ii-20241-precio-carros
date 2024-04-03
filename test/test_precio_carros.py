import pytest
from modelo.requerimientos_carros import EstandaresCarros 
from unittest.mock import patch

#Ejemplo
#Price,Year,Mileage,State,Make,Model
#34995,2017,9913, FL,Jeep,Wrangler

@pytest.fixture
def datos_carro_ok():   
    return 2017,9913,"FL","Jeep","Wrangler"

def test_prediccion_precio_carro_ok(mocker, datos_carro_ok):
    year, mileage, state, make, model = datos_carro_ok
    mocker.patch("modelo.requerimientos_carros.EstandaresCarros.predecir_precio", return_value = 34995)
    
    estandar_carro = EstandaresCarros()  
    predecir_price = estandar_carro.predecir_precio(year, mileage, state, make, model)  
    assert 0 < predecir_price <= 100000000 

@pytest.fixture
def datos_carro_fail_year(): 
    return "201a",9913,"FL","Jeep","Wrangler"

def test_prediccion_precio_con_year_invalido(mocker, datos_carro_fail_year):
    year, mileage, state, make, model = datos_carro_fail_year    
    estandar_carro = EstandaresCarros() 
    with pytest.raises(ValueError) as error:
        estandar_carro.predecir_precio(year, mileage, state, make, model)
    assert str (error.value) == "ERROR_YEAR"
    
@pytest.fixture
def datos_carro_fail_mileage():
    return 2017,99142948,"FL","Jeep","Wrangler"

def test_prediccion_precio_con_Mileage_invalido(mocker, datos_carro_fail_mileage):
    year, mileage, state, make, model = datos_carro_fail_mileage    
    estandar_carro = EstandaresCarros() 
    with pytest.raises(ValueError) as error:
        estandar_carro.predecir_precio(year, mileage, state, make, model)
    assert str (error.value) == "ERROR_MILEAGE"
    
@pytest.fixture
def datos_carro_fail_state():
    return 2017,9913,"FL++8","Jeep","Wrangler"

def test_prediccion_precio_con_state_invalido(mocker, datos_carro_fail_state):
    year, mileage, state, make, model = datos_carro_fail_state
    estandar_carro = EstandaresCarros()
    with pytest.raises(ValueError) as error:
        estandar_carro.predecir_precio(year, mileage, state, make, model)
    assert str(error.value) == "ERROR_STATE"
    
@pytest.fixture
def datos_carro_fail_make():
    return 2017,9913,"FL","jeep8678","Wrangler"

def test_prediccion_precio_con_make_invalido(mocker, datos_carro_fail_make):
    year, mileage, state, make, model = datos_carro_fail_make
    estandar_carro = EstandaresCarros()
    with pytest.raises(ValueError) as error:
        estandar_carro.predecir_precio(year, mileage, state, make, model)
    assert str(error.value) == "ERROR_MAKE"
    
@pytest.fixture
def datos_carro_fail_model():
    return 2017,9913,"FL","Jeep","P0ll0"

def test_prediccion_precio_con_model_invalido(mocker, datos_carro_fail_model):
    year, mileage, state, make, model = datos_carro_fail_model
    estandar_carro = EstandaresCarros()
    with pytest.raises(ValueError) as error:
        estandar_carro.predecir_precio(year, mileage, state, make, model)
    assert str(error.value) == "ERROR_MODEL"
    
'''Pruebas con el modelo'''
def test_modelo_prediccion_precio_carro_ok(mocker, datos_carro_ok):
    year, mileage, state, make, model = datos_carro_ok
    
    estandar_carro = EstandaresCarros()  
    predecir_price = estandar_carro.predecir_precio(year, mileage, state, make, model) 
    print ("El valor es: ",predecir_price) 
    assert 0 < predecir_price <= 100000000 
