# MMA Codex Agent

一个在本地 Codex 中运行的数学建模智能体，可以从读取题目开始，完成建模、计算、绘图、论文写作和最终检查。

最后更新：**2026-08-17**

## 开始使用

### 1. 准备 Codex

安装并登录 Codex CLI。然后在终端进入本项目：

```bash
cd /path/to/mma
codex
```

也可以在任意位置运行：

```bash
codex -C /path/to/mma
```

首次打开时，如果 Codex 询问是否信任该目录，请确认信任，否则项目中的 Agent 设置和 skills 不会加载。

完整数学建模任务会自动检查并在可用时使用本地 HMML 方法检索；无需手动启动。其启用条件、依赖安装、下载回退与关闭方式见下方“HMML 方法参考”章节。

### 2. 放入题目和数据

把题目和数据直接放在项目根目录。可以使用 PDF、Word、Excel、CSV、图片或文本文件，例如：

```text
mma/
├── problem.pdf
└── data.xlsx
```

不要修改原始文件。Codex 产生的代码、结果和论文会写入新的工作目录。

### 3. 告诉 Codex 要完成什么

完整解决一道中文题目并生成论文：

```text
完整解决 problem.pdf 中的数学建模题，数据在 data.xlsx。
使用中文撰写论文，实际运行所有计算，生成图表并编译最终 PDF。
```

解决 MCM/ICM 题目：

```text
完整解决 problem.pdf，按 MCM/ICM 英文论文格式输出最终 PDF。
```

只完成部分工作也可以：

```text
读取 problem.pdf，只比较可行的建模方法并给出实验计划，暂时不要写论文。
```

```text
检查现有计算结果和论文，修复数值、图表、引用和排版问题，重新生成 PDF。
```

任务中可以继续指定输出语言、竞赛类型、页数、必须使用的方法、禁止使用的方法以及最终文件要求。

## 运行过程

完整任务通常会依次完成：

1. 读取题目和数据；
2. 分析问题并比较模型；
3. 编写和运行计算代码；
4. 检查约束、结果和敏感性；
5. 生成图表并撰写论文；
6. 编译 PDF 并进行最终审核。

项目已经配置 Modeler、Coder、Writer 和 Reviewer。Codex 会按任务需要调用这些角色，用户不需要手动启动它们。

## Python 和其他依赖

推荐使用 Python 3.12，但用户不需要预先创建虚拟环境。

Codex 会先检查当前电脑上可用的工具：有 uv 时优先使用 uv，没有时使用 Conda 或现有 Python。缺少计算库、文档读取工具或 TeX 时，Codex 会说明缺少什么，并在需要安装或下载时请求确认。

生成论文 PDF 通常需要 XeLaTeX，建议同时安装 `latexmk` 和 BibTeX。不同题目可能还会用到 NumPy、pandas、SciPy、scikit-learn、Matplotlib 等包。

Linux、macOS 和原生 Windows 都可以使用；具体安装命令由 Codex 根据当前系统选择。

## HMML 方法参考

HMML（Hierarchical Mathematical Modeling Library）是随项目附带的本地数学建模方法库：它按方法类别收录常见建模思路、适用场景和方法说明。Codex 会把当前题目的英文描述与这些条目做语义匹配，给 Modeler 提供两三个可比较的候选方法，再结合题目的数据、假设、约束与验证要求作出选择。

它不是求解器、代码生成器或实时文献数据库：不会替代建模推导、数值实验和验证，检索排名也不能单独证明某个方法适用。

完整建模任务默认自动检查 HMML：

- 在项目本地环境中安装所需依赖并进行一次本地语义检索；
- 仅当 `all-MiniLM-L6-v2` 返回候选方法和有效余弦相似度时才启用；
- 中文请求首次下载模型时，优先使用中文镜像，失败后回退官方 Hugging Face；
- 安装、模型下载或语义评分失败时，Codex 自动关闭 HMML 并照常建模；
- 明确要求禁用 HMML 可跳过安装和检索；明确要求启用 HMML 可在此前失败后重试。

首次启用可能需要下载模型。依赖只安装在项目本地环境，不会修改系统全局 Python。数据来源、运行命令与诊断细节见 [`hmml/README.md`](hmml/README.md)。

## 在哪里查看结果

每个任务的文件默认保存在：

```text
mma/<任务名称>/
```

其中通常包括：

- `modeler/`：模型、公式、假设和验证方案；
- `coder/`：代码、数据结果和图表；
- `writer/`：LaTeX 文件和工作版 PDF；
- `reviewer/`：审核记录；
- 顶层最终 PDF：审核完成后的交付文件。

继续修改时，直接告诉 Codex 当前任务目录和要修改的内容，不需要重新开始整个题目。

## 常见情况

**Codex 没有加载项目角色或 skills**

确认启动时使用了 `codex -C /path/to/mma`，并且已经信任该目录。

**无法读取 PDF、Word 或 Excel**

把报错交给 Codex，它会检查并选择所需的本地读取工具。扫描版 PDF 可能需要 OCR。

**论文没有生成 PDF**

让 Codex 检查 XeLaTeX、字体、BibTeX 和编译日志，并继续修复到可以编译。

**网络不可用或 HMML 模型无法下载**

Codex 会禁用 HMML 并继续建模。需要 HMML 时，可以等网络恢复后要求重新检查。

## 贡献者

感谢以下贡献者对本项目的投入：

<table>
  <tr>
    <td align="center"><a href="https://github.com/rc314159-creator"><img src="https://github.com/rc314159-creator.png?size=96" width="80" alt="Ren Can"><br><sub><b>Ren Can</b></sub><br><sub>@rc314159-creator</sub></a></td>
    <td align="center"><a href="https://github.com/sillyDaibo"><img src="https://github.com/sillyDaibo.png?size=96" width="80" alt="Li Daibo"><br><sub><b>Li Daibo</b></sub><br><sub>@sillyDaibo</sub></a></td>
    <td align="center"><a href="https://github.com/TraFifholz"><img src="https://github.com/TraFifholz.png?size=96" width="80" alt="Zheng Libin"><br><sub><b>Zheng Libin</b></sub><br><sub>@TraFifholz</sub></a></td>
    <td align="center"><a href="https://github.com/Yuhaooou"><img src="https://github.com/Yuhaooou.png?size=96" width="80" alt="Jiang Yuhao"><br><sub><b>Jiang Yuhao</b></sub><br><sub>@Yuhaooou</sub></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/tianming23"><img src="https://github.com/tianming23.png?size=96" width="80" alt="Huang Hao"><br><sub><b>Huang Hao</b></sub><br><sub>@tianming23</sub></a></td>
    <td align="center"><a href="https://github.com/xinyuuu9"><img src="https://github.com/xinyuuu9.png?size=96" width="80" alt="Chen Xinyu"><br><sub><b>Chen Xinyu</b></sub><br><sub>@xinyuuu9</sub></a></td>
    <td align="center"><a href="https://github.com/Iiceee"><img src="https://github.com/Iiceee.png?size=96" width="80" alt="Xia Shumeng"><br><sub><b>Xia Shumeng</b></sub><br><sub>@Iiceee</sub></a></td>
    <td align="center"><a href="https://github.com/glhglhglh6"><img src="https://github.com/glhglhglh6.png?size=96" width="80" alt="Guo Luhong"><br><sub><b>Guo Luhong</b></sub><br><sub>@glhglhglh6</sub></a></td>
  </tr>
</table>

## 来源与许可证

本项目原创部分采用 [MIT License](LICENSE)。第三方材料不因此被重新许可，完整归属见 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。

HMML 数据来自 [HKUST USAIL/LLM-MM-Agent](https://github.com/usail-hkust/LLM-MM-Agent)，部分论文相关 skills 改编自 [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills)。中文模板附带的 Fandol 字体使用 GNU GPL v3 with the GPL font exception。
