class PromptJudgmentNode:
    """
    prompt动态判断
    
    This node compares a judgment string against multiple prompt criteria
    to decide which prompt to output.
    
    Inputs:
    - prompt1: First input prompt
    - prompt1_criteria: Comma-separated keywords for prompt1 (e.g., "woman,girl,female")
    - prompt2: Second input prompt
    - prompt2_criteria: Comma-separated keywords for prompt2 (e.g., "man,boy,male")
    - prompt3: Third input prompt (optional)
    - prompt3_criteria: Comma-separated keywords for prompt3 (optional)
    - judgment_criteria: The condition to judge which prompt to output
    
    The node will choose prompt1 if any keyword from prompt1_criteria is found in
    judgment_criteria, prompt2 if any keyword from prompt2_criteria is found, and so on.
    If multiple matches exist, the first match wins.
    """
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt1": ("STRING", {"multiline": True, "default": ""}),
                "prompt1_criteria": ("STRING", {"multiline": False, "default": ""}),
                "prompt2": ("STRING", {"multiline": True, "default": ""}),
                "prompt2_criteria": ("STRING", {"multiline": False, "default": ""}),
                "judgment_criteria": ("STRING", {"multiline": False, "default": ""})
            },
            "optional": {
                "prompt3": ("STRING", {"multiline": True, "default": ""}),
                "prompt3_criteria": ("STRING", {"multiline": False, "default": ""}),
            }
        }
    
    CATEGORY = "text"
    RETURN_TYPES = ("STRING",)
    FUNCTION = "judge_prompts"
    RETURN_NAMES = ("prompt",)
    
    def judge_prompts(self, prompt1, prompt1_criteria, prompt2, prompt2_criteria, 
                     judgment_criteria, prompt3="", prompt3_criteria=""):
        # 预处理所有字符串：转小写并去除空格
        prompt1_criteria_lower = prompt1_criteria.lower().strip()
        prompt2_criteria_lower = prompt2_criteria.lower().strip()
        prompt3_criteria_lower = prompt3_criteria.lower().strip() if prompt3_criteria else ""
        judgment_lower = judgment_criteria.lower().strip()
        
        # 将判断标准拆分为关键词列表
        prompt1_keywords = [kw.strip() for kw in prompt1_criteria_lower.split(",") if kw.strip()]
        prompt2_keywords = [kw.strip() for kw in prompt2_criteria_lower.split(",") if kw.strip()]
        prompt3_keywords = [kw.strip() for kw in prompt3_criteria_lower.split(",") if kw.strip()]
        
        # 判断逻辑
        # 首先检查是否有prompt1的关键词匹配
        for keyword in prompt1_keywords:
            if keyword and keyword in judgment_lower:
                print(f"匹配到prompt1关键词: {keyword}")
                return (prompt1,)
        
        # 然后检查是否有prompt2的关键词匹配
        for keyword in prompt2_keywords:
            if keyword and keyword in judgment_lower:
                print(f"匹配到prompt2关键词: {keyword}")
                return (prompt2,)
        
        # 最后检查是否有prompt3的关键词匹配（如果存在）
        if prompt3 and prompt3_criteria:
            for keyword in prompt3_keywords:
                if keyword and keyword in judgment_lower:
                    print(f"匹配到prompt3关键词: {keyword}")
                    return (prompt3,)
        
        # 如果没有匹配，默认返回prompt1
        print("没有匹配任何关键词，默认使用prompt1")
        return (prompt1,)