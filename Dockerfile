# Use NVIDIA CUDA runtime as base image
FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for PyQt5 and OpenGL
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-pyqt5 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxext6 \
    libxrender1 \
    libxkbcommon-x11-0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-xinerama0 \
    libxcb-xinput0 \
    libxcb-xfixes0 \
    libfontconfig1 \
    libdbus-1-3 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
# Using cupy-cuda11x to match the CUDA version in the base image
RUN pip3 install --no-cache-dir \
    cupy-cuda11x \
    numpy \
    PyQt5

# Set environment variables for GUI
ENV DISPLAY=host.docker.internal:0.0
ENV QT_X11_NO_MITSHM=1

# Command to run the application
CMD ["python3", "calcu.py"]
