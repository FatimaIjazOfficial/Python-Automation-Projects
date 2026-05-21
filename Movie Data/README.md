# Movie Data Script

### Description

This script scrapes a webpage to get a list of movie titles and saves them to a text file.

### Usage

1. **Fetch Webpage:**
   - The script makes an HTTP request to a specified URL containing the list of movies.
   - It fetches the HTML content of the webpage.

2. **Parse HTML:**
   - The HTML content is parsed using BeautifulSoup to locate and extract the relevant movie titles.

3. **Extract Movie Titles:**
   - The script finds all movie titles by searching for specific HTML tags and classes.
   - The extracted movie titles are stored in a list.

4. **Save to File:**
   - The script reverses the order of the movie titles and saves them to a text file named `movies.txt`.

### Example Scenarios

- **Fetching and parsing a list of the best movies from a webpage.**
- **Extracting and reversing the order of movie titles.**
- **Saving the movie titles to a text file for further use or analysis.**

## Prerequisites

Make sure you have the following libraries installed:

- `requests`
- `beautifulsoup4`
- `lxml`

You can install them using pip:

```sh
pip install requests beautifulsoup4 lxml
```

