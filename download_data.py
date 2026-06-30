"""
Book recommendation dataset from Kaggle.

Source: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset
"""

import os
import opendatasets as od


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
DATASET_URL = "https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset"


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    od.download(DATASET_URL, data_dir=DATA_DIR)
    print(f"\nDataset downloaded to: {DATA_DIR}")
    print("Files:")
    dataset_folder = os.path.join(DATA_DIR, "book-recommendation-dataset")
    for f in os.listdir(dataset_folder):
        size_mb = os.path.getsize(os.path.join(dataset_folder, f)) / (1024 * 1024)
        print(f"  {f} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()