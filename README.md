# Tugas 1 Analisis Big Data — Indonesian Political News

## Gambaran proyek

Proyek ini menganalisis korpus berita daring Indonesia dari dataset [Indonesian Political News (Cleaned)](https://huggingface.co/datasets/ardimardiana/indonesian-political-news-clean) menggunakan Polars Lazy API, DuckDB SQL, dan Plotly. Tujuan analisis adalah menggambarkan sebaran publikasi menurut waktu, domain media, label wilayah, dan panjang isi artikel. Hasilnya adalah**deskripsi korpus**, bukan pengukuran representatif terhadap seluruh pemberitaan politik Indonesia.

## Status pengerjaan

| Milestone | Deliverable | Status |
|---|---|---|
| 1 | Dataset >=500 MB atau >1 juta baris, data/README.md, notebook profiling | **Kode tersedia, hasil Run All perlu diverifikasi** |
| 2 | Data quality, cleaning Polars dan DuckDB `SUMMARIZE` | **Kode tersedia, hasil Run All perlu diverifikasi** |
| 3 | Analisis waktu/wilayah dan 6+ grafik interaktif | **Kode 8 grafik tersedia, hasil Run All perlu diverifikasi** |
| Final | 5+ insight, reproducibility, Docker | **Insight dihitung otomatis, Docker perlu diuji** |

Jangan ubah status menjadi selesai sebelum pengujian sendiri pada data asli dan commit bertahap.

## Dataset

- Nama: Indonesian Political News (Cleaned)
- Sumber: https://huggingface.co/datasets/ardimardiana/indonesian-political-news-clean
- DOI: https://doi.org/10.57967/hf/9063
- Lisensi pada halaman dataset: CC BY-SA 4.0
- Format: Parquet
- Metadata sumber: sekitar 1,63 juta baris, ukuran unduh beberapa GB. Angka final mengikuti notebook profiling lokal.
- Kolom penting: `news_title`, `news_text`, `news_hostname`, `news_date`, `news_kabkot`.

Informasi cara unduh, atribut dan lisensi selengkapnya ada di [data/README.md](data/README.md).

## Struktur repository

```text
.
├── .github/workflows/lint_check.yml
├── data/
│   ├── README.md
│   ├── raw/                        # file tidak di-commit
│   └── processed/                  # hasil cleaning tidak di-commit
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_eda_and_insights.ipynb
├── output/
│   ├── figures/                    # grafik HTML interaktif lokal
│   └── tables/                     # laporan kualitas dan insight
├── src/inspect_data.py
├── .gitignore
├── .dockerignore
├── requirements.txt
├── Dockerfile
└── README.md
```

## Alur analisis

1. **Profiling**: scan Parquet, verifikasi baris dan ukuran, schema, null/kosong, tanggal, pola kategori, panjang teks, kandidat duplikasi.
2. **Cleaning**: judul/isi wajib cukup panjang, tanggal dapat diparse, normalisasi host/judul, hapus duplikasi berdasarkan host+judul+tanggal, isi wilayah kosong menjadi `Tidak tersedia`. Outlier panjang teks ditandai, bukan dibuang. Hasil disimpan `data/processed/political_news_analysis.parquet` dengan `sink_parquet`.
3. **EDA**: 8 grafik Plotly untuk tren harian dan bulanan, domain, wilayah, hari mingguan, kelompok panjang artikel, domain per tahun dan outlier. Minimal 7 insight ditulis otomatis ke `output/tables/insights.md` ketika dieksekusi.

**Aturan cleaning bersifat pilihan operasional** yang perlu dievaluasi terhadap data. Normalisasi/kunci dedup bisa menghapus artikel berbeda dengan judul sama pada hari dan situs yang sama. Dataset sumber sudah berstatus *cleaned*, sehingga cleaning di sini adalah audit dan penyesuaian untuk studi.

## Menjalankan secara lokal (Windows CMD)

Masuk ke folder repository:

```cmd
cd /d "C:\path\ke\repository-teman"
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m jupyter lab
```

Di JupyterLab jalankan ketiga file `.ipynb` secara **berurutan**. Dataset harus ada di `data/raw/indonesian-political-news-clean/` atau atur `DATASET_DIR_OVERRIDE` bila disimpan di lokasi lain. Gunakan **Kernel → Restart Kernel and Run All Cells** setiap notebook.

## Menjalankan melalui Docker

```cmd
docker build -t bigdata-politik .
docker run --rm -p 8888:8888 -v "%cd%:/workspace" bigdata-politik
```

Untuk Linux/Ubuntu, volume mount-nya:

```bash
docker run --rm -p 8888:8888 -v "$(pwd):/workspace" bigdata-politik
```

Buka `http://localhost:8888/lab`. Konfigurasi Jupyter tanpa password/token **hanya untuk penggunaan lokal**. Jangan publikasikan port 8888 di jaringan publik. Data tidak ada dalam image, tetapi tersedia saat mount folder repo.

## Memakai Google Colab

Upload ketiga notebook ke Colab. Karena dataset berukuran besar, simpan Parquet mentah di Google Drive dan mount Drive terlebih dahulu:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Atur `DATASET_DIR_OVERRIDE` pada notebook 01 dan 02 ke folder Parquet di Drive. Sebelum EDA, pastikan output notebook 02 tersedia sebagai Parquet dan setel `PROCESSED_FILE_OVERRIDE` pada notebook 03. Runtime Colab dapat berbeda dan penyimpanannya sementara. Untuk dataset lebih dari 5 GB, kemampuan RAM/Drive Colab bisa menjadi keterbatasan, jalankan lokal atau Docker bila perlu.

## Data quality dan keterbatasan

- Periksa hasil jumlah baris aktual dan jumlah data yang ditolak secara transparan.
- Artikel dengan wilayah `Tidak tersedia` tetap digunakan, tetapi interpretasi spasial dibatasi pada label metadata.
- Artikel outlier menurut panjang teks tidak otomatis dianggap salah.
- Variasi domain dan tanggal bisa dipengaruhi proses koleksi dan kelengkapan sumber.
- Proses cleaning menghasilkan tabel analisis terpilih; berkas mentah tetap disimpan terpisah.
- Grafik HTML memakai pustaka Plotly dari CDN saat dibuka di luar notebook dan mungkin membutuhkan internet.

## Referensi teknis

- Dataset: https://huggingface.co/datasets/ardimardiana/indonesian-political-news-clean
- Polars Lazy API: https://docs.pola.rs/user-guide/concepts/lazy-api/
- DuckDB Parquet: https://duckdb.org/docs/stable/data/parquet/overview
- DuckDB SUMMARIZE: https://duckdb.org/docs/stable/sql/statements/summarize
- Plotly Python: https://plotly.com/python/

## AI Disclosure Statement

**Alat AI:** ChatGPT.

**Bagian yang dibantu:** bantuan penyusunan kerangka proyek, contoh kode Polars/DuckDB/Plotly, dokumentasi, serta rancangan validasi kualitas data. Penggunaan ini wajib disesuaikan dengan pekerjaan yang benar-benar dilakukan.

**Verifikasi oleh mahasiswa:** isi setelah pengujian, meliputi versi library, jumlah baris yang dihasilkan, pemeriksaan keluaran tiga notebook, pengujian Docker, review tiap cell, serta commit bertahap di repository pribadi. Jangan mengklaim pengujian yang belum terjadi.

## Identitas mahasiswa

- Nama: **[isi nama pemilik repo]**
- NIM: **[isi NIM pemilik repo]**
- GitHub: **[isi username pemilik repo]**

