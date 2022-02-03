from requests import get
import os


# get ip:
ip = get('https://api.ipify.org').content.decode('utf8')


# create html file
data = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Refresh" content="0; url='http://{str(ip)}:3000/'" />
    
    <title>moving you to scimedia...</title>
</head>
<body>
    You will be relocated to scimedia...
</body>
</html>
'''


# push to github

# delete dir
#os.remove("thescimedia.github.io")



# change file
f = open('index.html', "w")
f.write(data)
f.close

os.system('git add index.html') #git add index.html
os.system("git commit -m 'new ip'")#git commit -m 'new ip'
os.system("git push")

