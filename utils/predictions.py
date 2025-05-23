import os
import joblib
import pandas as pd
import numpy as np
import sqlite3
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "model.joblib")
DATA_FILE = os.path.join("data", "stock_data.db")

def train_model():
    """Latih model dan simpan"""
    try:
        conn = sqlite3.connect(DATA_FILE)
        df = pd.read_sql('SELECT * FROM stock_transactions', conn)
        conn.close()
        
        df['day_of_week'] = df['tanggal'].dt.day_name()
        df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday']).astype(int)
        
        X = df[['nama_stok', 'day_of_week', 'is_weekend']]
        y = df['quantity']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        model = CatBoostRegressor(
            iterations=1000,
            learning_rate=0.05,
            depth=6,
            verbose=100
        )
        model.fit(X_train, y_train, cat_features=['nama_stok', 'day_of_week'])
        
        os.makedirs(MODEL_DIR, exist_ok=True)
        joblib.dump(model, MODEL_PATH)
        
        return model
    except Exception as e:
        raise Exception(f"Gagal melatih model: {str(e)}")

def load_model():
    """Load model yang sudah dilatih"""
    if not os.path.exists(MODEL_PATH):
        return train_model()
    return joblib.load(MODEL_PATH)

def get_prediction_data():  # NAMA FUNGSI YANG DIPERBAIKI
    """Generate prediksi 30 hari ke depan"""
    model = load_model()
    conn = sqlite3.connect(DATA_FILE)
    products = pd.read_sql('SELECT DISTINCT nama_stok FROM stock_transactions', conn)['nama_stok'].tolist()
    conn.close()
    
    future_dates = pd.date_range(start=pd.Timestamp.today(), periods=30)
    predictions = []
    
    for date in future_dates:
        day = date.day_name()
        is_weekend = 1 if day in ['Saturday', 'Sunday'] else 0
        
        for product in products:
            pred = model.predict(pd.DataFrame({
                'nama_stok': [product],
                'day_of_week': [day],
                'is_weekend': [is_weekend]
            }))
            
            predictions.append({
                'tanggal': date,
                'nama_stok': product,
                'predicted_quantity': pred[0],
                'lower_bound': max(0, pred[0] - 2),  # Contoh confidence interval
                'upper_bound': pred[0] + 2
            })
    
    result = pd.DataFrame(predictions)
    result['kategori'] = np.where(
        result['predicted_quantity'] > 5, 'High',
        np.where(result['predicted_quantity'] > 2, 'Medium', 'Low')
    )
    return result