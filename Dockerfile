# Reproducible teaching image: never bake runtime secrets into build layers.
FROM python:3.12.7-slim
WORKDIR /srv
COPY requirements.lock ./requirements.lock
RUN pip install --no-cache-dir -r requirements.lock && useradd --system --uid 10001 appuser
COPY app ./app
USER 10001
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
