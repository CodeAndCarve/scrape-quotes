# Quote Scraper & Guessing Game

## Overview

This project is a fun and interactive quote guessing game that combines web scraping and simple game logic! It scrapes all quotes from the [Quotes to Scrape](https://quotes.toscrape.com/) website, then generates a random guessing game based on the collected quotes.

## Features

- **Web Scraping:** Automatically fetches all quotes (along with their authors) from the Quotes to Scrape website.
- **Random Game Generation:** Presents a random quote to the player and asks them to guess the author.
- **Replayability:** Each round selects a new random quote, making the game endlessly replayable.
- **Expandable:** Easily add features like hints, score tracking, or multiple-choice options.

## How It Works

1. **Scraping:** The application fetches all available quotes and their corresponding authors from the Quotes to Scrape website.
2. **Gameplay:** The player is shown a random quote and prompted to guess the author.
3. **Feedback:** The app checks the player's guess and provides feedback (correct/incorrect).
4. **Repeat:** The game continues with new random quotes until the player chooses to quit.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Install dependencies:**
    ```bs4, random
    ```

## Usage

Run the main script to start the game:

```python3 quotesScrapeProject.py
```

Follow the on-screen instructions to play.

## Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Example

```
Quote: "The greatest glory in living lies not in never falling, but in rising every time we fall."
Who is the author? > 
```

You will have 4 guesses remaining, if you guess correctly, you'll be congratulated! Otherwise, you'll be shown series of hints before the correct answer.

## Customization

Feel free to extend the game with features like:
- Score tracking
- Hint system (e.g., show the author's initials)
- Multiple-choice format
- Time limits

## License

This project is open source and available under the [MIT License](LICENSE).

---

Happy guessing!
