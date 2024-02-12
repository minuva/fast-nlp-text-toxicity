# Intro

A simple API server using FastAPI for serving a small and high quality toxicity classification model with onnxruntime package with fast CPU inference.

# Install from source
```bash
git clone https://github.com/minuva/toxicity-prediction-serverless.git
cd toxicity-prediction-serverless
pip install -r requirements.txt
```


# Run locally

Run the following command to start the server (from the root directory):

```bash
chmod +x ./run.sh
./run.sh
```

Check `config.py` for more configuration options.


# Run with Docker

Run the following command to start the server (the root directory):

```bash
docker build --tag toxic .
docker run -p 9612:9612 -it toxic
```

# Models

| Model | Description |
| --- | --- |
| [minuva/MiniLMv2-toxic-jigsaw](https://huggingface.co/minuva/MiniLMv2-toxic-jigsaw) | A small and high quality toxicity classification model trained on Jigsaw dataset. |
| [minuva/MiniLMv2-toxic-jigsaw-onnx](https://huggingface.co/minuva/MiniLMv2-toxic-jigsaw-onnx) | Quantized ONNX version