# Python Task Automation - Internship Project

Automate repetitive tasks using Python file handling, regex, and web scraping.

## Tasks Included

1. **Move JPG Files** - Organize image files into folders automatically
2. **Extract Emails** - Find and save all email addresses from text files
3. **Scrape Web Titles** - Fetch and save webpage titles

## Requirements

- Python 3.7+
- requests library

```bash
pip install requests
```

## Quick Start

1. **Download** the `task_automation.py` file

2. **Edit the `main()` function** - Uncomment the task you want to run:

   ```python
   # Task 1: Move images
   move_jpg_files("source_folder", "destination_folder")
   
   # Task 2: Extract emails
   extract_emails("input.txt", "emails.txt")
   
   # Task 3: Scrape title
   scrape_webpage_title("https://example.com", "title.txt")
   ```

3. **Run the script**:
   ```bash
   python task_automation.py
   ```

## Features

- ✅ Error handling for missing files and network issues
- ✅ Clear success/error messages
- ✅ Well-commented code
- ✅ Works on Windows, macOS, and Linux

## Example Usage

### Task 1: Move JPG Files
```python
move_jpg_files("photos", "organized_photos")
```
**Output:** Moves all .jpg files from `photos/` to `organized_photos/`

### Task 2: Extract Emails
```python
extract_emails("contacts.txt", "email_list.txt")
```
**Output:** Saves all unique emails to `email_list.txt`

### Task 3: Scrape Webpage
```python
scrape_webpage_title("https://python.org", "title.txt")
```
**Output:** Saves webpage title to `title.txt`

## Project Structure

```
project/
├── task_automation.py      # Main script
├── README.md               # This file
└── requirements.txt        # Dependencies
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | Run `pip install requests` |
| Permission denied | Check folder permissions |
| No files found | Verify file paths are correct |
| Connection error | Check internet connection |

## Learning Outcomes

- File I/O operations with `os` and `shutil`
- Pattern matching with regular expressions
- HTTP requests with `requests` module
- Error handling and user feedback
- Writing clean, documented code

## Author

**[Areeb Akhtar]**  
Student | Python Developer  
📧 your.email@example.com | 🐱 [@yourgithub](https://github.com/areebworldwide)

---

⭐ *Internship Project - October 2025*