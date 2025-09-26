FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV OPENAI_API_KEY="your_openai_api_key_here"

CMD ["python3", "examples/run_eval_example.py"]
