import os
import re

def sanitize_filename(title):
    """Sanitize and format the filename, removing numbers in parentheses."""
    title = re.sub(r'\(\d+\)$', '', title).strip()
    title = re.sub(r'[^a-zA-Z0-9_\-\s]', '', title)
    title = title.replace(' ', '_')
    return title

def extract_volume_number(title):
    """Extracts the volume number from the book title."""
    match = re.search(r'Volume\s(\d+)', title, re.IGNORECASE)
    return match.group(1) if match else "1"

def generate_markdown(title, author="Miya Kazuki"):
    """Generate markdown content for a book."""
    volume_number = extract_volume_number(title)
    sanitized_title = sanitize_filename(title)
    filename = f"books_markdown/{sanitized_title}_{volume_number}.md"
    
    markdown_content = f"""---
title: "{title} (Light Novel)"
author: {author}
authors: {author}
coverUrl: 
tags:
  - light-novel
  - book
---
"""
    
    os.makedirs("books_markdown", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Generated: {filename}")

book_titles = [
    'Ascendance of a Bookworm_ Part 1 Daughter of a Soldier Volume 1 (1459)',
    'Ascendance of a Bookworm_ Part 1 Daughter of a Soldier Volume 2 (1460)',
    'Ascendance of a Bookworm_ Part 1 Daughter of a Soldier Volume 3 (1458)',
    'Ascendance of a Bookworm_ Part 2 Apprentice Shrine Maiden Volume 1 (1462)',
    'Ascendance of a Bookworm_ Part 2 Apprentice Shrine Maiden Volume 2 (1461)',
    'Ascendance of a Bookworm_ Part 2 Apprentice Shrine Maiden Volume 3 (1463)',
    'Ascendance of a Bookworm_ Part 2 Apprentice Shrine Maiden Volume 4 (1464)',
    'Ascendance of a Bookworm_ Part 3 Adopted Daughter of an Archduke Volume 1 (1465)',
    'Ascendance of a Bookworm_ Part 3 Adopted Daughter of an Archduke Volume 2 (1467)',
    'Ascendance of a Bookworm_ Part 3 Adopted Daughter of an Archduke Volume 3 (1466)',
    'Ascendance of a Bookworm_ Part 3 Adopted Daughter of an Archduke Volume 4 (1468)',
    'Ascendance of a Bookworm_ Part 3 Adopted Daughter of an Archduke Volume 5 (1469)',
    'Ascendance of a Bookworm_ Part 4 Founder of the Royal Academy\'s So-Called Library Committee Vol (1470)',
    'Ascendance of a Bookworm_ Part 4 Founder of the Royal Academy\'s So-Called Library Committee Vol (1471)',
    'Ascendance of a Bookworm_ Part 4 Founder of the Royal Academy\'s So-Called Library Committee Vol (1472)',
    'Ascendance of a Bookworm_ Part 4 Founder of the Royal Academy\'s So-Called Library Committee Vol (1473)',
    'Ascendance of a Bookworm_ Part 4 Founder of the Royal Academy\'s So-Called Library Committee Vol (1474)',
    'Ascendance of a Bookworm_ Part 4 Founder of the Royal Academy\'s So-Called Library Committee Vol (1475)',
    'Ascendance of a Bookworm_ Part 4 Founder of the Royal Academy\'s So-Called Library Committee Vol (1476)',
    'Ascendance of a Bookworm_ Part 4 Founder of the Royal Academy\'s So-Called Library Committee Vol (1477)',
    'Ascendance of a Bookworm_ Part 4 Founder of the Royal Academy\'s So-Called Library Committee Vol (1478)',
    'Ascendance of a Bookworm_ Part 5 Avatar of a Goddess Volume 11 (1483)',
    'Ascendance of a Bookworm_ Part 5 Avatar of a Goddess Volume 1 (1480)',
    'Ascendance of a Bookworm_ Part 5 Avatar of a Goddess Volume 2 (1479)',
    'Ascendance of a Bookworm_ Part 5 Avatar of a Goddess Volume 3 (1481)',
    'Ascendance of a Bookworm_ Part 5 Avatar of a Goddess Volume 4 (1488)',
    'Ascendance of a Bookworm_ Part 5 Avatar of a Goddess Volume 5 (1490)',
    'Ascendance of a Bookworm_ Part 5 Avatar of a Goddess Volume 6 (1489)',
    'Ascendance of a Bookworm_ Part 5 Avatar of a Goddess Volume 9 (1485)',
    'Ascendance of a Bookworm_ Royal Academy Stories - First Year (1450)',
    'Ascendance of a Bookworm_ Short Story Collection Volume 1 (1457)'
]

for book in book_titles:
    generate_markdown(book)

