import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# visualizer 配置区域 (由 Agent 自主分析并填写)
# ==========================================
PREDECESSORS_PATH = ["coder/data/raw_data_v1.csv", "coder/data/emission_factors.xlsx"] # 前置输入数据
FIG_PATH = "..."   # 图表路径
PROGRAM_NAME = os.path.basename(__file__)
DESCRIPTION = "..." # 对图表意图的描述

def main():
    # --- 自主计算统计洞察 ---
    # Agent 需要根据实验目的，在此处编写最相关的分析代码
    insights = {}
    
    # 示例逻辑（Agent 会根据实际情况替换）：
    # if "对比实验":
    #     gap = (df['A'].mean() - df['B'].mean()) / df['B'].mean()
    #     insights["Performance_Gain"] = f"{gap:.2%}"
    # if "时间序列":
    #     slope = calculate_slope(df)
    #     insights["Growth_Trend"] = "Upward" if slope > 0 else "Downward"
    
    # --- 绘图逻辑 ---
    plt.figure(figsize=(10, 6))
    # ... plt.plot, plt.scatter ...
    plt.savefig(FIG_PATH, dpi=300, bbox_inches='tight')
    plt.close()
    
    return insights

if __name__ == "__main__":
    # 执行并获取 Agent 自主选择的指标
    calculated_insights = main()

    # 自动生成结构化的 .metadata
    try:
        meta_path = FIG_PATH + ".metadata"
        metadata_content = f"""### Visual Metadata for {os.path.basename(FIG_PATH)}
- **Description**: {DESCRIPTION}
- **Program**: `{PROGRAM_NAME}`
- **Predecessors**: {'\n-- '.join(PREDECESSORS_PATH)}
- **Autonomous Insights**: {'\n'.join([f"  - {k}: {v}" for k, v in calculated_insights.items()])}
"""
        with open(meta_path, "w", encoding="utf-8") as f:
            f.write(metadata_content)
        print(f"[+] Metadata created with autonomous insights.")
    except Exception as e:
        print(f"[!] Error: {e}")