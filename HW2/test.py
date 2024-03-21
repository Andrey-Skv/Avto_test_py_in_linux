import subprocess

FOLDER_TST = "/home/user/tst"
FOLDER_OUT = "/home/user/out"
FOLDER_1 = "/home/user/folder1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    # print(result.stdout)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False


def getout(cmd):
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout


def test_step1():
    # test1
    res1 = checkout(f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx2.7z", "Everything is Ok")
    res2 = checkout(f"ls {FOLDER_OUT}", "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    # test2
    res1 = checkout(f"cd {FOLDER_TST}; 7z e {FOLDER_OUT}/arx2.7z -o{FOLDER_1} -y", "Everything is Ok")
    res2 = checkout(f"ls {FOLDER_1}", "text1.txt")
    assert res1 and res2, "test2 FAIL"


def test_step3():
    # test3
    assert checkout(f"cd {FOLDER_OUT}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4
    assert checkout(f"cd {FOLDER_TST}; 7z d .{FOLDER_OUT}/arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    # test5
    assert checkout(f"cd {FOLDER_TST}; 7z u {FOLDER_OUT}/arx2.7z", "Everything is Ok"), "test5 FAIL"


def test_step6():
    # test6
    assert checkout(f'cd {FOLDER_OUT}; 7z l arx.7z', "arx.7z"), "test6 FAIL"


def test_step7():
    # test7
    res1 = checkout(f'cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx.7z',
                    "Everything is Ok")
    res2 = checkout(f'cd {FOLDER_OUT}; 7z x arx.7z -o{FOLDER_1} -y',
                    "Everything is Ok")
    assert res1 and res2, "test7 FAIL"


def test_step8():
    # test8
    res = []
    for i in FOLDER_TST:
        res1 = checkout(f'cd {FOLDER_TST}; 7z h {i}', "Everything is Ok")
        hash = getout(f'cd {FOLDER_TST}; crc32 {i}').upper()
        res.append(checkout(f'cd {FOLDER_TST}; 7z h {i}', hash))
    assert all(res), "test8 FAIL"


def test_neg1():
    # test1
    assert checkout_negative(f"cd {FOLDER_OUT}; 7z e arx2bad.7z -o{FOLDER_1} -y", "ERROR"), "test1 FAIL"


def test_neg2():
    # test2
    assert checkout_negative(f"cd {FOLDER_OUT}; 7z t arx2bad.7z", "ERROR"), "test2 FAIL"
