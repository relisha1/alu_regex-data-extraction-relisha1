This project is designed to extract key information from large text datasets using Python and regular expressions. It can identify and extract email addresses, URLs, phone numbers, and credit card numbers with high accuracy. Whether you're processing web data, logs, or documents, this tool helps automate data extraction efficiently.

How to Use

Clone the repository, navigate to the project directory, and run the script using Python. Simply modify the test_text variable in regex_extraction.py with your desired input text, and the script will extract the relevant details.

Example Output

When executed, the script scans the input text and extracts structured information like this:

Extracted Emails: ['user@example.com', 'firstname.lastname@company.co.uk']
Extracted URLs: ['https://www.example.com', 'https://subdomain.example.org/page']
Extracted Phone Numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
Extracted Credit Card Numbers: ['1234 5678 9012 3456', '1234-5678-9012-3456']

Project Structure

regex_extraction.py - The main script that processes text and extracts data.

test_cases.txt - A collection of sample text inputs for testing.

README.md - This document explaining the project.
