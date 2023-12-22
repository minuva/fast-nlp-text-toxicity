# Intro

A simple API server using FastAPI for serving a small and high quality toxicity classification model onnxruntime only for CPU inference.

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

| Model | 
| --- |
| [Ngit/MiniLM-L6-toxic-all-labels](https://huggingface.co/Ngit/MiniLM-L6-toxic-all-labels)
| [Ngit/MiniLM-L6-toxic-all-labels-onnx](https://huggingface.co/Ngit/MiniLM-L6-toxic-all-labels-onnx)