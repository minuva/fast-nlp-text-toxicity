FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt  .
RUN pip install -r requirements.txt


RUN apt-get update && \
    apt-get install -y --no-install-recommends git-lfs && \
    git lfs install && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN git clone https://huggingface.co/minuva/MiniLMv2-toxic-jigsaw-lite-onnx && rm -rf MiniLMv2-toxic-jigsaw-lite-onnx/.git

COPY . .

RUN chmod +x run.sh

EXPOSE 9612

CMD ./run.sh