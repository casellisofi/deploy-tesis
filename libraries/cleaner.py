from libraries import *
#from libraries import model_bert



#Diccionarios de subtipos
subtipos1 =  {0: 'CLIENTE_INSATISFECHO_CON_SERVICIO',1: 'COMPRA_DUPLICADA_ERROR_CLIENTE',
              2:'ERROR_CLIENTE',3:'ERROR_EN_LA_TARJETA',4:'FALTA_DOCUMENTACION_VACUNAS_PARA_EMBARCAR',5:'FRANQUICIA_DE_EQUIPAJE',
              6:'FUERZA_MAYOR',7:'INGRESO_DE_DATOS_INCORRECTOS', 8: 'MALAS_CONDICIONES_DE_SERVICIO_PRESTADO',9:'NO_SHOW',
              10:'POLITICA_DE_CANCELACION_O_CAMBIO'}
subtipos2 = {0:'ERROR_DE_COBRO',1:'ERROR_DE_EMISION',2:'ERROR_DE_INFORMACION_PROVISTA', 
             3:'ERROR_DE_REEMISION', 4:'ERROR_FLUJO_TECNOLOGIA',5:'INCUMPLIMIENTO_ACUERDO_CONCILIATORIO', 6:'PROBLEMA_EN_DEVOLUCION'}
subtipos3 = {0:'DIFERENCIAS_PROVEEDOR',1:'ERROR_EN_DEVOLUCION',2:'ERROR_EN_LA_TARJETA',3:'INCUMPLIMIENTO_DEL_SERVICIO', 4:'OVERBOOKING'}
subtipos4 = {0:'FRAUDE_AMIGABLE',1:'FRAUDE_RIESGO'}



#nlp = spacy.load('es_core_news_sm')

def acentos(text):
    text = str(unicodedata.normalize('NFKD', text).encode('ascii','ignore'))[2:-1]
    return text

    
def simbolos(text):
    text = re.sub('\[.*?¿\]\%', ' ', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…«»]', '', text)
    text = re.sub('\n', ' ', text)
    text = re.sub('\r', ' ', text)
    return text

def tokenize(text):
    text1 = nltk.tokenize.word_tokenize(text)
    return text1


def lemmatize(text):
#     text = nlp(text)
#     text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
     return text


#Aplica técnicas de limpieza de reclamoo para reclamos en ESPAÑOL
#Pasa el reclamoo a minúsculas, elimina simbolos, la letra ñ, corchetes, acentos, signos de puntuación adicionales y números.
def clean_reclamo_esp(reclamo):
    reclamo = reclamo.lower()
    reclamo = re.sub('\[.*?¿\]\%', ' ', reclamo)
    reclamo = re.sub('[%s]' % re.escape(string.punctuation), ' ', reclamo)
    reclamo = re.sub('\w*\d\w*', '', reclamo)
    reclamo = re.sub('[‘’“”…«»]', '', reclamo)
    reclamo = re.sub('\n', ' ', reclamo)
    reclamo = re.sub('\r', ' ', reclamo)
    reclamo = reclamo.replace('Ñ','N')
    reclamo = str(unicodedata.normalize('NFKD', reclamo).encode('ascii','ignore'))[2:-1]
    reclamo = reclamo.replace('ñ','n')
    reclamo = reclamo.replace('\t','')
    return reclamo
    
#Stop words en español
stop = stopwords.words('spanish')
stop.append('com')
stop.append('ar')
stop.append('nan')
stop.append('hotmail')
stop.append('gmail')
stop.append('vicky')
stop.append('sahagn lisandromonestes')
stop.append('sahagn')
stop.append('ic')
stop.append('despagar')
stop.append('depegar')
stop.append('s')
stop.append('ss')
stop.append('pa')
stop.append('ta')
stop.append('rs')
stop.append('aeros')

#Elimina las palabras que no son importantes 
def stopwords(text):
    text = [word.lower() for word in text.split() if word.lower() not in stop]
    return " ".join(text)
    #return text

#Elimina las palabras que no son importantes (stopwords)
def remove_stopwords_esp(reclamo):
    reclamo = [word.lower() for word in reclamo.split() if word.lower() not in stop]
    return " ".join(reclamo)


# #Aplica técnicas de limpieza de reclamoo para reclamos en PORTUGUES
# #Pasa el reclamoo a minúsculas, elimina simbolos, corchetes y números.
# def clean_reclamo_br(reclamo):
#     reclamo = reclamo.lower()
#     reclamo = re.sub('\[.*?¿\]\%', ' ', reclamo)
#     reclamo = re.sub('[%s]' % re.escape(string.punctuation), ' ', reclamo)
#     reclamo = re.sub('\w*\d\w*', '', reclamo)
#     reclamo = re.sub('[‘’“”…«»]', '', reclamo)
#     reclamo = re.sub('\n', ' ', reclamo)
#     reclamo = re.sub('\r', ' ', reclamo)
#     #reclamo = str(unicodedata.normalize('NFKD', reclamo).encode('ascii','ignore'))[2:-1]
#     reclamo = reclamo.replace('ñ','n')
#     reclamo = reclamo.replace('\t','')
#     return reclamo
    
# #Stop words en portugues
# stop_brasil = stopwords.words('portuguese')

# #Elimina las palabras que no son importantes (stopwords)
# def remove_stopwords_br(reclamo):
#     reclamo = [word.lower() for word in reclamo.split() if word.lower() not in stop_brasil]
#     return " ".join(reclamo)



#-------------------------CLASIFICACION DE TIPOS Y SUBTIPOS-----------------------------


#Retorna el nombre del tipo correspondiente a la etiqueta númerica
def name_tipos(tipo):
    if tipo == 0:
        name_tipo = 'DECISION_DE_NEGOCIO'
        return name_tipo
    elif tipo == 1:
        name_tipo = 'DISCONFORMIDAD_CLIENTE'
        return name_tipo
    elif tipo == 2:
        name_tipo = 'ERROR_DESPEGAR'
        return name_tipo
    elif tipo == 3:
        name_tipo = 'ERROR_PROVEEDOR'
        return name_tipo
    elif tipo == 4:
        name_tipo = 'FRAUDE'
        return name_tipo
    elif tipo == 5:
        name_tipo = 'SIN_IDENTIFICAR'
        return name_tipo
    
#Retorna el nombre del subtipo correspondiente a la etiqueta númerica
def name_subtipos(tipo,subtipo):
    if tipo == 1:
        return subtipos1.get(int(subtipo))
    elif tipo == 2:
        return subtipos2.get(int(subtipo))
    elif tipo == 3:
        return subtipos3.get(int(subtipo))
    elif tipo == 4:
        return subtipos4.get(int(subtipo))    
    

#Retorna la clasificación de subtipo en base al tipo y modelo de clasificacion que recibe de ARGENTINA
def subtipos_arg(tipo,reclamo,modelo):
    #tokenizer = BertTokenizer.from_pretrained('dccuchile/bert-base-spanish-wwm-uncased', do_lower_case=True)
    #reclamo_tokenized_bert = model_bert.regular_encode([reclamo], tokenizer, maxlen=100)
    if tipo == 'DECISION_DE_NEGOCIO':
        subtipo = 'LEY_DE_RETRACTO'
        return subtipo
    elif tipo == 'DISCONFORMIDAD_CLIENTE':
        tfidf1 = load(r"models/subtipos/tipo1_tfidf.pkl")
        vector = tfidf1.transform([reclamo])

        if modelo == 'nb':
                modeltipo1 = load(r"models/subtipos/NB_tipo1.pkl")
                subtipo = modeltipo1.predict(vector)
        elif modelo == 'svm':
                modeltipo1 = load(r"models/subtipos/SVM_tipo1.pkl")
                subtipo = modeltipo1.predict(vector)
        elif modelo == 'bert':
                #modeltipo1 = model_bert.saved_model(12,'models/subtipos/BERT_tipo1.h5','es')
                #pred = modeltipo1.predict(reclamo_tokenized_bert, verbose=1)
                #subtipo = np.argmax(pred, axis = 1)
                modeltipo1 = load(r"models/subtipos/SVM_tipo1.pkl")
                subtipo = modeltipo1.predict(vector)  
                              
        subtipo1 = name_subtipos(1,subtipo)
        return subtipo1

    elif tipo == 'ERROR_DESPEGAR':
        tfidf1 = load(r"models/subtipos/tipo2_tfidf.pkl")
        vector = tfidf1.transform([reclamo])
        
        if modelo == 'nb':
                modeltipo2 = load(r"models/subtipos/NB_tipo2.pkl")
                subtipo = modeltipo2.predict(vector)
        elif modelo == 'svm':
                modeltipo2 = load(r"models/subtipos/SVM_tipo2.pkl")
                subtipo = modeltipo2.predict(vector)
        elif modelo == 'bert':
                # modeltipo2 = model_bert.saved_model(7,'models/subtipos/BERT_tipo2.h5','es')
                # pred = modeltipo2.predict(reclamo_tokenized_bert, verbose=1)
                # subtipo = np.argmax(pred, axis = 1)
                modeltipo2 = load(r"models/subtipos/SVM_tipo2.pkl")
                subtipo = modeltipo2.predict(vector)
                
        subtipo2 = name_subtipos(2,subtipo)
        return subtipo2

    elif tipo == 'ERROR_PROVEEDOR':
        tfidf1 = load(r"models/subtipos/tipo3_tfidf.pkl")
        vector = tfidf1.transform([reclamo])
        
        if modelo == 'nb':
                modeltipo3 = load(r"models/subtipos/NB_tipo3.pkl")
                subtipo = modeltipo3.predict(vector)
        elif modelo == 'svm':
                modeltipo3 = load(r"models/subtipos/SVM_tipo3.pkl")
                subtipo = modeltipo3.predict(vector)
        elif modelo == 'bert':
                # modeltipo3 = model_bert.saved_model(5,'models/subtipos/BERT_tipo3.h5','es')
                # pred = modeltipo3.predict(reclamo_tokenized_bert, verbose=1)
                # subtipo = np.argmax(pred, axis = 1)
                modeltipo3 = load(r"models/subtipos/SVM_tipo3.pkl")
                subtipo = modeltipo3.predict(vector)
        subtipo3 = name_subtipos(3,subtipo)
        return subtipo3

    elif tipo == 'FRAUDE':
        tfidf1 = load(r"models/subtipos/tipo4_tfidf.pkl")
        vector = tfidf1.transform([reclamo])
        
        if modelo == 'nb':
                modeltipo4 = load(r"models/subtipos/NB_tipo4.pkl")
                subtipo = modeltipo4.predict(vector)
        elif modelo == 'svm':
                modeltipo4 = load(r"models/subtipos/SVM_tipo4.pkl")
                subtipo = modeltipo4.predict(vector)
        elif modelo == 'bert':
                # modeltipo4 = model_bert.saved_model(2,'models/subtipos/BERT_tipo4.h5','es')
                # pred = modeltipo4.predict(reclamo_tokenized_bert, verbose=1)
                # subtipo = np.argmax(pred, axis = 1)
                modeltipo4 = load(r"models/subtipos/SVM_tipo4.pkl")
                subtipo = modeltipo4.predict(vector)                
        subtipo4 = name_subtipos(4,subtipo)
        return subtipo4

    elif tipo == 'SIN_IDENTIFICAR':
        subtipo5 = 'SIN_IDENTIFICAR'
        return subtipo5
