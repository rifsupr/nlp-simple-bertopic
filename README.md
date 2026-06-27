# 🎬 BERTopic - Topic Modeling on IMDb Movie Reviews

Analisis topik pada ulasan film IMDb menggunakan **BERTopic**, sebuah metode topic modeling modern yang menggabungkan **Transformer Embeddings**, **UMAP**, **HDBSCAN**, dan **c-TF-IDF** untuk menemukan topik secara otomatis dari kumpulan dokumen.

---

## 📌 Deskripsi Project

Project ini bertujuan untuk mengeksplorasi topik-topik utama yang muncul pada ulasan film IMDb tanpa menggunakan label topik (Unsupervised Learning).

Dataset yang digunakan adalah **IMDb Movie Reviews Dataset** yang terdiri dari review positif dan negatif.

---

## 🎯 Tujuan

- Mempelajari konsep Topic Modeling menggunakan BERTopic
- Mengidentifikasi topik utama dalam review film
- Mengekstraksi keyword setiap topik
- Menampilkan visualisasi hasil clustering topik
- Menyimpan hasil analisis ke dalam file CSV dan HTML

---

## 🛠 Teknologi

- Python 3.10+
- BERTopic
- Sentence Transformers
- UMAP
- HDBSCAN
- Scikit-Learn
- Pandas
- Matplotlib
- Plotly

---

## 📂 Struktur Project

```
bertopic-imdb/
│
├── dataset/
│   └── IMDB Dataset.csv
│
├── output/
│   ├── document_topics.csv
│   ├── topic_info.csv
│   ├── topic_keywords.csv
│   ├── topic_barchart.html
│   ├── topic_heatmap.html
│   ├── topic_hierarchy.html
│   └── bertopic_model/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

Dataset yang digunakan:

**IMDb Movie Reviews Dataset**

Kolom yang digunakan:

| Kolom | Keterangan |
|--------|------------|
| review | Isi review film |
| sentiment | Label sentimen (Positive / Negative) |

Pada project ini, **BERTopic hanya menggunakan kolom `review`**.

Kolom `sentiment` digunakan untuk analisis tambahan.

---

## ⚙️ Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/username/bertopic-imdb.git

cd bertopic-imdb
```

---

### 2. Install Library

```bash
pip install -r requirements.txt
```

---

### 3. Jalankan Program

```bash
python main.py
```

---

## 🔄 Alur BERTopic

```
IMDb Reviews
      │
      ▼
Text Cleaning
      │
      ▼
Sentence Transformer
      │
      ▼
Embedding
      │
      ▼
UMAP
      │
      ▼
HDBSCAN
      │
      ▼
Topic Modeling
      │
      ▼
c-TF-IDF
      │
      ▼
Keyword Extraction
      │
      ▼
Visualization
```

---

## 📈 Output

Project menghasilkan beberapa file:

### CSV

- document_topics.csv
- topic_info.csv
- topic_keywords.csv

### HTML

- topic_barchart.html
- topic_heatmap.html
- topic_hierarchy.html

### Model

- bertopic_model/

---

## 📌 Contoh Output Topic

| Topic | Count | Keywords |
|--------|------:|----------|
| 0 | 125 | movie, film, story, actor |
| 1 | 98 | horror, scary, kill, blood |
| 2 | 86 | comedy, funny, laugh, joke |
| 3 | 73 | music, soundtrack, song |
| 4 | 64 | animation, disney, cartoon |

---

## 📊 Contoh Keyword

```
Topic 0

movie
film
story
actor
director
performance
```

---

## 📚 Konsep BERTopic

BERTopic bekerja melalui beberapa tahapan:

1. Sentence Embedding menggunakan Transformer
2. Reduksi dimensi menggunakan UMAP
3. Clustering menggunakan HDBSCAN
4. Keyword Extraction menggunakan c-TF-IDF
5. Visualisasi Topik

---

## 🚀 Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:

- Topic Evolution
- Dynamic Topic Modeling
- Sentiment Analysis per Topic
- Dashboard Streamlit
- Topic Labeling Otomatis
- Topic Reduction
- Hyperparameter Tuning

---

## 📖 Referensi

- BERTopic Documentation
  https://maartengr.github.io/BERTopic/

- Sentence Transformers
  https://www.sbert.net/

- IMDb Movie Reviews Dataset
  https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

---

## 👨‍💻 Author

Arif

Master's Student in Information Technology

Data Science & Artificial Intelligence Enthusiast
