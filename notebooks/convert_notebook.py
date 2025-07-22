import os
import sys
import nbformat
from nbconvert import MarkdownExporter
from datetime import datetime
import argparse

def convert_notebook_to_hugo(notebook_path, output_dir="../content/posts/"):
    """Convert Jupyter notebook to Hugo markdown post"""
    
    # Read the notebook
    with open(notebook_path, 'r') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Extract title from first markdown cell or filename
    title = os.path.splitext(os.path.basename(notebook_path))[0]
    if notebook.cells and notebook.cells[0].cell_type == 'markdown':
        first_line = notebook.cells[0].source.split('\n')[0]
        if first_line.startswith('#'):
            title = first_line.replace('#', '').strip()
    
    # Convert to markdown
    md_exporter = MarkdownExporter()
    (body, resources) = md_exporter.from_notebook_node(notebook)
    
    # Create Hugo front matter
    date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')

    ### TODO change this so that the font matter is taken from the file instead of hard coding it
    front_matter = f"""---
title: "{title}"
date: {date}
draft: false
tags: ["jupyter", "data-science"]
categories: ["blog"]
---

"""
    
    # Combine front matter and content
    hugo_content = front_matter + body
    
    # Create output filename
    output_filename = os.path.splitext(os.path.basename(notebook_path))[0] + '.md'
    output_path = os.path.join(output_dir, output_filename)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Write the file
    with open(output_path, 'w') as f:
        f.write(hugo_content)
    
    print(f"Converted {notebook_path} to {output_path}")
    
    # Handle images if any
    if 'outputs' in resources and resources['outputs']:
        img_dir = os.path.join(output_dir, '../static/images/')
        os.makedirs(img_dir, exist_ok=True)
        
        for filename, data in resources['outputs'].items():
            img_path = os.path.join(img_dir, filename)
            with open(img_path, 'wb') as f:
                f.write(data)
            print(f"Saved image: {img_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Jupyter notebook to Hugo post')
    parser.add_argument('notebook', help='Path to the Jupyter notebook')
    parser.add_argument('--output', default='../content/post/', help='Output directory')
    
    args = parser.parse_args()
    convert_notebook_to_hugo(args.notebook, args.output)