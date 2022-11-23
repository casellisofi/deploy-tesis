from libraries import *

"""
       _____LÓGICA DE LA FUSIÓN DE MODELOS PARA TIPOS____
       Definimos tres objetos: SVM() BAYES() Y BERT(), cuyos atributos de cada uno serán los tipos de reclamos.
       
       Cada objeto cuenta con el método "setRecall()" el cual recibe como parámetro un diccionario, dicho
       diccionario es el que cada modelo obtiene a través de la métrica "Reporte de clasificacion" 
       (sklearn.metrics.classification_report) en donde se encuentra el recall del modelo para cada tipo.
       El metodo setRecall() obtiene el recall de cada tipo para asignar a los atributos correspondientes.

       Cada objeto también cuenta con el método "getRecall()" el cual recibe como parametro un nombre o etiqueta
       númerica del tipo, y retorna su recall correspondiente.

       Por último, cada objeto tiene el método "mostrar()" el cual imprime por pantalla el recall de cada tipo.
"""

class SVM():
       
       def __init__(self):
           self.tipo0 = 0
           self.tipo1 = 0
           self.tipo2 = 0
           self.tipo3 = 0
           self.tipo4 = 0
           self.tipo5 = 0
       
       def setTipoCero(self,value):
              self.tipo0 = value

       def setTipoUno(self,value):
              self.tipo1 = value

       def setTipoDos(self,value):
              self.tipo2 = value

       def setTipoTres(self,value):
              self.tipo3 = value                                 

       def setTipoCuatro(self,value):
              self.tipo4 = value

       def setTipoCinco(self,value):
              self.tipo5 = value

       def setRecall(self,dic):
              self.setTipoCero(dic.get('DECISION_DE_NEGOCIO').get('recall'))
              self.setTipoUno(dic.get('DISCONFORMIDAD_CLIENTE').get('recall'))
              self.setTipoDos(dic.get('ERROR_DESPEGAR').get('recall'))
              self.setTipoTres(dic.get('ERROR_PROVEEDOR').get('recall'))
              self.setTipoCuatro(dic.get('FRAUDE').get('recall'))
              self.setTipoCinco(dic.get('SIN_IDENTIFICAR').get('recall'))
       

       def getRecall(self,clave):
              if clave == 'DECISION_DE_NEGOCIO' or clave == '0':
                     return self.tipo0
              elif clave == 'DISCONFORMIDAD_CLIENTE'or clave == '1':
                     return self.tipo1
              elif clave == 'ERROR_DESPEGAR'or clave == '2':
                     return self.tipo2
              elif clave == 'ERROR_PROVEEDOR'or clave == '3':
                     return self.tipo3
              elif clave == 'FRAUDE'or clave == '4':
                     return self.tipo4
              elif clave == 'SIN_IDENTIFICAR'or clave == '5':
                     return self.tipo5

       def mostrar(self):
              print("SVM - Recall tipo 0 : ",self.tipo0)
              print("SVM - Recall tipo 1 : ",self.tipo1)
              print("SVM - Recall tipo 2 : ",self.tipo2)
              print("SVM - Recall tipo 3 : ",self.tipo3)
              print("SVM - Recall tipo 4 : ",self.tipo4)
              print("SVM - Recall tipo 5 : ",self.tipo5)
              print("\n")

class BAYES():
       def setTipoCero(self,value):
              self.tipo0 = value

       def setTipoUno(self,value):
              self.tipo1 = value

       def setTipoDos(self,value):
              self.tipo2 = value

       def setTipoTres(self,value):
              self.tipo3 = value                                 

       def setTipoCuatro(self,value):
              self.tipo4 = value

       def setTipoCinco(self,value):
              self.tipo5 = value

       def __init__(self):
           self.tipo0 = 0
           self.tipo1 = 0
           self.tipo2 = 0
           self.tipo3 = 0
           self.tipo4 = 0
           self.tipo5 = 0


       def setRecall(self,dic):
              self.setTipoCero(dic.get('DECISION_DE_NEGOCIO').get('recall'))
              self.setTipoUno(dic.get('DISCONFORMIDAD_CLIENTE').get('recall'))
              self.setTipoDos(dic.get('ERROR_DESPEGAR').get('recall'))
              self.setTipoTres(dic.get('ERROR_PROVEEDOR').get('recall'))
              self.setTipoCuatro(dic.get('FRAUDE').get('recall'))
              self.setTipoCinco(dic.get('SIN_IDENTIFICAR').get('recall'))


       def getRecall(self,clave):
              if clave == 'DECISION_DE_NEGOCIO' or clave == '0':
                     return self.tipo0
              elif clave == 'DISCONFORMIDAD_CLIENTE'or clave == '1':
                     return self.tipo1
              elif clave == 'ERROR_DESPEGAR'or clave == '2':
                     return self.tipo2
              elif clave == 'ERROR_PROVEEDOR'or clave == '3':
                     return self.tipo3
              elif clave == 'FRAUDE'or clave == '4':
                     return self.tipo4
              elif clave == 'SIN_IDENTIFICAR'or clave == '5':
                     return self.tipo5

       def mostrar(self):
              print("BAYES Recall tipo 0 : ",self.tipo0)
              print("BAYES Recall tipo 1 : ",self.tipo1)
              print("BAYES Recall tipo 2 : ",self.tipo2)
              print("BAYES Recall tipo 3 : ",self.tipo3)
              print("BAYES Recall tipo 4 : ",self.tipo4)
              print("BAYES Recall tipo 5 : ",self.tipo5)
              print("\n")

class BERT():
       def setTipoCero(self,value):
              self.tipo0 = value

       def setTipoUno(self,value):
              self.tipo1 = value

       def setTipoDos(self,value):
              self.tipo2 = value

       def setTipoTres(self,value):
              self.tipo3 = value                                 

       def setTipoCuatro(self,value):
              self.tipo4 = value

       def setTipoCinco(self,value):
              self.tipo5 = value

       def __init__(self):
           self.tipo0 = 0
           self.tipo1 = 0
           self.tipo2 = 0
           self.tipo3 = 0
           self.tipo4 = 0
           self.tipo5 = 0


       def setRecall(self,dic):
              self.setTipoCero(dic.get('DECISION_DE_NEGOCIO').get('recall'))
              self.setTipoUno(dic.get('DISCONFORMIDAD_CLIENTE').get('recall'))
              self.setTipoDos(dic.get('ERROR_DESPEGAR').get('recall'))
              self.setTipoTres(dic.get('ERROR_PROVEEDOR').get('recall'))
              self.setTipoCuatro(dic.get('FRAUDE').get('recall'))
              self.setTipoCinco(dic.get('SIN_IDENTIFICAR').get('recall'))

       def getRecall(self,clave):
              if clave == 'DECISION_DE_NEGOCIO' or clave == '0':
                     return self.tipo0
              elif clave == 'DISCONFORMIDAD_CLIENTE'or clave == '1':
                     return self.tipo1
              elif clave == 'ERROR_DESPEGAR'or clave == '2':
                     return self.tipo2
              elif clave == 'ERROR_PROVEEDOR'or clave == '3':
                     return self.tipo3
              elif clave == 'FRAUDE' or clave == '4':
                     return self.tipo4
              elif clave == 'SIN_IDENTIFICAR' or clave == '5':
                     return self.tipo5

       def mostrar(self):
              print("BERT Recall tipo 0 : ",self.tipo0)
              print("BERT Recall tipo 1 : ",self.tipo1)
              print("BERT Recall tipo 2 : ",self.tipo2)
              print("BERT Recall tipo 3 : ",self.tipo3)
              print("BERT Recall tipo 4 : ",self.tipo4)
              print("BERT Recall tipo 5 : ",self.tipo5)
              print("\n")


"""
       __ELECCIÓN DEL MEJOR MODELO DE CLASIFICACIÓN POR CADA TIPO__

       best_recall():
       Recibe como parámetros la clasificacion de tipos que predijo cada modelo y compara quien de los tres 
       tiene mayor recall, el modelo ganador devuelve su clasificacion
       Parámetros: - svm,bert,bayes son los OBJETOS INSTANCIADOS (guardados en un .pkl)
                   - tipoSVM,tipoBERT,tipoBAYES son los tipos que cada modelo predijo 

       best_recall_model():
       Aplica la misma lógica que best_recall pero en vez de retornar la clasificación del modelo ganador,
       devuelve el nombre del modelo            

"""
def best_recall(svm,bert,bayes,tipoSVM,tipoBERT,tipoBAYES):
       recallsvm = svm.getRecall(tipoSVM)
       recallbert = bert.getRecall(tipoBERT)       
       recallbayes = bayes.getRecall(tipoBAYES)
       if recallbayes > recallsvm and recallbayes > recallbert:
              return tipoBAYES
       elif recallsvm > recallbayes and recallsvm > recallbert:
              return tipoSVM
       elif recallbert > recallbayes and recallbert > recallsvm:
              return tipoBERT
       elif recallsvm == recallbert or recallsvm == recallbayes:
              return tipoSVM
       elif recallbayes == recallbert or recallbayes == recallsvm:
              return tipoBAYES       

def best_recall_model(svm,bert,bayes,tipoSVM,tipoBERT,tipoBAYES):
       recallsvm = svm.getRecall(tipoSVM)
       recallbert = bert.getRecall(tipoBERT)       
       recallbayes = bayes.getRecall(tipoBAYES)
       if recallbayes > recallsvm and recallbayes > recallbert:
              return 'NB'
       elif recallsvm > recallbayes and recallsvm > recallbert:
              return 'SVM'
       elif recallbert > recallbayes and recallbert > recallsvm:
              return 'BERT'
       elif recallsvm == recallbert or recallsvm == recallbayes:
              return 'SVM'
       elif recallbayes == recallbert or recallbayes == recallsvm:
              return 'BAYES'    


"""
       _____LÓGICA DE LA FUSIÓN DE MODELOS PARA SUBTIPOS____
       Definimos tres objetos: SVM() BAYES() Y BERT(), cuyos atributos de cada uno serán los subtipos de reclamos.
       
       Cada objeto cuenta con el método "setRecall()" el cual recibe como parámetro un diccionario, dicho
       diccionario es el que cada modelo obtiene a través de la métrica "Reporte de clasificacion" 
       (sklearn.metrics.classification_report) en donde se encuentra el recall del modelo para cada subtipo.
       El metodo setRecall() obtiene el recall de cada subtipo para asignar a los atributos correspondientes.

       Cada objeto también cuenta con el método "getRecall()" el cual recibe como parametro un nombre de subtipo, 
       y retorna su recall correspondiente.

       Por último, cada objeto tiene el método "mostrar()" el cual imprime por pantalla el recall de cada subtipo.
"""

class SVM_subtipos():
       
       def __init__(self):
           self.sub0 = 0
           self.sub1 = 0
           self.sub2 = 0
           self.sub3 = 0
           self.sub4 = 0
           self.sub5 = 0
           self.sub6 = 0
           self.sub7 = 0
           self.sub8 = 0
           self.sub9 = 0
           self.sub10 = 0
           self.sub11 = 0
           self.sub12 = 0
           self.sub13 = 0
           self.sub14 = 0
           self.sub15 = 0
           self.sub16 = 0
           self.sub17 = 0
           self.sub18 = 0
           self.sub19 = 0
           self.sub20 = 0
           self.sub21 = 0
           self.sub22 = 0
           self.sub23 = 0
           self.sub24 = 0
           self.sub25 = 0
           self.sub26 = 0
           self.sub27 = 0
           
       def setsub0(self,value):
              self.sub0 = value

       def setsub1(self,value):
              self.sub1 = value

       def setsub2(self,value):
              self.sub2 = value

       def setsub3(self,value):
              self.sub3 = value                                 

       def setsub4(self,value):
              self.sub4 = value

       def setsub5(self,value):
              self.sub5 = value

       def setsub6(self,value):
              self.sub6 = value

       def setsub7(self,value):
              self.sub7 = value

       def setsub8(self,value):
              self.sub8 = value

       def setsub9(self,value):
              self.sub9 = value                                 

       def setsub10(self,value):
              self.sub10 = value

       def setsub11(self,value):
              self.sub11 = value
       def setsub12(self,value):
              self.sub12 = value

       def setsub13(self,value):
              self.sub13 = value

       def setsub14(self,value):
              self.sub14 = value

       def setsub15(self,value):
              self.sub15 = value                                 

       def setsub16(self,value):
              self.sub16 = value

       def setsub17(self,value):
              self.sub17 = value

       def setsub18(self,value):
              self.sub18 = value

       def setsub19(self,value):
              self.sub19 = value

       def setsub20(self,value):
              self.sub20 = value

       def setsub21(self,value):
              self.sub21 = value                                 

       def setsub22(self,value):
              self.sub22 = value

       def setsub23(self,value):
              self.sub23 = value

       def setsub24(self,value):
              self.sub24 = value

       def setsub25(self,value):
              self.sub25 = value
              
 

       def setRecall(self,dic):
              self.setsub0(dic.get('CLIENTE_INSATISFECHO_CON_SERVICIO').get('recall'))
              self.setsub1(dic.get('COMPRA_DUPLICADA_ERROR_CLIENTE').get('recall'))
              self.setsub2(dic.get('ERROR_CLIENTE').get('recall'))
              self.setsub3(dic.get('ERROR_EN_LA_TARJETA').get('recall'))
              self.setsub4(dic.get('FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR').get('recall'))
              self.setsub5(dic.get('FRANQUICIA_DE_EQUIPAJE').get('recall'))
              self.setsub6(dic.get('FUERZA_MAYOR').get('recall'))
              self.setsub7(dic.get('INGRESO_DE_DATOS_INCORRECTOS').get('recall'))
              self.setsub8(dic.get('MALAS_CONDICIONES_DE_SERVICIO_PRESTADO').get('recall'))
              self.setsub9(dic.get('NO_SHOW').get('recall'))
              self.setsub10(dic.get('POLITICA_DE_CANCELACION_O_CAMBIO').get('recall'))
              self.setsub12(dic.get('ERROR_DE_COBRO').get('recall'))
              self.setsub13(dic.get('ERROR_DE_EMISION').get('recall'))
              self.setsub14(dic.get('ERROR_DE_INFORMACION_PROVISTA').get('recall'))
              self.setsub15(dic.get('ERROR_DE_REEMISION').get('recall'))
              self.setsub16(dic.get('ERROR_FLUJO_TECNOLOGIA').get('recall'))
              self.setsub17(dic.get('INCUMPLIMIENTO_ACUERDO_CONCILIATORIO').get('recall'))
              self.setsub18(dic.get('PROBLEMA_EN_DEVOLUCION').get('recall'))
              self.setsub19(dic.get('DIFERENCIAS_PROVEEDOR').get('recall'))
              self.setsub20(dic.get('ERROR_EN_DEVOLUCION').get('recall'))
              self.setsub21(dic.get('ERROR_EN_LA_TARJETA2').get('recall'))
              self.setsub22(dic.get('INCUMPLIMIENTO_DEL_SERVICIO').get('recall'))
              self.setsub23(dic.get('OVERBOOKING').get('recall'))
              self.setsub24(dic.get('FRAUDE_AMIGABLE').get('recall'))              
              self.setsub25(dic.get('FRAUDE_RIESGO').get('recall')) 

       def getRecall(self,clave):
              if clave == 'CLIENTE_INSATISFECHO_CON_SERVICIO':
                     return self.sub0
              elif clave == 'COMPRA_DUPLICADA_ERROR_CLIENTE':
                     return self.sub1
              elif clave == 'ERROR_CLIENTE':
                     return self.sub2
              elif clave == 'ERROR_EN_LA_TARJETA':
                     return self.sub3
              elif clave == 'FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR':
                     return self.sub4
              elif clave == 'FRANQUICIA_DE_EQUIPAJE':
                     return self.sub5
              elif clave == 'FUERZA_MAYOR':
                     return self.sub6        
              elif clave == 'INGRESO_DE_DATOS_INCORRECTOS':
                     return self.sub7
              elif clave == 'MALAS_CONDICIONES_DE_SERVICIO_PRESTADO':
                     return self.sub8
              elif clave == 'NO_SHOW':
                     return self.sub9
              elif clave == 'POLITICA_DE_CANCELACION_O_CAMBIO':
                     return self.sub10
              elif clave == 'ERROR_DE_COBRO':
                     return self.sub12
              elif clave == 'ERROR_DE_EMISION':
                     return self.sub13
              elif clave == 'ERROR_DE_INFORMACION_PROVISTA':
                     return self.sub14
              elif clave == 'ERROR_DE_REEMISION':
                     return self.sub15
              elif clave == 'ERROR_FLUJO_TECNOLOGIA':
                     return self.sub16
              elif clave == 'INCUMPLIMIENTO_ACUERDO_CONCILIATORIO':
                     return self.sub17
              elif clave == 'PROBLEMA_EN_DEVOLUCION':
                     return self.sub18
              elif clave == 'DIFERENCIAS_PROVEEDOR':
                     return self.sub19
              elif clave == 'ERROR_EN_DEVOLUCION':
                     return self.sub20
              elif clave == 'ERROR_EN_LA_TARJETA2':
                     return self.sub21
              elif clave == 'INCUMPLIMIENTO_DEL_SERVICIO':
                     return self.sub22
              elif clave == 'OVERBOOKING':
                     return self.sub23
              elif clave == 'FRAUDE_AMIGABLE':
                     return self.sub24
              elif clave == 'FRAUDE_RIESGO':
                     return self.sub25
              elif clave == 'SIN_IDENTIFICAR':
                     return 0.30
              elif clave == 'LEY_DE_RETRACTO':
                     return 0.77


       def mostrar(self):
              print("SVM - CLIENTE_INSATISFECHO_CON_SERVICIO: ",self.sub0)
              print("SVM - COMPRA_DUPLICADA_ERROR_CLIENTE: ",self.sub1)
              print("SVM - ERROR_CLIENTE: ",self.sub2)
              print("SVM - ERROR_EN_LA_TARJETA: ",self.sub3)
              print("SVM - FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR: ",self.sub4)
              print("SVM - FRANQUICIA_DE_EQUIPAJE: ",self.sub5)
              print("SVM - FUERZA_MAYOR: ",self.sub6)
              print("SVM - INGRESO_DE_DATOS_INCORRECTOS: ",self.sub7)
              print("SVM - MALAS_CONDICIONES_DE_SERVICIO_PRESTADO: ",self.sub8)
              print("SVM - NO_SHOW: ",self.sub9)
              print("SVM - POLITICA_DE_CANCELACION_O_CAMBIO: ",self.sub10)
              print("SVM - ERROR_DE_COBRO: ",self.sub12)
              print("SVM - ERROR_DE_EMISION: ",self.sub13)
              print("SVM - ERROR_DE_INFORMACION_PROVISTA: ",self.sub14)
              print("SVM - ERROR_DE_REEMISION: ",self.sub15)
              print("SVM - ERROR_FLUJO_TECNOLOGIA: ",self.sub16)
              print("SVM - INCUMPLIMIENTO_ACUERDO_CONCILIATORIO: ",self.sub17)
              print("SVM - PROBLEMA_EN_DEVOLUCION: ",self.sub18)
              print("SVM - DIFERENCIAS_PROVEEDOR: ",self.sub19)
              print("SVM - ERROR_EN_DEVOLUCION: ",self.sub20)
              print("SVM - ERROR_EN_LA_TARJETA2: ",self.sub21)
              print("SVM - INCUMPLIMIENTO_DEL_SERVICIO: ",self.sub22)
              print("SVM - OVERBOOKING: ",self.sub23)
              print("SVM - FRAUDE_AMIGABLE: ",self.sub24)
              print("SVM - FRAUDE_RIESGO: ",self.sub25)

class BERT_subtipos():
       
       def __init__(self):
           self.sub0 = 0
           self.sub1 = 0
           self.sub2 = 0
           self.sub3 = 0
           self.sub4 = 0
           self.sub5 = 0
           self.sub6 = 0
           self.sub7 = 0
           self.sub8 = 0
           self.sub9 = 0
           self.sub10 = 0
           self.sub11 = 0
           self.sub12 = 0
           self.sub13 = 0
           self.sub14 = 0
           self.sub15 = 0
           self.sub16 = 0
           self.sub17 = 0
           self.sub18 = 0
           self.sub19 = 0
           self.sub20 = 0
           self.sub21 = 0
           self.sub22 = 0
           self.sub23 = 0
           self.sub24 = 0
           self.sub25 = 0
           self.sub26 = 0
           self.sub27 = 0
                  
       def setsub0(self,value):
              self.sub0 = value

       def setsub1(self,value):
              self.sub1 = value

       def setsub2(self,value):
              self.sub2 = value

       def setsub3(self,value):
              self.sub3 = value                                 

       def setsub4(self,value):
              self.sub4 = value

       def setsub5(self,value):
              self.sub5 = value

       def setsub6(self,value):
              self.sub6 = value

       def setsub7(self,value):
              self.sub7 = value

       def setsub8(self,value):
              self.sub8 = value

       def setsub9(self,value):
              self.sub9 = value                                 

       def setsub10(self,value):
              self.sub10 = value

       def setsub11(self,value):
              self.sub11 = value
       def setsub12(self,value):
              self.sub12 = value

       def setsub13(self,value):
              self.sub13 = value

       def setsub14(self,value):
              self.sub14 = value

       def setsub15(self,value):
              self.sub15 = value                                 

       def setsub16(self,value):
              self.sub16 = value

       def setsub17(self,value):
              self.sub17 = value

       def setsub18(self,value):
              self.sub18 = value

       def setsub19(self,value):
              self.sub19 = value

       def setsub20(self,value):
              self.sub20 = value

       def setsub21(self,value):
              self.sub21 = value                                 

       def setsub22(self,value):
              self.sub22 = value

       def setsub23(self,value):
              self.sub23 = value

       def setsub24(self,value):
              self.sub24 = value

       def setsub25(self,value):
              self.sub25 = value

       def setsub26(self,value):
              self.sub26 = value
              
       def setsub27(self,value):
              self.sub27 = value       


       def setRecall(self,dic):
              self.setsub0(dic.get('CLIENTE_INSATISFECHO_CON_SERVICIO').get('recall'))
              self.setsub1(dic.get('COMPRA_DUPLICADA_ERROR_CLIENTE').get('recall'))
              self.setsub2(dic.get('ERROR_CLIENTE').get('recall'))
              self.setsub3(dic.get('ERROR_EN_LA_TARJETA').get('recall'))
              self.setsub4(dic.get('FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR').get('recall'))
              self.setsub5(dic.get('FRANQUICIA_DE_EQUIPAJE').get('recall'))
              self.setsub6(dic.get('FUERZA_MAYOR').get('recall'))
              self.setsub7(dic.get('INGRESO_DE_DATOS_INCORRECTOS').get('recall'))
              self.setsub8(dic.get('MALAS_CONDICIONES_DE_SERVICIO_PRESTADO').get('recall'))
              self.setsub9(dic.get('NO_SHOW').get('recall'))
              self.setsub10(dic.get('POLITICA_DE_CANCELACION_O_CAMBIO').get('recall'))
              self.setsub12(dic.get('ERROR_DE_COBRO').get('recall'))
              self.setsub13(dic.get('ERROR_DE_EMISION').get('recall'))
              self.setsub14(dic.get('ERROR_DE_INFORMACION_PROVISTA').get('recall'))
              self.setsub15(dic.get('ERROR_DE_REEMISION').get('recall'))
              self.setsub16(dic.get('ERROR_FLUJO_TECNOLOGIA').get('recall'))
              self.setsub17(dic.get('INCUMPLIMIENTO_ACUERDO_CONCILIATORIO').get('recall'))
              self.setsub18(dic.get('PROBLEMA_EN_DEVOLUCION').get('recall'))
              self.setsub19(dic.get('DIFERENCIAS_PROVEEDOR').get('recall'))
              self.setsub20(dic.get('ERROR_EN_DEVOLUCION').get('recall'))
              self.setsub21(dic.get('ERROR_EN_LA_TARJETA2').get('recall'))
              self.setsub22(dic.get('INCUMPLIMIENTO_DEL_SERVICIO').get('recall'))
              self.setsub23(dic.get('OVERBOOKING').get('recall'))
              self.setsub24(dic.get('FRAUDE_AMIGABLE').get('recall'))              
              self.setsub25(dic.get('FRAUDE_RIESGO').get('recall')) 
              
       def getRecall(self,clave):
              if clave == 'CLIENTE_INSATISFECHO_CON_SERVICIO':
                     return self.sub0
              elif clave == 'COMPRA_DUPLICADA_ERROR_CLIENTE':
                     return self.sub1
              elif clave == 'ERROR_CLIENTE':
                     return self.sub2
              elif clave == 'ERROR_EN_LA_TARJETA':
                     return self.sub3
              elif clave == 'FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR':
                     return self.sub4
              elif clave == 'FRANQUICIA_DE_EQUIPAJE':
                     return self.sub5
              elif clave == 'FUERZA_MAYOR':
                     return self.sub6        
              elif clave == 'INGRESO_DE_DATOS_INCORRECTOS':
                     return self.sub7
              elif clave == 'MALAS_CONDICIONES_DE_SERVICIO_PRESTADO':
                     return self.sub8
              elif clave == 'NO_SHOW':
                     return self.sub9
              elif clave == 'POLITICA_DE_CANCELACION_O_CAMBIO':
                     return self.sub10
              elif clave == 'ERROR_DE_COBRO':
                     return self.sub12
              elif clave == 'ERROR_DE_EMISION':
                     return self.sub13
              elif clave == 'ERROR_DE_INFORMACION_PROVISTA':
                     return self.sub14
              elif clave == 'ERROR_DE_REEMISION':
                     return self.sub15
              elif clave == 'ERROR_FLUJO_TECNOLOGIA':
                     return self.sub16
              elif clave == 'INCUMPLIMIENTO_ACUERDO_CONCILIATORIO':
                     return self.sub17
              elif clave == 'PROBLEMA_EN_DEVOLUCION':
                     return self.sub18
              elif clave == 'DIFERENCIAS_PROVEEDOR':
                     return self.sub19
              elif clave == 'ERROR_EN_DEVOLUCION':
                     return self.sub20
              elif clave == 'ERROR_EN_LA_TARJETA2':
                     return self.sub21
              elif clave == 'INCUMPLIMIENTO_DEL_SERVICIO':
                     return self.sub22
              elif clave == 'OVERBOOKING':
                     return self.sub23
              elif clave == 'FRAUDE_AMIGABLE':
                     return self.sub24
              elif clave == 'FRAUDE_RIESGO':
                     return self.sub25
              elif clave == 'SIN_IDENTIFICAR':
                     return 0
              elif clave == 'LEY_DE_RETRACTO':
                     return 0
              
       def mostrar(self):
              print("BERT - CLIENTE_INSATISFECHO_CON_SERVICIO: ",self.sub0)
              print("BERT - COMPRA_DUPLICADA_ERROR_CLIENTE: ",self.sub1)
              print("BERT - ERROR_CLIENTE: ",self.sub2)
              print("BERT - ERROR_EN_LA_TARJETA: ",self.sub3)
              print("BERT - FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR: ",self.sub4)
              print("BERT - FRANQUICIA_DE_EQUIPAJE: ",self.sub5)
              print("BERT - FUERZA_MAYOR: ",self.sub6)
              print("BERT - INGRESO_DE_DATOS_INCORRECTOS: ",self.sub7)
              print("BERT - MALAS_CONDICIONES_DE_SERVICIO_PRESTADO: ",self.sub8)
              print("BERT - NO_SHOW: ",self.sub9)
              print("BERT - POLITICA_DE_CANCELACION_O_CAMBIO: ",self.sub10)
              print("BERT - ERROR_DE_COBRO: ",self.sub12)
              print("BERT - ERROR_DE_EMISION: ",self.sub13)
              print("BERT - ERROR_DE_INFORMACION_PROVISTA: ",self.sub14)
              print("BERT - ERROR_DE_REEMISION: ",self.sub15)
              print("BERT - ERROR_FLUJO_TECNOLOGIA: ",self.sub16)
              print("BERT - INCUMPLIMIENTO_ACUERDO_CONCILIATORIO: ",self.sub17)
              print("BERT - PROBLEMA_EN_DEVOLUCION: ",self.sub18)
              print("BERT - DIFERENCIAS_PROVEEDOR: ",self.sub19)
              print("BERT - ERROR_EN_DEVOLUCION: ",self.sub20)
              print("BERT - ERROR_EN_LA_TARJETA2: ",self.sub21)
              print("BERT - INCUMPLIMIENTO_DEL_SERVICIO: ",self.sub22)
              print("BERT - OVERBOOKING: ",self.sub23)
              print("BERT - FRAUDE_AMIGABLE: ",self.sub24)
              print("BERT - FRAUDE_RIESGO: ",self.sub25)

class BAYES_subtipos():
       def setsub0(self,value):
              self.sub0 = value

       def setsub1(self,value):
              self.sub1 = value

       def setsub2(self,value):
              self.sub2 = value

       def setsub3(self,value):
              self.sub3 = value                                 

       def setsub4(self,value):
              self.sub4 = value

       def setsub5(self,value):
              self.sub5 = value

       def setsub6(self,value):
              self.sub6 = value

       def setsub7(self,value):
              self.sub7 = value

       def setsub8(self,value):
              self.sub8 = value

       def setsub9(self,value):
              self.sub9 = value                                 

       def setsub10(self,value):
              self.sub10 = value

       def setsub11(self,value):
              self.sub11 = value

       def setsub12(self,value):
              self.sub12 = value

       def setsub13(self,value):
              self.sub13 = value

       def setsub14(self,value):
              self.sub14 = value

       def setsub15(self,value):
              self.sub15 = value                                 

       def setsub16(self,value):
              self.sub16 = value

       def setsub17(self,value):
              self.sub17 = value

       def setsub18(self,value):
              self.sub18 = value

       def setsub19(self,value):
              self.sub19 = value

       def setsub20(self,value):
              self.sub20 = value

       def setsub21(self,value):
              self.sub21 = value                                 

       def setsub22(self,value):
              self.sub22 = value

       def setsub23(self,value):
              self.sub23 = value

       def setsub24(self,value):
              self.sub24 = value

       def setsub25(self,value):
              self.sub25 = value

       def setsub26(self,value):
              self.sub26 = value
              
       def setsub27(self,value):
              self.sub27 = value


       def __init__(self):
           self.sub0 = 0
           self.sub1 = 0
           self.sub2 = 0
           self.sub3 = 0
           self.sub4 = 0
           self.sub5 = 0
           self.sub6 = 0
           self.sub7 = 0
           self.sub8 = 0
           self.sub9 = 0
           self.sub10 = 0
           self.sub11 = 0
           self.sub12 = 0
           self.sub13 = 0
           self.sub14 = 0
           self.sub15 = 0
           self.sub16 = 0
           self.sub17 = 0
           self.sub18 = 0
           self.sub19 = 0
           self.sub20 = 0
           self.sub21 = 0
           self.sub22 = 0
           self.sub23 = 0
           self.sub24 = 0
           self.sub25 = 0

       def setRecall(self,dic):
              self.setsub0(dic.get('CLIENTE_INSATISFECHO_CON_SERVICIO').get('recall'))
              self.setsub1(dic.get('COMPRA_DUPLICADA_ERROR_CLIENTE').get('recall'))
              self.setsub2(dic.get('ERROR_CLIENTE').get('recall'))
              self.setsub3(dic.get('ERROR_EN_LA_TARJETA').get('recall'))
              self.setsub4(dic.get('FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR').get('recall'))
              self.setsub5(dic.get('FRANQUICIA_DE_EQUIPAJE').get('recall'))
              self.setsub6(dic.get('FUERZA_MAYOR').get('recall'))
              self.setsub7(dic.get('INGRESO_DE_DATOS_INCORRECTOS').get('recall'))
              self.setsub8(dic.get('MALAS_CONDICIONES_DE_SERVICIO_PRESTADO').get('recall'))
              self.setsub9(dic.get('NO_SHOW').get('recall'))
              self.setsub10(dic.get('POLITICA_DE_CANCELACION_O_CAMBIO').get('recall'))
              self.setsub12(dic.get('ERROR_DE_COBRO').get('recall'))
              self.setsub13(dic.get('ERROR_DE_EMISION').get('recall'))
              self.setsub14(dic.get('ERROR_DE_INFORMACION_PROVISTA').get('recall'))
              self.setsub15(dic.get('ERROR_DE_REEMISION').get('recall'))
              self.setsub16(dic.get('ERROR_FLUJO_TECNOLOGIA').get('recall'))
              self.setsub17(dic.get('INCUMPLIMIENTO_ACUERDO_CONCILIATORIO').get('recall'))
              self.setsub18(dic.get('PROBLEMA_EN_DEVOLUCION').get('recall'))
              self.setsub19(dic.get('DIFERENCIAS_PROVEEDOR').get('recall'))
              self.setsub20(dic.get('ERROR_EN_DEVOLUCION').get('recall'))
              self.setsub21(dic.get('ERROR_EN_LA_TARJETA2').get('recall'))
              self.setsub22(dic.get('INCUMPLIMIENTO_DEL_SERVICIO').get('recall'))
              self.setsub23(dic.get('OVERBOOKING').get('recall'))
              self.setsub24(dic.get('FRAUDE_AMIGABLE').get('recall'))              
              self.setsub25(dic.get('FRAUDE_RIESGO').get('recall')) 
              
       def getRecall(self,clave):
              if clave == 'CLIENTE_INSATISFECHO_CON_SERVICIO':
                     return self.sub0
              elif clave == 'COMPRA_DUPLICADA_ERROR_CLIENTE':
                     return self.sub1
              elif clave == 'ERROR_CLIENTE':
                     return self.sub2
              elif clave == 'ERROR_EN_LA_TARJETA':
                     return self.sub3
              elif clave == 'FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR':
                     return self.sub4
              elif clave == 'FRANQUICIA_DE_EQUIPAJE':
                     return self.sub5
              elif clave == 'FUERZA_MAYOR':
                     return self.sub6        
              elif clave == 'INGRESO_DE_DATOS_INCORRECTOS':
                     return self.sub7
              elif clave == 'MALAS_CONDICIONES_DE_SERVICIO_PRESTADO':
                     return self.sub8
              elif clave == 'NO_SHOW':
                     return self.sub9
              elif clave == 'POLITICA_DE_CANCELACION_O_CAMBIO':
                     return self.sub10
              elif clave == 'ERROR_DE_COBRO':
                     return self.sub12
              elif clave == 'ERROR_DE_EMISION':
                     return self.sub13
              elif clave == 'ERROR_DE_INFORMACION_PROVISTA':
                     return self.sub14
              elif clave == 'ERROR_DE_REEMISION':
                     return self.sub15
              elif clave == 'ERROR_FLUJO_TECNOLOGIA':
                     return self.sub16
              elif clave == 'INCUMPLIMIENTO_ACUERDO_CONCILIATORIO':
                     return self.sub17
              elif clave == 'PROBLEMA_EN_DEVOLUCION':
                     return self.sub18
              elif clave == 'DIFERENCIAS_PROVEEDOR':
                     return self.sub19
              elif clave == 'ERROR_EN_DEVOLUCION':
                     return self.sub20
              elif clave == 'ERROR_EN_LA_TARJETA2':
                     return self.sub21
              elif clave == 'INCUMPLIMIENTO_DEL_SERVICIO':
                     return self.sub22
              elif clave == 'OVERBOOKING':
                     return self.sub23
              elif clave == 'FRAUDE_AMIGABLE':
                     return self.sub24
              elif clave == 'FRAUDE_RIESGO':
                     return self.sub25
              elif clave == 'SIN_IDENTIFICAR':
                     return 0
              elif clave == 'LEY_DE_RETRACTO':
                     return 0.8
              
       def mostrar(self):
              print("BAYES - CLIENTE_INSATISFECHO_CON_SERVICIO: ",self.sub0)
              print("BAYES - COMPRA_DUPLICADA_ERROR_CLIENTE: ",self.sub1)
              print("BAYES - ERROR_CLIENTE: ",self.sub2)
              print("BAYES - ERROR_EN_LA_TARJETA: ",self.sub3)
              print("BAYES - FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR: ",self.sub4)
              print("BAYES - FRANQUICIA_DE_EQUIPAJE: ",self.sub5)
              print("BAYES - FUERZA_MAYOR: ",self.sub6)
              print("BAYES - INGRESO_DE_DATOS_INCORRECTOS: ",self.sub7)
              print("BAYES - MALAS_CONDICIONES_DE_SERVICIO_PRESTADO: ",self.sub8)
              print("BAYES - NO_SHOW: ",self.sub9)
              print("BAYES - POLITICA_DE_CANCELACION_O_CAMBIO: ",self.sub10)
              print("BAYES - ERROR_DE_COBRO: ",self.sub12)
              print("BAYES - ERROR_DE_EMISION: ",self.sub13)
              print("BAYES - ERROR_DE_INFORMACION_PROVISTA: ",self.sub14)
              print("BAYES - ERROR_DE_REEMISION: ",self.sub15)
              print("BAYES - ERROR_FLUJO_TECNOLOGIA: ",self.sub16)
              print("BAYES - INCUMPLIMIENTO_ACUERDO_CONCILIATORIO: ",self.sub17)
              print("BAYES - PROBLEMA_EN_DEVOLUCION: ",self.sub18)
              print("BAYES - DIFERENCIAS_PROVEEDOR: ",self.sub19)
              print("BAYES - ERROR_EN_DEVOLUCION: ",self.sub20)
              print("BAYES - ERROR_EN_LA_TARJETA2: ",self.sub21)
              print("BAYES - INCUMPLIMIENTO_DEL_SERVICIO: ",self.sub22)
              print("BAYES - OVERBOOKING: ",self.sub23)
              print("BAYES - FRAUDE_AMIGABLE: ",self.sub24)
              print("BAYES - FRAUDE_RIESGO: ",self.sub25)




"""
       __ELECCIÓN DEL MEJOR MODELO DE CLASIFICACIÓN POR CADA SUBTIPO__

       best_recall_subtipos():
       Recibe como parámetros la clasificacion de subtipos que predijo cada modelo y compara quien de los tres 
       tiene mayor recall, el modelo ganador devuelve su clasificacion
       Parámetros: - svm,bert,bayes son los OBJETOS INSTANCIADOS (guardados en un .pkl)
                   - subtipoSVM,subtipoBERT,subtipoBAYES son los subtipos que cada modelo predijo 

       best_recall_subtipos_model():
       Aplica la misma lógica que best_recall pero en vez de retornar la clasificación del modelo ganador,
       devuelve el nombre del modelo            

"""

def best_recall_subtipos(svm,bert,bayes,subtipoSVM,subtipoBERT,subtipoBAYES):
       recallsvm = svm.getRecall(subtipoSVM)
       recallbert = bert.getRecall(subtipoBERT)       
       recallbayes = bayes.getRecall(subtipoBAYES)
       if recallbayes > recallsvm and recallbayes > recallbert:
              return subtipoBAYES
       elif recallsvm > recallbayes and recallsvm > recallbert:
              return subtipoSVM
       elif recallbert > recallbayes and recallbert > recallsvm:
              return subtipoBERT
       elif recallsvm == recallbert or recallsvm == recallbayes:
              return subtipoSVM
       elif recallbayes == recallbert or recallbayes == recallsvm:
              return subtipoBAYES       

def best_recall_subtipos_model(svm,bert,bayes,subtipoSVM,subtipoBERT,subtipoBAYES):
       recallsvm = svm.getRecall(subtipoSVM)
       recallbert = bert.getRecall(subtipoBERT)       
       recallbayes = bayes.getRecall(subtipoBAYES)
       if recallbayes > recallsvm and recallbayes > recallbert:
              return 'NB'
       elif recallsvm > recallbayes and recallsvm > recallbert:
              return 'SVM'
       elif recallbert > recallbayes and recallbert > recallsvm:
              return 'BERT'
       elif recallsvm == recallbert or recallsvm == recallbayes:
              return 'SVM'
       elif recallbayes == recallbert or recallbayes == recallsvm:
              return 'BAYES'    