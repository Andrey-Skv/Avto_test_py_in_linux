import subprocess
FOLDER_TST = "/home/user/Andrey/tst"
FOLDER_OUT = "/home/user/Andrey/out"
FOLDER_1 = "/home/user/Andrey/folder1"

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

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