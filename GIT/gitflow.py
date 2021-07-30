# ===============================================================================================
# ВИДЫ flow
# ===============================================================================================

# === Central Workflow
Репозиторий содержит только одну главную ветку master. Все изменения комитятся в нее. 
Репозиторий может быть локальным, без удаленных копий или храниться удаленно, где он может быть клонирован или запушен.

Идеально подходит для одиночного проекта.

# === Developer Branch Workflow
У каждого разработчика есть своя личная ветка. Все изменения, опубликованные в удаленном репозитории будут в этой ветке. Вся работа может быть выполнена на разных ветках, но потом должна будет слита(merged) в одну главную ветвь.

Больше подойдет для небольшого проекта с ограниченным количеством требований и небольшим количеством разработчиков, которым нужно чтобы их изменения в проекте были просмотрены до слияния с веткой master. Допустим у вас групповое задание, каждый участник делает свою часть, а затем публикует её в удаленном репозитории для того чтобы остальные её увидели до того, как она будет слита. В идеале это должно быть сделано с помощью запроса pull (merge). Также это может стать удобным способом для представления пулла в команде или организации.

# === Feature Branch Workflow
Под каждую фичу создается ветка. Все эти ветки мержаться в ветку dev со стабильным тестируемым кодом. dev сливается с master после теста. 

В своей простейшей форме репозиторий мог бы иметь основную ветку со стабильным, доступным кодом и другими ветками для разных фич (или багов, или улучшений), которые можно бы было интегрировать в главную ветку. То есть репозиторий будет иметь второстепенную основную ветку (dev) которая будет хранить тестируемый стабильный код для отправки пользователям, когда он будет слит с master. В этом случае ветка с фичами будет слита с dev, а не с master.

Этот подход больше подходит командам, которые используют какой-то метод по управлению проектами(например Agile). Давайте скажем, что ваш проект находится в продолжительной разработке и вам нужно добавить набор фич до следующего релиза. Эти фичи назначены разным разработчикам, которые создают отдельную ветку для каждой опубликованной фичи до того, как она будет слита с dev для тестирования. Когда вы готовы к релизу, dev сливается с master.

# Issue Branch Workflow
Очень похожа на предыдущую модель с одним лишь различием. Ветки создаются из заданий в проектном трекере. Ветки могут иметь одинаковые названия id заданий. И здесь только одна ветка на задание и одно задание на ветку.

Лучше всего подойдет проектам, которые управляются по какому-то методу. Однако, несмотря на это, больше подходит тем проектам, в которых фичи готовятся не одним разработчиком. Например, если бы вы работали над самим интерфейсом, а другой разработчик работал над его другим аспектом. Он может быть применен в обоих проектах, релизы которых выходят постоянно или время от времени.

# Forking Workflow
Куча веток - форков. Доступ только для чтения. Слияние в главную через запрос и подтверждение. Подходит для опенсорса.

Благодаря этой модели, дополнения проекта осуществляются путем создания разветвления его репозитория. Все изменения фиксируются в любой ветке репозитория, а затем возвращаются в исходное хранилище с pull запросом. Разработчики будут иметь доступ только к чтению в удаленном репозитории.

Чаще всего используется в проектах с открытым исходным кодом и публичными репозиториями. Каждый кто может просматривать репозиторий может сделать разветвление. До тех пор, пока они могут просматривать репозиторий им не нужен доступ для того чтобы внести изменения напрямую в репозиторий. Когда они закончили свою работу, они могут сделать запрос, который вы будете рассматривать и решите, что же с ним делать, интегрировать, отказать или просить доработать до окончательного слияния с проектом.

# Patch Workflow
Используя этот подход, разработчики добавляют изменения в репозиторий вместе с патчем - файлом, который содержит все изменения в репозитории. Этот патч применяется кем-то, кто может напрямую писать в репозиторий, например maintainer/owner.

Используется если разработчик не может напрямую писать в репозиторий, но имеет доступ к исходному коду. Если, например, вы поделились кодом своего проекта с другом или он получил доступ к вашему удаленному репозиторию. После тех изменений, которые вы закомиттили в их копию исходного кода создается патч и отправляется вам. Вы применяете их к репозиторию чтобы обновить его. Также используется теми, кто не является главным разработчиком проекта.


# ===============================================================================================
# GIT-Flow
# ===============================================================================================
# Считается что идеален для Agile команд

# Master
Рабочая версия для клиента с релиз тегами. 
Сюда можно мержится только из веток Release и Hotfix.

# Develop
Рабочая версия для команды разработиков и QA. 
Создается в начале из Master.
Каждый коммит в нее должен быть рабочим кодом.

# Feature/Purchase
Разрабатываемая функциональность. 
Создается из Develop для конкретного разработчика и задачи.

По завершению разработки из Develop берется последний коммит и сливается с этой веткой (интеграция). Это можно делать в процессе разработки (каждое утро или чаще) для актуальности кода - помогает снизить конфликты при мерже.

CI создает build и далее код тестируется QA. После успешного теста мержится в Develop.

# Release
Тестирование новой версии. 
Создается из Develop в конце разработки новой функциональности для этой версии или Milestone. 
Новую функциональность из Feature в эту ветку включать нельзя.

Разработчик закоммитил. CI собрал build. Полноценное тестирование build QA.

После успешных тестов мержится в Master с тегом v2.0  +  в Develop чтобы у разработчиков была самая актуальная и протестированная версия продукта.

# Hotfix
Тестирование исправлений. Для срочных исправлений продакшн кода. 
Создается из последнего коммита в Master.

Тестируется QA

После успешных тестов мержится в Master и Develop с тегом v2.1.