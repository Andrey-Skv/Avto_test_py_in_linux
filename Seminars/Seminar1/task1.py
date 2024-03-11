import subprocess
import string


def checkout(cmd, text, flag=False):
    result = subprocess.run("cat /etc/os-release", shell = True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if flag:
        for c in string.punctuation:
            s = result.stdout.replace(c, "")
        listout = s.split()
        if '22.04.4' in out and 'jammy' in out and not result.returncode:
            return True
        else:
            return False
    else:
        if '22.04.4' in out and 'jammy' in out and not result.returncode:
            return True
        else:
            return False