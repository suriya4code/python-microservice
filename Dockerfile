FROM python:3.10.0-alpine3.15
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY Src Src
ENV FLASK_APP=main.py
ENV FLASK_ENV = production
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
HEALTHCHECK --interval=30s --retries=3 --start-period=5s \
CMD curl -f http://localhost:5000/IsHealthy || exit 1
ENTRYPOINT [ "python", "./Src/main.py" ]