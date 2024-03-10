# This file can clean  irregular ips and domains like bellow:
# http: ip(:port)       # if it has ports , the ports will be delete
# https: ip(:port)
# http:domain(:port)
# https:domain(:port)

import re

class GetPureIpAndDomain:
    def __init__(self,mixIPandDomainFile):
        self.mixIPandDomainFile = mixIPandDomainFile
        self.ip_domain_dataframe = {}
        self.init_ip_list = []
        self.init_domain_list = []
        self.ip_list = []
        self.domain_list = []
        self.ip_domain_dataframe["ip_list"] = self.ip_list
        self.ip_domain_dataframe["domain_list"] = self.domain_list
        self.ip_domain_dataframe["init_ip_list"] = self.init_ip_list
        self.ip_domain_dataframe["init_domain_list"] = self.init_domain_list


    def processIPAndDomian(self):

        mixfile = self.mixIPandDomainFile
        with open(mixfile, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()                    # delete blank space of header and tail
                pattern = r"(https?://)?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?::\d+)?)"  # match init link including ip and domain
                match = re.search(pattern, line)

                if match:
                    matched_ip = match.group()
                    self.init_ip_list.append(matched_ip)
                    pure_IP = re.sub(r'(https?://)?',"" ,re.sub(r':\d+', "" ,matched_ip))
                    self.ip_list.append(pure_IP)
                else:
                    self.init_domain_list.append(line)
                    pure_Domain = re.sub(r'(https?://)?',"" ,re.sub(r':\d+',"",line))
                    self.domain_list.append(pure_Domain)
        return self.ip_domain_dataframe



if __name__ == "__main__":
    test_ip_domain = GetPureIpAndDomain('domain.txt')
    test_ip_domain.processIPAndDomian()
    print(test_ip_domain.domain_list)
    print("----"*30)
    print(test_ip_domain.ip_list)
    print("----"*30)
    print(test_ip_domain.ip_domain_dataframe)


