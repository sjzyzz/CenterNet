from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .exdet import ExdetDetector
from .ddd import DddDetector
from .ctdet import CtdetDetector
from .multi_pose import MultiPoseDetector
from .multi_class_pose import MultiClassPoseDetector

detector_factory = {
    'exdet': ExdetDetector,
    'ddd': DddDetector,
    'ctdet': CtdetDetector,
    'multi_pose': MultiPoseDetector,
    'thu_multi_pose': MultiPoseDetector,
    'multi_class_pose': MultiClassPoseDetector
}
