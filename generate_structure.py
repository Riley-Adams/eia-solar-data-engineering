import os
import fnmatch

def generate_project_structure(root_dir='.',
                               exclude_dirs=['.git', '__pycache__', '.venv', 'venv', '.idea', '.vscode'],
                               exclude_files=['*.pyc', '*.pyo', '*.pyd', '*.so', '*.dll', '*.class']):
    
    """
    Generate a structured represantation of the project's folders and files

    Parameters:
    - root_dir: Starting directory (default: current directory)
    - exclude_dirs: Directories to exclude from the output
    - exclude_files: File patterns to exclude from the output
    
    Returns:
    - String representation of the project structure
    """
    
    output = []
    output.append('# Project Structure\n')
    
    for root, dirs, files in os.walk(root_dir):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Calculate the current level for indentation
        level = root.replace(root_dir, '').count(os.sep)
        indent = '    ' * level
        
        # Add the current directory to the output
        if level > 0: # Skip the root directory itself
            output.append(f"{indent}📁 {os.path.basename(root)}/")
            
        # Add each file in the current directory
        file_indent = '    ' * (level + 1)
        for file in sorted(files):
            # Skip excluded files
            if any(fnmatch.fnmatch(file, pattern) for pattern in exclude_files):
                continue 
            
            output.append(f"{file_indent}📄 {file}")
            
    return '\n'.join(output)
    
# Generate and print the structure
if __name__ == "__main__":
    structure = generate_project_structure()
    
    # Print to console
    print(structure)
    
    # Save to file
    with open('project_structure.md', 'w', encoding='utf-8') as f:
        f.write(structure)
    
    print("\nProject structure has been saved to 'project_structure.md'")