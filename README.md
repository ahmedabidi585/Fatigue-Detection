# Fatigue-Detection 👁️🚘

**Fatigue-Detection** is a real-time computer vision system developed in Python. It uses **OpenCV** and **MediaPipe** to analyze facial landmarks (Face Mesh) and detect driver fatigue or drowsiness by calculating the **Eye Aspect Ratio (EAR)**.

---

## 🌟 Main Features

* **📹 Video Testing and Capture**: Quick and simple verification of the webcam video stream.
* **👤 Real-Time Facial Analysis**: Complete facial landmark mapping using the 468 landmarks provided by MediaPipe Face Mesh.
* **👁️ Eye Aspect Ratio (EAR) Calculation**: Accurate measurement of eye closure in real time.
* **🚨 Automatic Fatigue Alert**: Displays a visual warning (`FATIGUE DETECTED`) on the video stream when the eyes remain closed for more than 2 seconds.

---

## 🛠️ Technologies Used

* **Python 3.8+**
* **OpenCV** (`opencv-python`): Real-time image capture and processing.
* **MediaPipe** (`mediapipe`): Advanced facial landmark detection using Face Mesh.
* **NumPy** (`numpy`): Mathematical, matrix, and scientific computations.

---

## 📂 Project Structure

```text
Fatigue-Detection/
├── assets/             # Media files, screenshots, and demos
├── data/               # Test data or recordings
├── docs/               # Additional documentation
├── models/             # Pre-trained models (if applicable)
├── src/                # Source code modules
├── cameratest.py       # Webcam testing script
├── detection.py        # Main fatigue detection script (EAR)
├── face.py             # MediaPipe Face Mesh demonstration
├── test.py             # Python environment verification script
├── .gitignore          # Files and directories ignored by Git
├── requirements.txt    # Project dependencies
└── README.md           # Main project documentation
```

---

## 🚀 Installation and Setup

### 1. Prerequisites

Make sure you have **Python 3.8 or later** installed on your machine.

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Fatigue-Detection.git
cd Fatigue-Detection
```

### 3. Create and Activate a Virtual Environment

Creating a virtual environment is recommended.

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### 1. Verify the Installation

To check that all required libraries are correctly installed:

```bash
python test.py
```

### 2. Test the Camera

To make sure the webcam is working correctly:

```bash
python cameratest.py
```

Press **`q`** to exit.

### 3. Test Facial Detection (Face Mesh)

To visualize real-time facial landmark tracking:

```bash
python face.py
```

Press **`q`** to exit.

### 4. Run the Fatigue Detection System

Start the fatigue monitoring system and EAR calculation:

```bash
python detection.py
```

* **EAR Threshold**: Set to `0.20`.
* **Alert Duration**: If the eyes remain closed for more than **2 seconds**, the **`FATIGUE DETECTED`** warning appears in red on the screen.
* Press **`q`** to exit.

---

## 🧠 Eye Aspect Ratio (EAR)

The **Eye Aspect Ratio (EAR)** is a geometric measurement based on the distances between the upper and lower eyelid landmarks relative to the distance between the corners of the eye.

$$
EAR = \frac{||p_2 - p_6|| + ||p_3 - p_5||}{2 \times ||p_1 - p_4||}
$$

When the eyes are open, the EAR value is relatively high and stable. When the person closes their eyes or blinks, the EAR decreases significantly and approaches zero.

This makes EAR a useful metric for detecting prolonged eye closure, which can be an indicator of driver drowsiness.


---

## 📄 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.
