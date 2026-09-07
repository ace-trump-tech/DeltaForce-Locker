"""
FishDetector — 鱼种 + 浮漂视觉识别
基于 YOLO-omni Fish v3 + 骨骼点投票降噪
"""

import random
from typing import List, Tuple
import numpy as np


class FishDetector:
    """
    鱼种识别 + 浮漂位移检测
    - detect_species:      鱼种分类
    - detect_float_drift:  浮漂位移检测
    - multi_frame_vote:    多帧投票降噪
    - warmup:              模型预热
    """

    VERSION = "3.0.0"
    INPUT_SIZE = (640, 640)

    def __init__(
        self,
        weights_path: str = "models/weights/fish_v3.pt",
        conf_thres: float = 0.5,
        iou_thres: float = 0.45,
    ):
        self.weights_path = weights_path
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self._loaded = False

    def load(self) -> None:
        # 教学占位实现
        self._loaded = True

    def detect_species(self, frame: np.ndarray) -> List[dict]:
        # 教学占位实现
        return []

    def detect_float_drift(self, frame: np.ndarray) -> Tuple[float, float]:
        # 教学占位实现
        return (0.0, 0.0)

    def multi_frame_vote(self, detections: List[dict]) -> List[dict]:
        # 教学占位实现
        return detections

    def warmup(self, n_runs: int = 3) -> None:
        # 教学占位实现
        return
