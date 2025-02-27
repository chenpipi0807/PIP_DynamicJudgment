# ComfyUI Dynamic Judgment Node

一个功能强大的ComfyUI自定义节点，能够根据关键词动态判断并选择输出哪张图像。

![微信截图_20250226204826](https://github.com/user-attachments/assets/835af010-6729-42bd-971d-1a3b32bb42b3)

## 介绍

Dynamic Judgment Node（动态判断节点）允许您基于文本匹配来选择两张输入图像中的一张作为输出。它通过比较判断条件文本与每张图像相关联的关键词列表来做出决策。

### 功能更新

新增了prompt判断，prompt三选一生效，用法和图像一致

### 主要特点

*   为两张输入图像分别设置关键词列表（用英文逗号分隔）
*   基于文本匹配智能选择输出哪张图像
*   支持掩码（mask）输入和输出
*   简单易用，完美集成到ComfyUI工作流中

## 安装方法

1.  进入您的ComfyUI安装目录
2.  将此仓库克隆到`custom_nodes`文件夹中：

## 使用方法

1. 在ComfyUI中，加载Dynamic Judgment Node。
2. 为每张输入图像设置关键词列表。
3. 输入判断条件文本。
4. 节点将基于文本匹配结果选择输出图像。
