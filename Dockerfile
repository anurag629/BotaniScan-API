FROM python:3.8.0

RUN apt-get update && apt-get install -y --no-install-recommends \
      bzip2 \
      g++ \
      git \
      graphviz \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      wget \
      python3-tk && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt update && apt install -y ffmpeg

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

# Minimize image size 
# RUN (apt-get autoremove -y; \
#      apt-get autoclean -y)

# Minimize image size with sudo command and give permission to user
RUN (apt-get autoremove -y; \
     apt-get autoclean -y; \
     rm -rf /var/lib/apt/lists/*; \
     echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers; \
     chown -R user:user $HOME; \
     chmod -R 777 $HOME)

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
