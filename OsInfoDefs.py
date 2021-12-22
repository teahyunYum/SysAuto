import subprocess
import os
import socket
import re
import psutil, datetime

# temp=psutil.net_if_addrs()#os상 인터넷들

# a=list(temp.keys())
# print(psutil.disk_usage('c:'))
# print(psutil.net_if_stats())
def CRinfo():
    temp=[]
    temp.append(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
    temp.append(list(psutil.cpu_stats())[2])
    temp1=[x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    temp.append(round(temp1[2],4))
    temp1=list(psutil.virtual_memory())[0]
    temp.append(str(temp1)[:-9])
    temp1=list(psutil.virtual_memory())[1]
    temp.append(str(temp1)[:-9])
    temp1=psutil.virtual_memory()[3]
    temp.append(str(temp1)[:-9])
    temp.append(list(psutil.virtual_memory())[2])
    return temp
def Disklist():
    listtemp=[]
    temp=list(psutil.disk_partitions(all=True))
    for i in range(len(temp)):
        listtemp.append(temp[i][1].replace(":\\",""))
    return listtemp
def seldisk(num, name):
    temp=[]
    temp1=list(psutil.disk_io_counters(perdisk=True)[f'PhysicalDrive{num}'])
    temp.append(temp1[0])
    temp.append(temp1[4])
    temp.append(temp1[1])
    temp.append(temp1[5])
    name=name+":"
    temp.append(str(list(psutil.disk_usage(f'{name}'))[1])[:-9])
    temp.append(list(psutil.disk_usage(f'{name}'))[3])
    return temp

# os.system("chcp 949")
# temp=subprocess.getstatusoutput(["netsh","interface","ipv4","show", "config"])
def networklist():
    temp=subprocess.check_output(["netsh","interface","ipv4","show", "config"],text=True)
    p=re.compile('".*"')
    networklist=re.findall(p,temp)
    return networklist
def selnetwork(temp):
    # temp.replace('"',"")
    networkinfo=[]
    sequence=["netsh","interface","ipv4","show", "config"]
    sequence.append(temp)
    temp=subprocess.check_output(sequence,text=True)
    try:networkinfo.append(re.search('IP 주소.*',temp).group().replace('IP 주소:',"").replace(" ",""))
    except AttributeError:networkinfo.append('-')
    try:networkinfo.append(re.search('기본 게이트웨이:.*',temp).group().replace('기본 게이트웨이:',"").replace(" ",""))
    except AttributeError:networkinfo.append('-')
    try:networkinfo.append(re.search('마스크 .*',temp).group().replace("마스크 ","").replace(')',""))
    except AttributeError:networkinfo.append('-')
    try:networkinfo.append(re.search('.*DNS 서버',temp).group().replace('  ','').replace("된 DNS 서버",""))
    except AttributeError:networkinfo.append('-')
    try:networkinfo.append(re.search('DNS 서버.*',temp).group().replace("DNS 서버:","").replace(" ",""))
    except AttributeError:networkinfo.append('-')
    if '없음' in networkinfo[4]:networkinfo.pop(),networkinfo.pop(),networkinfo.append('-'),networkinfo.append('-')
    if '-' != networkinfo[4]:networkinfo.append(re.search('                                      .*',temp).group().replace(" ",""))
    else:networkinfo.append('-')
    return networkinfo
    
def networkused(temp):
    info=psutil.net_io_counters(pernic=True)
    info=list(info[f'{temp}'])
    info[0]=round(info[0]/1000000000,3)
    info[1]=round(info[1]/1000000000,3)
    del info[2:4]
    del info[4:6]
    info2=psutil.net_if_stats()
    info.append(list(info2[f'{temp}'])[2])
    info.append(list(info2[f'{temp}'])[3])
    return info
def ipset(temp,temp1):
    sequence=["netsh","interface","ipv4","set", "address",str(temp),"static"]
    dnssequence=["netsh","interface","ipv4","set", "dns",str(temp),"static","primary"]
    dnssequence2=["netsh","interface","ipv4","add", "dns",str(temp)]
    sequence.append(temp1[0])
    sequence.append(temp1[2])
    sequence.append(temp1[1])
    dnssequence.insert(7,temp1[3])
    dnssequence2.append(temp1[4])
    subprocess.call(sequence)
    subprocess.call(dnssequence)
    subprocess.call(dnssequence2)
def DHSPset(temp):
    sequence=["netsh","interface","ipv4","set", "address",str(temp),"dhcp"]
    sequence2=["netsh","interface","ipv4","set", "dns",str(temp),"dhcp"]
    subprocess.call(sequence)
    subprocess.call(sequence2)

# nametemp=['이더넷']
# DHSPset(nametemp)
# nametemp1=['Loopback Pseudo-Interface 1']
# temp=['172.30.1.50','172.30.1.254','255.255.255.0','168.126.63.1','168.126.63.2']
# temp1=['-','-','-','-','-']
# ipset(nametemp,temp)
# temp=psutil.net_if_stats()
# print(temp['이더넷'])
# print(psutil.net_if_stats())
# print(psutil.net_if_stats())#speed,mtu
# print(psutil.net_io_counters(pernic=True))#byte sent보낸, byte recv받은,errout, errin,

# temp1=re.search('"',temp)
# f=open('temp.txt','w')
# # f.write(temp[1])
# f.close
# file=open('temp.txt','r')

# while True:
#     file=open('temp.txt','r')
#     line=file.readline()
#     print(line)
#     getname=re.findall('[""]+',line)    
#     if ""==line:
#         break
# print(getname)
# 

    
# print(interfacelist)

        
    

# print(psutil.cpu_stats())#cpu status 3번 부팅이후 소프트웨어중단수
# print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))#마지막 부팅일자
# print(psutil.getloadavg())#평균 시스템 부하 1분,5분, 15분
# print([x / psutil.cpu_count() * 100 for x in psutil.getloadavg()])
# os.system("chcp 94")
# os.system("chcp 437")

# os.system("chcp 65001")
# temp=subprocess.run(["netsh","interface","ipv4","show", "addresses"],capture_output=True)
# temp=subprocess.run(["netsh","interface","ipv4","show", "config"],capture_output=True,text=True)

# f.write(temp)
# temp1=subprocess.run(["netsh","interface","ipv4","show", "interface"],capture_output=False)
# print()
# temp=subprocess.run(["ipconfig"],capture_output=True)
# temp2=temp.stderr

# print(temp)

# print(temp,type(temp))
# print(temp,type(temp))
# print(psutil.virtual_memory())#메모리 total=전체, available=사용가능메모리, percent=37.6 사용중 
# print(psutil.disk_io_counters(perdisk=True))
# print(psutil.disk_partitions(all=False))
# p = psutil.Process()
# print(p.io_counters())
# print(psutil.net_connections(kind='inet'))
