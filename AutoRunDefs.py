import subprocess
import PyautoDefs as atodef
import re

def defaulpowesaveing():
    sequence=["powercfg","/GETACTIVESCHEME"]
    temp=subprocess.check_output(sequence,text=True)
    temp=temp[49:].replace(')',"").replace(" ","").replace("(","")
    return temp
def username():
    sequence=["echo", "%username%"]
    temp=subprocess.check_output(sequence,text=True,shell=True).replace("\n","")
    return temp
def updatestate():
    sequence=["reg","query","HKLM\SYSTEM\CurrentControlSet\Services\wuauserv","/v","start"]
    temp=subprocess.check_output(sequence,text=True,shell=True)[-3:].replace(" ","").replace("\n","")
    if temp=='3':temp='수동'
    elif temp=='2':temp='자동'
    elif temp=='4':temp='사용안함'
    return temp
def defenderstate():
    temp=subprocess.check_output(['powershell','-command',"get-NetFirewallProfile"],text=True)
    temp=re.search("Enabled.*",temp).group().replace("Enabled","").replace(" ","").replace(":","")
    return temp
def powerset():
    sequence=[]
    sequence.append(["powercfg","/s", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"])
    sequence.append(["powercfg","/x", "standby-timeout-ac", "0"])
    sequence.append(["powercfg","/x", "monitor-timeout-ac", "0"])
    sequence.append(["powercfg","/x", "disk-timeout-ac", "0"])
    sequence.append(["powercfg","/setacvalueindex", "scheme_current","2a737441-1930-4402-8d77-b2bebba308a3","48e6b7a6-50f5-4782-a5d4-53bb8f07e226","0"])
    sequence.append(["powercfg","/setacvalueindex", "scheme_current","7516b95f-f776-4464-8c53-06167f40cc99","fbd9aa66-9553-4097-ba44-ed6e9d65eab8","0"])
    sequence.append(["powercfg","/setacvalueindex", "scheme_current","0012ee47-9041-4b5d-9b77-535fba8b1442","6738e2c4-e8a5-4a42-b16a-e040e769756e","0"])
    for i in range(len(sequence)):subprocess.call(sequence[i])
def useraccountset():
    temp=username()
    sequence=[]
    # sequence.append(["net","user","administrator","/active:yes"])
    sequence.append(["net","localgroup","administrators",temp,"/add"])
    # sequence.append(["net","user","administrator","/active:no"])
    sequence.append(["reg","add","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System","/v","EnableLUA","/t","REG_DWORD","/d","0","/f"])
    for i in range(len(sequence)):subprocess.call(sequence[i])
def updatedisabled():
    sequence=[]
    sequence.append(["reg","add",r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\uhssvc","/v","Start","/t","REG_DWORD","/d", "4", "/f"])
    sequence.append(["reg","add","HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv","/v","Start","/t","REG_DWORD","/d", "4", "/f"])
    sequence.append(["reg","add","HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WaasMedicSvc","/v","Start","/t","REG_DWORD","/d", "4", "/f"])
    sequence.append(["reg","add",r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\UsoSvc","/v","Start","/t","REG_DWORD","/d", "4", "/f"])
    sequence.append(["sc","config","uhssvc","start=disabled"])
    sequence.append(["sc","config","wuauserv","start=disabled"])
    sequence.append(["sc","config","WaasMedicSvc","start=disabled"])
    sequence.append(["sc","config","UsoSvc","start=disabled"])
    sequence.append(["net","stop","wuauserv"])
    for i in range(len(sequence)):subprocess.call(sequence[i])
def updatereset():
    sequence=[]
    sequence.append(["reg","add","HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv","/v","Start","/t","REG_DWORD","/d", "2", "/f"])
    sequence.append(["reg","add","HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WaasMedicSvc","/v","Start","/t","REG_DWORD","/d", "2", "/f"])
    sequence.append(["reg","add",r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\UsoSvc","/v","Start","/t","REG_DWORD","/d", "2", "/f"])
    sequence.append(["sc","config","wuauserv","start=auto"])
    sequence.append(["sc","config","WaasMedicSvc","start=auto"])
    sequence.append(["sc","config","UsoSvc","start=auto"])
    sequence.append(["net","start","wuauserv"])
    for i in range(len(sequence)):subprocess.call(sequence[i])
def defenderdisabled():
    subprocess.check_output(['powershell','-command',"Set-NetFirewallProfile -Profile Domain, Public, Private -Enabled False"])

def defaultlist(*args):
    temp=[]
    for i in args:temp.append(i)
    return temp

def sysdefault():
    temp=defaultlist(defaulpowesaveing(),username(),updatestate(),defenderstate())
    return temp

def runset(temp):
    with open('checklist.text','w') as f:
        for i in range(len(temp)):
            f.write(str(temp[i])+'\n')
    if temp[0]==True:powerset()
    else:pass
    if temp[1]==True:useraccountset()
    else:pass
    if temp[2]==True:updatedisabled()
    else:pass
    if temp[3]==True:defenderdisabled()
    else:pass
    if temp[4]==True:atodef.allrun()
    else:pass
    



