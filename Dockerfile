# Stage 1: Build Frontend
# This stage uses Node.js to compile your frontend into static assets.
FROM node:20-slim AS frontend-builder
WORKDIR /app/frontend

# Copy package files and install dependencies first to leverage Docker cache
COPY frontend/package*.json ./
RUN npm install

# Copy the rest of the frontend source code and build the application
COPY frontend/ ./

# ---> ADD THESE FOUR LINES <---
ARG VITE_API_URL
ARG VITE_WS_URL
ENV VITE_API_URL=$VITE_API_URL
ENV VITE_WS_URL=$VITE_WS_URL


RUN npm run build

# ---

# Stage 2: Install Backend Dependencies
# This stage installs Python packages in a clean environment.
FROM python:3.11-slim AS backend-builder
WORKDIR /app

# Copy requirements file and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# ---

# Stage 3: Final Production Image
# This is the final, optimized image that will be deployed.
FROM python:3.11-slim
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Copy installed Python packages from the backend-builder stage
COPY --from=backend-builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

# Copy the built frontend assets from the frontend-builder stage
# These will be served by your Python backend.
COPY --from=frontend-builder /app/frontend/dist/ ./static/

# Copy all your application source code into the final image.
# The .dockerignore file ensures unnecessary files are excluded.
COPY . .

# Create a non-root user for better security
RUN useradd -m -u 1000 appuser
# Ensure the appuser owns the application files
RUN chown -R appuser:appuser /app
USER appuser

# Expose the port the app will run on
EXPOSE 8000

# The command to start your application when a container is created
# This assumes your FastAPI instance in 'app.py' is named 'app'
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
