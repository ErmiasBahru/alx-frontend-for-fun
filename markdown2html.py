#!/usr/bin/python3
"""
Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
"""


import sys
import os


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)

    with open(sys.argv[1]) as markdown:
        with open(sys.argv[2], "w") as html:
            for tag in markdown:
                length = len(tag)
                heading = tag.lstrip("#")
                html_heading = length - len(heading)

                if 1 <= html_heading <= 6:
                    tag = "<h{}>".format(html_heading) + heading.strip() + '</h{}>\n'.format(html_heading)
                    html.write(tag)

    exit(0)


if __name__ == '__main__':
    main()
