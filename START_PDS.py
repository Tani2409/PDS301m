import subprocess
import os
import time
import sys

# ĐƯỜNG DẪN DỰ ÁN SILVER
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_BACKEND = os.path.join(ROOT_DIR, "Project", "backend")
PROJECT_FRONTEND = os.path.join(ROOT_DIR, "Project", "frontend")

# BIẾN MÔI TRƯỜNG (Cố định PATH Windows)
PYTHON_PATH = r"C:\Program Files\Python312"
NODE_PATH = r"C:\Program Files\nodejs"
os.environ["PATH"] = f"{PYTHON_PATH};{PYTHON_PATH}\\Scripts;{NODE_PATH};" + os.environ["PATH"]

def start_process(cwd, command, name):
    if not os.path.exists(cwd):
        print(f"[SKIPPING] {name}: Thư mục không tồn tại: {cwd}")
        return None
    print(f"[STARTING] {name} tại {cwd}...")
    return subprocess.Popen(command, cwd=cwd, shell=True)

def main():
    print("=" * 60)
    print("      SILVER PROJECT - AUTOMATED LAUNCHER (V2.0)")
    print("=" * 60)

    # 1. Start Backend Project
    backend = start_process(PROJECT_BACKEND, "python run.py", "Project Backend")
    
    # 2. Start Frontend Project
    frontend = start_process(PROJECT_FRONTEND, "npm run dev -- --port 5173", "Project Frontend")
    
    print("\n[OK] Hệ thống đang khởi động...")
    time.sleep(5)
    
    print("\n--- Danh mục truy cập ---")
    print("Silver UI: http://localhost:5173")
    print("Swagger UI: http://localhost:5000/apidocs (Test API tại đây)")
    print("API Base: http://localhost:5000/api")
    print("\nNhấn Ctrl + C để dừng toàn bộ.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[STOPPING] Đang tắt hệ thống...")
        if backend: backend.terminate()
        if frontend: frontend.terminate()
        print("[DONE] Đã tắt sạch.")

if __name__ == "__main__":
    main()
