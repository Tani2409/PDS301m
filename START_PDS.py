import subprocess
import os
import time
import sys

# ĐƯỜNG DẪN CÁC DỰ ÁN (Tối ưu cho Repo con)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ASM_DIR = os.path.join(ROOT_DIR, "..", "ASM") # Tìm ASM ở thư mục cha nếu có
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
    print("      SILVER PROJECT - AUTOMATED LAUNCHER (V1.1)")
    print("=" * 60)

    # 1. Start Backend Project
    backend = start_process(PROJECT_BACKEND, "python run.py", "Project Backend")
    
    # 2. Start Frontend Project
    frontend = start_process(PROJECT_FRONTEND, "npm run dev -- --port 5173", "Project Frontend")
    
    # 3. Start ASM (Nếu người dùng đang chạy ở bộ sưu tập chung PDS)
    asm = None
    if os.path.exists(ASM_DIR):
        asm = start_process(ASM_DIR, "streamlit run app_dashboard.py --server.port 8503", "ASM Weather")

    print("\n[OK] Hệ thống đang khởi động...")
    time.sleep(5)
    
    print("\n--- Danh mục truy cập ---")
    print("Silver UI: http://localhost:5173")
    if asm: print("Weather ASM: http://localhost:8503")
    print("API: http://localhost:5000/api/silver-price")
    print("\nNhấn Ctrl + C để dừng toàn bộ.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[STOPPING] Đang tắt hệ thống...")
        if backend: backend.terminate()
        if frontend: frontend.terminate()
        if asm: asm.terminate()
        print("[DONE] Đã tắt sạch.")

if __name__ == "__main__":
    main()
