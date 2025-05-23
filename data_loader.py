import os
import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "stock_data.db")
CSV_FILE = os.path.join(DATA_DIR, "Pembelian 2024 - Status Ready.csv")

def clean_currency(x):
    if isinstance(x, str):
        return int(x.replace(',', '').replace(' ', '').replace('"', ''))
    return x

def initialize_data():
    """Proses data CSV ke SQLite database"""
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        
        if not os.path.exists(CSV_FILE):
            st.error(f"File data tidak ditemukan di: {CSV_FILE}")
            return False

        df = pd.read_csv(CSV_FILE)
        
        # Pembersihan data
        df['harga_satuan'] = df['harga_satuan'].apply(clean_currency)
        df['jumlah'] = df['jumlah'].apply(clean_currency)
        df['tanggal'] = pd.to_datetime(df['tanggal'])
        
        # Filter produk
        produk_pilihan = [
            'TEPUNG SEGITIGA 1kg', 'EKOMIE 3,6kg (isi6)', 'INDOMILK BOTOL',
            'INDOMIE GORENG', 'TEPUNG CAKRA 1kg', 'GULA RAJA GULA/NUSA KITA/KBA(50kg)'
            # ... (tambahkan semua produk sesuai kebutuhan)
        ]
        df = df[df['nama_stok'].isin(produk_pilihan)]
        
        # Simpan ke SQLite
        conn = sqlite3.connect(DATA_FILE)
        df.to_sql('stock_transactions', conn, if_exists='replace', index=False)
        conn.close()
        
        return True
    except Exception as e:
        st.error(f"Gagal memproses data: {str(e)}")
        return False