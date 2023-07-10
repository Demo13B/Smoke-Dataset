import json
with open('final_dataset/annotation.json') as f:
    data = json.load(f)

for idx, image in enumerate(data['images']):
    if image['file_name'] == '4_2_0_flare_0030_jpg.rf.0cce856c8984852cf7434900d7fe0767.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0030_jpg.rf.0cce856c8984852cf7434900d7fe0767.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_0_flare_0039_jpg.rf.11dc298a17e2d09b5ff38741cb173b3b.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_1_flare_0039_jpg.rf.11dc298a17e2d09b5ff38741cb173b3b.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_1_flare_0196_jpg.rf.46af7d996a3d25b8e99f39403ab8eeb7.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_0_flare_0092_jpg.rf.546b4a2d6d297f0b8f021625afe7fd10.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0092_jpg.rf.546b4a2d6d297f0b8f021625afe7fd10.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0162_jpg.rf.3bb3d12f9d03c755559a2ae410eb7366.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0055_jpg.rf.46d5c65f91087f396d2275052ff41ca3.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_1_flare_0053_jpg.rf.54ed5008f2a72c49d08a4cf85e4d81b1.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0078_jpg.rf.9a4a193a84de33eaa4f5e5e841f3dd67.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_0_flare_0211_jpg.rf.86911db9cd67f045b4dc0060945fcb7e.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0211_jpg.rf.86911db9cd67f045b4dc0060945fcb7e.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_0_flare_0180_jpg.rf.b3d4aac3ff6a82fb1fea3ea44087a09a.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_0_flare_0142_jpg.rf.c16395039d0b368062ef17cc4f9f1032.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_0_flare_0124_jpg.rf.b5d66bb90978f9a7eba1a98bb31917db.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0124_jpg.rf.b5d66bb90978f9a7eba1a98bb31917db.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0172_jpg.rf.79070634130311fd76e888420a1c0c63.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_0_flare_0025_jpg.rf.cc2f2be6be25e2feb2fe4e6044195c0e.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_1_flare_0025_jpg.rf.cc2f2be6be25e2feb2fe4e6044195c0e.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_1_flare_0061_jpg.rf.d68903018c79a3eccbcba77322193d86.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0179_jpg.rf.c1b82c5e6074563782172ba22d661c54.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_0_0_flare_0026_jpg.rf.c57fa646ad4bfcd90d9f76b1a4ea4d72.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_1_flare_0045_jpg.rf.d936ab48de4c7835e1eb37add2170173.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_0_flare_0145_jpg.rf.dc1a8582ffd200b84667baef7e2a3211.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0145_jpg.rf.dc1a8582ffd200b84667baef7e2a3211.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_0_flare_0090_jpg.rf.dbb7ea16cbe32a731eaf5087eacd35c3.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_0_flare_0122_jpg.rf.e0b743deb4d49c08ac21528c1e503dbc.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_0_flare_0014_jpg.rf.f1de3e3c899c4bcb6566256abc612452.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_1_flare_0014_jpg.rf.f1de3e3c899c4bcb6566256abc612452.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0029_jpg.rf.e36015e5abe223a72b20161793a5b90d.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_0_flare_0128_jpg.rf.f23112aa17e61efed6a17963a8b4f12e.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_1_flare_0128_jpg.rf.f23112aa17e61efed6a17963a8b4f12e.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_2_1_flare_0128_jpg.rf.f23112aa17e61efed6a17963a8b4f12e.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)
    elif image['file_name'] == '4_1_0_flare_0126_jpg.rf.e6af3c93cb3891992405eead0b56bc4b.jpg':
        for idx2, annotation in enumerate(data['annotations']):
            if annotation['image_id'] == image['id']:
                data['annotations'].pop(idx2)
        data['images'].pop(idx)

with open('annotations.json', 'w') as f:
    json.dump(data, f)
