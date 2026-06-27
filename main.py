import os
import pandas as pd

from bertopic import BERTopic

# =====================================================
# CONFIG
# =====================================================

DATASET_PATH = "dataset/IMDB Dataset.csv"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================================
# LOAD DATASET
# =====================================================

print("Loading dataset...")

df = pd.read_csv(DATASET_PATH)

print(df.head())

print(df.shape)

print(df.isnull().sum())

# =====================================================
# CLEANING
# =====================================================

df["review"] = (
    df["review"]
        .str.replace("<br />", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
)

# =====================================================
# SAMPLE
# =====================================================

# Untuk belajar gunakan 1000 data dulu
df = df.sample(
    1000,
    random_state=42
).reset_index(drop=True)

documents = df["review"].tolist()

# =====================================================
# BERTopic
# =====================================================

print("Training BERTopic...")

topic_model = BERTopic(

    language="english",

    min_topic_size=20,

    calculate_probabilities=True,

    verbose=True

)

topics, probs = topic_model.fit_transform(documents)

print("Training selesai")

# =====================================================
# TOPIC INFO
# =====================================================

topic_info = topic_model.get_topic_info()

print(topic_info)

topic_info.to_csv(

    f"{OUTPUT_DIR}/topic_info.csv",

    index=False

)

# =====================================================
# DOCUMENT TOPIC
# =====================================================

df["Topic"] = topics

df.to_csv(

    f"{OUTPUT_DIR}/document_topics.csv",

    index=False

)

# =====================================================
# KEYWORDS
# =====================================================

rows = []

for topic in topic_info.Topic:

    if topic == -1:
        continue

    words = topic_model.get_topic(topic)

    if words is None:
        continue

    for word, score in words:

        rows.append({

            "Topic": topic,

            "Keyword": word,

            "Score": score

        })

keyword_df = pd.DataFrame(rows)

keyword_df.to_csv(

    f"{OUTPUT_DIR}/topic_keywords.csv",

    index=False

)

print(keyword_df.head())

# =====================================================
# VISUALIZATION
# =====================================================

print("Saving visualization...")

try:

    topic_model.visualize_barchart().write_html(

        f"{OUTPUT_DIR}/topic_barchart.html"

    )

except Exception as e:

    print(e)

try:

    topic_model.visualize_hierarchy().write_html(

        f"{OUTPUT_DIR}/topic_hierarchy.html"

    )

except Exception as e:

    print(e)

try:

    topic_model.visualize_heatmap().write_html(

        f"{OUTPUT_DIR}/topic_heatmap.html"

    )

except Exception as e:

    print(e)

print("Selesai")