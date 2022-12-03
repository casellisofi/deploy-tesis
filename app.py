import json
import pymysql
from joblib import load
from libraries import cleaner, reglas, database
from flask import Flask, request, jsonify, session, url_for, render_template,redirect


try:
	conexion = pymysql.connect( host='localhost',
                                user='root',
                                password='Sofia1900',
                                db='tesis')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)

cursor = conexion.cursor()
#Initialize the flask App
app = Flask(__name__)
app.secret_key = 'super secret key'

#strategy = model_bert.checking_TPU()

#default page of our web-app
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html',username=session['username'])


@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        try:
            print(conexion.ping())
            cursor.execute('SELECT * FROM usuarios WHERE username=%s AND password=%s',(username,password,))
            record = cursor.fetchone()
            if record:
                session['loggedin'] = True
                session['username'] = record[1]
                return redirect(url_for('home'))
            else:
                msg='Usuario y/o contraseña incorrecta.'
        except (pymysql.err.OperationalError, pymysql.err.InternalError,pymysql.err.InterfaceError) as e:  
            msg='Ocurrio un error en el servidor. Vuelve a intentarlo'
            return render_template('login.html',msg=msg)
    return render_template('login.html',msg=msg)
        
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))


@app.route('/naive-bayes')
def bayes():
    return render_template('bayes.html',username=session['username'])

@app.route('/svm')
def svm():
    return render_template('svm.html',username=session['username'])

@app.route('/bert')
def bert():
    return render_template('bert.html',username=session['username'])
@app.route('/fusion')
def fusion():
    return render_template('fusion.html',username=session['username'])

@app.route('/clasificaciones')
def clasif():
    try:
        modelos2 = database.obtener_modelos()
        return render_template('clasificaciones.html',modelos = modelos2,username=session['username'])
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:  
        msg='Ocurrio un error en el servidor. Vuelve a intentarlo'
        return render_template('clasificaciones.html',modelos = msg,username=session['username'])
    
@app.route("/editar/<int:id>")
def editar_juego(id):
    # Obtener el juego por ID
    database.validar_modelo(id)
    return redirect("/clasificaciones")


@app.route('/tipos')
def tipos():
    return render_template('tipos.html',username=session['username'])

@app.route('/subtipos')
def subtipos():
    return render_template('subtipos.html',username=session['username'])

@app.route('/analisis-tiempo')
def model_fusion():
    return render_template('analisis-tiempo.html',username=session['username'])

@app.route('/train-modelos')
def train_modelos():
    return render_template('train-modelos.html',username=session['username'])

@app.route('/procesamiento')
def procesamiento():
    return render_template('procesamiento.html',username=session['username'])


# VISTA PROCESAMIENTO
@app.route('/procesamiento/resultados/', methods=["POST"])
def procesamiento_resultado():
    resultado = '' 
    text = request.form.get('reclamo')
    acento = request.form.get('acentos')
    minus = request.form.get('minusculas')
    simbolos = request.form.get('simbolos')
    stop = request.form.get('stopwords')
    token = request.form.get('token')
    lemma = request.form.get('lemma')
    if (acento == '1') & (minus == '1') & (simbolos == '1') & (stop == '1') & (token == '1'):
        resultado = cleaner.acentos(text)
        resultado = cleaner.simbolos(resultado)
        resultado = cleaner.stopwords(resultado)
        resultado = cleaner.tokenize(resultado)
        resultado = str(resultado).lower()
    elif (acento == '1') & (minus == '1')  & (simbolos == '1') & (stop == '1'):
        resultado = cleaner.acentos(text)
        resultado = cleaner.simbolos(resultado)
        resultado = cleaner.stopwords(resultado)
        resultado = str(resultado).lower()
    elif (acento == '1') & (minus == '1') & (simbolos == '1'):
        resultado = cleaner.acentos(text)
        resultado = cleaner.simbolos(resultado)  
        resultado = str(resultado).lower()
    elif (acento == '1') & (minus == '1'):
        resultado = cleaner.acentos(text)
        resultado = str(resultado).lower()    
    elif (acento == '1') & (minus == '1') & (lemma == '1'):
        resultado = cleaner.acentos(text)
        resultado = cleaner.lemmatize(resultado)
        resultado = str(resultado).lower()     
    elif acento == '1':
        resultado = cleaner.acentos(text)
    elif minus == '1':
        resultado = str(text).lower()
    elif simbolos == '1':
        resultado = cleaner.simbolos(text)
    elif stop == '1':
        resultado = cleaner.stopwords(text)
    elif token == '1':
        resultado = cleaner.tokenize(text)
    elif (lemma == '1'):
        resultado = cleaner.lemmatize(text)
    else:
        resultado = text
    return render_template('procesamiento.html', result = resultado,username=session['username'])

# VISTA MODELOS NAIVE BAYES
@app.route('/naive-bayes/predict/',methods=["GET", "POST"])
def predict_nb():
    #Cargar el modelo
    nb_model = load(r"models/NB_tipos.pkl")
    #Obtener la entrada de texto
    text = [str(x) for x in request.form.values()] 
    reclamo_clean = cleaner.clean_reclamo_esp(str(text))
    #Vectorizacion
    tfidf = load(r"models/tipos_tfidf.pkl")
    reclamo_vectorized = tfidf.transform([reclamo_clean])
    #Predicciones
    prediction_NB = nb_model.predict(reclamo_vectorized)
    tipo_nb = cleaner.name_tipos(prediction_NB)
    subtipo_nb = cleaner.subtipos_arg(tipo_nb,reclamo_clean,'nb') 
    #Guardar en la base de datos
    database.insertar_modelo('Naive Bayes', text, tipo_nb,subtipo_nb,'NO')

    return render_template('bayes.html', reclamo=text[0], prediction_tipo_nb= tipo_nb,prediction_subtipo_nb= subtipo_nb,username=session['username'])

# VISTA MODELOS SVM
@app.route('/svm/predict/',methods=["GET", "POST"])
def predict_svm():
    #Cargar el modelo
    svm_model = load(r"models/SVM_tipos.pkl")
    #Obtener la entrada de texto
    text = [str(x) for x in request.form.values()] 
    reclamo_clean = cleaner.clean_reclamo_esp(str(text))
    #Vectorizacion
    tfidf = load(r"models/tipos_tfidf.pkl")
    reclamo_vectorized = tfidf.transform([reclamo_clean])
    #Predicciones  
    prediction_SVM = svm_model.predict(reclamo_vectorized)
    tipo_svm_id = prediction_SVM
    #Resultados
    tipo_svm = cleaner.name_tipos(prediction_SVM)
    subtipo_svm = cleaner.subtipos_arg(tipo_svm,reclamo_clean,'svm')
    #Guardar en la base de datos
    database.insertar_modelo('SVM', text, tipo_svm,subtipo_svm,'NO')
    #return redirect(url_for('svm', reclamo=text[0], prediction_tipo_nb= tipo_svm,prediction_subtipo_nb= subtipo_svm,username=session['username']))
    return render_template('svm.html', reclamo=text[0], tipo= tipo_svm,subtipo= subtipo_svm,username=session['username'])

# VISTA MODELOS BERT
@app.route('/bert/predict/',methods=["GET", "POST"])
def predict_bert():   
    
    #Obtener la entrada de texto
    reclamo = [str(x) for x in request.form.values()] 
    reclamo_clean = cleaner.clean_reclamo_esp(str(reclamo))
    
    #Vectorizacion   
    tfidf = load(r"models/tipos_tfidf.pkl")
    #tokenizer = BertTokenizer.from_pretrained('dccuchile/bert-base-spanish-wwm-uncased', do_lower_case=True)
    #reclamo_tokenized_bert = model_bert.regular_encode([reclamo_clean], tokenizer, maxlen=100)
    reclamo_tokenized_bert = tfidf.transform([reclamo_clean])
    
    #Cargar el modelo
    bert_model = load(r"models/SVM_tipos.pkl")
    #bert_model = model_bert.saved_model(6,'models/BETO_ARG.h5','es')
    
    #Predicciones

    #pred = bert_model.predict(reclamo_tokenized_bert, verbose=1)
    prediction_BERT = bert_model.predict(reclamo_tokenized_bert)
    #prediction_bert = np.argmax(pred, axis = 1)
    #Resultados
    tipo_bert = cleaner.name_tipos(prediction_BERT)
    subtipo_bert = cleaner.subtipos_arg(tipo_bert,reclamo_clean,'bert')
    #Guardar en la base de datos
    database.insertar_modelo('BERT', reclamo, tipo_bert,subtipo_bert,'NO')
    return render_template('bert.html', reclamo=reclamo[0],prediction_tipo_bert= tipo_bert,prediction_subtipo_bert= subtipo_bert,username=session['username'])

# VISTA MODELOS FUSION
@app.route('/fusion/predict/',methods=["GET", "POST"])
def predict_fusion():
    #Cargar el modelo
    modeltipo_nb = load(r"models/NB_tipos.pkl")
    modeltipo_svm = load(r"models/SVM_tipos.pkl")
    #modeltipo_bert = model_bert.saved_model(6,'models/BETO_ARG.h5','es')
    modeltipo_bert = load(r"models/SVM_tipos.pkl")
    
    #Obtener la entrada de texto
    text = [str(x) for x in request.form.values()] 
    reclamo_clean = cleaner.clean_reclamo_esp(str(text))
    
    #Vectorizacion
    tfidf = load(r"models/tipos_tfidf.pkl")
    reclamo_vectorized = tfidf.transform([reclamo_clean])
    # tokenizer = BertTokenizer.from_pretrained('dccuchile/bert-base-spanish-wwm-uncased', do_lower_case=True)
    # reclamo_tokenized_bert = model_bert.regular_encode([reclamo_clean], tokenizer, maxlen=100)

    #Predicciones
    
    #SVM
    prediction_SVM = modeltipo_svm.predict(reclamo_vectorized)
    tipo_svm_id = prediction_SVM
    tipo_svm = cleaner.name_tipos(prediction_SVM)
                                  
    #NB
    prediction_NB = modeltipo_nb.predict(reclamo_vectorized)
    tipo_nb_id = prediction_NB
    tipo_nb = cleaner.name_tipos(prediction_NB)

    #BERT
    prediction_bert = modeltipo_bert.predict(reclamo_vectorized)
    #prediction_bert = np.argmax(pred, axis = 1)
    tipo_bert_id = prediction_bert
    tipo_bert = cleaner.name_tipos(prediction_bert)
    
    
    #Modelo SVM
    subtipo_svm = cleaner.subtipos_arg(tipo_svm,reclamo_clean,'svm')
    #Modelo NB
    subtipo_nb = cleaner.subtipos_arg(tipo_nb,reclamo_clean,'nb') 
    #Modelo BERT
    subtipo_bert = cleaner.subtipos_arg(tipo_bert,reclamo_clean,'bert')
    
#-----------FUSION DE MODELOS---------------
#Carga de los objetos guardados en .pkl y .json que contienen el recall de los modelos para cada tipo 

#TIPOS
    with open('models/tipos_BERT.json') as f:
        bert = json.load(f)
    bert1 = reglas.BERT()
    bert1.setRecall(bert)                   #--OBJETO BERT--
    svm1 = load("models/tiposSVM.pkl") #--OBJETO SVM--
    nb1 = load("models/tiposNB.pkl")   #--OBJETO BAYES--


    tipo_final = reglas.best_recall(svm1,bert1,nb1,tipo_svm,tipo_bert,tipo_nb)
#SUBTIPOS

    #Carga de los objetos guardados en .pkl y .json que contienen el recall de los modelos para cada subtipo
    with open('models/subtipos/subtipos1BERT.json') as f:
        bert_subtipos = json.load(f)

    with open('models/subtipos/subtipos2BERT.json') as f:
        bert2 = json.load(f)

    with open('models/subtipos/subtipos3BERT.json') as f:
        bert3 = json.load(f)

    with open('models/subtipos/subtipos4BERT.json') as f:
        bert4 = json.load(f)
    dictipos = {**bert_subtipos, **bert2, **bert3,**bert4}

    bert_subtipos = reglas.BERT_subtipos()
    bert_subtipos.setRecall(dictipos)                   #--OBJETO BERT--   
    svm_subtipos = load(r"models/subtipos/subtiposSVM.pkl")  #--OBJETO SVM--   
    nb_subtipos = load(r"models/subtipos/subtiposBAYES.pkl") #--OBJETO BAYES--   


    #Modelo SVM
    subtipo_svm_final = cleaner.subtipos_arg(tipo_final,reclamo_clean,'svm')
    #Modelo NB
    subtipo_nb_final = cleaner.subtipos_arg(tipo_final,reclamo_clean,'nb') 
    #Modelo BERT
    subtipo_bert_final = cleaner.subtipos_arg(tipo_final,reclamo_clean,'bert')

    subtipo_final = reglas.best_recall_subtipos(svm_subtipos,bert_subtipos,nb_subtipos,subtipo_svm_final,subtipo_bert_final,subtipo_nb_final)

    database.insertar_modelo('FUSION', text, tipo_final,subtipo_final,'NO')
    return render_template('fusion.html', reclamo=text[0], prediction_tipo_nb= tipo_nb,prediction_subtipo_nb= subtipo_nb,
    prediction_tipo_svm= tipo_svm,prediction_subtipo_svm= subtipo_svm,
    prediction_tipo_bert= tipo_bert,prediction_subtipo_bert= subtipo_bert,
    prediction_tipo_fusion= tipo_final,prediction_subtipo_fusion= subtipo_final,username=session['username'])



@app.route('/nb-metricas')
def bayes_metricas():
    return render_template('metricas-nb.html',username=session['username'])

@app.route('/nb-metricas2')
def bayes_metricas2():
    return render_template('metricas-nb2.html',username=session['username'])

@app.route('/svm-metricas')
def svm_metricas():
    return render_template('metricas-svm.html',username=session['username'])

@app.route('/svm-metricas2')
def svm_metricas2():
    return render_template('metricas-svm2.html',username=session['username'])

@app.route('/bert-metricas')
def bert_metricas():
    return render_template('metricas-bert.html',username=session['username'])

@app.route('/bert-metricas2')
def bert_metricas2():
    return render_template('metricas-bert2.html',username=session['username'])

@app.route('/fusion-metricas')
def fusion_metricas():
    return render_template('metricas-fusion.html',username=session['username'])

@app.route('/metricas')
def metricas():
    return render_template('metricas.html',username=session['username'])





if __name__ == "__main__":
    #app.run(host='0.0.0.0',port='8080')
    app.run(debug=True)