import pandas as pd
import pickle
import datetime
dia_de_hoy = datetime.datetime.now().date()


# df = pd.read_csv('..\data\train.csv')
df = pd.read_csv('../data/df_tinto_limpio_con_category.csv', index_col= 'Unnamed: 0')

# Cargar modelo
modelo_guardado = '../memoria.ipynb/mejor_modelo.pkl'
modelo = pickle.load(open(modelo_guardado, 'rb'))

# Hacer predicciones
X_prediccion = df.drop(columns=['category'], axis=1)  # Ajusta 'target_column' según el nombre de tu columna objetivo
predicciones = modelo.predict(X_prediccion)


pd.DataFrame({'Predicciones': predicciones}).to_csv(f"../data/predicciones_{dia_de_hoy}.csv", index=False)





