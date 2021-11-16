import requests;
import sys;

arg=sys.argv[1];
print(arg);
#exit();
data = {"del": arg};
cookies={"PHPSESSID": "4c67s45dtunmuibvdco9baru7m"};
headers={"Content-Type": "application/x-www-form-urlencoded"};
r= requests.post('http://10.10.11.104/files.php', cookies=cookies, data=data, headers=headers);
isSuccess = r.text.find('Success! File was deleted!');
if isSuccess :
  print('success');
else :
  print('error');
