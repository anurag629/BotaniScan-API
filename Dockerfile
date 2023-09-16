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
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

# Create a non-root user
RUN useradd -m -u 1000 user

# Set environment variables
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Set the working directory
WORKDIR $HOME/app

# Copy the application code
COPY --chown=user . $HOME/app

# Switch to the non-root user
USER user

# Install Python dependencies
COPY ./requirements.txt $HOME/app/
RUN pip install --no-cache-dir --upgrade -r $HOME/app/requirements.txt

# Clean up unnecessary files for a smaller image size
RUN find /var/cache/apt/archives /var/lib/apt/lists /tmp -mindepth 1 -delete && \
    chmod -R 777 $HOME

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
