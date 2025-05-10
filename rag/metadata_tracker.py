import os
import json
from time import time
from rag.vector_store import create_vectorstore_from_pdfs

TRACKER_FILE = "rag/metadata.json"
DOC_FOLDER = "rag/sample_docs"

def get_file_mod_times(directory):
    return {f: os.path.getmtime(os.path.join(directory, f))
            for f in os.listdir(directory) if f.endswith('.pdf')}

def load_previous_mod_times():
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_mod_times(mod_times):
    with open(TRACKER_FILE, 'w') as f:
        json.dump(mod_times, f, indent=2)

def detect_changes(old, new):
    changed = []
    for file, mod_time in new.items():
        if file not in old or old[file] < mod_time:
            changed.append(file)
    return changed

def auto_update_indexes():
    print("Checking for modified PDFs...")
    old_times = load_previous_mod_times()
    new_times = get_file_mod_times(DOC_FOLDER)

    changed_files = detect_changes(old_times, new_times)
    if not changed_files:
        print("No changes detected.")
        return

    print("Changes detected in:", changed_files)
    create_vectorstore_from_pdfs(DOC_FOLDER)
    save_mod_times(new_times)
    print("Indexes updated.")

if __name__ == "__main__":
    auto_update_indexes()
