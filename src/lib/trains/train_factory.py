from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .ctdet import CtdetTrainer
from .ddd import DddTrainer
from .exdet import ExdetTrainer
from .multi_pose import MultiPoseTrainer
from .multi_class_pose import MultiClassPoseTrainer

train_factory = {
    'exdet': ExdetTrainer,
    'ddd': DddTrainer,
    'ctdet': CtdetTrainer,
    'multi_pose': MultiPoseTrainer,
    'thu_multi_pose': MultiPoseTrainer,
    'multi_class_pose': MultiClassPoseTrainer,
}
