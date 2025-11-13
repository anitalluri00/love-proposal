# Use official lightweight Python image
FROM python:3.11-slim

# set working dir
WORKDIR /app

# copy requirements and install
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy app
COPY . /app

# expose Streamlit default port
EXPOSE 8501

# recommended Streamlit config to run in container
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# run
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
