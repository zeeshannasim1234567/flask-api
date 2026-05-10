
# 1. Start with a lightweight Linux computer that already has Python 3.9 installed
FROM python:3.9-slim

# 2. Create a working directory inside the container called /app
WORKDIR /app

# 3. Copy everything from your laptop's current folder into the container's /app folder
COPY . /app

# 4. Read the grocery list and install Flask
RUN pip install -r requirements.txt

# 5. Open port 5000 so the container can talk to the outside world
EXPOSE 5000

# 6. The final command to start your Flask restaurant
CMD ["python", "app.py"]

