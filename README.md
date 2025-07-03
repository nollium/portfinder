# Portfinder

A command-line tool to find and manage processes binding to ports on your system.

![Portfinder output](https://github.com/user-attachments/assets/f55c3ab4-4b1d-4056-b25f-1290fb30ceb0)


## Features

- List all processes binding to ports
- Filter by specific ports
- Option to kill processes binding to specific ports
- Colorful and readable output

## Installation

You can install portfinder directly from GitHub:

```bash
pip install git+https://github.com/nollium/portfinder.git
```

**or with pipx:**

```bash
pipx install git+https://github.com/nollium/portfinder.git
```

## Usage

List all bound ports:
```bash
portfinder
```

List specific ports:
```bash
portfinder 80 443 8080
```

Kill processes binding to specific ports:
```bash
portfinder 80 443 --kill
```

## CI/CD

This project uses GitHub Actions for continuous integration and delivery:

- **Test Build**: Runs on every push/PR to ensure the code builds successfully
- **Latest Release**: Automatically updates the "latest" release with new binaries on every merge to main
- **Version Release**: Creates official releases when version tags are pushed (e.g., `v1.0.0`)

## License

MIT License
