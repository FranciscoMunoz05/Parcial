'''
calcular salario de un empelado segun su hora trabajadas
'''

class Aslariado():
    def __init__(self, horaxJ,css,se):
        self.horaxJ = horaxJ
        self.css = css
        self.se =  se
    
    def salarioBruto(self, horaJob):
        totalSalarioB = horaJob*self.horaxJ
        return totalSalarioB
        
    def seguroSocial(self, sB):
        totalScc = sB * self.css
        return totalScc
        
    def seguroEducativo(self, sBS):
        totalSs = sBS * self.se 
        return totalSs
        
    def salarioNeto(self, sB,sE, sS):
        totalNeto = sb - (sE-sS)
        return totalNeto
        
horas = float(input("Ingrese las horas trabajadas: "))
asalariado = Aslariado(1.32,
                            0.09,#---9%
                            0.0125)#---1.25%

sb = asalariado.salarioBruto(horas)
se = asalariado.seguroSocial(sb)
ss = asalariado.seguroEducativo(sb)
sn = asalariado.salarioNeto(sb,se,ss)
print ("Salario Bruto: ", "{:.2f}".format(sb))
print ("Seguro Social: ", "{:.2f}".format(se))
print ("Seguro Educativo: ", "{:.2f}".format(ss))
print ("_____________________")
print ("Salario Final neto: ", "{:.2f}".format(sn))