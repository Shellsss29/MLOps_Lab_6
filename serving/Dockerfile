FROM python:3.10-slim

WORKDIR /app

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY wait-for-model.sh /app/wait-for-model.sh

RUN chmod +x /app/wait-for-model.sh
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "wait-for-model.sh"]
