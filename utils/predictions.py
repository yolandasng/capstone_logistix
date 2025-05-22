import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def get_prediction_data():
    """Get prediction data (mock data for now - replace with your actual model)."""
    produk_pilihan = [
'TEPUNG SEGITIGA 1kg', 'EKOMIE 3,6kg (isi6)', 'EKOMIE 2 (renteng)', 'INDOMILK BOTOL', 'INDOMILK KIDS UHT', 'INDOMIE GORENG',
'TEPUNG CAKRA 1kg', 'TEPUNG CAKRA SAK (25kg)', 'TEPUNG KANJI ROSE BRAND', 'TEPUNG KETAN ROSE BRAND', 'DDS SEDAP KARE SP', 'DDS SEDAP SOTO',
'DDS SEDAP KOREA', 'GULA RAJA GULA/NUSA KITA/KBA(50kg)','TEPUNG PAYUNG(25kg)','INDOMIE GRG ACEH', 'INDOMIE KRIUK', 'INDOMIE RENDANG', 'INDOMIE SOTO SP', 'SARIMIE 2 KECAP',
'SARIMIE 2 KREMES', 'POPMIE B AYAM BAWANG', 'POPMIE B BASO', 'P…MINYAK SABRINA REFF 1LT', 'INDOMIE RAWON', 'SARIMIE 2 KOREA','MINYAK SABRINA REFF 2LT', 'POPMIE PEDAS GLEDEK','MIE TELUR 3 AYAM',
'MINYAK KITA BOTOL 1LT', 'MINYAK SUNCO REFF 2lt','SAJIKU 220gr','TEPUNG DRAGONFLY', 'TEPUNG VIRGO PEYEK','SUSU ZEE CO RTG',
'SUSU ZEE VAN RTG','POPMIE GORENG SP', 'DDS SEDAP GORENG BAG','GULA (50kg)','3 SAPI JUMBO',
'INDOMIE RENDANG JUMBO', 'INDOMIE GORENG JUMBO',  'INTERMIE PEDAS', 'DDS SEDAP BUMBU','POPMIE MI GORENG','DDS EKOMIE 3,6kg (isi6)',
'TEPUNG GEPREK SAKURA'
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
