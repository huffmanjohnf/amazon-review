import os
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from amazon_review import ROOT_DATA_DIR

FILE = "Reviews.csv"
KAGGLE_CONFIG_DIR = os.path.join(ROOT_DATA_DIR, ".kaggle")


def download_dataset(root_dir: str = ROOT_DATA_DIR, kaggle_dir: str = KAGGLE_CONFIG_DIR):
    os.environ["KAGGLE_CONFIG_DIR"] = kaggle_dir
    os.system("kaggle datasets download -d snap/amazon-fine-food-reviews -f {} -p {}".format(FILE, root_dir))
    os.system("unzip -o {0}/{1}.zip -d {0} ; rm {0}/{1}.zip".format(root_dir, FILE))

    return


def split_data(root_dir: str = ROOT_DATA_DIR, num_samples: int = 100000, val_size: float = 0.1):
    df = pd.read_csv(os.path.join(root_dir, "Reviews.csv"), usecols=[6, 9], nrows=num_samples)
    df.columns = ["rating", "title"]
    df_train, df_val = train_test_split(df, test_size=val_size, random_state=42)

    return df_train, df_val


def preprocess(df: pd.DataFrame):
    text = df["title"].tolist()
    text = [str(t).encode("ascii", "replace") for t in text]
    text = np.array(text, dtype=object)[:]

    labels = df["rating"].tolist()
    labels = [1 if i >= 4 else 0 if i == 3 else -1 for i in labels]
    labels = np.array(pd.get_dummies(labels), dtype=int)[:]

    return labels, text


def load_datasets(root_dir: str = ROOT_DATA_DIR, kaggle_dir: str = KAGGLE_CONFIG_DIR):
    if not (Path(root_dir) / FILE).exists():
        download_dataset(root_dir, kaggle_dir)

    df_train, df_val = split_data()
    y_train, x_train = preprocess(df_train)
    y_val, x_val = preprocess(df_val)

    return y_train, x_train, y_val, x_val
