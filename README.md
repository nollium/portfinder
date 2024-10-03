# portfinder
Nicely displays which process is listening on some ports

![image](https://github.com/user-attachments/assets/f55c3ab4-4b1d-4056-b25f-1290fb30ceb0)

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
