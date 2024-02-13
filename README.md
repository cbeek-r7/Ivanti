# Ivanti
Folder containing scripts/tools to scan for possible Ivanti related indicators of compromise

the Check_implant script is based on the blog from Orange Cyberdefense: 
https://www.orangecyberdefense.com/fileadmin/general/pdf/Ivanti_Connect_Secure_-_Journey_to_the_core_of_the_DSLog_backdoor.pdf

The code is pretty simple and have choosen to scan for the index2.txt file.
A comrpomised host will give the output of the 'uname - a' command.

Example output of a vulnerable host usingn the script:

Content found at https://x.x.x.x/dana-na/imgs/index2.txt:
Linux localhost2 4.15.18.34-production #1 SMP Fri Jun 17 13:08:47 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux uid=0(root) gid=0(root) groups=0(root)
