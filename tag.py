import os
import yaml
import sys

def add_tag_to_markdown(directory, tag):
    tag = tag.replace(" ", "")  # Remove spaces from tag
    
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) < 3:
                    continue  # Skip malformed files
                
                metadata = yaml.safe_load(parts[1])
                
                if "tags" not in metadata:
                    metadata["tags"] = []
                
                if tag not in metadata["tags"]:
                    metadata["tags"].append(tag)
                
                updated_metadata = yaml.dump(metadata, sort_keys=False, default_flow_style=False)
                updated_content = f"---\n{updated_metadata}---\n{parts[2]}"
                
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(updated_content)
                
                print(f"Updated {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    tag = input("Enter the tag to add: ")
    add_tag_to_markdown(directory, tag)

