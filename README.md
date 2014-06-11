git-qdiff
=========

So you miss `bzr qdiff` ?
-------------------------

Of course you do ! Why would you be there ?

Installation
------------

    pip install --upgrade git-qdiff

Dependencies
------------

- git (1.7.11+)
- bazaar
- qbzr tools
- rsync

Usage
-----

Once installed, you should be able to use this command from any git repository:

    git qdiff

And this should launch your favorite difftool:

![screenshot](https://github.com/amigrave/git-qdiff/raw/master/screenshot.png)

Of course you can use the same notations as you would with `git diff`:

```bash
# Show both staged and unstaged changes
$ git qdiff HEAD

# Using tilde and carrets
$ git qdiff HEAD~2..HEAD~3

# Between commits
$ git qdiff 53c43de..7c70faf

# Between branches
$ git qdiff my_feature..origin/master

# ...
```

Known problem
-------------

- `Refresh` button won't work

Before reporting an issue, please check that your `bzr qdiff` tool works well.

License
-------

This software is licensed under the MIT license
