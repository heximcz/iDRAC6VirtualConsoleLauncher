---
### Fork from [gethvi/iDRAC...](https://github.com/gethvi/iDRAC6VirtualConsoleLauncher)

### Changes

- an interactive console (safer input for a password)
- remove another cli args

### Knowledge

- if you have a problem with "Pass all keystrokes to server" try to run this script as root

---

# iDRAC 6 Virtual Console Launcher
Python 3 launcher for iDRAC 6 Virtual Console (including Virtual Media).

Tested on Debian Buster, Windows 10 and MacOS Catalina.

## Installation
To run the Virtual Console, you need to download old Java Runtime Environment 7u80 from Oracle:

https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html

Below are direct links that only work when you log in and accept Oracle license agreement.

**Windows:**
[jre-7u80-windows-x64.tar.gz](https://download.oracle.com/otn/java/jdk/7u80-b15/jre-7u80-windows-x64.tar.gz)

**Linux:**
[jre-7u80-linux-x64.tar.gz](https://download.oracle.com/otn/java/jdk/7u80-b15/jre-7u80-linux-x64.tar.gz)

**MacOS:**
[jre-7u80-macosx-x64.tar.gz](https://download.oracle.com/otn/java/jdk/7u80-b15/jre-7u80-macosx-x64.tar.gz)


Extract the files and place them where the script expects it:

```
iDRAC6VirtualConsoleLauncher
├── iDRAC6VirtualConsoleLauncher.py
├── jre
│   ├── bin
│   │   └── java.exe (java)
│   └── ...
|
├── requirements.txt
└── README.md
```

Install dependencies:

`pip3 install -r requirements.txt`

or use (Linux) distribution packages:

`apt install python3-requests`

## Usage
```
usage: iDRAC6VirtualConsoleLauncher.py
```