import os
import hashlib
import torch
import numpy as np
from PIL import Image, ImageOps, ImageSequence
from pathlib import Path

import folder_paths
from comfy.utils import common_upscale

class DynamicJudgmentNode:
    """
    图像动态判断
    
    This node compares a judgment string against two sets of criteria
    to decide which image to output.
    
    Inputs:
    - image1: First input image
    - image1_criteria: Comma-separated keywords for image1 (e.g., "woman,girl,female")
    - image2: Second input image
    - image2_criteria: Comma-separated keywords for image2 (e.g., "man,boy,male")
    - judgment_criteria: The condition to judge which image to output
    
    The node will choose image1 if any keyword from image1_criteria is found in
    judgment_criteria, and image2 if any keyword from image2_criteria is found.
    If multiple matches exist, the first match wins.
    """
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image1": ("IMAGE",),
                "image1_criteria": ("STRING", {"multiline": False, "default": ""}),
                "image2": ("IMAGE",),
                "image2_criteria": ("STRING", {"multiline": False, "default": ""}),
                "judgment_criteria": ("STRING", {"multiline": False, "default": ""})
            },
            "optional": {
                "mask1": ("MASK",),
                "mask2": ("MASK",),
            }
        }
    
    CATEGORY = "image"
    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "judge_images"
    
    def judge_images(self, image1, image1_criteria, image2, image2_criteria, judgment_criteria, mask1=None, mask2=None):
        # 预处理所有字符串：转小写并去除空格
        image1_criteria_lower = image1_criteria.lower().strip()
        image2_criteria_lower = image2_criteria.lower().strip()
        judgment_lower = judgment_criteria.lower().strip()
        
        # 将判断标准拆分为关键词列表
        image1_keywords = [kw.strip() for kw in image1_criteria_lower.split(",") if kw.strip()]
        image2_keywords = [kw.strip() for kw in image2_criteria_lower.split(",") if kw.strip()]
        
        # 创建默认掩码
        default_mask = torch.zeros((64, 64), dtype=torch.float32, device="cpu")
        
        # 判断逻辑
        # 首先检查是否有图1的关键词匹配
        for keyword in image1_keywords:
            if keyword and keyword in judgment_lower:
                print(f"匹配到图1关键词: {keyword}")
                return (image1, mask1 if mask1 is not None else default_mask)
        
        # 然后检查是否有图2的关键词匹配
        for keyword in image2_keywords:
            if keyword and keyword in judgment_lower:
                print(f"匹配到图2关键词: {keyword}")
                return (image2, mask2 if mask2 is not None else default_mask)
        
        # 如果没有匹配，默认返回图1
        print("没有匹配任何关键词，默认使用图1")
        return (image1, mask1 if mask1 is not None else default_mask)