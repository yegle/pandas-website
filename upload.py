import os

def upload():
    'push a copy to the pydata dev directory'
    os.system('cd _build/html; rsync -avz . pandas@pandas.pydata.org '
              '/usr/share/nginx/pandas/ -essh')

if __name__ == '__main__':
    upload()
