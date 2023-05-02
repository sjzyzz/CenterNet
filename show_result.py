''''检查模型的输出情况，看看是哪里写错了'''
import cv2
import json
from random import choice
import os.path as osp

color_pane = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
]

if __name__ == '__main__':
    gt_path = '/root/CenterNet/data/thu_basketball/annotations/test.json'
    with open(gt_path) as f:
        gt_json = json.load(f)
    # 读入数据
    result_path = 'exp/multi_class_pose/dla_1x_original/results.json'
    with open(result_path) as f:
        result_json = json.load(f)
    # 随机选一张图片
    img_info = choice(gt_json['images'])
    img_id = img_info['id']
    img_path = osp.join('data/thu_basketball/images/test', img_info['file_name'])
    # 画图
    anns = []
    for res in result_json:
        if res['image_id'] == img_id:
            anns.append(res)

    img = cv2.imread(img_path)
    print(f'There are {len(anns)} person in this picture')
    for ann in anns:
        bbox = ann['bbox']
        category = int(ann['category_id'] - 1)
        ul = (int(bbox[0]), int(bbox[1]))
        br = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        if 0.4 < ann['score']:
            img = cv2.rectangle(img, ul, br, color_pane[category])
    cv2.imwrite('result.jpg', img)
