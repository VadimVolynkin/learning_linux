
# ===== просмотр информации о железе

# Модели северных и южных мостов.
# IDE, SATA, SCSI контроллеры.
# Графический контроллер.
# Модели сетевых интерфейсов.
lspci

# более подробно по каждому компоненту
lspci -v

# инфа о процессоре
sudo lshw -c cpu
sudo dmidecode --type processor
sudo cat /proc/cpuinfo

# инфа о мат плате
sudo dmidecode --type baseboard

# инфа об оперативной памяти
sudo lshw -short | grep -i "memory"
sudo dmidecode --type memory

# инфа о дисках
lsblk -a
lshw -class disk -class storage
sudo smartctl -i /dev/sda
sudo smartctl -A /dev/sda
