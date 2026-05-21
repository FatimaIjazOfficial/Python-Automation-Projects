Main BeautifulSoup Script

### Description

This script demonstrates basic web scraping techniques using BeautifulSoup. It includes reading an HTML file, parsing it, and extracting various elements from it.

### Usage

1. **Read HTML File:**
   - The script reads an HTML file named `website.html` from the local directory.

2. **Parse HTML:**
   - The HTML content is parsed using BeautifulSoup, allowing you to navigate and search the HTML tree structure.

3. **Extract Data:**
   - The script demonstrates different ways to extract data from the HTML, such as:
     - Finding the first occurrence of a tag (e.g., `<title>`, `<a>`, `<p>`).
     - Finding all occurrences of a tag (e.g., all `<a>` tags).
     - Extracting text and attributes from tags.
     - Using CSS selectors to find elements by ID, class, or tag.

### Example Scenarios

- **Extracting the title of the webpage.**
- **Finding and printing all anchor (`<a>`) tags.**
- **Extracting and printing the text and href attributes of all anchor tags.**
- **Using CSS selectors to find elements by class or ID.**

## Prerequisites

Make sure you have the following libraries installed:

- `requests`
- `beautifulsoup4`
- `lxml`

You can install them using pip:

```sh
pip install requests beautifulsoup4 lxml
```