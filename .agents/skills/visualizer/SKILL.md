---
name: visualizer
description: >
  Data analysis and visualization engine. It executes plotting scripts and generates paired outputs: 
  a chart file (e.g., `.png`) and a mandatory `.png.metadata` sidecar file. 
  The metadata file must contain the chart's description, data lineage, and most importantly, 
  program-calculated statistical insights (e.g., extrema, variance, trends). 
  These insights serve as the sole basis for figure descriptions in the paper, 
  preventing visual hallucinations by the writer.
description_zh: >
  数据分析与可视化引擎。执行绘图脚本，并生成配对的输出：
  一个图表文件（如 `.png`）及一个强制性的 `.png.metadata` 侧边栏文件。
  元数据文件必须包含图表描述、数据血缘，以及最重要的：程序计算的客观统计洞察（如极值、方差、趋势等）。
  这些统计摘要作为论文图表描述的唯一依据，彻底杜绝因视觉盲区导致的幻觉描述。
---

# Visualizer 技能指南
本技能用于指导 Coder Agent 进行数据分析与可视化绘图。

其核心目标是：进行可视化实验、保证流程可追溯、成果可溯源，并通过程序计算客观的统计摘要，为 Writer 提供图表描述的唯一依据，彻底杜绝因视觉盲区导致的幻觉描述。

## 1. 核心原则与工作流
1. 严格使用模板：先加载本技能，再使用与本 `SKILL.md` 同目录下的 `template.py` 作为代码起点。不要使用旧版源码树路径、仓库外路径或自行 glob 猜路径；加载后的 bundled skill 目录就是唯一模板来源。
2. 只实现业务逻辑：你只需要在模板指定的业务逻辑区域（如 `main()` 函数内部）编写绘图代码和统计洞察（Insights）计算代码。一个代码只绘制一张图片并保存。
3. 不动主程序：绝对不要修改模板中的 `if __name__ == "__main__":` 主程序块。输出 metadata 的相关逻辑已经在模板中详细给出，主程序会自动调用并生成。
4. 完善配置区域：你必须根据当前绘图的具体情况，准确填写模板顶部的配置区域（如 `PREDECESSORS_PATH`, `FIG_PATH`, `DESCRIPTION` 等）。

## 2. 模板使用说明

模板文件 `template.py` 包含三个主要部分：

### 2.1 配置区域 (必须填写)
```python
PREDECESSORS_PATH = ["coder/data/raw_data_v1.csv", "coder/data/emission_factors.xlsx"] # 前置输入数据
FIG_PATH = "..."   # 图表路径
PROGRAM_NAME = os.path.basename(__file__)
DESCRIPTION = "..." # 对图表意图的描述
```
- `PREDECESSORS_PATH`: 绘图所依赖的前置数据源路径列表。
- `FIG_PATH`: 生成的图表保存路径（通常为 `.png`）。
- `DESCRIPTION`: 至关重要。详细描述该图表的意图、展示的变量关系、图表类型（如折线图、散点图）等。

### 2.2 业务逻辑与统计洞察区域 (必须实现)
```python
def main():    
    # --- 自主计算统计洞察 ---
    insights = {}
    # ... 计算极值、方差、趋势、对比差距等 ...
    
    # --- 绘图逻辑 ---
    # ... plt.plot, plt.savefig ...
    
    return insights
```
- 绘图逻辑：使用 matplotlib/seaborn 等库绘制高质量图表，并保存到 `FIG_PATH`。
- 统计洞察 (Insights)：这是 Visualizer 最关键的一步！你必须编写代码，从数据中提取出客观的统计结论（例如：最大值出现的时间、两组数据的平均差异百分比、整体趋势的斜率等），并存入 `insights` 字典返回。
- Writer 看不到图片，只能看到你计算出的 `insights`。如果你的 `insights` 是空的或毫无意义的，Writer 就会在论文中胡编乱造。

### 2.3 主程序与 Metadata 生成区域 (严禁修改)
```python
if __name__ == "__main__":
    calculated_insights = main()
    # --- 自动生成结构化的 .metadata ---
    # ...
```
- 这部分代码会自动接收你返回的 `insights`，并结合配置信息，生成一个 `.png.metadata` 文件。
- 这个 metadata 文件是 Writer 描述图表的唯一依据，绝对不能破坏这部分逻辑。

## 3. 图表生成标准
图表是你仅次于代码的最重要产出物——它们会直接出现在最终报告中，对评分有重大影响。

尺寸与分辨率：
- 默认图表尺寸：单图 `(10, 6)`，宽幅对比图 `(12, 5)`
- DPI：300（打印质量必须）
- 保存：`plt.savefig("coder/figure/xxx.png", dpi=300, bbox_inches='tight')`
- 使用 `plt.savefig()`，不用 `plt.show()`

标签与标题：
- 每个坐标轴必须有带单位的标签："Temperature (°C)"、"Time (days)"
- 标题要简洁明确："Q1: Predicted vs Actual Values"
- 多条线/系列时必须有图例
- 字号：标题 14pt，轴标签 12pt，刻度标签 10pt，图例 10pt

子图用法：
- 对比多个结果时，使用子图放在一张图里：
  `fig, axes = plt.subplots(1, 3, figsize=(18, 5))`
- 对比展示优先用子图，而不是分开的小图

颜色方案：
- 分类数据使用 seaborn 默认调色板或 matplotlib `'tab10'`
- 连续数据使用序列色谱（`'viridis'`、`'plasma'`）
- 确保色盲友好：避免仅用红绿区分

图表语言规则：
- 协调者在你的任务开头传入 `[产出语言 / Output Language: ...]`。
- 图表标题、坐标轴标签、图例、标注必须使用指定的产出语言。
- 如果产出语言是"中文"，所有图表文字用中文。
- 如果产出语言是"English"，所有图表文字用英文。
- 如需中文图表，选择本机已安装的中文字体，并在保存前用最小样图确认中文和负号均能正常渲染；没有可用字体时报告阻塞。可优先尝试 `WenQuanYi Zen Hei`、`SimHei` 或 `DejaVu Sans`，并设置 `plt.rcParams['axes.unicode_minus'] = False`。

生成后验证（每次生成图表后必须执行）：
1. 运行脚本并检查退出码 — 0 表示成功
2. 确认 PNG 文件已创建：使用 execute_command("ls coder/figure/") 确认
3. 如果脚本失败或有字体缺失警告，修复后重新生成

## 4. 交付标准

每次使用 visualizer 技能后，必须确保产出成对的文件：
1. 图表文件 (如 `figure1.png`)：高质量的可视化结果。
2. 元数据文件 (如 `figure1.png.metadata`)：包含图表描述、数据源、生成程序，以及最关键的 Autonomous Insights（自主统计洞察）。

只有当这两个文件都成功生成，且 metadata 中的 insights 能够充分支撑论文对该图表的文字分析时，你的任务才算完成。
