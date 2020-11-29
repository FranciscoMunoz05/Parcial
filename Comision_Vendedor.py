'''
Calcular la comision que le corresponde al vendedor
'''
class Vendedor(object):
    def __init__(self, comision):
        self.comision = comision
        
    def ventasMensuales(self, ve1,ve2,ve3):
        totalVentas = ve1+ve2+ve3
        return totalVentas
        
    def comisionNeta(self, totalV):
        totalComision = totalV * self.comision
        return totalComision
        
vendedor1 = Vendedor(0.10)
print ("Ventas del Mes Vendedor")
v1 = float(input("Ingresar Venta 1: "))
v2 = float(input("Ingresar Venta 2: "))
v3 = float(input("Ingresar Venta 3: "))
ventasMT = vendedor1.ventasMensuales(v1,v2,v3)
comision = vendedor1.comisionNeta(ventasMT)
print("____________________________________")

print("Ventas Total del Mes: ", ventasMT)
print("Comisión Total del Vendedor: ",comision) 

