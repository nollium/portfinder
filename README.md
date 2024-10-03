# portfinder
Nicely displays which process is listening on some ports

![image](https://github.com/user-attachments/assets/e41f387a-515b-428c-bb6a-2228cc310674)

## Install
```
pip install -r requirements.txt # psutil, rich
```

## Usage
```
sudo python3 portfinder.py
```
Portfinder can be launched as an unpriviledged user but it will have bad results on priviledged processes


It's just a small psutil wrapper which displays the output nicely in a rich table
