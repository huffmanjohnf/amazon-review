import os
import time

import tensorflow as tf
import tensorflow_hub as hub

from amazon_review import MODEL_DIR


def get_model() -> tf.keras.Sequential:
    print("Loading model ...")
    hub_layer = hub.KerasLayer(
        "https://tfhub.dev/google/tf2-preview/nnlm-en-dim50/1",
        output_shape=[50],
        input_shape=[],
        dtype=tf.string,
        name="input",
        trainable=False,
    )
    model = tf.keras.Sequential()
    model.add(hub_layer)
    model.add(tf.keras.layers.Dense(25, activation="relu"))
    model.add(tf.keras.layers.Dense(3, activation="softmax", name="output"))
    model.compile(loss="categorical_crossentropy", optimizer="Adam", metrics=["accuracy"])
    model.summary()
    return model


def export_model(model: tf.keras.Sequential, model_dir: str = MODEL_DIR):
    path = os.path.join(MODEL_DIR, str(int(time.time())))
    tf.saved_model.save(model, path)
