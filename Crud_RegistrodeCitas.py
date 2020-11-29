
#Programa de registrar Cita con crud y POO

class Medico(object):
    '''    
    def __init__(self, id_medico, nombre):
        self.id_medico = id_medico
        self.nombre = nombre
    '''
    def __init__(self):
        pass

    listMedico = []
        
        #Crud medico
    def registrarMedico(self, id_medico, nombre):
        matrix = []
        matrix.append(id_medico)
        matrix.append(nombre)
        self.listMedico.append(matrix)
        print ("Medico Registrado ")
        
    def obtenerMedicos(self):
        print ("Lista Paciente:",  self.listMedico)
        
    def actualizarMedico(self, select, nombre):
        m = [select+1,nombre]
        self.listMedico[select] = m 
        print ("nombre de medico actualizado ")
        
    def eliminarMedico(self, selectRID):
        self.listMedico.pop(selectRID)
#__________________________________________________________________________________        
class Paciente(object):
    '''    
    def __init__(self, id_, nombre):
        self.id_medico = id_medico
        self.nombre = nombre
    '''
    def __init__(self):
        pass

    listPaciente = []
        
        #Crud Paciente
    def registrarPaciente(self, id_medicoP, nombreP):
        matrixP = []
        matrixP.append(id_medicoP)
        matrixP.append(nombreP)
        self.listPaciente.append(matrixP)
        print ("Paciente Registrado ")
        
    def obtenerPaciente(self):
        print ("Lista Paciente:",  self.listPaciente)
        
    def actualizarPaciente(self, selectM, nombreM):
        w = [selectM+1,nombreM]
        self.listPaciente[selectM] = w 
        print ("nombre de Paciente actualizado...")
        
    def eliminarPaciente(self, selectEID):
        self.listPaciente.pop(selectEID)
        print ("Paciente Eliminado...")
        
#__________________________________________________________________________________        
class Clinica(object):
    '''    
    def __init__(self, id_, nombre):
        self.id_medico = id_medico
        self.nombre = nombre
    '''
    def __init__(self):
        pass

    listClinica = []
        
        #Crud Clinica
    def registrarClinica(self, id_medicoC, nombreC):
        matrixC = []
        matrixC.append(id_medicoC)
        matrixC.append(nombreC)
        self.listClinica.append(matrixC)
        print ("Clinica Registrada ")
        
    def obtenerClinica(self):
        print ("Lista Clinica:",  self.listClinica)
        
    def actualizarClinica(self, selectC, nombreC):
        q = [selectC+1,nombreC]
        self.listClinica[selectC] = q
        print ("nombre de Clinica actualizado...")
        
    def eliminarClinica(self, selectLID):
        self.listClinica.pop(selectLID)
        print ("Clinica Eliminado...")
#__________________________________________________________________________________  
#__________________________________________________________________________________  
class Cita(Medico, Paciente, Clinica):
    
    def __init__(self):
        pass
    
    listCita = []
    
    def registrarCita(self, id_dem):
        print("\n")
        print("selecionar Clinica")
        print ("Lista Clinica (Seleción):",  self.listClinica)
        dem_clinica = int(input("Ingresar ID de la Clinica: "))
        print("\n")
        print("selecionar Paciente")
        print ("Lista Paciente (Seleción):",  self.listPaciente)
        dem_paciente = int(input("Ingresar ID del Paciente: "))
        print("\n")
        print("selecionar Medico")
        print ("Lista Medico (Seleción):",  self.listMedico)
        dem_medico = int(input("Ingresar ID del Medico: "))
        
        matrixE = []
        matrixE.append(id_dem)
        matrixE.append(Clinica.listClinica[dem_clinica-1])
        matrixE.append(Paciente.listPaciente[dem_paciente-1])
        matrixE.append(Medico.listMedico[dem_medico-1])
        self.listCita.append(matrixE)
        print ("Cita Registrada ")
        
        
    def totalCitas(self):
        print ("Cantidad de Citas registradas en el sistema: ", len(self.listCita))
        
    def todasCita(self):
        for i in self.listCita:
            print("Lista de Citas: ", i)
            
    def buscarCitaXPasi(self):
        print ("Lista Paciente (Seleción):",  self.listPaciente)
        bxp_paciente = int(input("Ingresar ID del Paciente a buscar citas: "))
        print("\n")
        #print ("Se encontro: ",self.listCita.index())
        print ("Se encontro: ",[(index, row.index(bxp_paciente)) for index, 
        row in enumerate(self.listCita) if bxp_paciente in row])
        print("Registro encontrado x Paciente: ",self.listCita[bxp_paciente-1])
        
    def buscarCitaXClin(self):
        print ("Lista Clinica (Seleción):",  self.listClinica)
        bxp_clinica = int(input("Ingresar ID del Clinica a buscar citas: "))
        print("\n")
        #print ("Se encontro: ",self.listCita.index())
        print ("Se encontro: ",[(index, row.index(bxp_clinica)) for index, 
        row in enumerate(self.listCita) if bxp_clinica in row])
        print("Registro encontrado x Clinica: ",self.listCita[bxp_clinica-1])
  
medicos = Medico()
paciente = Paciente()
clinica = Clinica()
cita = Cita()

#para tener registros de pruebas y default en el sistema
medicos.registrarMedico(1,"Mario Sabera")
paciente.registrarPaciente(1,"dario samudo")
clinica.registrarClinica(1,"Santiago")
#2 sample
medicos.registrarMedico(2,"Sabedra mai")
paciente.registrarPaciente(2,"sima rum")
clinica.registrarClinica(2,"Chiriqui")

mx1 = [1,[1,"Mario Sabera"], [1, "dario samudo"],[1,"Santiago"]] 
mx2 = [2,[1,"Mario Sabera"], [2, "Carlos Gem"],[3,"Panama"]]
cita.listCita.append(mx1)
cita.listCita.append(mx2)

#-------------------------------------------------------------------  
def menuPrincipal():
    
    def imprimirMenu():
        print("_______________Programa de Citas Medicas_______________")
        print("1. Registrar Medicos")
        print("2. Obtener Lista de Midicos")
        print("3. Actualizar datos Medico")
        print("4. Eliminar datos Medico")
        print("5. Registrar Paciente")
        print("6. Obtener Lista de Paciente")
        print("7. Actualizar datos Paciente")
        print("8. Eliminar datos Paciente")
        print("9. Registrar Clinica")
        print("10. Obtener Lista de Clinica")
        print("11. Actualizar datos Clinica")
        print("12. Eliminar datos Clinica")
        print("13. Registrar Cita Medica")
        print("14. Total de Citas Actuales")
        print("15. Busquedas de Citas")
        print("16. Salir")
        print("______________________________")
    def passEnter():
        input("Presiona Enter para volver al menu principal...")
    def clean():
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
        print("\n\n\n")
    
    activo_menu = True
    
    while activo_menu:
        imprimirMenu()
        Selec = input("Ingresar la opción de su selecion [1-16]: ")
#__________________________________________________________________________________Crud Medico        
        if Selec == '1':
            clean()
            print ("Registrar Medico")
            
            #Registrar Medico
            countid = len(medicos.listMedico)
            nombre = input("Ingresar nombre del medico: ")
            countid += 1
            medicos.registrarMedico(countid , nombre)
            
            passEnter()
            
        elif Selec == '2':
            clean()
            print ("Lista de Medicos")
            medicos.obtenerMedicos()
            passEnter()
            
        elif Selec == '3':
            clean()
            print ("Actualizar medico")
            print("Lista de Medicos: ", medicos.listMedico)
            select = int(input("Ingresar numero id a modificar: "))
            name = input("Ingresar nombre medico: ")
            select -=1
            medicos.actualizarMedico(select,name)
            print(medicos.listMedico)
            passEnter()
        
        elif Selec == '4':
            clean()
            print ("Eliminar medico")
            print("Lista de Medicos: ", medicos.listMedico)
            selectE = int(input("Ingresar numero id medico a Eliminar: "))
            selectE -=1
            medicos.eliminarMedico(selectE)
#__________________________________________________________________________________Crud Paciente 
        elif Selec == '5':
            clean()
            print ("Registrar Paciente")
            
            #Registrar Paciente
            countidP = len(paciente.listPaciente)
            nombreP = input("Ingresar nombre del Paciente: ")
            countidP += 1
            paciente.registrarPaciente(countidP , nombreP)
            
            passEnter()
            
        elif Selec == '6':
            clean()
            
            #Obtener Pacientes Lista
            print ("Lista de Paciente")
            paciente.obtenerPaciente()
            
            passEnter()
            
        elif Selec == '7':
            clean()
            
            print ("Actualizar Paciente")
            print("Lista de Paciente: ", paciente.listPaciente)
            selectP = int(input("Ingresar numero id a modificar: "))
            nameP = input("Ingresar nombre paciente: ")
            selectP -=1
            paciente.actualizarPaciente(selectP,nameP)
            print(paciente.listPaciente)
            
            passEnter()
        
        elif Selec == '8':
            clean()
            
            print ("Eliminar Paciente")
            print("Lista de Paciente: ", paciente.listPaciente)
            selectEP = int(input("Ingresar numero id paciente a eliminar: "))
            selectEP -=1
            paciente.eliminarPaciente(selectEP)
            
            passEnter()
#__________________________________________________________________________________Crud Clinica            
        elif Selec == '9':
            clean()
            print ("Registrar Clinica")
            
            #Registrar Clinica
            countidC = len(clinica.listClinica)
            nombreC = input("Ingresar nombre del Clinica: ")
            countidC += 1
            clinica.registrarClinica(countidC , nombreC)
            
            passEnter()
            
        elif Selec == '10':
            clean()
            
            #Obtener Clinica Lista
            print ("Lista de Clinicas")
            clinica.obtenerClinica()
            
            passEnter()
            
        elif Selec == '11':
            clean()
            
            print ("Actualizar Clinica")
            print("Lista de Clinica: ",  clinica.listClinica)
            selectC = int(input("Ingresar numero id a modificar: "))
            nameC = input("Ingresar nombre Clinica: ")
            selectC -=1
            clinica.actualizarClinica(selectC,nameC)
            print(clinica.listClinica)
            
            passEnter()
            
        elif Selec == '12':
            clean()
            
            print ("Eliminar Clinica")
            print("Lista de Clinica: ", clinica.listClinica)
            selectEPC = int(input("Ingresar numero id paciente a eliminar: "))
            selectEPC -=1
            clinica.eliminarClinica(selectEPC)
            
            passEnter()
            
        elif Selec == '13':
            clean()
            print ("Registrar Clinica")
            
            #Registrar Cita
            countidCC = len(cita.listCita)
            countidCC += 1
            cita.registrarCita(countidCC)
            
            passEnter()
            
        elif Selec == '14':
            clean()
            
            cita.totalCitas()
            
            passEnter()
            
        elif Selec == '15':
            clean()
            print("Que desea consultar: ")
            print("1. Imprimir todas las Citas")
            print("2. Buscar una Cita por Paciente")
            print("3. Buscar una Cita por Clinica")
            value_user = input("Ingresar una opción: ")
            if(value_user == "1"):
                clean()
                cita.todasCita()
            elif(value_user == "2"):
                clean()
                cita.buscarCitaXPasi()
            elif(value_user == "3"):
                clean()
                cita.buscarCitaXClin()
            else:
                print ("error de selecion!")
            
            #elif(value_user == 3):
            print ("\n")
            passEnter()
            
        elif Selec == '16':
            activo_menu = False
        else:
            input("Selecion invalida. Ingrese un valor de opción valido: ")
    return activo_menu  
    
menuPrincipal()