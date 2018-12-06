import subprocess

# DomainName=input('please input the domain name:')
DomainName = '150.129.193.72'
p1 = subprocess.Popen(['echo'],stdout=subprocess.PIPE,stderr=0)
p2 = subprocess.Popen(['openssl','s_client','-servername','{}','-connect','{}:443'.format(DomainName,DomainName)],stderr=0,stdin=p1.stdout,stdout=subprocess.PIPE)
p3 = subprocess.Popen(['openssl','x509','-noout','-dates'], stdin=p2.stdout, stdout=subprocess.PIPE,stderr=0)
out,err = p3.communicate()
print(out)
# print(err)
# print(out.split('\\n'))