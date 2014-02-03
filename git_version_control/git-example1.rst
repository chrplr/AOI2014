==========
Git basics
==========

:Author: 
    Christophe Pallier <christophe@pallier.org>

:Version: 0.1 of 2012/08/31

.. contents::
..
    1   Creating a local repository
    2   Adding files to the local repository
    3   Creating a snapshot, or commiting
    4   Modifying the project
    5   Renaming a file
    6   Recovering a file deleted by accident
    7   Checking for changes
    8   Faster commit
    9   Downloading the most recent changes from the distant repository
    10  Pushing your changes to the distant repository

Creating a local repository
---------------------------

From scratch:

::

    $ mkdir git-test
    $ cd git-test
    $ git init
    Initialized empty Git repository in /home/pallier/cours/Python/version_control/git-test/.git/

Importing from an existing project on the Internet:

::

    $ git clone git clone https://github.com/chrplr/pyepl_examples


Adding files to the local repository
------------------------------------

The command 'git add' is used to tell git which files it must *track*::

    $ echo 'essai1' > readme.txt
    $ git add readme.txt

Interestingly, you can also add whole directories, for example:: 
    
    $ git add . 
    
Note that it is possible to prevent certain files to be tracked (see https://help.github.com/articles/ignoring-files).
    
To check which files are currently being *tracked* (or *staged*), use the command git status::
    
    $ git status
    # On branch master
    #
    # Initial commit
    #
    # Changes to be committed:
    #   (use "git rm --cached <file>..." to unstage)
    #
    #       new file:   readme.txt
    #

    
Creating a snapshot, or commiting
---------------------------------
    
Once you are satisfied with the files in your working directory, you can take a snapshot. This is also called  *commiting* your changes::
    
    $ git commit
    [master (root-commit) a7a3a47] First commit
    1 file changed, 1 insertion(+)
    create mode 100644 readme.txt

    
Modifying the project
---------------------

Let us now modify the file readme.txt in the working directory::

    $ echo 'line2' >readme.txt
    
The command git status allows us to compare the state of files in the current directory and in the repository::     
    
    $ git status
    # On branch master
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       modified:   readme.txt
    #
    no changes added to commit (use "git add" and/or "git commit -a")
    $ git add readme.txt
    $ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       modified:   readme.txt
    #


Let us create a new file, readme2.txt::

    $ echo 'trial2' >readme2.txt
    $ ls
    readme2.txt  readme.txt
    $ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       modified:   readme.txt
    #
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #       readme2.txt

We now add readme2.txt to the repository::

    $ git add readme2.txt
    $ git commit
    [master a7e25a1] First revision; added readme2.txt
    2 files changed, 2 insertions(+), 1 deletion(-)
    create mode 100644 readme2.txt

Let us consult the history of the project::

    $ git log
    commit a7e25a158ce52a75c62381420f7dc375de631b1b
    Author: Christophe Pallier <christophe@pallier.org>
    Date:   Mon Aug 27 10:49:54 2012 +0200

	First revision; added readme2.txt

    commit a7a3a47edfae9d7c720356b691000a81ded73906
    Author: Christophe Pallier <christophe@pallier.org>
    Date:   Mon Aug 27 10:47:32 2012 +0200

	First commit



    $ git status
    # On branch master
    nothing to commit (working directory clean)

Renaming a file
---------------

To rename a tracked file, you should use git mv rather then just mv:    
    
    $ git mv file.ori file.new
    
    
Recovering a file deleted by accident
-------------------------------------

Let us delete readme2.txt "by accident"::

    $ rm readme2.txt # oops
    $ ls
    readme.txt
    $ git status
    # On branch master
    # Changes not staged for commit:
    #   (use "git add/rm <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       deleted:    readme2.txt
    #
    no changes added to commit (use "git add" and/or "git commit -a")


To recover it::

    $ git checkout -- readme2.txt
    $ ls
    readme2.txt  readme.txt
    $ cat readme2.txt
    trial2

Checking for changes
--------------------    

Let us now modify readme2.txt and then compare the file in the current directory from the ones in the last commit::

    $ echo 'line2 of 2' > readme2.txt
    $ git diff
    diff --git a/readme2.txt b/readme2.txt
    index 33d1e15..e361691 100644
    --- a/readme2.txt
    +++ b/readme2.txt
    @@ -1 +1 @@
    -trial2
    +line2 of 2
    $ git status
    # On branch master
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       modified:   readme2.txt
    #
    no changes added to commit (use "git add" and/or "git commit -a")

    
Faster commit
-------------
    
The command 'git commit -a' performs both a 'git add' and a 'git commit'::
    

    $ git commit -a
    [master a74359e] Second revision
    1 file changed, 1 insertion(+), 1 deletion(-)
    $ git log
    commit a74359e148aff0c369b6ddd482d0fbe0e7ad93ab
    Author: Christophe Pallier <christophe@pallier.org>
    Date:   Mon Aug 27 10:52:50 2012 +0200

	Second revision

    commit a7e25a158ce52a75c62381420f7dc375de631b1b
    Author: Christophe Pallier <christophe@pallier.org>
    Date:   Mon Aug 27 10:49:54 2012 +0200

	First revision; added readme2.txt

    commit a7a3a47edfae9d7c720356b691000a81ded73906
    Author: Christophe Pallier <christophe@pallier.org>
    Date:   Mon Aug 27 10:47:32 2012 +0200

	First commit


    
Downloading the most recent changes from the distant repository
---------------------------------------------------------------
    
If you imported your repository from the internet with 'git clone', you can import the recent changes with::
    
    
    $ git pull
    

Pushing your changes to the distant repository
----------------------------------------------

You can send your modified repository (after commiting) to the original internet repository::     
    
    $ git push
    
