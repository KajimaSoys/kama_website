# Резервное копирование

| Скрипт | Что | Когда (UTC / МСК) | Хранение | Шифрование |
|---|---|---|---|---|
| `pg_backup.sh` | дамп БД `pg_dump -Fc` из `db-kama` | каждый час в :35 | 48 почасовых + 30 ежедневных | age |
| `config_backup.sh` | `.env`, `client/.env.production`, crontab, `/etc/nginx`, `/etc/letsencrypt`, `/etc/docker/daemon.json` | 04:45 / 07:45 | 30 дней | age |
| `media_backup.sh` | инкрементальный снимок `media/` (rsync `--link-dest`) | 05:00 / 08:00 | 5 снимков | нет (всё публичное) |

Бэкапы складываются в `~/backups/kama_website/{db,config,media}`, логи в `~/logs/`.
Время сдвинуто относительно cube_website (:05, 04:15, 04:30), чтобы задачи не пересекались.

## Установка на сервере (один раз)

1. Пакеты: `sudo apt install age rsync`.
2. Открытый ключ age (тот же, что у cube_website, или новый) положить в
   `~/kama_website/scripts/backup/age-recipients.txt` — по одному `age1...` на строку.
   Файл в `.gitignore`, приватный ключ на сервер не кладём.
3. Root-хелпер для системной конфигурации:
   ```bash
   sudo install -o root -g root -m 0755 ~/kama_website/scripts/backup/kama-config-snapshot /usr/local/sbin/kama-config-snapshot
   echo 'kajimasoys ALL=(root) NOPASSWD: /usr/local/sbin/kama-config-snapshot ""' | sudo tee /etc/sudoers.d/kama-config-snapshot
   sudo chmod 0440 /etc/sudoers.d/kama-config-snapshot && sudo visudo -c
   ```
   Хелпер копируется, а не линкуется: файл в репозитории может менять обычный пользователь,
   а запускается он от root.
4. `mkdir -p ~/logs` и прогнать каждый скрипт руками, проверить строку `OK` в выводе.
5. `crontab -e`, добавить:
   ```
   # kama_website: БД каждый час в :35
   35 * * * * $HOME/kama_website/scripts/backup/pg_backup.sh >> $HOME/logs/kama_pg_backup.log 2>&1
   # kama_website: .env, nginx, letsencrypt каждый день в 07:45 МСК
   45 4 * * * $HOME/kama_website/scripts/backup/config_backup.sh >> $HOME/logs/kama_config_backup.log 2>&1
   # kama_website: снимок media каждый день в 08:00 МСК
   0 5 * * * $HOME/kama_website/scripts/backup/media_backup.sh >> $HOME/logs/kama_media_backup.log 2>&1
   ```

## Восстановление

```bash
# БД
age -d -i key.txt db_2026-11-17_1435.dump.age > db.dump
docker exec -i db-kama sh -c 'pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" --clean --if-exists --no-owner' < db.dump

# Конфигурация
age -d -i key.txt config_2026-11-17.tar.gz.age | tar -xzf - -C restore/
tar -xzf restore/system-etc.tar.gz -C restore/etc-root/

# media: снимок — обычная папка
rsync -a ~/backups/kama_website/media/media_2026-11-17/ ~/kama_website/media/
sudo chown -R 10001:10001 ~/kama_website/media
```
