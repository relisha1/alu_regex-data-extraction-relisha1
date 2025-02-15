import re

def extract_emails(text):
    """Extracts valid email addresses from the given text."""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def extract_urls(text):
    """Extracts valid URLs (http and https) from the given text."""
    pattern = r'\bhttps?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}(?:/[^\s]*)?\b'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    """Extracts phone numbers in different formats, including international numbers."""
    pattern = r'\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_time(text):
    """Extracts time in both 12-hour and 24-hour formats."""
    pattern = r'\b(?:0?[1-9]|1[0-2]):[0-5][0-9] ?[APap][Mm]|\b(?:[01]?\d|2[0-3]):[0-5]\d\b'
    return re.findall(pattern, text)

if __name__ == '__main__':
    sample_text = '''
        Contact us at support@example.com or sales@example.co.uk.
        Visit our website at https://www.example.com or http://example.org/page.
        Call us at (123) 456-7890, 123-456-7890, 123.456.7890, or +1 987-654-3210.
        The event starts at 14:30 and ends at 2:30 PM.
        Invalid email: user@.com and malformed URL: http://example
        Random text with no matches.
    '''

    print("Emails Found:", extract_emails(sample_text) or "None")
    print("URLs Found:", extract_urls(sample_text) or "None")
    print("Phone Numbers Found:", extract_phone_numbers(sample_text) or "None")
    print("Times Found:", extract_time(sample_text) or "None")
