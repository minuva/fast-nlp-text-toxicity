# Fast text toxicity classification

An efficient open-source text toxicity classification system built on FastAPI 🚀. It uses a compact and accurate model running on onnxruntime for rapid CPU-based processing. It is an ideal solution for applications requiring fast and reliable toxicity classification without the need for GPU hardware. More details about the model in the [model page](https://huggingface.co/minuva/MiniLMv2-toxic-jigsaw).


# Install from source
```bash
git clone https://github.com/minuva/fast-nlp-text-toxicity.git
cd fast-nlp-text-toxicity
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
| [minuva/MiniLMv2-toxic-jigsaw](https://huggingface.co/minuva/MiniLMv2-toxic-jigsaw) | A small and high quality toxicity classification model trained on Jigsaw dataset. |
| [minuva/MiniLMv2-toxic-jigsaw-onnx](https://huggingface.co/minuva/MiniLMv2-toxic-jigsaw-onnx) | Quantized ONNX version