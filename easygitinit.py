import sys
import os

if len(sys.argv) < 6:
    print "Usage: python easygitinit.py username password desiredlocation repositoryname file1,file2,fileN"
    print "Required to use at least one file"
    quit()

username,password,directory,repository,files = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]
files = sys.argv[5].split(',')


os.system('cd '+str(directory)+' && mkdir '+str(repository)+' && cd '+str(repository)+' && git init')

for myfile in files:
    os.system('cd '+str(directory)+'/'+str(repository)+' && git add ' +str(myfile))

os.system('cd '+str(directory)+'/'+str(repository)+' && git commit -m "first commit" && git remote add origin https://github.com/'+str(username)+'/'+str(repository)+'.git && git push -u origin master')




