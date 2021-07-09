# ===================================================================================================================================
# РАСПАКОВКА TAR
# ===================================================================================================================================

# РАСПАКОВКА TAR.GZ
tar -xzvf Archive.tar.gz                # распаковка всего архива сюда же
tar -xzvf Archive.tar.gz dir            # распаковка только 1 директории
tar -xzvf Archive.tar.gz file.txt       # распаковка только 1 файл
tar -ztvf Archive.tar.gz                # показ содержимого перед началом распаковки


-x  # извлечение файлов из архива
-c  # создать архив
-v  # отображение списка обрабатываемых файлов на экране
-t  # показ содержимого перед распаковкой
-f  # указывание имени архива. f всегда в конце опций.

-z  # использовать Gzip для tar.gz , иначе будет просто tar (архив без сжатия)
-j  # использовать bzip2 для tar.bz2, иначе будет просто tar (архив без сжатия)
-J  # использовать xz для tar.xz, иначе будет просто tar (архив без сжатия)


# СОЗДАНИЕ АРХИВА С КОМПРЕССИЕЙ И БЕЗ
tar -cf mytar.tar source
tar -czf mytar.gz source
tar -cjf mytar.bz2 source
tar -cJf mytar.xz source


# ===================================================================================================================================
# АРХИВАЦИЯ И КОМПРЕССИЯ-ДЕКОМПРЕССИЯ gzip   bzip2   xz (только 1 файла)
# ===================================================================================================================================
# bzip2 самая высокая компрессия

gzip mytar.tar            # этот файл станет mytar.tar.gz
gunzip mytar.tar.gz       # декомпрессия в mytar.tar

bzip2 mytar.tar           # этот файл станет mytar.tar.bz2
bunzip2 mytar.tar.bz2     # декомпрессия в mytar.tar

xz mytar.tar              # этот файл станет mytar.tar.xz
unxz mytar.tar.xz         # декомпрессия в mytar.tar


# ===================================================================================================================================
# АРХИВАЦИЯ И КОМПРЕССИЯ ZIP
# ===================================================================================================================================

zip -r myzip.zip source
unzip myzip.zip
