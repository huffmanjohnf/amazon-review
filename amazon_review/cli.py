import tensorflow as tf
import typer

from amazon_review import CHECKPOINT_DIR, ROOT_DATA_DIR
from amazon_review.dataset import KAGGLE_CONFIG_DIR, load_datasets
from amazon_review.model import export_model, get_model

app = typer.Typer()


@app.command()
def train(EPOCHS: int = 5, BATCH_SIZE: int = 32, kaggle_dir: str = KAGGLE_CONFIG_DIR, data_dir: str = ROOT_DATA_DIR):
    y_train, x_train, y_val, x_val = load_datasets(data_dir, kaggle_dir)
    model = get_model()
    model.fit(
        x_train,
        y_train,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        verbose=1,
        validation_data=(x_val, y_val),
        callbacks=[
            tf.keras.callbacks.ModelCheckpoint(
                CHECKPOINT_DIR,
                monitor="val_loss",
                verbose=1,
                save_best_model=True,
                save_weights_only=False,
                mode="auto",
            ),
        ],
    )
    export_model(model)
