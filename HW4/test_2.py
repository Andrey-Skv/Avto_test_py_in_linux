from sshcheckers import ssh_checkout_negative, ssh_checkout


import yaml


with open('config.yaml') as f:
   # читаем документ YAML
   data = yaml.safe_load(f)


class Testneg:
   def test_nstep1(self, make_folders, make_bad_arx):
       # test neg 1
       assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"], f"cd {data['folder_out']}; "
                                                                              f"7z e {make_bad_arx}.{data['type']}"
                                                                              f" -o{data['folder_ext']} -y", "ERROR:"),\
           "test1 FAIL"


   def test_nstep2(self, make_bad_arx):
       # test neg 2
       assert ssh_checkout_negative(data["ip"], data["user"], data["passwd"], f"cd {data['folder_out']};"
                                                                              f" 7z t {make_bad_arx}.{data['type']}",
                                    "ERROR:"), "test2 FAIL"


   def test_nstep3(self):
       res = []
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], f"echo '{data['passwd']}' | sudo -S dpkg -r"
                                                                         f" {data['pkgname']}", "Удаляется"))
       res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], f"echo '{data['passwd']}' | "
                                                                         f"sudo -S dpkg -s {data['pkgname']}",
                               "Status: deinstall ok"))
       assert all(res), "test3 FAIL"

