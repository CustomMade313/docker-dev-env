import os 
import shutil


os.mkdir('conf')
os.mkdir('mysql')
os.mkdir('redis')
os.mkdir('src')

os.chdir('conf')
os.mkdir('nginx')
os.chdir('..')
shutil.move('default.conf', 'conf/nginx')