import pandas as pd
import os

# ==========================================
# 实验配置区域 (Agent 必须填写)
# ==========================================
FILE_PATH = "coder/data/processed_sample.csv"  # 产出文件路径
DESCRIPTION = "描述该数据的物理含义，例如：各省份2023年碳排放模拟计算结果" 
PREDECESSORS_PATH = ["coder/data/raw_data_v1.csv", "coder/data/emission_factors.xlsx"] # 前置输入数据
PROGRAM_NAME = os.path.basename(__file__) # 自动获取本程序名称

def main():
    """业务逻辑：生成数据"""
    print(f"[*] Running {PROGRAM_NAME}...")
    
    # 模拟数据生成
    df = pd.DataFrame({"alpha": [0.1, 0.2, 0.3], "result": [10.5, 12.1, 14.8]})
    
    # 必须保存文件
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    df.to_csv(FILE_PATH, index=False)
    print(f"[+] Data saved to {FILE_PATH}")

if __name__ == "__main__":
    main()

    # --- 自动生成侧边栏元数据 (One-to-One Metadata) ---
    try:
        df_temp = pd.read_csv(FILE_PATH, nrows=0)
        headers = ", ".join(df_temp.columns.tolist())
        meta_path = FILE_PATH + ".metadata"
        
        metadata_content = f"""### Metadata for {os.path.basename(FILE_PATH)}
- **Description**: {DESCRIPTION}
- **Program**: `{PROGRAM_NAME}`
- **Headers**: `{headers}`
- **Predecessors**: {'\n-- '.join(PREDECESSORS_PATH)}
"""
        with open(meta_path, "w", encoding="utf-8") as f:
            f.write(metadata_content)
            
        print(f"[+] Metadata created: {meta_path}")
    except Exception as e:
        print(f"[!] Failed to create metadata: {e}")