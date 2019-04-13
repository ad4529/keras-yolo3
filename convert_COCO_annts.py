import json
from pprint import PrettyPrinter

with open('/home/ad0915/Desktop/MSCOCO/annotations_trainval2017/annotations/instances_val2017.json') as f:
    data1 = json.load(f)
#p = PrettyPrinter(depth=1)
#p.pprint(data)
f.close()
with open('/home/ad0915/Desktop/MSCOCO/annotations_trainval2017/annotations/instances_train2017.json') as f:
    data2 = json.load(f)
f.close()

result_tuple1 = [(x['image_id'],x['bbox'],x['category_id']) for x in data1['annotations']]
imgs1 = [(x['id'],x['width'],x['height']) for x in data1['images']]
names_coco = [x['id'] for x in data1['categories']]
result_tuple2 = [(x['image_id'],x['bbox'],x['category_id']) for x in data2['annotations']]
imgs2 = [(x['id'],x['width'],x['height']) for x in data2['images']]
result_tuple1.sort(key=lambda tup: tup[0])
imgs1.sort(key=lambda t: t[0])
new_list = []
counter = -1
count = 0
#[print (x) for x in result_tuple]
path = '/home/ad0915/Desktop/MSCOCO/val2017/'
prev_imgid = 0
for sample in result_tuple1:
    if (sample[0]!=prev_imgid):
        img_id = str(sample[0])
        num_zeros = 12-len(img_id)
        img_id = path + '0'*num_zeros + img_id + '.jpg'
        prev_imgid = sample[0]
        new_list.append(img_id)
        counter+=1
        iw = imgs1[count][0]
        ih = imgs1[count][0]
        count+=1

    temp = sample[1]
    sample[1][0] = int(temp[0])
    sample[1][1] = int(temp[1])
    sample[1][2] = int(temp[0]+temp[2])
    sample[1][3] = int(temp[1]+temp[3])
    bbox = [str(i) for i in sample[1]]
    bbox = ",".join(bbox)
    new_list[counter] = new_list[counter] + ' ' + bbox + ',' + str(names_coco.index(sample[2]))

result_tuple2.sort(key=lambda tup: tup[0])
#[print (x) for x in result_tuple]
path = '/home/ad0915/Desktop/MSCOCO/train2017/'
prev_imgid = 0
count=0
for sample in result_tuple2:
    if (sample[0]!=prev_imgid):
        img_id = str(sample[0])
        num_zeros = 12-len(img_id)
        img_id = path + '0'*num_zeros + img_id + '.jpg'
        prev_imgid = sample[0]
        new_list.append(img_id)
        counter+=1
        iw = imgs2[count][0]
        ih = imgs2[count][0]
        count += 1

    temp = sample[1]
    sample[1][0] = int(temp[0])
    sample[1][1] = int(temp[1])
    sample[1][2] = int(temp[0] + temp[2])
    sample[1][3] = int(temp[1] + temp[3])
    bbox = [str(i) for i in sample[1]]
    bbox = ",".join(bbox)
    new_list[counter] = new_list[counter] + ' ' + bbox + ',' + str(names_coco.index(sample[2]))

f=open('coco_annotations.txt','w')
[f.write(i+'\n') for i in new_list]
f.close()

#print()