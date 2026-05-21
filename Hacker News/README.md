# Hacker News Script

### Description

This script scrapes the Hacker News website to find the most upvoted article.

### Usage

1. **Fetch Webpage:**
   - The script makes an HTTP request to the Hacker News website.
   - It fetches the HTML content of the webpage.

2. **Parse HTML:**
   - The HTML content is parsed using BeautifulSoup to locate and extract relevant information about articles.

3. **Extract Article Titles and Links:**
   - The script finds all article titles and their corresponding links.
   - The extracted titles and links are stored in lists.

4. **Extract Upvotes:**
   - The script finds the number of upvotes for each article.
   - It determines the article with the highest number of upvotes.

5. **Print the Most Upvoted Article:**
   - The script prints the title, upvotes, and link of the most upvoted article.

### Example Scenarios

- **Fetching and parsing the latest articles from Hacker News.**
- **Extracting titles, links, and upvote counts for each article.**
- **Identifying and printing the most popular article based on upvotes.**

## Prerequisites

Make sure you have the following libraries installed:

- `requests`
- `beautifulsoup4`
- `lxml`

You can install them using pip:

```sh
pip install requests beautifulsoup4 lxml
```
