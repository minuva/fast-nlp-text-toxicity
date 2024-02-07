# Intro

A simple API server using FastAPI for serving a small and high quality toxicity classification model with onnxruntime package for CPU inference to Google Cloud Run.

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


# Deploy to cloun Run

The following commands will deploy the model to Google Cloud Run:

```bash
gcloud projects create toxic-cloudrun
gcloud config set project toxic-cloudrun
docker build --tag gcr.io/toxic-cloudrun/toxicml .
docker push gcr.io/toxic-cloudrun/toxicml
gcloud run deploy toxic-ml-app --platform managed --region europe-west3 --image gcr.io/toxic-cloudrun/flowml --service-account yourservice-account --allow-unauthenticated
```

# Example call
```bash
curl -X 'POST' \
  'http://127.0.0.1:9612/toxicity' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "texts": ["hello", "this is pure trash"]
}'
```

# Models

| Model | Description |
| --- | --- |
| [minuva/MiniLMv2-toxic-jigsaw](https://huggingface.co/minuva/ | MiniLMv2-toxic-jigsaw) | A small and high quality toxicity classification model trained on Jigsaw dataset. |
| [minuva/MiniLMv2-toxic-jigsaw-onnx](https://huggingface.co/minuva/MiniLMv2-toxic-jigsaw-onnx) | Quantized ONNX version