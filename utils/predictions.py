import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def get_prediction_data():
    """Get prediction data (mock data for now - replace with your actual model)."""
    produk_pilihan = [
        'TEPUNG SEGITIGA 1kg', 'EKOMIE 3,6kg (isi6)', 'INDOMILK BOTOL', 
        'GULA RAJA GULA/NUSA KITA/KBA(50kg)', 'MINYAK KITA REFF 1LT'
    ]
    
    future_dates = pd.date_range(start=datetime.today(), periods=30)
    
    data = []
    for date in future_dates:
        for product in produk_pilihan:
            base_value = np.random.randint(5, 50)
            day_factor = 1.2 if date.weekday() in [4, 5] else 1.0
            predicted = round(base_value * day_factor)
            
            data.append({
                'tanggal': date,
                'nama_stok': product,
                'predicted_quantity': predicted,
                'lower_bound': round(predicted * 0.8),
                'upper_bound': round(predicted * 1.2),
                'kategori': 'Pasti Dibeli' if predicted > 2 else ('Ragu' if predicted > 0 else 'Tidak Perlu Dibeli')
            })
    
    return pd.DataFrame(data)