# amazon-review
Simple text classifier for Amazon reviews

This project demonstrates the simplicity of model deployment using [TensorFlow Serving with Docker](https://www.tensorflow.org/tfx/serving/docker). Here I have built out a modular version of Snehan Kekre's guided Coursera project, [TensorFlow Serving with Docker for Model Deployment](https://www.coursera.org/projects/tensorflow-serving-docker-model-deployment?action=enroll). I highly recommend going through the course for a great overview of the modeling and deployment concepts implemented here.

The premise of the model is to classify Amazon review text as positive, negative, or neutral sentiments.

## Getting started

1. Set up a conda environment for the project and activate it
```
conda create -n amazon python=3.8
conda activate amazon
```
2. Clone the repo
```
git clone https://github.com/huffmanjohnf/amazon-review.git
```
3. Cd to the repo and run `make init`
4. Run a training job by running `train` and provide the configuration options
    - For the training data to download, you must provide a [Kaggle API](https://www.kaggle.com/docs/api) path. Otherwise, manually download `Reviews.csv` from [Kaggle dataset](https://www.kaggle.com/snap/amazon-fine-food-reviews/data) and provide the path to its parent directory
    - Run `train --help` for a full list of options
```
train --EPOCHS=5 --BATCH-SIZE=32, --kaggledir="./data/.kaggle"
```
5. Use `tensorflow/serving` Docker image to deploy the trained model and expose REST (port 8501) and gRPC (port 8500) endpoints
```
docker pull tensorflow/serving
docker run -p 8500:8500 -p 8501:8501 \
        --mount type=bind,source=`pwd`/model,target=/models/model \
        -e MODEL_NAME=model -t tensorflow/serving
```

## Inference with your model

1. In a new local terminal `cd` to the repo and activate the `amazon` environment (or whichever name you created)
2. Spin up a REST client by running `client`
3. Inference with your model by creating your own amazon review (be as kind or mean as you'd like) and see how it does!
4. If you are not happy with your model, try training for more epochs! 
    - If you keep the server running, you'll notice any new models will automatically be loaded for inference