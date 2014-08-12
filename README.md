git-qdiff
=========

So you miss `bzr qdiff` ?
-------------------------

Of course you do ! Why would you be here ?

Installation
------------

    $ sudo pip install --upgrade git-qdiff

Dependencies
------------

- git (1.7.11+)
- bazaar
- qbzr tools
- rsync

Usage
-----

Once installed, you should be able to use this command from any git repository:

    $ git qdiff

And this should launch your favorite difftool:

![screenshot](https://github.com/amigrave/git-qdiff/raw/master/screenshot.png)

Of course you can use the same notation as you would with `git diff`:

```bash
# Show both staged and unstaged changes
$ git qdiff HEAD

# Using tilde and carrets
$ git qdiff HEAD~2..HEAD~3

# Between commits
$ git qdiff 53c43de..7c70faf

# Before merging branches
$ git qdiff origin/master...my_feature_branch

# ...
```

Known problem
-------------

- `Refresh` button won't work

Before reporting an issue, please check that your `bzr qdiff` tool works well
and that you can actually commit something with bazaar.

Goodies
-------

### tig

For those using [tig](http://jonas.nitro.dk/tig/), here's a handy shortcut bound to `D` key.
Add this to your `.gitconfig`:

```ini
[tig "bind"]
    generic = D !git qdiff %(commit)~1..%(commit)
```

*Note: Don't try this on the "unstaged changes" line in tig's log view*

License
-------

This software is licensed under the MIT license
