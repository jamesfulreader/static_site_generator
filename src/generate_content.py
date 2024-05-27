import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, destination_path):
  for filename in os.listdir(dir_path_content):
    from_path = os.path.join(dir_path_content, filename)
    destination_path = os.path.join(destination_path, filename)

    if os.path.isfile(from_path):
      destination_path = Path(destination_path).with_suffix(".html")
      generate_page(from_path, template_path, destination_path)
    else:
      generate_pages_recursive(from_path, template_path, destination_path)

def extract_title(md):
  lines = md.split("\n")
  for line in lines:
    if line.startswith("# "):
      return line[2:]
    raise ValueError("No title in markdown")

def generate_page(from_path, template_path, destination_path):
  print(f"* {from_path} {template_path} generating page in {destination_path}")

  from_file = open(from_path, "r")
  markdown_content = from_file.read()
  from_file.close()

  template_file = open(template_path, "r")
  template = template_file.read()
  template_file.close()

  node = markdown_to_html_node(markdown_content)

  html = node.to_html()

  title = extract_title(markdown_content)

  template = template.replace("{{ Title }}", title)
  template = template.replace("{{ Content }}", html)

  destination_dir_path = os.path.dirname(destination_path)

  if destination_dir_path != "":
    os.makedirs(destination_dir_path, exist_ok=True)

  to_file = open(destination_path, "w")
  to_file.write(template)
