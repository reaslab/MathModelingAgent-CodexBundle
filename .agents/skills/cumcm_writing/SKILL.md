---
name: cumcm-writing
description: >
  CUMCM paper writing guide built on the bundled template_zh.
  Activate only when the coordinator has identified a Chinese CUMCM / national contest report.
  Provides file-by-file instructions tied to the LaTeX template structure.
  Enforces Chinese output and forbids fallback to MCM/template_en.
description_zh: >
  国赛论文写作指南，基于内置 template_zh 模板。
  仅在 Coordinator 已识别为中文 CUMCM / 国赛论文时激活。
  提供与 LaTeX 模板结构逐文件对应的使用说明。
  强制中文输出，禁止兜底切换到 MCM/template_en。
---

# CUMCM 国赛论文写作指南

本技能基于 `assets/latex-templates/template_zh/` 模板，提供逐文件的模板使用说明。
国赛论文使用中文撰写，评委阅卷时间有限，论文的结构清晰度、数学严谨性和视觉呈现直接决定评审分数。

---

## 0. 技能目的与运行边界

本技能只负责中文 CUMCM / 国赛论文写作，不负责判断题目属于哪个比赛，也不是模板缺失或编译失败时的兜底策略。

在本地工作流中，本技能负责中文国赛的模板文件、章节内容、图表、公式和篇幅细则；Coordinator 与 Writer 角色负责调度、任务拆分、最终验收和全局硬门槛。若通用写作 skill 与本技能冲突，以本技能的国赛要求和 Coordinator 的硬门槛为准；若本技能与 Coordinator 的全局流程冲突，以 Coordinator 为准。篇幅不足时应优先补充有证据的推导、实验、对比、验证、灵敏度、稳健性和局限性，不得因为通用的简洁建议而提前收尾。

硬性边界：

- 只有在 Coordinator 明确识别为 CUMCM / 国赛 / 中文数学建模竞赛时使用本技能。
- 输出语言必须是中文，包括章节标题、图表标题、正文、摘要和回应 Coordinator 的状态说明。
- 模板必须来自 `assets/latex-templates/template_zh/`，复制整个目录到当前 case 的 `writer/` 后再编辑。
- `writer/README.md` 必须记录 `Template source: assets/latex-templates/template_zh/`、`Copied entrypoint: main.tex`、`Template family evidence: ctexart + bundled Fandol fonts + natbib/bibliography pairing`、`Output language: 中文` 和 `Language evidence: ...`。
- 保留 `ctexart` 文档类、模板自带 `fonts/` 目录和相对路径 Fandol 字体配置。
- 最终论文正文、题注、表格、摘要、参考文献和 PDF 中的非代码清单内容不得出现本地文件地址、工作区路径、模板源路径、代码/数据文件名、工具产物路径或 agent 交接措辞；这些路径证据只写入 `writer/README.md` / Paper Status。
- 如果模板目录缺失、字体目录缺失、`xelatex` 不可用或编译返回 fatal error，立即报告阻塞原因。不要改用 `template_en`、`article`、英文 MCM 模板，也不要删除中文字体配置绕过问题。

### 1.1 终稿文体与数值表达

正文是数学建模论文，不是算法开发记录、程序验收报告或项目交付说明。删除“旧版结果、增强计算、已验收、后续回补、计算产物、图件元数据、公共评估器、计算标识”等内部制作痕迹；直接说明采用的模型、计算、结果和验证。除非术语本身属于题目中的严格数学定义，不要用“接口、口径、基线、选择门、回看、落地、复用、绑定结果、结果强度”等项目管理词替代具体的模型、变量、估计、比较或结论。

每段只承担一个功能：提出问题、建立模型、推导/求解、报告结果、解释比较或说明局限。一个结果只在摘要、对应结果章节和最终结论中完整陈述；其他位置只引用它，并补充原因、差异、适用条件或局限。正文中的工程管理量、预测量和统计量通常保留两到三位有效小数，摘要应进一步按读者可理解的精度表达；仅在误差分析、阈值判定或题目明确要求时保留更多位数，并说明必要性。

统一术语强度和分类层级：不要混用“修正、消除、压制”或“出现、证据不足、不显著”。按证据写成逻辑对称的结论，例如“支持存在显著效应”“证据不足”“不支持存在显著效应”，并说明指标变化及其含义。拆开翻译腔、口语化和连续名词堆叠；避免“负的优势”“改善为负”“稳定但不算强”等含混表述，改为明确的条件、指标方向和结论。

---

## 1. 模板概览

模板位于 `assets/latex-templates/template_zh/`，基于 `ctexart` 文档类，已配置随模板携带的 Fandol 字体和 natbib 引用格式。

`main.tex` 通过 `\input{}` 引入以下文件：

```
\input{abstract}           -> abstract.tex          摘要
\input{01-restatement}     -> 01-restatement.tex    问题重述与分析
\input{02-assumptions}     -> 02-assumptions.tex    模型假设与符号说明
\input{03-q1}              -> 03-q1.tex             问题一的建模与求解
                              (04-q2.tex, ...)      问题二、三、四...（Writer 自行创建）
\input{evaluation}         -> evaluation.tex        模型评价与改进
\bibliography{references}  -> references.bib        参考文献
\input{appendix}           -> appendix.tex          附录
```

使用时先确认 `assets/latex-templates/template_zh/main.tex` 存在，再将整个模板目录复制到当前 case 的 `writer/`，然后在 `writer/` 中编辑各文件。从当前 case 目录使用 `latexmk -xelatex -interaction=nonstopmode -halt-on-error writer/main.tex` 本地编译；若没有 `latexmk`，则在 `writer/` 内依次运行 `xelatex -> bibtex -> xelatex -> xelatex` 并保留日志。

模板中的 `\usepackage[numbers]{natbib}` 和 `\bibliographystyle{plainnat}` 是刻意配对的，不要修改。

核心设计原则：每个子问题一个独立文件（`03-q1.tex`, `04-q2.tex`, ...），
每个文件内含完整的四段结构（问题分析、模型建立、模型求解、结果分析）。
Writer 根据题目的子问题数量自行创建对应文件，并在 `main.tex` 中添加 `\input{}`。

模板、语言和文件树要求都是硬性验收项，不是写作建议。最终论文必须保留 template_zh 的 `main.tex`、`abstract.tex`、`01-restatement.tex`、`02-assumptions.tex`、逐子问题 `03-q1.tex` / `04-q2.tex` / ...、`evaluation.tex`、`appendix.tex`、`references.bib`、`figure/`、`main.pdf` 和 `README.md`；`writer/main.pdf` 只作编译产物，Reviewer PASS 后还必须在 `mma/{work_name}/` 放置一份按论文标题或题目主题命名的最终 PDF，不能叫 `main.pdf`、`final.pdf` 或 `{work_name}.pdf`。

---

## 2. 逐文件使用说明

### 2.1 abstract.tex -- 摘要

模板中有"三段式"占位提示和关键词占位。

摘要是评委最先阅读的部分，很多评委仅凭摘要完成初步分档。400-600 字内完整呈现整篇论文的核心成果。按子问题逐一说明所用模型方法和核心数值结果。摘要末尾列出 3-5 个关键词。

摘要中不要出现图表引用、参考文献引用或大段公式推导。

摘要应在所有子问题完成后最后撰写，因为需要包含每个子问题的具体数值结果。

摘要以完整呈现全部子问题的实际结果为准，不为凑篇幅重复方法或结果。

### 2.2 01-restatement.tex -- 问题重述与分析

模板包含三个 `\subsection`：问题背景、问题概述、总体分析思路。

问题重述不是复制赛题原文，而是用数学语言重新描述。明确定义输入数据（自变量）、输出目标（因变量）、约束条件和优化目标。如果赛题有多个子问题，逐一列出每个子问题的数学化表述。

"总体分析思路"小节说明整体建模逻辑和各问题之间的数学依赖关系。这里只做总体梳理，不写任务流程、实现步骤或项目化“技术路线”；每个问题的详细分析在对应的 Qi 章节中展开。

这个文件不依赖 Modeler 或 Coder 的输出，可以在题目就绪后最先撰写。

以完整界定问题、输入、输出和约束为准；不要用固定篇幅压缩必要的建模背景。

### 2.3 02-assumptions.tex -- 模型假设与符号说明

模板包含两个 `\section`：模型假设、符号说明。

模型假设：以段落形式逐条论述每个假设，说明假设的依据和合理性。每条假设应对模型建立产生实质影响，并且尽可能量化。假设通常 5-8 条，按从宏观到微观排列。随着各子问题推进，Writer 可在此追加新引入的假设。

符号说明：保持模板中的三线表格式。按类别分组：先写输入变量，再写中间变量，最后写模型参数。每个符号必须在正文中首次使用前定义。向量用粗体 $\mathbf{x}$，矩阵用大写粗体 $\mathbf{A}$，标量用斜体 $x$。

这个文件可以在框架搭建阶段先写初始假设骨架，后续随各子问题推进增量补充。

以每个假设和符号都得到充分定义、说明其影响为准。

### 2.4 03-q1.tex, 04-q2.tex, ... -- 各子问题的建模与求解（论文主体）

模板中提供了 `03-q1.tex` 作为问题一的骨架示例，包含四个 `\subsection`：

```
\section{问题一的建模与求解}
  \subsection{问题分析}     -- 分析核心矛盾和解题切入点
  \subsection{模型建立}     -- 建模动机 -> 数学公式 -> 参数说明
  \subsection{模型求解}     -- 算法/方法 -> 求解过程
  \subsection{结果分析}     -- 图表穿插正文，误差分析
```

Writer 为每个子问题复制这个四段结构，创建独立文件（`04-q2.tex`, `05-q3.tex`, ...），
并在 `main.tex` 中添加对应的 `\input{}`。

每个文件内的写作要求：

问题分析：分析这个问题的核心矛盾和切入点。聚焦于"主要矛盾是什么、打算用什么思路解决"，控制在 1-2 段。不是重复后文的模型介绍。

模型建立：先解释建模思路和选择该方法的原因，再给出完整的数学公式推导。公式推导过程不能跳步，关键步骤之间用文字衔接。公式编号使用 `\equation` 或 `\align` 环境，用 `\eqref{eq:xxx}` 引用。

模型求解：说明求解算法和计算过程。如果使用标准算法，引用原始文献并说明参数选择。

结果分析：充分使用图表展示结果——拟合图、对比图、误差分析图等。图表放在首次引用处（使用 `[H]` 浮动选项），每张图/表后写分析段落。对比型结果优先用表格呈现。引用图表时使用非断行空格：`如图~\ref{fig:xxx}所示`，`由式~\eqref{eq:xxx}可得`。

引用图表时，先读取对应的 `.png.metadata` 文件获取 Coder 程序自动计算的统计洞察（Autonomous Insights），基于 metadata 中的具体数值来撰写分析文字。你无法看到图片内容，所有关于图表特征的描述必须来自 metadata。

一篇好的国赛论文正文通常需要 8-12 张图表。

每个 Qi 文件在对应问题的 Modeler 方案和 Coder 结果就绪后即可撰写，不必等待其他问题完成。这是支持增量并行写作的核心设计。

每个 Qi 的深度由其已验证的模型、结果和讨论决定；不要为章节预分配固定页数。

### 2.5 evaluation.tex -- 模型评价与改进

模板包含两个 `\subsection`：模型优点、模型不足与改进方向。

以段落形式论述（不要用 itemize 或 enumerate 列表）。每个优点/不足用一段，结合具体数据论证。模型不足要真诚讨论局限性，每条不足最好对应一条改进思路。如果灵敏度分析放在本章也是合理的。

这个文件需要所有子问题完成后撰写。

完整讨论模型适用范围、优势、局限和可验证的改进方向。

### 2.6 appendix.tex -- 附录

模板中有 `\lstinputlisting` 的注释示例。

仅当 Coordinator 将任务明确标为高教社杯且 `Code appendix: required` 时，核心代码必须使用 `\lstinputlisting` 引入 Coder 的实际代码文件，禁止用文字描述代替代码，禁止用 `\begin{lstlisting}` 手写代码块。路径从 `writer/` 出发用 `../coder/` 相对路径。每段代码前加一句说明其功能。其他任务不附加代码；保留 Coder 的脚本、README 和执行证据即可，附录可仅放补充图表或详细推导。

示例：
```tex
以下为问题一模型求解的核心代码：
\lstinputlisting[language=Python, caption={问题一：模型求解},
  firstline=10, lastline=80]{../coder/solve_q1.py}
```

补充图表：正文放不下但有分析价值的图可放此处。

详细推导：正文中为保持流畅而省略的推导步骤。

---

## 3. 参考文献（references.bib）

国赛论文的参考文献应涵盖：所用数学方法的原始论文或经典教材，类似问题的已有研究，使用的算法或工具库的文档，赛题相关的背景资料。引用数量根据实际引用需求确定，不设硬性下限。

补充或核验参考文献时，必须通过当前会话可用的 web search 在至少 2-3 个方向检索：模型方法关键词、应用领域关键词和评价方法关键词；再打开来源核验元数据，确保引用来源多样化。

每个 `.bib` 条目必须包含 `author`、`title`、`year` 三个字段。引用键使用"作者年份主题"格式，如 `wang2023prediction`。绝不凭记忆编造参考文献。

正文中凡是引用了他人的方法、结论或数据的地方都要标注 `\cite{}`。

---

## 4. LaTeX 规范与篇幅控制

公式规范：所有数学符号首次出现时必须定义。公式推导关键步骤之间用文字衔接，如"将式~\eqref{eq:1}代入式~\eqref{eq:2}，化简可得："。避免连续多个公式之间没有任何文字。行内公式用 `$...$`，独立公式用 `\begin{equation}...\end{equation}`。

图表规范：图片分辨率不低于 300 dpi，使用 `\includegraphics[width=0.8\textwidth]{figure/xxx.png}`。表格使用三线表（`\toprule`, `\midrule`, `\bottomrule`）。对比表格中最优结果加粗，列标题包含单位。

篇幅控制：除非用户明确指定页数，完整论文以 25 页实质正文作为不对称审查基线。正文仅计渲染 PDF 中从“问题背景”（或等价的首个正文节）开始、到“参考文献”前一页结束的区间；不计前置部分、参考文献、明确标注的附录和代码清单。该基线既不是硬性下限，也不是完成上限：达到后仍须继续写完所有已验证的推导、数据来源、实验、基准对比、灵敏度分析、稳健性检验和局限性讨论；超过基线只要逻辑通顺、证据充分且相关，不作篇幅惩罚。低于基线时，缺口越大，必须给出越具体、越有证据支撑的覆盖矩阵说明；不得以“题目简单”或填充重复内容代替说明。编译后记录物理 PDF 正文页数，由 Reviewer 作最终判断。各章节按证据覆盖程度组织，不使用静态页数分配。

路径控制：正文、摘要、图表题注、表格、参考文献和最终 PDF 中的非代码清单内容不能出现 `/tmp/`、`mma/`、`../coder/`、模板来源路径、原始 `.py` / `.csv` / `.json` / `.xlsx` / `.metadata` 文件名等本地文件地址。

---

## 5. 增量写作节奏

论文写作不是"全部素材就绪后一次性写完"，而是随着建模和编码的推进逐步成型。Writer 会被 Coordinator 多次派发，每次只负责报告的一部分。

典型节奏：

第一轮（题目就绪后，不依赖 Modeler/Coder）：
  从 assets/latex-templates/template_zh/ 复制完整模板到 writer/，
  在 writer/README.md 记录模板来源、复制入口、模板家族证据、输出语言和语言证据，
  将 main.tex 中的 \title{} 设为具体标题（不保留占位符），
  编写 01-restatement.tex，
  用 websearch + webfetch 建立 references.bib 的初始条目，
  02-assumptions.tex 写入初始假设骨架，
  编译确认框架可通过。

每当一个子问题 Qi 的 Modeler 方案 + Coder 结果到位：
  创建对应的 Qi 文件（如 04-q2.tex），按四段结构完整撰写，
  在 main.tex 中添加 \input{}，
  补充 02-assumptions.tex 中 Qi 引入的新假设，
  用 websearch + webfetch 搜索本章方法相关的参考文献，追加到 references.bib，
  编译 PDF 确认整体可通过。

所有子问题完成后（收尾阶段，必须执行）：
  用所有子问题的具体数值结果更新 abstract.tex，
  撰写 evaluation.tex，
  整理 appendix.tex（用 \lstinputlisting 引入代码），
  确认 \title{} 是具体标题（若仍为占位符则更新），
  如需补充参考文献，用 websearch + webfetch 搜索并追加，
  最终编译。

增量更新时，先读取已有 .tex 文件了解当前进度，在已有内容基础上追加，不要删除或重写已完成的部分。

---

## 6. 编译环境与常见错误

| 项目 | 值 |
|------|------|
| 引擎 | XeTeX (xelatex)，原生 Unicode |
| 中文字体 | 模板内置 `writer/fonts/` Fandol 字体，相对路径加载 |
| 操作系统 | 本地系统 |
| 宏包 | 本地 TeX 发行版；缺少宏包时记录明确依赖，不静默更换模板 |

常见错误与修复：

`natbib Error: Bibliography not compatible` -- .bib 条目缺少 author 或 year 字段，逐条检查。

`Citation 'x' undefined` -- \cite 键名与 .bib 中不匹配（区分大小写），或者 bibtex 没有运行。执行完整的参考文献编译序列。

`File 'x.png' not found` -- 图表需要先复制到 writer/figure/，然后用 figure/x.png 路径引用。确认你是在 writer/ 目录下编译，而不是在模板源目录里。

`Font ... not found` -- 确认 `writer/fonts/` 是从模板目录完整复制过来的。不要改用 SimSun、SimHei 或其他系统字体名。

`Undefined control sequence \setCJKmainfont` -- 通常表示没有按 xelatex/ctex 链路编译，或模板被破坏。报告阻塞，不要删除字体配置。

`This is pdfTeX ... format=pdflatex` -- 编译器不匹配。中文模板必须使用 `xelatex`；报告编译器不匹配，不要切换到英文模板。

`Overfull \hbox` / `Overfull \vbox` -- 常见于长公式、URL、表格单元格、题注或代码清单超出版心。最终定稿必须检查编译输出或 `.log`，逐项修复后重新编译，并在 Paper Status 中记录零警告证据；编译成功不等于可提交。
