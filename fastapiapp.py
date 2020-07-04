from fastapi import FastAPI
import numpy as np
import pickle
model = pickle.load(open('model.pickle', 'rb'))
app = FastAPI()
@app.get("/predict")
def predict_complex_model(experience :int):
    final_features=np.array(experience)
    final_features=final_features.reshape(1,-1)
    print(final_features)
    prediction = model.predict(final_features)
    return {'The salary for the given experience could be {}'.format(prediction)}