"""Daftar ukuran dan jumlah file Parquet tanpa memuat isi ke RAM."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
data_dir = PROJECT_ROOT / "data" / "raw" / "indonesian-political-news-clean"
files = sorted(data_dir.rglob("*.parquet")) if data_dir.exists() else []
print("Folder:", data_dir)
print("Jumlah file:", len(files))
print("Total ukuran GB:", round(sum(f.stat().st_size for f in files)/1e9,3))
