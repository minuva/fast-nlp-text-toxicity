FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements-onnx.txt  .
RUN pip install -r requirements-onnx.txt


RUN apt-get update && \
    apt-get install -y --no-install-recommends git-lfs && \
    git lfs install && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN git clone https://huggingface.co/Ngit/MiniLMv2-L6-H384-goemotions-v2 && rm -rf MiniLMv2-L6-H384-goemotions-v2/.git
RUN git clone https://huggingface.co/Ngit/MiniLM-L6-toxic-all-labels && rm -rf MiniLM-L6-toxic-all-labels/.git

COPY . .

RUN chmod +x run_onnx.sh

EXPOSE 9612

CMD ./run_onnx.sh