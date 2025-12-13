from modelo_vehiculo_BMW_Z4 import BMW_Z4
from modelo_vehiculo_MINI_VAN import MiniVan
from modelo_vehiculo_Bolqueta import Bolqueta

# Instancias de cada vehículo
bmw = BMW_Z4("BMW Z4", "Rojo", "combustion de 3.0L", 2, 2, "Gasolina")
minivan = MiniVan("Mini Van", "Blanco", "combustion de 2.0L", 4, 7, "Gasolina")
bolqueta = Bolqueta("Bolqueta", "Amarillo", "Diesel de 5.0L ", 2, 3, "Diesel")

vehiculos = [bmw, minivan, bolqueta]

for v in vehiculos:
    print(f"\nVEHÍCULO: {v.modelo}")
    print(f"Color: {v.color}, Motor: {v.motor}, Puertas: {v.num_puertas}, Capacidad: {v.capacidad_pasajeros}, Combustible: {v.tipo_combustible}")
    print(v.arranque())
    print(v.aceleracion_frenado())
    print(v.sistema_direccion())
    print(v.climatizacion())
    print(v.tipo_seguridad())
    print(v.luces())
    print(v.sistema_ventanas())
    print(v.sistema_espejo())
    if hasattr(v, 'capacidad_carga'):
        print(v.capacidad_carga())
    if hasattr(v, 'transporte_carga'):
        print(v.transporte_carga())
