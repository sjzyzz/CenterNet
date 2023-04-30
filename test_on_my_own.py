from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

if __name__ == '__main__':
    cocoGt = COCO('data/thu_basketball/annotations/test.json')
    print(cocoGt)
    for ann in cocoGt.dataset['annotations']:
        ann['category_id'] = 1
    resFile = 'exp/thu_multi_pose/dla_1x/results.json'
    cocoDt = cocoGt.loadRes(resFile)
    cocoEval = COCOeval(cocoGt, cocoDt, 'keypoints')
    cocoEval.evaluate()
    cocoEval.accumulate()
    cocoEval.summarize()
