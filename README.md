# RedditScraper

A Reddit user comments and data scraper using PRAW

## Config files setup

1. Create a reddit app [here](https://www.reddit.com/prefs/apps/). Choose "personal use script".
2. Copy `credentials.default.json` to `credentials.json` and fill in your `app_id` (located under "personal use script"), `app_secret` and `user_agent` (the name of your app).
3. Copy `config.default.json` to `config.json` and change at least the `redditor` field to the name of the user you wish to scrape from.

## Usage

1. Run `python3 scraper.py` (or simply `./scraper.py`) to start scraping. You will need to specify `-c` (`--comments`) and/or `-p` (`--posts`) to specify what you want to scrape, otherwise nothing will happen. By default the limit of posts to scrape will be 10. You can change this with the `-l` or `--limit` argument. A value of 0 means the scraper will search for posts or comments until the end.  
   The parser will scrape comments/posts until the specified limit into your `comments_folder` and/or `posts_folder`.
2. Run `python3 compiler.py` (or simply `./compiler.py`) to combine all your collected files into `comments.json` and/or `posts.json` files. Use this file as you wish.