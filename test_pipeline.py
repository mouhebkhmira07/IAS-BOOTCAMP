import os
import subprocess
import sys

def run_step(name, command):
    print(f"--- Running {name} ---")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        print(f"✅ {name} complete.")
    except subprocess.CalledProcessError as e:
        print(f"❌ {name} failed.")
        print(e.stderr)
        return False
    return True

def test_all():
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    # 1. Check dependencies
    if not run_step("Dependency Check", "pip install -r requirements.txt"):
        return

    # 2. Run Pipeline (DVC)
    # This will run src/vision/load_model.py as defined in dvc.yaml
    if not run_step("Pipeline Execution (DVC)", "dvc repro"):
        print("Note: If you don't have DVC installed, run 'python src/vision/load_model.py' directly.")
        if not run_step("Direct Model Load", f"{sys.executable} src/vision/load_model.py"):
            return

    # 3. Linting Check
    run_step("Linting", "flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics")

    # 4. Streamlit Import Check
    run_step("Streamlit Validation", f"{sys.executable} -c \"import streamlit; print('Streamlit is ready')\"")

    print("\n" + "="*30)
    print("🚀 ALL SYSTEMS GO!")
    print("To launch the UI, run: streamlit run app.py")
    print("="*30)

if __name__ == "__main__":
    test_all()
