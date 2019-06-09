# Contributing

First off, thank you for considering contributing to Assist.

Assist is an open source project and we would love to receive contributions from our community — you!

There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, creating tests, submitting bug reports and feature requests, or writing code which can be incorporated into Assist itself. We greatly value all contributions.

## Working on Assist

The process of setting up Assist for development isn't different. To activate virtual environment mode, just run

```
$ source assistant/bin/activate
```

## Branching Guide

The `master` branch contains the latest changes, and is not guaranteed to be stable. It represents WIP for the next release. Stable versions are tagged using SemVer.

First you'll need to fork the repository.

On your fork, create a branch and work on it. Submit your pull requests to the master, if any instruction is not explicitly specified for your changes by the maintainers.

## Commit messages

We have a handful of simple standards for commit messages to keep complete track of changes.

- **1st line**: Max 90 character summary written in past tense
- **2nd line**: [Always blank]
- **3rd line**: refs/closes #000 or no issue
- **4th line**: A list of extra details or anything else worth mentioning

## Pull Requests

Please provide plenty of context and reasoning around your changes, to help us merge quickly. Closing an already open issue is our preferred workflow. If your PR gets out of date, we may ask you to rebase as you are more familiar with your changes than we will be.

## Tests

The automated tests are currently in development. Changes have to be manually verified at the moment ⚒
