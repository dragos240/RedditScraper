#!/usr/bin/python3
import praw
import json
from argparse import ArgumentParser
import os.path as path


def parse_comment(comment):
    content = {
        "comment_id": comment.id,
        "comment_body": comment.body,
        "timestamp": comment.created_utc,
        "permalink": comment.permalink,
        "thread_link": comment.submission.permalink
    }
    return content


def parse_post(post):
    content = {
        "post_id": post.id,
        "post_body": post.selftext,
        "timestamp": post.created_utc,
        "permalink": post.permalink
    }
    return content


def main():
    parser = ArgumentParser()
    parser.add_argument("-l", "--limit",
                        type=int,
                        help="Number of post/comments to parse (0 for all)",
                        default=10)
    parser.add_argument("-c", "--comments",
                        action="store_true", help="Parse comments")
    parser.add_argument("-p", "--posts",
                        action="store_true", help="Parse posts")
    args = parser.parse_args()

    limit = args.limit
    do_parse_comments = args.comments
    do_parse_posts = args.posts

    app_id = ""
    app_secret = ""
    user_agent = ""
    with open("credentials.json") as f:
        data = json.loads(f.read())
        app_id = data["app_id"]
        app_secret = data["app_secret"]
        user_agent = data["user_agent"]

    comments_folder = ""
    posts_folder = ""
    redditor = ""
    with open("config.json") as f:
        data = json.loads(f.read())
        comments_folder = data["comments_folder"]
        posts_folder = data["posts_folder"]
        redditor_name = data["redditor"]

    reddit = praw.Reddit(client_id=app_id,
                         client_secret=app_secret,
                         user_agent=user_agent)
    redditor = reddit.redditor(redditor_name)

    if do_parse_comments:
        print("Scraping {} comments...".format(limit))
        for comment in redditor.comments.new(limit=limit):
            print("Scraping comment id '{}'".format(comment.id))
            with open(path.join(comments_folder,
                                "comment_{}.json"
                                .format(comment.id)), 'w') as f:
                data = json.dumps(parse_comment(comment))
                f.write(data)

    if do_parse_posts:
        print("Scraping {} posts...".format(limit))
        for post in redditor.submissions.new(limit=limit):
            if post.selftext != "":
                print("Scraping post id '{}'".format(post.id))
                with open(path.join(posts_folder,
                                    "post_{}.json"
                                    .format(post.id)), 'w') as f:
                    data = json.dumps(parse_post(post))
                    f.write(data)


if __name__ == "__main__":
    main()
