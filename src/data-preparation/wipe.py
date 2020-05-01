import shutil

dirs = ['../../data/', '../../gen/data-preparation/']

print('deleting all generated and downloaded raw data files')
for mydir in dirs:
    try:
        shutil.rmtree(mydir)
    except:
        print('cannot delete dir ' + mydir + '. Maybe it does not exist?')

        
print('done.')