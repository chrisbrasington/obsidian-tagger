# Add Tag to Markdown Files

This script adds a specified tag to all markdown (`.md`) files in a given directory. The tag will be formatted by removing spaces before being added to the `tags` section in the front matter.

## Usage

1. Run the script with the directory path:
   ```sh
   python add_tag.py /path/to/markdown/files
   ```
2. Enter the tag when prompted.

## Requirements
- Python 3
- PyYAML (`pip install pyyaml`)

## Features
- Adds a user-specified tag to markdown metadata.
- Ensures the tag is formatted correctly (no spaces).
- Skips malformed files without modifying them.

## License
MIT
