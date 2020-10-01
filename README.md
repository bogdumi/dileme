# Dileme

`dileme.py` is a simple Python program to scrape magazine covers using `BeautifulSoup`.

## Install requirements

`pip install -r requirements.txt`

## Run program

`python3 dileme.py <path_to_directory> <number_of_issues_to_save>`

### Notes:

- Recommended `path_to_directory` is `./arhiva/`, as this has already been added to `.gitignore`

- There is no maximum `number_of_issues_to_save`, but saving more than the latest issue number may provide duplicates. Check `https://dilemaveche.ro/galerie/coperta-saptamanii` for the latest issue number.
