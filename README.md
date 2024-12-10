# portfinder
Nicely displays which process is listening on some ports

![image](https://github.com/user-attachments/assets/f55c3ab4-4b1d-4056-b25f-1290fb30ceb0)

## Install
```
pip install -r requirements.txt # psutil, rich
```

## Usage
```
sudo python3 portfinder.py [PORTS] [--kill]
```

- **PORTS**: Optional list of ports to filter. Only processes listening on these ports will be displayed.
- **--kill**: Optional flag to terminate matched processes with SIGKILL.

### Examples
- Display all listening processes:
  ```
  sudo python3 portfinder.py
  ```

- Display processes listening on ports 22, 80, and 8080:
  ```
  sudo python3 portfinder.py 22 80 8080
  ```

- Display and kill processes listening on ports 22, 80, and 8080:
  ```
  sudo python3 portfinder.py 22 80 8080 --kill
  ```

Portfinder can be launched as an unprivileged user, but it will have limited results on privileged processes.

It's just a small psutil wrapper which displays the output nicely in a rich table.
