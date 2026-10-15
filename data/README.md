# Dokumentasi Dataset — Indonesian Political News (Cleaned)

## Identitas

| Aspek | Keterangan |
|---|---|
| Nama | Indonesian Political News (Cleaned) |
| Penyedia | ardimardiana (Hugging Face) |
| Sumber | https://huggingface.co/datasets/ardimardiana/indonesian-political-news-clean |
| DOI | https://doi.org/10.57967/hf/9063 |
| Lisensi yang tercantum pada halaman dataset | CC BY-SA 4.0 |
| Format | Parquet |
| Bahasa | Indonesia |
| Ukuran/jumlah baris | Sekitar 5,45 GB / 1,63 juta baris menurut metadata saat persiapan. **Verifikasi ulang dari file lokal.** |
| Unit analisis | Satu artikel berita dalam korpus |

Dataset merupakan versi yang telah dibersihkan oleh penyedia. Proyek ini tetap menjalankan audit data quality tambahan dengan Polars dan DuckDB.

## Kolom sumber

Dataset menampilkan 15 atribut: `id`, `news_title`, `news_source`, `news_author`, `news_hostname`, `news_date`, `news_text`, `news_tags`, `news_kabkot`, `news_intent`, `news_image`, `update_date`, `create_date`, `news_guid`, dan `news_raw_data` pada Data Studio. Kolom `news_intent` dan `news_raw_data` dapat berisi informasi kompleks. Analisis proyek menggunakan subset yang relevan untuk menghemat RAM.

## Unduh ulang di Windows CMD

Dari root repository, jalankan instalasi yang diperlukan:

```cmd
python -m pip install huggingface_hub
```

Kemudian unduh file Parquet:

```cmd
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='ardimardiana/indonesian-political-news-clean', repo_type='dataset', local_dir='data/raw/indonesian-political-news-clean', allow_patterns='data/*.parquet', max_workers=3)"
```

Lokasi target:

```text
data/raw/indonesian-political-news-clean/data/*.parquet
```

Notebook mencari `.parquet` secara rekursif. Jika dataset sudah ada di folder lain (`C:\Users\...\bigdata_teman` atau Google Drive), sesuaikan `DATASET_DIR_OVERRIDE` di sel konfigurasi notebook 01 dan 02. Jangan memindahkan hasil cleaning ke `data/raw/`.

## Validasi kelengkapan

```cmd
python src/inspect_data.py
```

Cocokkan total file, baris aktual dan ukuran yang ditampilkan notebook 01 dengan metadata versi dataset yang diunduh. **Jangan menuliskan angka aktual sebelum Run All selesai.**

## Penyimpanan dan atribusi

- `data/raw/`: file asli Parquet, jangan dimodifikasi.
- `data/processed/`: hasil cleaning untuk EDA, dibangun oleh notebook 02.
- Raw/processed dikecualikan dari Git melalui `.gitignore`.
- Data mentah tidak dicopy ke Docker image melalui `.dockerignore`. Saat container jalan, volume mount menampilkan data lokal.
- Periksa kondisi lisensi dan atribusikan penyedia serta sumber asal sebelum redistribusi. Lisensi dataset tercantum CC BY-SA 4.0, sedangkan isi artikel pihak ketiga mungkin mempunyai hak penggunaan tersendiri.
- `news_kabkot` merupakan label atribut dataset, **tidak boleh ditafsirkan sebagai lokasi aktual artikel tanpa validasi lebih lanjut**.
- Informasi publikasi dan periode data mengikuti metadata sumber dan hasil profiling aktual, bukan asumsi semua artikel berada pada satu tahun.
