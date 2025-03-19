import os
import yaml
import sys

def clean_text(text):
    """ Remove non-printable characters from the text. """
    return ''.join(c for c in text if c.isprintable() or c in '\n\r\t')

def add_tags_to_markdown(directory, tags):
    tags = [tag.strip().replace(" ", "") for tag in tags.split(",")]  # Process multiple tags
    
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, "r", encoding="utf-8", errors="replace") as file:
                content = file.read()
            
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) < 3:
                    continue  # Skip malformed files
                
                raw_metadata = clean_text(parts[1])  # Clean the YAML front matter
                
                try:
                    metadata = yaml.safe_load(raw_metadata)
                    if metadata is None:  # Handle cases where YAML is empty
                        metadata = {}
                except yaml.YAMLError as e:
                    print(f"Skipping {filename} due to YAML error: {e}")
                    continue
                
                if "tags" not in metadata or not isinstance(metadata["tags"], list):
                    metadata["tags"] = []
                
                # Add only new tags
                for tag in tags:
                    if tag and tag not in metadata["tags"]:
                        metadata["tags"].append(tag)
                
                updated_metadata = yaml.dump(metadata, sort_keys=False, default_flow_style=False)
                updated_content = f"---\n{updated_metadata}---\n{parts[2]}"
                
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(updated_content)
                
                print(f"Updated {filename}")

if __name__ == "__main__":
    default_directory = os.path.expanduser("~/obsidian/_inbox/")
    
    if len(sys.argv) < 2:
        print(f"Assuming default: {default_directory}")
        directory = default_directory
    else:
        directory = sys.argv[1]

    tags = input("Enter the tags to add (comma-separated): ")
    add_tags_to_markdown(directory, tags)

