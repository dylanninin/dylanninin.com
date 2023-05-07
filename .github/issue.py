import os

# see https://pygithub.readthedocs.io/en/latest/examples.html
from github import Github

DEST = '_posts'
CATEGORY = 'Post'
FMT_DATE = '%Y-%m-%d'
SINCE_DATE = '2023-01-01'
POST_HEADER = '''---
layout: post
title: {title}
categories: [{category}]
tags : [{tags}]
---
'''
gh = Github(os.environ.get('GH_PAT'))
repo = gh.get_repo(os.environ.get('GH_REPO'))


def export_issues():
    issues = repo.get_issues(state='closed')
    for issue in issues:
        date = issue.created_at.strftime(FMT_DATE)
        if date < SINCE_DATE:
            break
        tags = [i.name for i in issue.labels]
        if 'post' not in tags:
            print(f'skip issue-{issue.number}: {issue.title}')
            continue
        else:
            print(f'export issue-{issue.number}: {issue.title}')
            export_issue(issue.number)


def export_issue(number):
    issue = repo.get_issue(number=number)
    date = issue.created_at.strftime(FMT_DATE)
    slug = issue.title.replace('  ', ' ').replace(' ', '-').lower()
    path = f'{DEST}/{date}-{slug}.md'
    tags = ','.join([i.name for i in issue.labels])
    header = POST_HEADER.format(title=issue.title, category=CATEGORY, tags=tags)
    comments = '\n'.join([i.body for i in issue.get_comments()])
    with open(path, 'w') as f:
        f.write(header + '\n')
        f.write(issue.body + '\n')
        f.write(comments)
    return path


if __name__ == '__main__':
    export_issues()
