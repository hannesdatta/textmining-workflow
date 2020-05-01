import json

f = open('../../gen/data-preparation/temp/fortnite_astronomical_dataset/fortnite_allevent.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

outfile.write('id\tcreated_at\ttext\n')

cnt = 0
for line in con:
    if (len(line)<=5): continue

    cnt+=1
    obj = json.loads(line.replace('\n',''))

    text = obj.get('text')
    text = text.replace('\t', '').replace('\n', '')

    outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\n')
    if (cnt>1000): break

print('done.')
