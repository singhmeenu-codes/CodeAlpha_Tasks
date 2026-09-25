"""
Task Automation: Email Address Extractor
------------------------------------------
Reads a .txt file, finds every email address in it using a regular
expression, and writes the unique addresses to a new output file.

Key Concepts Used: re, file handling, os.

Usage:
    python3 email_extractor.py input.txt
    python3 email_extractor.py input.txt -o found_emails.txt

If no input file is given, the script looks for "input.txt" in the
same folder and creates a small sample file to demonstrate the tool
if one doesn't already exist.
"""

import os
import re
import sys

# Regex pattern for matching typical email addresses
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")


def create_sample_file(path):
    """Create a small sample .txt file so the script is runnable out of the box."""
    sample_text = (
        "Meeting notes - contact John at john.doe@example.com for details.\n"
        "CC: sarah_smith99@company.co.in and support@my-site.org\n"
        "Invalid mentions: not-an-email, @missing-user.com, plain.text\n"
        "Duplicate check: john.doe@example.com again.\n"
    )
    with open(path, "w") as f:
        f.write(sample_text)
    print(f"No input file found, so a sample file was created at '{path}'.")


def extract_emails(input_path):
    """Read the input file and return a list of unique emails, in order found."""
    with open(input_path, "r") as f:
        content = f.read()

    matches = EMAIL_PATTERN.findall(content)

    # Preserve order while removing duplicates
    seen = set()
    unique_emails = []
    for email in matches:
        if email not in seen:
            seen.add(email)
            unique_emails.append(email)

    return unique_emails


def save_emails(emails, output_path):
    """Write the list of emails to the output file, one per line."""
    with open(output_path, "w") as f:
        for email in emails:
            f.write(email + "\n")


def main():
    # Basic command-line argument handling (with sensible defaults)
    input_path = "input.txt"
    output_path = "extracted_emails.txt"

    args = sys.argv[1:]
    if len(args) >= 1:
        input_path = args[0]
    if "-o" in args:
        idx = args.index("-o")
        if idx + 1 < len(args):
            output_path = args[idx + 1]

    if not os.path.exists(input_path):
        create_sample_file(input_path)

    emails = extract_emails(input_path)

    if not emails:
        print(f"No email addresses were found in '{input_path}'.")
        return

    save_emails(emails, output_path)

    print(f"Found {len(emails)} unique email address(es) in '{input_path}':")
    for email in emails:
        print(f"  - {email}")
    print(f"\nSaved to '{output_path}'.")


if __name__ == "__main__":
    main()