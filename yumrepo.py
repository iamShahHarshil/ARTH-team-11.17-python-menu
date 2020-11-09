import os

path = os.path.join('/etc/yum.repos.d','yum.repo')
app = open(path,'w')
app_data = '''[dvd1]
baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream
gpgcheck=0

[dvd2]
baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS
gpgcheck=0\n\n'''

app.write(app_data)
app.close()
