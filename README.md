# RTXCALC 🚀

**RTXCALC** is a modern GPU-accelerated calculator built with **Python**, **CuPy**, and **PyQt5**.  
- 🧮 **Math** runs on your NVIDIA RTX GPU via **CUDA**.  
- 🖥️ **GUI** is fully hardware-accelerated using **OpenGL**.  
- ✨ Clean neon UI, responsive layout, and full keyboard support.  

---

## ✨ Features
- ✅ **CUDA math acceleration** with CuPy (runs on RTX GPU cores).  
- ✅ **OpenGL-accelerated GUI** (smooth rendering on GPU pipeline).  
- ✅ Supports **multi-operation expressions** (e.g., `3+5*2-4/2`).  
- ✅ **Keyboard input**:  
  - Numbers/operators directly from keyboard.  
  - `Enter` = evaluate.  
  - `Backspace` = delete last char.  
  - `ESC` = clear display.  
- ✅ Futuristic **RTX neon theme**.  

---

## 🛠️ Requirements
- Python **3.10** (recommended)  
- NVIDIA GPU with CUDA support (tested on RTX 2050)  
- Conda (preferred for environment management)  

---

## 📦 Setup

### 1. Create Environment
```powershell
mamba create -n calculator -c conda-forge python=3.10 pyqt cupy numpy -y
conda activate calculator
```

### 2. Install dependencies
```powershell
pip install pyqt5
```

---

## ▶️ Run RTXCALC
```powershell
python calcu.py
```

---

## 🎮 Usage
- Type `3+5*2-4/2` → Press **Enter** → Output: `11.0  [GPU]`  
- Click buttons or type on your keyboard.  
- **GPU info** (e.g., `NVIDIA GeForce RTX 2050`) is displayed at the top.  

---

## ⚡ Tech Stack
- **[CuPy](https://cupy.dev/)** → GPU math (CUDA backend).  
- **[PyQt5](https://riverbankcomputing.com/software/pyqt/)** → GUI framework.  
- **OpenGL (via Qt QSurfaceFormat)** → Hardware-accelerated rendering.  

---

## 📸 Screenshot
![RTXCALC Screenshot](screenshot.png)

---

## 🚀 Future Work
- Add **scientific mode** (`sin`, `cos`, `sqrt`, `log`) with CuPy.  
- Add **history panel** with GPU-accelerated logs.  
- Optional **CUDA-OpenGL interop** for direct GPU buffer rendering.  

---

💚 Built for **RTX GPUs** — enjoy lightning-fast math with a smooth GPU-accelerated interface.  
