from .dynamic_judgment_node import DynamicJudgmentNode
from .prompt_judgment_node import PromptJudgmentNode

NODE_CLASS_MAPPINGS = {
    "DynamicJudgmentNode": DynamicJudgmentNode,
    "PromptJudgmentNode": PromptJudgmentNode
}

# Make sure to use matching names
NODE_DISPLAY_NAME_MAPPINGS = {
    "DynamicJudgmentNode": "图像动态判断",
    "PromptJudgmentNode": "prompt动态判断"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
