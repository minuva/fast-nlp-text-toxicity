# FlashML

FlashML is a simple FastAPI server that serves fast and lightweight models for text classification using onnxruntime only for CPU inference.

# Install from source
```bash
git clone https://github.com/Ngitai/FlashML.git
cd FlashML
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
docker build --tag flashml .
docker run -p 9612:9612 -it flashml
```

# Models

| Model | 
| --- |
| [Ngit/MiniLM-L6-toxic-all-labels](https://huggingface.co/Ngit/MiniLM-L6-toxic-all-labels)
| [Ngit/MiniLM-L6-toxic-all-labels-onnx](https://huggingface.co/Ngit/MiniLM-L6-toxic-all-labels-onnx)