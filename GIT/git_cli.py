# ПРАВИЛА ПОЛЕТА В ГИТЕ
https://github.com/k88hudson/git-flight-rules/blob/master/README_ru.md

# ВИДЕОТУТОРИАЛ
https://www.youtube.com/watch?v=g0GgtqlhHaw&list=PLDyvV36pndZFHXjXuwA_NywNrVQO0aQqb&index=16


# ===============================================================================================
# РЕКОМЕНДАЦИИ
# ===============================================================================================


# заголовок коммита должен быть не более 50 символов, далее может быть строка отступа и описание
# далее примеры хороших заголовков
feat: added new feature sorting on somepage.html
test: added test of class UserModel
build(routes-for-api-docs): initial version
refactor(routes): rename url '/pages/<int:id>'
fix: validate 'parameter[].property' values


# ===============================================================================================
# POPULAR COMMAND
# ===============================================================================================
# https://www.youtube.com/watch?v=3HJoXpC9vAM


# для старта
git init                                  # создает git в текущей папке
git branch -M main                        # создает ветку main
git remote add origin git@github.com:VadimVolynkin/SomeRepo.git  # создает привязку к origin
git remote remove origin                  # удаляет привязку к origin
git remote -v                             # показывает все удаленные репо
git add .                                 # добавляет все файлы в stage 
git status                                # делает статус 
git commit -m "Some Message"              # делает коммит
git commit -am "Some Message"             # git add . + git commit -m ""
git commit ‐‐amend                        # допишет в последний коммит в локальной ветке
git commit -a --amend -m "Some comment"   # добавить все дописать в последний коммит в локальной ветке
git merge develop                         # обновляет текущую ветку коммитами из develop 
git push -u origin main                   # пушит в удаленный репо в ветку main
git push --set-upstream origin develop    # создает в удаленном репо ветку develop и пушит в нее
git clone git@github.com:VadimVolynkin/SomeRepo.git
git clone https://gist.github.com/VadimVolynkin/deff9f06fc01c104dd29f2b4264678e4
rm -rf .git                               # удаляет git
git rm -r src_path                        #  = rm -r src_path + git add src_path (удалит из проекта и индекса, но закоммитит)
git rm -r --cached src_path               # удаляет из индекса, но закоммитит

nano .git/config


# === работа с ветками
git branch                                # список локальных веток
git branch -a                             # список всех веток (local and remote)

git branch new_branch                     # создаем новую ветку
git checkout -b new_branch2               # создаст новую ветку и переключится на нее(изменения текущей ветки будут перенесены)
git checkout new_branch                   # переключаемся на послений коммит в new_branch(изменения текущей ветки могут быть перенесены)
git branch -D new_branch                  # удаляем ветку

git merge develop                         # обновляет текущую ветку коммитами из develop 
git merge origin/master                   # слить ветки ветка с изменениями/куда

git branch -v                             # покажет последний коммит в текущей ветке


# === получение изменений из удаленного репо
git fetch origin                          # получить изменения из удаленного репо origin
git pull                                  # git fetch + git merge одной командой
git pull origin main                      # явное указание откуда брать


# === откат после commit
git reset --hard HEAD^1                   # возврат на 1 коммит, все изменения удалены
git reset ‐‐soft HEAD^1                   # возврат на 1 коммит + оставить все текущие изменения в stage

# === очистка директории
git clean -dxf                            # удаляет из директории только неотслеживаемые файлы, d - директории, x - файлы из .gitignore 

# === удаление файлов из stage(после add)
git reset .                               # удаляет из stage все файлы
git reset index.html                      # удаляет из stage файл

# === отмена внесенных в файлы изменений до stage(до add)
git checkout -- .                         # отмена всех изменений
git checkout -- index.html                # отмена изменений в файле
git checkout -f HEAD                      # отмена всех изменений
git checkout -f                           # отмена всех изменений

# === восстановление файла 
git checkout hash index.html              # до состояния на момент коммита
git checkout HEAD index.html              # до состояния текущего коммита    
git checkout index.html                   # до состояния текущего коммита из индекса в рабочую директорию    


# === stash(позволяет отложить изменения, а потом снова вернуть)
git stash                                 # соберет незакоммиченные изменения, удаляет их из файлов, и архивирует в гит 
git stash pop                             # вернет изменения из stash в эту ветку или другую ветку(возможна ошибка)


# === перенос коммитов из master в ветку fix

# нужно создать в мастере ветку fix
git checkout -b fix

# нужно передвинуть мастер назад к нужному коммиту
# при этой операции все коммиты выше достанутся ветке fix
git branch master -f hash_of_right_master_commit
# тоже самое с checkout
git checkout -B master hash_of_right_master_commit


# === reflog(история ссылок)
git reflog
git reflog master
git reflog --date=iso                     # покажет ссылки с датами



# работа с тегами
git tag v2.0                              # создать тег
git tag -d v2.0                           # удалить локальный тег
git push origin v2.0                      # запушить тег

git push origin :refs/tags/<tag-name>     # remove tag



git pull ‐‐rebase
git log ‐‐no-merges                       # list commit without merge and conflicts commit - only changes
git revert ‐‐no-commit [commit]
git diff -w                               # watch changes between 2 commits
git log 2                                 # смотреть последние 2 коммита


https://github.com/k88hudson/git-flight-rules/blob/master/README_ru.md
git show                 последний коммит в HEAD 
git log -n1 -p


git show <commitid>:filename

git commit --amend --only -m 'xxxxxxx'











# === MERGE(2 ветки сливаются в 1)
# merge не меняет историю, поэтому подходит для работы над feature1 веткой сразу нескольих разработчиков

# все изменения попадут в мастер в виде 1 коммита
git merge develop                         # обновляет текущую ветку коммитом из develop
git merge develop feature1                # обновляет develop коммитом из feature1

# мержит в текущую ветку новый коммит из удаленного репо origin/develop
git merge origin/master                   


# === REBASE(добавляет новые коммиты к старым)

# rebase удобно использовать для обновления своей feature1 ветки из develop
# с rebase опасно работать если с feature1 веткой работает сразу несколько разработчиков
# все изменения из feature1 будут добавлены после всех коммитов develop
git rebase develop

# обновляет текущую ветку из удаленного репо origin/develop 
git pull --rebase origin/develop          

# интерактивный rebase одной ветки в другую
git rebase -i feature1                     # интерактивный rebase  на feature1

# интерактивный rebase текущей ветки чтобы изменить историю
git rebase -i HEAD~3                       # редактирование второго коммита с конца    
# edit 4b6e19a The second to last commit   # edit указывает что этот коммит будем менять, остальные оставим
# pick f4037ec The last commit
# --- popular options
# pick    # без изменений
# reword  # без изменений + изменение commit message
# fixup   # изменения этого коммита будут записаны в предыдущий коммит(как amend). Сам коммит исчезнет.
# drop    # удалит коммит
git add .                                  # вносит изменения в stage
git commit --amend                         # пересоздаст коммит с прежним сообщением
git rebase --continue                      # продолжит изменения
git push origin feature1 --force           # запушит в удаленную ветку feature1
git push origin +feature1                  # тоже самое (запушит в удаленную ветку feature1)


# REVERT(новый коммит, который отменяет изменения в коммите с ошибкой. Реверт не меняет историю.)
git revert hash_badcommit


# CHERRY PICK(переносит 1 конкретный коммит в выбранную ветку)
git cherry-pick hash
git cherry-pick hash --edit        # выполнит команду с старым commit message
git cherry-pick hash --no-commit   # перенесет коммит в целевую ветку, но не создаст там коммит, а даст возможность доработать

# === Global Setting
git config --global user.name "Vadim Volynkin"
git config --global user.email "some@mail.ru"
git config -l



# ===============================================================================================
# GIT ALIAS
# ===============================================================================================
# ~/.gitconfig

[alias]
    a = add
    amend = commit --amend
    c = commit
    ca = commit --amend
    ci = commit -a
    co = checkout
    d = diff
    dc = diff --changed
    ds = diff --staged
    extend = commit --amend -C HEAD
    f = fetch
    loll = log --graph --decorate --pretty=oneline --abbrev-commit
    g =  log --graph --abbrev-commit --decorate --all --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(dim white) - %an%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n %C(white)%s%C(reset)'
    m = merge
    one = log --pretty=oneline
    outstanding = rebase -i @{u}
    reword = commit --amend --only
    s = status
    unpushed = log @{u}
    wc = whatchanged
    wip = rebase -i @{u}
    zap = fetch -p
    day = log --reverse --no-merges --branches=* --date=local --since=midnight --author=\"$(git config --get user.name)\"
    delete-merged-branches = "!f() { git checkout --quiet main && git branch --merged | grep --invert-match '\\*' | xargs -n 1 git branch --delete; git checkout --quiet @{-1}; }; f"




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


# ===============================================================================================
# COMMIT
# ===============================================================================================

git cherry -v master                   # list commit for current branch
git log                                # list all commit
git log --oneline                      # list all commit with messages
git log -1                             # history of last change
git log -1 -p                          # what was changed in last commit
git show b10cc123                      # check changes in last commit
git show 18411fd:hello.txt             # show state of file in commit
git diff 09bd8cc..ba25c0ff             # check changes between 2 commits
git difftool 09bd8cc..ba25c0ff         # the same action with graphics
git checkout 09bd8cc1 hello.txt        # change commit version for file
git commit --amend -m "third commit"   # commit in repo with amend last commit
git revert 09bd8cc1                    # after push on server create commit what will cancel changes in some commit
git revert HEAD                        # after push on server create commit what will cancel changes in last commit. Return state to last commit in br.
git stash                              # save temporary files state in buffer if we need to change branch(its NOT commit)
git stash pop                          # get this state back from buffer
git reset --soft B                     # go to B with C changes in index(added new changes). If commit B => new C = old C
git reset --mixed B   or git reset B   # go to B without changes C in index. We have changes what need to add and commit to get new C = old C
git reset --hard B                     # go to B and delete all changes C. Current state files = state B.
Work with file
git checkout -- hello.txt              # download last version from this branch repo
git show 18411fd:hello.txt             # show state of file in commit
git checkout 09bd8cc1 hello.txt        # change file to commit version

 
# ===============================================================================================
# .gitignore
# ===============================================================================================

*.log      игнорить все лог файлы
logs/      директорию
file.txt

