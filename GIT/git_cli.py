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
test: added test class UserModel
build(routes-for-api-docs): initial version
refactor(routes): rename url '/pages/<int:id>'
fix: validate 'parameter[].property' values


# ===============================================================================================
# POPULAR COMMAND
# ===============================================================================================
# https://www.youtube.com/watch?v=3HJoXpC9vAM


# старт
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

git merge develop                         # слить в текущую ветку develop 
git merge origin/master                   # слить в текущую ветку origin/master 

git branch -v                             # покажет последний коммит в текущей ветке


# === перенос коммитов из master в ветку fix

# нужно создать в мастере ветку fix
git checkout -b fix

# нужно передвинуть мастер назад к нужному коммиту
# при этой операции все коммиты выше достанутся ветке fix
git branch master -f hash_of_right_master_commit
# тоже самое с checkout
git checkout -B master hash_of_right_master_commit


# === получение изменений из удаленного репо
git fetch origin                          # получить изменения из удаленного репо origin
git pull                                  # git fetch + git merge одной командой
git pull origin main                      # явное указание откуда брать


# === ADD(добавление в индекс)
git add .
git add index.html
git add -p index.html


# === COMMIT(добавление в репозиторий)
git commit -m "some message"
git commit -am "some message"             # = git add + git commit
git commit -c "some message"              # сделать коммит с уже имеющимся сообщением
git commit --amend -m "some message"      # внесет изменения в последний коммит(пересоздаст его) + новый коммент
git commit --amend --reset-author         # внесет изменения в последний коммит(пересоздаст его) + запишет текущего автора


# === RESET откат после commit
git reset --hard HEAD^1                   # возврат на 1 коммит, текущий stage удален, рабочая директория сброшена
git reset ‐‐soft HEAD^1                   # возврат на 1 коммит, текущий stage останется, рабочая директория остается
git reset ‐‐soft hash                     # перемещает ветку на нужный коммит, текущий stage останется, рабочая директория остается
git reset --mixed HEAD^1                  # возврат на 1 коммит, текущий stage удален, рабочая директория остается
git reset                                 # по умолчанию --mixed, в данном случае очистит от stage текущий коммит
git reset index.html                      # удаляет из stage файл


# === CLEAN(очистка директории)
git clean -dxf                            # удаляет из директории только неотслеживаемые файлы, d - директории, x - файлы из .gitignore 


# === отмена внесенных в файлы изменений до stage(до add)
git checkout -- .                         # отмена всех изменений
git checkout -- index.html                # отмена изменений в файле
git checkout -f HEAD                      # отмена всех изменений
git checkout -f                           # отмена всех изменений


# === восстановление файла 
git checkout hash index.html              # до состояния на момент коммита
git checkout HEAD index.html              # до состояния текущего коммита    
git checkout index.html                   # до состояния текущего коммита из индекса в рабочую директорию    


# === STASH(позволяет отложить изменения, а потом снова вернуть)
git stash                                 # соберет незакоммиченные изменения, удаляет их из файлов, и архивирует в гит 
git stash pop                             # вернет изменения из stash в эту ветку или другую ветку(возможна ошибка)


# === REFLOG(история ссылок)
git reflog
git reflog master
git reflog feature -1                     # покажет посследнюю запись
git reflog --date=iso                     # покажет ссылки с датами


# === LOG
git log                                   # выведет лог текущей ветки
git log master                            # выведет лог ветки master
git log master --online                   # выведет лог ветки master кратко
git log feature ^master                   # покажет коммиты feature кроме коммитов доступных из ветки master
git log master..feature                   # то же самое
git log index.html                        # покажет коммиты в которых менялся файл
git log -p index.html                     # покажет коммиты в которых менялся файл + различия
git log --grep Run -i feature             # покажет все коммиты ветки feature со словом Run в заголовке (-i - регистронезависимость)
git log --author=Vadim                    # покажет все коммиты ветки с автором
git log --committer=Vadim                 # покажет все коммиты ветки с коммиттером
git log --before '2018-02-23'             # покажет все коммиты до
git log --after '2018-02-23 08:30:00 +02' # покажет все коммиты после


# === DIFF
git diff hash1 hash2                      # сравнивает состояние на момент 2 коммитов
git diff master feature                   # сравнивает состояние на момент последних коммитов в ветках
git diff master...feature                 # что именно изменилось в feature после отхождения от master
git diff HEAD                             # сравнивает рабочую директорию с коммитом из HEAD
git diff                                  # сравнивает рабочую директорию с индексом(покажет изменения не в индексе)
git diff --cached                         # сравнивает индекс с последним коммитом(покажет что попадетв следующий коммит)
git diff --no-index file1.py file2.py     # сравнивает любые 2 файла на диске независимо от наличия git
git diff HEAD^1                           # родитель 1 у merge commit
git diff HEAD^2                           # родитель 2 у merge commit
git diff HEAD^1^                          # первый родитель первого родителя у merge commit
git diff HEAD^2^                          # первый родитель второго родителя у merge commit
git diff HEAD~3                           # переход по первому родителю на 3 коммита вниз(те по ветке вниз)


# работа с тегами
git tag v2.0                              # создать тег
git tag -d v2.0                           # удалить локальный тег
git push origin v2.0                      # запушить тег

git push origin :refs/tags/<tag-name>     # remove tag


# === MERGE(2 ветки сливаются в 1)
# merge не меняет историю, поэтому подходит для работы над feature1 веткой сразу нескольих разработчиков

# все коммиты develop попадут в мастер(через слияние перемоткой)
git merge develop                         # обновляет текущую ветку master коммитами из develop
git merge master develop                  # обновляет master коммитами из develop

# мержит через создание коммита слияния(исключает мерж через перемотку)
# все коммиты ветки feature остаются в ней
# коммит слияния содержит в себе все коммиты feature
git merge --no-ff --no-edit feature
git config merge.ff false                           # включает --no-ff во все коммиты по умолчанию
git config branch.master.mergeoptions '--no-ff'     # включает --no-ff для конкретной ветки по умолчанию

# мержит в текущую ветку новый коммит из удаленного репо origin/develop
git merge origin/master      

# выполнит мерж перенеся только последний коммит из fix
# промежуточные коммиты ветки fix не будут включены 
# при использовании --squash файл MERGE_HEAD не создается
git merge --squash fix

# отмена слияния сделанного только что
git reset --hard ORIG_HEAD


# === REBASE(добавляет новые коммиты к старым)

# rebase удобно использовать для обновления своей feature1 ветки из develop
# с rebase опасно работать если с feature1 веткой работает сразу несколько разработчиков
# все изменения из feature1 будут добавлены после всех коммитов develop
git rebase develop                             # перебазирует develop на вершину текущей ветки
git rebase develop feature                     # перебазирует feature на вершину develop

# перебазирование части ветки на мастер
# от ветки master отходит ветка feature, а от нее fix
git rebase --onto master feature               # перебазирует коммиты от feature до fix

# запуск комманды после каждого перебазированного коммита(обычно это тесты)
git rebase -x 'run tests' master               # в случае падения тестов перебазирование остановится для исправления

# отмена изменений rebase
git reset --hard ORIG_HEAD

# обновляет текущую ветку из удаленного репо origin/develop 
git pull --rebase origin/develop          

# интерактивный rebase одной ветки в другую
git rebase -i feature1                     # интерактивный rebase  на feature1

# интерактивный rebase текущей ветки чтобы изменить историю
git rebase -i HEAD~3                       # редактирование второго коммита с конца  
# --- popular options
# pick f4037ec The last commit             # копирование без изменений 
# reword                                   # копирование без изменений + редактируем commit message
# edit 4b6e19a The second to last commit   # скопирует коммит и позволит отредактировать(сделать amend)
# quash                                    # коммит нужно слить с предыдущим, сообщения объединить, коммит удалить
# fixup                                    # коммит нужно слить с предыдущим, сообщения удалить, коммит удалить
# exec                                     # добавление произвольных коммандпосле копирования коммита(например тесты)
# drop                                     # удалит коммит

git add .                                  # вносит изменения в stage
git commit --amend                         # пересоздаст коммит с прежним сообщением
git rebase --continue                      # продолжит изменения
git push origin feature1 --force           # запушит в удаленную ветку feature1
git push origin +feature1                  # тоже самое (запушит в удаленную ветку feature1)

git rebase --abort                         # удалит информацию о процессе rebase, вернув все в исходное состояние
git rebase --skip                          # пропустит коммит в случае конфликта


# сделает заплатку типа аменда после любого коммита
git commit -a --fixup=32d44                # создаем коммит заплатку с исправлениями для коммита 32d44. Поставит коммит сразу после 32d44. 
git rebase -i --autosquash                 # перебазирует ветку, плохой коммит и заплатка будут объединены.

git config --global rebase.autoSquash true # включает autosquash по умолчанию для git rebase -i

# === REVERT(новый коммит, который отменяет изменения в коммите с ошибкой(создает обратный коммит). Реверт не меняет историю.)
git revert hash_badcommit


# === CHERRY PICK(копирует 1 конкретный коммит в выбранную ветку)
git cherry-pick hash
git cherry-pick hash --edit        # выполнит команду с старым commit message
git cherry-pick hash --no-commit   # скопирует коммит в целевую ветку, но не создаст там коммит, а даст возможность доработать
git cherry-pick --abort            # отменит коммит, вернет как было
git cherry-pick --continue         # продолжит выполнение cherry-pick
git cherry-pick --quit             # остановиться сейчас и сбросить полученное состояние


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
    l = log --format=format:'%C(yellow)%h %C(green)%ad %C(dim white)[%an] %C(dim cyan)%s%C(reset)%C(bold blue)%d' --date=format:'%F %R'
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

