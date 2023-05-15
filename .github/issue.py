from io import BytesIO
import os

import requests

# see https://pygithub.readthedocs.io/en/latest/examples.html
from github import Github

BLOG_BASE = os.environ.get('BLOG_BASE') or 'https://dylanninin.com'
GITHUB_TOKEN = os.environ.get('GH_PAT')
IMAGE_DEST = 'assets/images/issues'
IMAGE_EXT = '.png'
POST_DEST = '_posts'
POST_CATEGORY = 'Post'
POST_FILTER_LABEL = 'post'
POST_FILTER_DATE = '2023-01-01'
FMT_DATE = '%Y-%m-%d'
POST_LAYOUT = '''---
layout: post
title: {title}
categories: [{categories}]
tags : [{tags}]
---
'''
POST_FOOTER = '''Original Post

- Issue: [{title}]({url})
- Created: {created_at}
- Updated: {updated_at}

'''

README_HEADER = '''
Blog
---

- [GitHub Issue as a Blog](https://github.com/dylanninin/dylanninin.com/issues/72)
- [Public Blog](https://dylanninin.com)

---

Issues
---

'''


gh = Github(GITHUB_TOKEN)
repo = gh.get_repo(os.environ.get('GH_REPO'))


def render_readme(posts):
    with open('README.md', 'w') as f:
        f.write(README_HEADER)
        for post in posts:
            text = '- [{title}]({url}) - {date}\n'.format(**post)
            f.write(text)


def export_issues():
    issues = repo.get_issues(state='closed')
    posts = []
    for issue in issues:
        date = issue.created_at.strftime(FMT_DATE)
        if date < POST_FILTER_DATE:
            break
        tags = [i.name for i in issue.labels]
        if POST_FILTER_LABEL not in tags:
            print(f'skip issue-{issue.number}: {issue.title}')
            remove_issue(issue.number)
        else:
            print(f'export issue-{issue.number}: {issue.title}')
            post = export_issue(issue.number)
            posts.append(post)
    render_readme(posts)


def remove_issue(number):
    issue = repo.get_issue(number=number)
    date = issue.created_at.strftime(FMT_DATE)
    slug = issue.title.replace('  ', ' ').replace(' ', '-').lower()
    path = f'{POST_DEST}/{date}-{slug}.md'
    if os.path.exists(path):
        print(f'remove issue-{issue.number}: {issue.title}, path: {path}')
        os.remove(path)


def export_issue(number):
    issue = repo.get_issue(number=number)
    date = issue.created_at.strftime(FMT_DATE)
    slug = issue.title.replace('  ', ' ').replace(' ', '-').lower()
    path = f'{POST_DEST}/{date}-{slug}.md'
    # label as tags
    tags = ','.join([i.name for i in issue.labels])
    # milestone as category
    categories = issue.milestone.title if issue.milestone else POST_CATEGORY
    layout = POST_LAYOUT.format(title=issue.title, categories=categories, tags=tags)
    # comments as content parts
    comments = '\n'.join([i.body for i in issue.get_comments()])

    # footer = POST_FOOTER.format(title=issue.title, created_at=issue.created_at, updated_at=issue.updated_at, url=issue.html_url)

    content = '\n'.join([layout, issue.body, comments])
    content = update_links(content)

    with open(path, 'w') as f:
        f.write(content)

    post = {
        'title': issue.title,
        'date': date,
        'url': issue.html_url,
        'path': path,
    }
    return post


def update_links(content):
    assets = download_images(content)
    # update links
    for k, v in assets.items():
        v = os.path.join(BLOG_BASE, v)
        content = content.replace(k, v)
    return content


def download_image(url):
    path = os.path.join(IMAGE_DEST, os.path.basename(url))
    if not path.endswith(IMAGE_EXT):
        path = path + IMAGE_EXT
    if os.path.exists(path):
        print(f'skip exists: path={path}, url={url}')
        return path
    print(f'download: path={path}, url={url}')
    resp = requests.get(url, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    if resp.status_code == 200:
        buf = BytesIO(resp.content)
        buf.seek(0)
        with open(path, 'wb') as f:
            f.write(buf.getbuffer())
        return path
    return path


def download_images(text):
    result = {}
    for line in text.split('\n'):
        if line.startswith('<img'):
            url = line.split('"')[-2]
            result[url] = download_image(url)
    return result


if __name__ == '__main__':
    export_issues()
