#!/usr/bin/python3
import json
from os import walk
import os.path as path


def main():
    comments_folder = ""
    posts_folder = ""
    comments_file = ""
    posts_folder = ""
    with open("config.json") as f:
        data = json.loads(f.read())
        comments_folder = data["comments_folder"]
        posts_folder = data["posts_folder"]
        comments_file = data["comments_file"]
        posts_file = data["posts_file"]

    comments = []
    for _, _, filenames in walk(comments_folder):
        for filename in filenames:
            pathname = path.join(comments_folder, filename)
            with open(pathname, 'r') as f:
                data = json.loads(f.read())
                comments.append(data)
    with open(comments_file, 'w') as f:
        data = json.dumps(comments)
        f.write(data)

    posts = []
    for _, _, filenames in walk(posts_folder):
        for filename in filenames:
            pathname = path.join(posts_folder, filename)
            with open(pathname, 'r') as f:
                data = json.loads(f.read())
                posts.append(data)
    with open(posts_file, 'w') as f:
        data = json.dumps(posts)
        f.write(data)


if __name__ == "__main__":
    main()
