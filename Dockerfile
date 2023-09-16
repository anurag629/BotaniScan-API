# Use a smaller base image
FROM python:3.8-slim

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
      bzip2 \
      g++ \
      git \
      graphviz \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      wget \
      python3-tk \
      ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m -u 1000 user

# Set environment variables
ENV HOME=/home/user \
    TMP_DIR=/tmp/app-temp \
    PATH=/home/user/.local/bin:$PATH

# Set the working directory
WORKDIR $HOME/app

# Copy the application code
COPY --chown=user . $HOME/app

# Switch to the non-root user
USER user

# Install Python dependencies in a temporary directory
RUN mkdir $TMP_DIR && \
    pip install --no-cache-dir --upgrade -r $HOME/app/requirements.txt -t $TMP_DIR && \
    rm -rf $TMP_DIR/__pycache__ && \
    mv $TMP_DIR/* $HOME/app/ && \
    rm -rf $TMP_DIR

# Clean up unnecessary files for a smaller image size
RUN rm -rf /tmp/* && \
    chmod -R 777 $HOME

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
