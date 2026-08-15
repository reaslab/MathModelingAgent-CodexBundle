---
name: data-engine
description: >
  Numerical experiment engine. It executes experiment scripts 
  and generates paired outputs: a `.csv`/`.txt`/`.json` result file and a mandatory `.csv.metadata`/`.txt.metadata`/`.json.metadata` sidecar file. 
  The metadata file must contain the data's physical description, generating program name, 
  column headers, and data lineage (predecessors). This ensures that every dataset is 
  self-documenting and fully traceable for the writer.
description_zh: >
  数值实验引擎。执行任何可视化任务以外的任务脚本，并生成配对的输出：
  一个 `.csv`/`.txt`/`.json` 结果文件及一个强制性的 `.csv.metadata`/`.txt.metadata`/`.json.metadata` 侧边栏文件。
  元数据文件必须包含数据的物理含义描述、生成程序名、表头字段及数据血缘（前置数据）。
  确保每个数据集都是自说明的，且为后续写作提供完整的溯源路径。
---

# Data Engine 技能指南 (Data Engine Skill Guide)

本技能用于指导 Coder Agent 执行数值实验、数据处理或仿真脚本，并规范化输出结果。
其核心目标是：进行实验、保证流程可追溯、成果可溯源，并提供详尽的描述，避免 Writer 因缺失数据阅读能力而产生幻觉。

## 1. 核心原则与工作流

1. 严格使用模板：先加载本技能，再使用与本 `SKILL.md` 同目录下的 `template.py` 作为代码起点。不要使用旧版源码树路径、仓库外路径或自行 glob 猜路径；加载后的 bundled skill 目录就是唯一模板来源。
2. 只实现业务逻辑：你只需要在模板指定的业务逻辑区域（如 `main()` 函数内部）编写数据处理或仿真代码。一个代码只产出一个数据文件并保存。
3. 不动主程序：绝对不要修改模板中的 `if __name__ == "__main__":` 主程序块。输出 metadata 的相关逻辑已经在模板中详细给出，主程序会自动调用并生成。
4. 完善配置区域：你必须根据当前实验的具体情况，准确填写模板顶部的配置区域（如 `FILE_PATH`, `DESCRIPTION`, `PREDECESSORS_PATH` 等）。
5. 必须形成文件：严禁将结果直接通过print输出，必须将结果保存为 TXT//CSV 文件，并确保 metadata 文件正确生成。

## 2. 模板使用说明

模板文件 `template.py` 包含三个主要部分：

### 2.1 实验配置区域 (必须填写)
```python
FILE_PATH = "coder/data/processed_sample.txt"  # 产出文件路径
DESCRIPTION = "描述该数据的物理含义，例如：各省份2023年碳排放模拟计算结果" 
PREDECESSORS_PATH = ["coder/data/raw_data_v1.csv", "coder/data/emission_factors.json"] # 前置输入数据
PROGRAM_NAME = os.path.basename(__file__) # 自动获取本程序名称
```
- `FILE_PATH`: 明确指定输出数据的路径。
- `DESCRIPTION`: 至关重要。必须详细描述该数据的物理含义、包含的指标、数据的时间/空间范围等。Writer 将完全依赖此描述来理解数据，描述越详细，Writer 产生幻觉的概率越低。
- `PREDECESSORS_PATH`: 列出生成此数据所依赖的所有前置数据文件的路径，确保数据血缘可追溯。

### 2.2 业务逻辑区域 (必须实现)
```python
def main():
    """业务逻辑：生成数据"""
    print(f"[*] Running {PROGRAM_NAME}...")
    # ... 你的数据处理/仿真代码 ...
    # 必须保存文件到 FILE_PATH
```
- 在此处编写你的核心算法、数据清洗、特征工程或数值模拟代码。
- 确保最终结果被正确保存到 `FILE_PATH` 指定的位置。

### 2.3 主程序与 Metadata 生成区域 (严禁修改)
```python
if __name__ == "__main__":
    main()
    # --- 自动生成侧边栏元数据 (One-to-One Metadata) ---
    # ...
```
- 这部分代码会自动读取你生成的数据文件，提取表头，并结合你填写的配置信息，生成一个 `.csv.metadata` 文件。
- 这个 metadata 文件是 Writer 理解数据的唯一凭证，绝对不能破坏这部分逻辑。

## 3. 数据生成标准
生成后验证（每次生成数据后必须执行）：
1. 运行脚本并检查退出码 — 0 表示成功
2. 确认 CSV 文件已创建：使用 execute_command("ls coder/data/") 确认
3. 如果脚本失败，修复后重新生成

## 4. 交付标准

每次使用 data-engine 技能后，必须确保产出成对的文件：
1. 数据文件 (如 `result.csv`)：包含真实的计算结果。
2. 元数据文件 (如 `result.csv.metadata`)：包含数据的详细描述、生成程序、表头和前置依赖。

只有当这两个文件都成功生成，且 metadata 中的描述足够详尽时，你的任务才算完成。
