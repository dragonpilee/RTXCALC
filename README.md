# ⚡ RTXCALC - GPU-Accelerated Calculator v1.0

![RTXCALC Banner](https://img.shields.io/badge/RTXCALC-v1.0-magenta?style=flat-square)
![Engine](https://img.shields.io/badge/Engine-CuPy%2FPyQt5-blue?style=flat-square)
![Creator](https://img.shields.io/badge/Creator-Alan%20Cyril%20Sunny-green?style=flat-square)
![Python](https://img.shields.io/badge/Language-Python%203.10+-blue)
![GUI](https://img.shields.io/badge/UI-PyQt5%20%2B%20OpenGL-purple)
![MIT License](https://img.shields.io/badge/License-MIT-blue)

> **Developed by ALAN CYRIL SUNNY**  
> If you like this project, please ⭐ [star the repository](https://github.com/dragonpilee/rtxcalc)!

---

## 🧠 RTXCALC - GPU-Accelerated Calculator

A modern, lightning-fast calculator app that runs all math on your NVIDIA RTX GPU using **CuPy** and features a beautiful, hardware-accelerated **PyQt5** GUI.

- ⚡ **CUDA math acceleration** — all calculations run on your RTX GPU  
- 🖥️ **OpenGL-accelerated GUI** — smooth, responsive interface  
- 🎨 Futuristic neon theme and clean layout  
- ⌨️ Full keyboard support for fast input  
- 🏷️ Displays your GPU model at the top

---

## ✨ Features

- **GPU Math**: All calculations use CuPy and run on CUDA cores.
- **OpenGL GUI**: Hardware-accelerated rendering via Qt.
- **Multi-operation Expressions**: Supports complex math like `3+5*2-4/2`.
- **Keyboard Input**:  
  - Type numbers/operators directly  
  - `Enter` = evaluate  
  - `Backspace` = delete last character  
  - `ESC` = clear display
- **Neon RTX Theme**: Modern, glowing UI.
- **GPU Info**: Shows your NVIDIA GPU name in the header.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **GPU Math**: [CuPy](https://cupy.dev/) (CUDA backend)
- **GUI**: [PyQt5](https://riverbankcomputing.com/software/pyqt/) + OpenGL (QSurfaceFormat)
- **Platform**: Windows, Linux (with CUDA GPU)

---

## 💻 Requirements

- Python 3.10 (recommended)
- NVIDIA GPU with CUDA support (tested on RTX 2050)
- Conda or Mamba for environment management

---

## 📦 Installation

### 1. Create Environment

```powershell
mamba create -n calculator -c conda-forge python=3.10 pyqt cupy numpy -y
conda activate calculator
```

### 2. Install Dependencies

```powershell
pip install pyqt5
```

```powershell
python calcu.py
```

---

## 🐳 Dockerized Execution

RTXCALC is now fully dockerized with NVIDIA GPU and GUI support.

### 1. Prerequisites
- **NVIDIA Container Toolkit** installed on host.
- **X11 Server** (e.g., [VcXsrv](https://sourceforge.net/projects/vcxsrv/)) if running on Windows.

### 2. Launching
From the project root, simply run:

```powershell
docker compose up
```

The container will automatically link your GPU and attempt to display the GUI on `host.docker.internal:0.0`.

---

## 📝 Usage

- Type math expressions (e.g., `3+5*2-4/2`) and press **Enter**  
- Click buttons or use your keyboard  
- See your GPU info (e.g., `NVIDIA GeForce RTX 2050`) at the top  
- Output is labeled `[GPU]` to confirm CUDA execution

---

## ⚙️ Options & Controls

| Action         | Description                      |
|----------------|----------------------------------|
| Type numbers   | Input digits/operators           |
| Enter/Return   | Evaluate expression (on GPU)     |
| Backspace      | Delete last character            |
| ESC            | Clear display                    |
| Mouse Click    | Use on-screen buttons            |

---

## 📁 Project Structure

```
📦 RTXCALC/
 ┣ calcu.py                  # Main calculator script
 ┗ README.md                 # Project README
```

---



---

## 🚀 Future Work

- Scientific mode (`sin`, `cos`, `sqrt`, `log`) with CuPy
- History panel with GPU-accelerated logs
- CUDA-OpenGL interop for direct GPU buffer rendering

---

## 📝 License

MIT License — free to use, modify, and share. Attribution appreciated.

---

💚 Built for **RTX GPUs** — enjoy lightning-fast math with a smooth GPU-accelerated interface.
