import os
import shutil

def copy_files_recursive(source_dir_path, destination_dir_path):
  if not os.path.exists(destination_dir_path):
    os.mkdir(destination_dir_path)

  for filename in os.listdir(source_dir_path):
    source_path = os.path.join(source_dir_path, filename)
    destination_path = os.path.join(destination_dir_path, filename)

    print(f"moving * {source_path} to {destination_path}")

    if os.path.isfile(source_path, destination_path):
      shutil.copy(source_path, destination_path)
    else:
      copy_files_recursive(source_path, destination_path)