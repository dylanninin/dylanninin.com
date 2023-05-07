import os

# see https://pygithub.readthedocs.io/en/latest/examples.html
from github import Github

POST_DEST = '_posts'
POST_CATEGORY = 'Post'
POST_FILTER_LABEL = 'post'
POST_FILTER_DATE = '2023-01-01'
FMT_DATE = '%Y-%m-%d'
POST_HEADER = '''---
layout: post
title: {title}
categories: [{categories}]
tags : [{tags}]
---
'''
POST_FOOTER = '''
---
Original Post

- Issue: [{title}]({html_url})
- Created: {created_at}
- Updated: {updated_at}
'''


gh = Github(os.environ.get('GH_PAT'))
repo = gh.get_repo(os.environ.get('GH_REPO'))


def export_issues():
    issues = repo.get_issues(state='closed')
    for issue in issues:
        date = issue.created_at.strftime(FMT_DATE)
        if date < POST_FILTER_DATE:
            break
        tags = [i.name for i in issue.labels]
        if POST_FILTER_LABEL not in tags:
            print(f'skip issue-{issue.number}: {issue.title}')
            continue
        else:
            print(f'export issue-{issue.number}: {issue.title}')
            export_issue(issue.number)


def export_issue(number):
    issue = repo.get_issue(number=number)
    date = issue.created_at.strftime(FMT_DATE)
    slug = issue.title.replace('  ', ' ').replace(' ', '-').lower()
    path = f'{POST_DEST}/{date}-{slug}.md'
    # label as tags
    tags = ','.join([i.name for i in issue.labels])
    # milestone as category
    categories = issue.milestone.title if issue.milestone else POST_CATEGORY
    header = POST_HEADER.format(title=issue.title, categories=categories, tags=tags)
    # comments as content parts
    comments = '\n'.join([i.body for i in issue.get_comments()])
    footer = POST_FOOTER.format(title=issue.title, created_at=issue.created_at, updated_at=issue.updated_at, html_url=issue.html_url)
    with open(path, 'w') as f:
        f.write(header + '\n')
        f.write(issue.body + '\n')
        f.write(comments)
        f.write(footer)
    return path


if __name__ == '__main__':
    export_issues()
