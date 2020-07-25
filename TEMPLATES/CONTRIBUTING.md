# Contributing

First off, thank you for considering contributing to Assist.

Assist is an open source project and we would love to receive contributions from our community — you!

There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, creating tests, submitting bug reports and feature requests, or writing code which can be incorporated into Assist itself. We greatly value all contributions.

## Branching Guide

The `master` branch contains the latest changes, and is not guaranteed to be stable. 

First you'll need to fork the repository.

On your fork, create a branch and work on it. Submit your pull requests to the master, if any instruction is not explicitly specified for your changes by the maintainers.

## Working on Assist
  
**Step 01 :** The process of setting up Assist for development isn't different. To activate virtual environment mode, just run

```
$ source venv/bin/activate
```
**Step 02 :** Then, The new feature must be added to `/assistant/plugins/` 
**Step 03 :** Make sure that the code is in the form of a definition which preferably takes arguments.
**Step 04 :** In `__main__.py` add the feature by importing it from the plugins package.
**Step 05 :**Follow PEP8 standard for code by running `./test.py`.
**Step 06 :** Make sure to add it in the `assist_instruction.py` file and [FEATURES.md](/FEATURES.md) file.


## Commit messages

We have a handful of simple standards for commit messages to keep complete track of changes.

-  **1st line**: Max 90 character summary written in past tense
-  **2nd line**: [Always blank]
-  **3rd line**: refs/closes #000 or no issue
-  **4th line**: A list of extra details or anything else worth mentioning
  
## Pull Requests

Please provide plenty of context and reasoning around your changes, to help us merge quickly. Closing an already open issue is our preferred workflow. If your PR gets out of date, we may ask you to rebase as you are more familiar with your changes than we will be.  

## Tests

The automated tests are currently in development. Changes have to be manually verified at the moment ⚒