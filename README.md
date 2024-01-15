# Files_Moving_Tool

### Introduction
This Python script (`file_mover.py`) facilitates the efficient movement of files from one directory to another and subsequently deletes the original files. The purpose of this script is to automate the relocation process for better organization or backup purposes.

### Features
- **File Movement:** The script traverses through the specified source directory, moves each file to the target directory, and prints a success message for each file moved.
- **File Deletion:** After successfully moving a file, the script deletes the original file from the source directory to free up space.

### Prerequisites
Before using the script, ensure that:

- Python is installed on your system.
- The `shutil` module, which is part of the Python Standard Library, is available.

### Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/house40105/Files_Moving_Tool.git
   ```
2. Navigate to the script's directory:
   ```sh
   cd path/to/your_script
   ```
3. Open the script (`file_mover.py`) and set the appropriate values for `or_mypath` (original folder path) and `tg_mypath` (target folder path).
4. Run the script:
   ```sh
   python file_mover.py
   ```

### Configuration
Adjust the following variables in the script to match your specific use case:  
```sh
or_mypath = "given path"  # Original folder path
tg_mypath = "given path"  # Target folder path
```

### Workflow
1. The script locates the current working directory to the specified path (`or_mypath`).
2. It iterates through each file in the source directory (`or_mypath`) and moves it to the target directory (`tg_mypath`).
3. After successfully moving each file, it deletes the original file from the source directory.
4. The script prints informative messages about each step, indicating successful file movements and deletions.

### Caution
- Ensure that the specified directories exist before running the script.
- Double-check the paths to avoid unintentional overwriting or deletion of files.

### Customization
Feel free to customize the script according to your needs. You can modify file extensions, add error handling, or enhance the script for specific use cases.

### Conclusion
This script simplifies the process of organizing files by automating the movement and deletion tasks. Use it responsibly, ensuring that you have backups and validating paths before execution. If you encounter any issues or have suggestions for improvement, feel free to open an issue or contribute to the codebase.
