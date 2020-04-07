# Notes on How to Use Git and Interact with Github

## Notes were derived from the Codacademy module on Git


### Git projects have three parts:

1.  A working directory: where you will be doing al lteh work: creating, editing, and organzing files.

2.  A staging area:  lists changes you make to the working directory.

3.  A repository:  Git permanently stores those changes as different versions of the project.


```
$ git init
```
   Initializes the project and sets up the tools to begin tracking changes on a project.

```
$ git status
```
   Checks and reports the status of changes.
   Files in *Red* are untracked meaning git has not started tracking changes. 


```
$ git add <filename>
```
   To start tracking changes, files need to be first added to the staging area.
   Use *git add* to add to the staging area.
   Text in green is in the staging area.

```
$ git diff <filename>
```
   Checks the difference between the working directory and the staging area.

```
$ git commit -m "enter your message here"
```
   The last step in the Git workflow
   Commits permanently.  Stores changes from the staging area in side repository.
   Standard conventions of a commit message:
   1.  Must be in quotation marks.
   2.  Written in present tense.
   3.  50 characters or less

```
$ git log
```
   Lists commits to repository chronologically.

### In Git, the commit you are on is *HEAD* known as the head commit.  In most cases the most recently made commit is the head commit.

```
$ git show HEAD
```
   Shows you the head commit.
   Output shows everthing the git log command displays for the HEAD commit, plus all the files changes that were committed. 

```
$ git checkout HEAD <fileneame>
```
   Will restore the file in your working directory to look exactly as it did when you made the last commit.  Essentially erases the changes made since the last commit.

   Working Directory --> Staging Area --> Repository

```
$ git reset HEAD <filename>
```

   Resets the file in the staging area to be the same as the HEAD commit.  It does not discard file changes from the working directory it just removes them from the staging area.

```
$ git reset SHA
```

   Rewinds a project to a specific commit.  SHA is a specific log code number for a commit (the first seven characters).  This is a great way to rewind history.

```
$ git checkout HEAD <filename>
```

   Discards changes in the working directory.



   Once the repository is made and committed, it can be pushed to Github website.

   First, go to the website and create a repository.  After this, you will have initial information like this.  [insert picture]

   Since you have made the initial commit, add the remote repository, and commit it to github.

```
$ git remote add origin https://github.com/mcelrjo/trinotateExtractor.git

$ git push -u origin master
```