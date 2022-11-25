# import tensorflow as tf
# import numpy as np
# import transformers

# # Chequea los recursos disponibles para la ejecucion 
# def checking_TPU():
#     try:
#         tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
#         print('Running on TPU ', tpu.master())
#     except ValueError:
#         tpu = None

#     if tpu:
#         tf.config.experimental_connect_to_cluster(tpu)
#         tf.tpu.experimental.initialize_tpu_system(tpu)
#         strategy = tf.distribute.TPUStrategy(tpu)
#         return strategy
#     else:
#         # Default distribution strategy in Tensorflow. Works on CPU and single GPU.
#         strategy = tf.distribute.get_strategy()
#         return strategy

# # Modelo con 12 neuronas, equivalente a la cantidad de subtipos
# def build_model(transformer, neuronas, max_len = 512, loss='categorical_crossentropy'):
#     input_word_ids = tf.keras.layers.Input(shape=(max_len,), dtype = tf.int32, name = "input_word_ids")
#     sequence_output = transformer(input_word_ids)[0]
#     cls_token = sequence_output[:, 0, :]
#     # Agrega una droput layer
#     x = tf.keras.layers.Dropout(0.3)(cls_token)
#     # Usa una dense layer de 'x' neuronas, que corresponde a la cantidad de tipos que poseemos.
#     # Si a futuro se añaden nuevos tipos, el número de neuronas debe modificarse.
#     out = tf.keras.layers.Dense(neuronas, activation='softmax')(x)
#     model = tf.keras.Model(inputs = input_word_ids, outputs = out)
#     # Usa entropía cruzada categórica como loss ya que es un problema de clasificación de clases múltiples.
#     model.compile(tf.keras.optimizers.Adam(learning_rate = 3e-5), loss = loss, metrics = ['accuracy'])
#     return model

# # huggingface tokenizer
# def regular_encode(texts, tokenizer, maxlen=512):
#     enc_di = tokenizer.batch_encode_plus(
#         texts,
#         return_attention_mask=False,
#         return_token_type_ids=False,
#         # pad_to_max_length proximamente va quedar deprecado, si se cambia el valor y hay algun error al truncar es en esta linea.
#         pad_to_max_length=True,
#         max_length=maxlen
#     )

#     return np.array(enc_di['input_ids'])


# def new_beto(neuronas):
#     # Creando un modelo beto-based
#     transformer_layer = transformers.TFAutoModel.from_pretrained('dccuchile/bert-base-spanish-wwm-uncased', output_attentions=False)
#     model = build_model(transformer_layer, neuronas, max_len=100)
#     return model

# def new_bert(neuronas):
#     # Crea un modelo de bert en portugues
#     transformer_layer = transformers.TFAutoModel.from_pretrained('neuralmind/bert-base-portuguese-cased', output_attentions=False, from_pt=True)
#     model = build_model(transformer_layer, neuronas, max_len=100)
#     return model


# # Cargando el modelo guardado
# def saved_model(neuronas,ruta,idioma):
#     if idioma == 'es':
#         model = new_beto(neuronas)
#         model.load_weights(ruta)
#     else:
#         model = new_bert(neuronas)
#         model.load_weights(ruta)
#     return model
