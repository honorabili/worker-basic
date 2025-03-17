FROM python:3.10-slim

WORKDIR /
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY sentiment_analysis.py /

# Start the container
CMD ["python3", "-u", "sentiment_analysis.py"]
