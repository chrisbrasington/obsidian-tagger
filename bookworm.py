import os
import re

# List of book titles (cleaned up)
books = [
    "Ascendance of a Bookworm Part 1 Daughter of a Soldier Volume 1",
    "Ascendance of a Bookworm Part 1 Daughter of a Soldier Volume 2",
    "Ascendance of a Bookworm Part 1 Daughter of a Soldier Volume 3",
    "Ascendance of a Bookworm Part 2 Apprentice Shrine Maiden Volume 1",
    "Ascendance of a Bookworm Part 2 Apprentice Shrine Maiden Volume 2",
    "Ascendance of a Bookworm Part 2 Apprentice Shrine Maiden Volume 3",
    "Ascendance of a Bookworm Part 2 Apprentice Shrine Maiden Volume 4",
    "Ascendance of a Bookworm Part 3 Adopted Daughter of an Archduke Volume 1",
    "Ascendance of a Bookworm Part 3 Adopted Daughter of an Archduke Volume 2",
    "Ascendance of a Bookworm Part 3 Adopted Daughter of an Archduke Volume 3",
    "Ascendance of a Bookworm Part 3 Adopted Daughter of an Archduke Volume 4",
    "Ascendance of a Bookworm Part 3 Adopted Daughter of an Archduke Volume 5",
    "Ascendance of a Bookworm Part 4 Founder of the Royal Academy's So-Called Library Committee Volume 1",
    "Ascendance of a Bookworm Part 4 Founder of the Royal Academy's So-Called Library Committee Volume 2",
    "Ascendance of a Bookworm Part 4 Founder of the Royal Academy's So-Called Library Committee Volume 3",
    "Ascendance of a Bookworm Part 4 Founder of the Royal Academy's So-Called Library Committee Volume 4",
    "Ascendance of a Bookworm Part 4 Founder of the Royal Academy's So-Called Library Committee Volume 5",
    "Ascendance of a Bookworm Part 4 Founder of the Royal Academy's So-Called Library Committee Volume 6",
    "Ascendance of a Bookworm Part 4 Founder of the Royal Academy's So-Called Library Committee Volume 7",
    "Ascendance of a Bookworm Part 4 Founder of the Royal Academy's So-Called Library Committee Volume 8",
    "Ascendance of a Bookworm Part 4 Founder of the Royal Academy's So-Called Library Committee Volume 9",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 1",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 2",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 3",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 4",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 5",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 6",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 7",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 8",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 9",
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 10", 
    "Ascendance of a Bookworm Part 5 Avatar of a Goddess Volume 11",
    "Ascendance of a Bookworm Royal Academy Stories - First Year",
    "Ascendance of a Bookworm Short Story Collection Volume 1",
]

# Output directory
output_dir = "books_markdown"
os.makedirs(output_dir, exist_ok=True)

# Process each book
for book in books:
    title_metadata = book  # The title should match the filename exactly

    # Extract part and volume for seriesSort (format: X.Y)
    part_match = re.search(r"Part (\d+)", book)
    volume_match = re.search(r"Volume (\d+)", book)

    if part_match and volume_match:
        series_sort = f"{part_match.group(1)}.{volume_match.group(1)}"
    else:
        series_sort = ""  # Leave empty for books without Part/Volume format

    # Format filename
    filename = f"{title_metadata}.md"
    filepath = os.path.join(output_dir, filename)

    # Markdown content
    markdown_content = f"""---
title: "{title_metadata}"
author: Miya Kazuki
authors: Miya Kazuki
coverUrl: 
tags:
  - light-novel
  - book
  - seriesSort: {series_sort}
---
"""

    # Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Created: {filepath}")

print("Markdown files successfully created!")

