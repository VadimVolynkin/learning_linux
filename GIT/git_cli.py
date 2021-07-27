

https://github.com/VadimVolynkin?tab=repositories            my repo
https://devpractice.ru/category/git/
https://geekbrains.ru/events                                 advanced git

# ===============================================================================================
# POPULAR COMMAND
# ===============================================================================================

git init
git remote add origin git@github.com:VadimVolynkin/SomeRepo.git
git remote remove origin
git remote -v
git add .
git status
git commit -m "Some Message"
git commit ‐‐amend                        # amend last commit in local branch
git commit -a --amend -m "Some comment"
git push -u origin main
git clone git@github.com:VadimVolynkin/SomeRepo.git
git clone https://gist.github.com/VadimVolynkin/deff9f06fc01c104dd29f2b4264678e4
rm -rf .git
nano .git/config

git branch -a                             # list all branches (local and remote)

git tag v2.0
git tag -d v2.0                           # remove local tag

git push origin :refs/tags/<tag-name>     # remove tag
git push origin v2.0

git pull origin main
git pull                                  # git fetch + git merge
git pull ‐‐rebase

git fetch                                 # get changes from server and save it in refs/remotes/
git merge                                 # merge changes to local
git log ‐‐no-merges                       # list commit without merge and conflicts commit - only changes
git revert ‐‐no-commit [commit]
git diff -w                               # watch changes between 2 commits

git reset ‐‐soft HEAD^                    # return to last commit with add changes
git reset --soft HEAD~3                   # remove last 3 comment, but state will be like last
git reset --hard HEAD~2                   # remove last 2 commits


# Global Setting
git config --global user.name "Vadim Volynkin"
git config --global user.email "some@mail.ru"
git config -l

# ===============================================================================================
# BRANCHES
# ===============================================================================================

git branch amazing_new_feature            # create new branch
git checkout -b amazing_new_feature       # create and go to new branch
git checkout -b new-branch-name origin/new-branch-name          # create, switch and clone from remote
git checkout amazing_new_feature          # change brench
git checkout --orphan <branch_name>       # create new branch without history
git branch -m <new-branch-name>           # rename branch
git branch                                # list all branches
git branch -vv                            # list all branches with commits
git merge amazing_new_feature             # make this in master branch. Command will merge from another branch (dev)
git branch -d awesome_new_feature         # remove local branch
git branch –D awesome_new_feature         # remove local branch without wait merge in master branch
git push origin :<remote_branchname>      # remove remote branch
git branch --merged master                # list all branches what were merged in master
git branch --merged master | grep -v '^\*' | xargs -n 1 git branch -d      # remove all branches what were merged in master

-----------------------------------------------------------------------------------

usage: git branch [<options>] [-r | -a] [--merged | --no-merged]
   or: git branch [<options>] [-l] [-f] <branch-name> [<start-point>]
   or: git branch [<options>] [-r] (-d | -D) <branch-name>...
   or: git branch [<options>] (-m | -M) [<old-branch>] <new-branch>
   or: git branch [<options>] (-c | -C) [<old-branch>] <new-branch>
   or: git branch [<options>] [-r | -a] [--points-at]
   or: git branch [<options>] [-r | -a] [--format]

Generic options
    -v, --verbose         show hash and subject, give twice for upstream branch
    -q, --quiet           suppress informational messages
    -t, --track           set up tracking mode (see git-pull(1))
    -u, --set-upstream-to <upstream>
                          change the upstream info
    --unset-upstream      Unset the upstream info
    --color[=<when>]      use colored output
    -r, --remotes         act on remote-tracking branches
    --contains <commit>   print only branches that contain the commit
    --no-contains <commit>
                          print only branches that don't contain the commit
    --abbrev[=<n>]        use <n> digits to display SHA-1s

Specific git-branch actions:
    -a, --all             list both remote-tracking and local branches
    -d, --delete          delete fully merged branch
    -D                    delete branch (even if not merged)
    -m, --move            move/rename a branch and its reflog
    -M                    move/rename a branch, even if target exists
    -c, --copy            copy a branch and its reflog
    -C                    copy a branch, even if target exists
    --list                list branch names
    -l, --create-reflog   create the branch's reflog
    --edit-description    edit the description for the branch
    -f, --force           force creation, move/rename, deletion
    --merged <commit>     print only branches that are merged
    --no-merged <commit>  print only branches that are not merged
    --column[=<style>]    list branches in columns
    --sort <key>          field name to sort on
    --points-at <object>  print only branches of the object
    -i, --ignore-case     sorting and filtering are case insensitive
    --format <format>     format to use for the output




# ===============================================================================================
# COMMIT
# ===============================================================================================

git cherry -v master                                  list commit for current branch

git log                                                       list all commit

git log --oneline                                        list all commit with messages

git log -1                                                   history of last change

git log -1 -p                                               what was changed in last commit

git show b10cc123                                   check changes in last commit

git show 18411fd:hello.txt                        show state of file in commit

git diff 09bd8cc..ba25c0ff                         check changes between 2 commits

git difftool 09bd8cc..ba25c0ff                   the same action with graphics

git checkout 09bd8cc1 hello.txt               change commit version for file

git commit --amend -m "third commit"     commit in repo with amend last commit

git revert 09bd8cc1                                  after push on server create commit what will cancel changes in some commit

git revert HEAD                                        after push on server create commit what will cancel changes in last commit. Return state to last commit in branch.

git stash                                                   save temporary files state in buffer if we need to change branch(its NOT commit)

git stash pop                                            get this state back from buffer

git reset --soft B                                       go to B with C changes in index(added new changes). If commit B => new C = old C

git reset --mixed B   or git reset B            go to B without changes C in index. We have changes what need to add and commit to get new C = old C

git reset --hard B                                      go to B and delete all changes C. Current state files = state B.
Work with file

git checkout -- hello.txt                            download last version from this branch repo

git show 18411fd:hello.txt                        show state of file in commit

git checkout 09bd8cc1 hello.txt               change file to commit version

 



Resolve merge conflicts

git mergetool                                             tool with graphic interface
SSH KEY

ssh-keygen

cat ~/.ssh/id_rsa.pub





 

