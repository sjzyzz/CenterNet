from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .sample.ddd import DddDataset
from .sample.exdet import EXDetDataset
from .sample.ctdet import CTDetDataset
from .sample.multi_pose import MultiPoseDataset
from .sample.thu_multi_pose import THUMultiPoseDataset
from .sample.thu_multi_class_pose import THUMultiClassPoseDataset

from .dataset.coco import COCO
from .dataset.pascal import PascalVOC
from .dataset.kitti import KITTI
from .dataset.coco_hp import COCOHP
from .dataset.thu_basketball import THU_Basketball
from .dataset.thu_basketball_hp import THU_Basketball_HP
from .dataset.thu_multi_class_pose import THU_Multi_Class_Pose

dataset_factory = {
    'coco': COCO,
    'pascal': PascalVOC,
    'kitti': KITTI,
    'coco_hp': COCOHP,
    'thu_basketball': THU_Basketball,
    'thu_basketball_hp': THU_Basketball_HP,
    'thu_multi_class_pose': THU_Multi_Class_Pose
}

_sample_factory = {
    'exdet': EXDetDataset,
    'ctdet': CTDetDataset,
    'ddd': DddDataset,
    'multi_pose': MultiPoseDataset,
    'thu_multi_pose': THUMultiPoseDataset,
    'multi_class_pose': THUMultiClassPoseDataset,
}


def get_dataset(dataset, task):
    class Dataset(dataset_factory[dataset], _sample_factory[task]):
        pass

    return Dataset
