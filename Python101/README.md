# Environment



```shell
~/Desktop/python101 ❯ python3 -m venv python_101
~/Desktop/python101 ❯ source python_101/bin/activate
~/Desktop/python101 ❯ pip install -r requirements.txt                 python101
```


# Run

## Cron

```shell
## You need postgresql up and running
~/Desktop/python101 ❯ source python_101/bin/activate
~/Desktop/python101 ❯ python3 cron.py                                  python101
```

## Server

```shell
## You need postgresql up and running
~/Desktop/python101 ❯ source python_101/bin/activate
~/Desktop/python101 ❯ gunicorn run:app                                python101
[2021-09-22 11:16:04 +0300] [69751] [INFO] Starting gunicorn 20.1.0
[2021-09-22 11:16:04 +0300] [69751] [INFO] Listening at: http://127.0.0.1:8000 (69751)
[2021-09-22 11:16:04 +0300] [69751] [INFO] Using worker: sync
[2021-09-22 11:16:04 +0300] [69752] [INFO] Booting worker with pid: 69752
```

