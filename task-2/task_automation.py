# ============================================================================
# PYTHON TASK AUTOMATION - INTERNSHIP PROJECT
# Student Name: [Areeb Akhtar]
# Date:1 October 2025
# 
# Description: Three automation scripts demonstrating file handling, regex,
#              and web scraping using Python standard libraries
# ============================================================================

import os
import shutil
import re
import requests
from pathlib import Path


# ============================================================================
# TASK 1: Move all .jpg files from a folder to a new folder
# ============================================================================

def move_jpg_files(source_folder, destination_folder):
    """
    Moves all .jpg files from source folder to destination folder.
    
    Args:
        source_folder (str): Path to the source folder containing .jpg files
        destination_folder (str): Path to the destination folder
    
    Returns:
        int: Number of files moved successfully
    """
    try:
        # Check if source folder exists
        if not os.path.exists(source_folder):
            print(f"❌ Error: Source folder '{source_folder}' does not exist!")
            return 0
        
        # Create destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"✓ Created destination folder: {destination_folder}")
        
        # Counter for moved files
        files_moved = 0
        
        # Iterate through all files in source folder
        for filename in os.listdir(source_folder):
            # Check if file has .jpg extension (case-insensitive)
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                source_path = os.path.join(source_folder, filename)
                destination_path = os.path.join(destination_folder, filename)
                
                # Move the file
                shutil.move(source_path, destination_path)
                print(f"  → Moved: {filename}")
                files_moved += 1
        
        # Print success message
        if files_moved > 0:
            print(f"\n✅ Successfully moved {files_moved} JPG file(s) to '{destination_folder}'")
        else:
            print(f"\n⚠️  No JPG files found in '{source_folder}'")
        
        return files_moved
    
    except PermissionError:
        print(f"❌ Error: Permission denied. Check folder access rights.")
        return 0
    except Exception as e:
        print(f"❌ Unexpected error occurred: {str(e)}")
        return 0


# ============================================================================
# TASK 2: Extract all email addresses from a .txt file
# ============================================================================

def extract_emails(input_file, output_file):
    """
    Extracts all email addresses from a text file and saves them to another file.
    
    Args:
        input_file (str): Path to the input text file
        output_file (str): Path to the output file for extracted emails
    
    Returns:
        int: Number of unique emails extracted
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"❌ Error: Input file '{input_file}' does not exist!")
            return 0
        
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regular expression pattern for email addresses
        # Matches standard email format: username@domain.extension
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # Find all email addresses
        emails = re.findall(email_pattern, content)
        
        # Remove duplicates by converting to set, then back to sorted list
        unique_emails = sorted(set(emails))
        
        if not unique_emails:
            print(f"⚠️  No email addresses found in '{input_file}'")
            return 0
        
        # Write emails to output file
        with open(output_file, 'w', encoding='utf-8') as file:
            for email in unique_emails:
                file.write(email + '\n')
        
        # Print results
        print(f"\n✅ Successfully extracted {len(unique_emails)} unique email(s):")
        for email in unique_emails:
            print(f"  → {email}")
        print(f"\n📄 Emails saved to: {output_file}")
        
        return len(unique_emails)
    
    except PermissionError:
        print(f"❌ Error: Permission denied. Check file access rights.")
        return 0
    except UnicodeDecodeError:
        print(f"❌ Error: Unable to read file. Check file encoding.")
        return 0
    except Exception as e:
        print(f"❌ Unexpected error occurred: {str(e)}")
        return 0


# ============================================================================
# TASK 3: Scrape the title of a webpage and save it to a text file
# ============================================================================

def scrape_webpage_title(url, output_file):
    """
    Scrapes the title of a webpage and saves it to a text file.
    
    Args:
        url (str): URL of the webpage to scrape
        output_file (str): Path to the output file for the title
    
    Returns:
        str: The extracted title or None if failed
    """
    try:
        # Send GET request to the webpage
        print(f"🌐 Fetching webpage: {url}")
        response = requests.get(url, timeout=10)
        
        # Check if request was successful
        if response.status_code != 200:
            print(f"❌ Error: Failed to fetch webpage (Status code: {response.status_code})")
            return None
        
        # Extract title using regex
        # Matches content between <title> and </title> tags
        title_pattern = r'<title>(.*?)</title>'
        match = re.search(title_pattern, response.text, re.IGNORECASE)
        
        if match:
            title = match.group(1).strip()
            
            # Save title to file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(f"Webpage Title:\n")
                file.write(f"URL: {url}\n")
                file.write(f"Title: {title}\n")
            
            print(f"\n✅ Successfully scraped title:")
            print(f"  → {title}")
            print(f"\n📄 Title saved to: {output_file}")
            
            return title
        else:
            print(f"⚠️  No title tag found in the webpage")
            return None
    
    except requests.exceptions.Timeout:
        print(f"❌ Error: Request timed out. Check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print(f"❌ Error: Failed to connect. Check the URL and your internet connection.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching webpage: {str(e)}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error occurred: {str(e)}")
        return None


# ============================================================================
# MAIN PROGRAM - Demo/Testing Section
# ============================================================================

def main():
    """
    Main function to demonstrate all automation tasks.
    Uncomment the task you want to test.
    """
    print("=" * 70)
    print("PYTHON TASK AUTOMATION - INTERNSHIP PROJECT")
    print("=" * 70)
    
    # --------------------------------------------------------------------
    # TASK 1 DEMO: Move JPG files
    # --------------------------------------------------------------------
    print("\n📁 TASK 1: Moving JPG Files")
    print("-" * 70)
    
    # Example usage - modify paths as needed
    source = "source_images"  # Change to your source folder
    destination = "organized_images"  # Change to your destination folder
    
    # Uncomment to run:
    # move_jpg_files(source, destination)
    print("⚠️  Task 1 is commented out. Update paths and uncomment to run.")
    
    
    # --------------------------------------------------------------------
    # TASK 2 DEMO: Extract emails
    # --------------------------------------------------------------------
    print("\n\n📧 TASK 2: Extracting Email Addresses")
    print("-" * 70)
    
    # Example usage - modify paths as needed
    input_txt = "sample_text.txt"  # Change to your input file
    output_txt = "extracted_emails.txt"  # Change to your output file
    
    # Uncomment to run:
    # extract_emails(input_txt, output_txt)
    print("⚠️  Task 2 is commented out. Update paths and uncomment to run.")
    
    
    # --------------------------------------------------------------------
    # TASK 3 DEMO: Scrape webpage title
    # --------------------------------------------------------------------
    print("\n\n🌐 TASK 3: Scraping Webpage Title")
    print("-" * 70)
    
    # Example usage - modify URL as needed
    webpage_url = "https://www.python.org"  # Change to any webpage URL
    output_file = "webpage_title.txt"  # Change to your output file
    
    # Uncomment to run:
    # scrape_webpage_title(webpage_url, output_file)
    print("⚠️  Task 3 is commented out. Update URL and uncomment to run.")
    
    
    print("\n" + "=" * 70)
    print("💡 TIP: Uncomment the task you want to test in the main() function")
    print("=" * 70)


# Run the program
if __name__ == "__main__":
    main()


# ============================================================================
# USAGE EXAMPLES:
# ============================================================================
"""
To use these functions in your own scripts:

1. MOVE JPG FILES:
   move_jpg_files("my_photos", "organized_photos")

2. EXTRACT EMAILS:
   extract_emails("contacts.txt", "email_list.txt")

3. SCRAPE WEBPAGE:
   scrape_webpage_title("https://example.com", "page_title.txt")
"""

# ============================================================================
# LEARNING NOTES FOR STUDENTS:
# ============================================================================
"""
KEY CONCEPTS DEMONSTRATED:

1. File Operations (os module):
   - os.path.exists(): Check if files/folders exist
   - os.makedirs(): Create directories
   - os.listdir(): List files in a directory
   - os.path.join(): Safely combine paths

2. File Moving (shutil module):
   - shutil.move(): Move files from one location to another

3. Regular Expressions (re module):
   - re.findall(): Find all matches of a pattern
   - re.search(): Find first match of a pattern
   - Email pattern: Validates standard email formats
   - HTML pattern: Extracts content between tags

4. Web Requests (requests module):
   - requests.get(): Fetch webpage content
   - Timeout handling: Prevent hanging requests
   - Status code checking: Verify successful requests

5. Error Handling:
   - try-except blocks for graceful error management
   - Specific exceptions for different error types
   - User-friendly error messages

6. Best Practices:
   - Docstrings for documentation
   - Clear variable names
   - Input validation
   - Return values for testability
   - Comments explaining complex logic
"""