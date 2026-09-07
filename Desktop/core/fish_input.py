"""
FishInputSimulator — 自动钓鱼模拟输入
SendInput / pynput 鼠标轨迹模拟 + 平滑插值
"""

import time
import random


class FishInputSimulator:
    """
    自动钓鱼模拟输入
    - activate:         激活输入模拟器
    - cast_bait_mouse:  抛竿鼠标轨迹
    - reel_in_sequence: 收线按键序列
    - smooth_move:      平滑鼠标移动
    - click:            单击（抛竿 / 收线触发）
    - deactivate:       卸载输入模拟器
    """

    VERSION = "2.4.0"

    def __init__(self, sensitivity: float = 0.7, smooth: bool = True):
        self.sensitivity = sensitivity
        self.smooth = smooth
        self._active = False

    def activate(self) -> None:
        # 教学占位实现
        self._active = True

    def cast_bait_mouse(self, x: int, y: int) -> None:
        # 教学占位实现
        return

    def reel_in_sequence(self, duration_ms: int = 1500) -> None:
        # 教学占位实现
        return

    def smooth_move(self, dx: int, dy: int) -> None:
        # 教学占位实现
        return

    def click(self, button: str = "left") -> None:
        # 教学占位实现
        return

    def deactivate(self) -> None:
        # 教学占位实现
        self._active = False
