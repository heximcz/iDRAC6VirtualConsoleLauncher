#!/usr/bin/env python3


import zipfile
import requests
import io
import pathlib
import sys
import urllib3
import subprocess
import re
from getpass import getpass

def get_libraries(url, path):
    response = requests.get(url)
    with zipfile.ZipFile(file=io.BytesIO(response.content)) as zip:
        for member in zip.infolist():
            if member.filename.endswith(DYNLIBEX):
                print('Extracting: ' + member.filename)
                zip.extract(member, path=path)


def main():
    user = input('User: ')
    passwd = getpass(prompt='Password:')
    host = input('HOST[:PORT]: ')

    url = urllib3.util.parse_url(host)
    host = url.host
    if url.port:
        port = url.port
    else:
        port = 5900

    avctvm_url = 'http://{0}/software/avctVM{1}.jar'.format(host, PLATFORM)
    avctkvmio_url = 'http://{0}/software/avctKVMIO{1}.jar'.format(host, PLATFORM)
    avctkvm_url = 'http://{0}/software/avctKVM.jar'.format(host)

    pwd = pathlib.Path(sys.path[0])
    # Hostdir is a striped version of host, because some chars can avoid LD load within java - as example IPv6 address with []
    hostdir = pwd.joinpath('host_' + re.sub('[^a-zA-Z0-9]+', '', host))
    java = pwd.joinpath('jre').joinpath('bin').joinpath('java' + BINARYEX)

    libdir = hostdir.joinpath('lib')
    libdir.mkdir(parents=True, exist_ok=True)

    get_libraries(url=avctvm_url, path=libdir)
    get_libraries(url=avctkvmio_url, path=libdir)

    print('Downloading: avctKVM.jar')
    response = requests.get(avctkvm_url)
    with open('avctKVM.jar', 'w+b') as file:
        file.write(response.content)

    if java.exists():
        subprocess.run([
            str(java.absolute()),
            '-cp',
            'avctKVM.jar',
            '-Djava.library.path={}'.format(libdir),
            'com.avocent.idrac.kvm.Main',
            'ip={}'.format(host),
            'kmport={}'.format(port),
            'vport={}'.format(port),
            'user={}'.format(user),
            'passwd={}'.format(passwd),
            'apcp=1',
            'version=2',
            'vmprivilege=true',
            '"helpurl=https://{}/help/contents.html"'.format(host)
        ])


if __name__ == '__main__':
    if sys.platform.startswith('linux'):
        PLATFORM = 'Linux64'
        DYNLIBEX = '.so'
        BINARYEX = ''
    elif sys.platform.startswith('win'):
        PLATFORM = 'Win64'
        DYNLIBEX = '.dll'
        BINARYEX = '.exe'
    elif sys.platform.startswith('darwin'):
        PLATFORM = 'Mac64'
        DYNLIBEX = '.jnilib'
        BINARYEX = ''
    else:
        print('Unsupported platform.')
        sys.exit(0)

    main()
