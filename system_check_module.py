import psutil
import platform
import cv2
import tkinter as tk
from tkinter import messagebox
import sys

#  GPU CHECK

def get_gpu_info():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            return ", ".join([gpu.name for gpu in gpus])
        else:
            return "Not Detected"
    except:
        return "Not Detected"


# CUDA CHECK 
try:
    import torch
    cuda_available = torch.cuda.is_available()
except:
    cuda_available = False


def run_system_check():
    root = tk.Tk()
    root.withdraw()

    # SYSTEM CHECK

    # RAM
    ram = psutil.virtual_memory().total / (1024 ** 3)

    # CPU
    cpu_name = platform.processor() or "Unknown CPU"
    cores = psutil.cpu_count(logical=True)
    cpu = f"{cpu_name} ({cores} cores)"

    # OS
    os_name = platform.system()

    # CAMERA
    cam = cv2.VideoCapture(0)
    camera_available = cam.isOpened()
    cam.release()

    # GPU
    gpu_name = get_gpu_info()

    # RECOMMENDED SPECS
    recommended = {
        "RAM": "8 GB",
        "CPU": "Intel i5 / Ryzen 5",
        "GPU": "Optional (NVIDIA preferred)",
        "AI Acceleration": "CUDA Supported GPU",
        "OS": "Windows / Linux",
        "Camera": "Required"
    }

    # CURRENT SPECS
    current = {
        "RAM": f"{ram:.2f} GB",
        "CPU": cpu,
        "GPU": gpu_name,
        "AI Acceleration": "Available (CUDA)" if cuda_available else "Not Available",
        "OS": os_name,
        "Camera": "Available" if camera_available else "Not Found"
    }

    # CHECK ISSUES
    issues = []

    if ram < 4:
        issues.append(f"Low RAM: {ram:.2f} GB (Minimum 4GB recommended)")

    if not camera_available:
        issues.append("Webcam not detected")

    if os_name not in ["Windows", "Linux"]:
        issues.append(f"Unsupported OS: {os_name}")

    if not cuda_available:
        issues.append("GPU acceleration not available (system may run slower)")

    # DISPLAY MESSAGE
    spec_message = "SYSTEM SPECIFICATIONS\n\n"

    spec_message += "Current System:\n"
    for k, v in current.items():
        spec_message += f"{k}: {v}\n"

    spec_message += "\n Recommended:\n"
    for k, v in recommended.items():
        spec_message += f"{k}: {v}\n"

    # FINAL DECISION
    if issues:
        issue_text = "\n".join(issues)

        proceed = messagebox.askyesno(
            "System Warning",
            f"{spec_message}\n\n⚠ Issues Found:\n{issue_text}\n\nDo you still want to run this project?"
        )

        if not proceed:
            sys.exit()
    else:
        messagebox.showinfo("System Check", spec_message)