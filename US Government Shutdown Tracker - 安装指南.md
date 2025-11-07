# US Government Shutdown Tracker - 安装指南

## 📦 Skill源文件安装方法

### 方法1: 通过Claude界面上传(推荐)

1. **解压ZIP文件**
   - 解压 `us-gov-shutdown-tracker.zip`
   - 你会得到 `us-gov-shutdown-tracker/` 文件夹

2. **压缩为skill格式**
   - 将整个 `us-gov-shutdown-tracker/` 文件夹
   - 重新压缩为 `.zip` 格式
   - 将扩展名改为 `.skill`
   - 例如: `us-gov-shutdown-tracker.skill`

3. **上传到Claude**
   - 打开Claude设置 → Skills
   - 点击 "Upload Skill"
   - 选择 `.skill` 文件上传
   - 启用该skill

### 方法2: 手动打包(如果方法1不work)

运行包内的打包脚本:

```bash
# 如果你在Linux/Mac环境
cd /path/to/us-gov-shutdown-tracker
zip -r ../us-gov-shutdown-tracker.skill ./*

# 然后上传生成的 us-gov-shutdown-tracker.skill 文件
```

---

## 📁 文件结构说明

```
us-gov-shutdown-tracker/
├── SKILL.md                          # Skill主配置文件(必需)
├── scripts/                          # 分析脚本
│   ├── analyze_shutdown.py          # 数据获取和分析
│   └── visualize.py                 # 图表生成
└── references/                       # 参考文档
    ├── historical_cases.md          # 历史案例对比(2013/2018/2025)
    └── data_sources.md              # FRED API技术文档
```

**重要**: 不要修改文件结构,Claude需要按这个结构来读取文件。

---

## 🚀 安装后使用

### 第一次使用

安装完成后,直接对话:

```
"分析最新的政府停摆流动性情况"
```

Claude会:
1. 自动从FRED API获取数据
2. 运行分析脚本
3. 生成中文报告
4. 生成英文图表

### 验证安装

如果skill正确安装,当你提到以下关键词时skill会自动触发:
- "政府停摆"
- "TGA"
- "SOFR溢价"
- "流动性压力"
- "变相加息"

---

## 🔍 故障排除

### 问题1: Skill没有触发

**原因**: Description可能没有正确加载

**解决**:
1. 检查 `SKILL.md` 文件是否完整
2. 重新上传skill
3. 确认skill已启用

### 问题2: 脚本执行失败

**原因**: Python依赖缺失

**解决**:
Skill会自动安装依赖,如果失败,手动安装:
```bash
pip install requests pandas matplotlib --break-system-packages
```

### 问题3: 数据获取失败

**原因**: FRED API连接问题

**解决**:
1. 检查网络连接
2. FRED API偶尔有短暂故障,稍后重试
3. API密钥已内置在脚本中,无需配置

---

## 📊 配套文档说明

ZIP包中还包含:

- **README.md** - 快速开始指南
- **停摆流动性分析报告.md** - 最新分析报告示例(中文)
- **shutdown_2025_analysis.png** - 可视化图表示例(英文)

这些是演示文档,不影响skill功能。

---

## ⚙️ 高级配置(可选)

### 修改默认日期

编辑 `scripts/analyze_shutdown.py`:

```python
# 第109行附近
if start_date is None:
    start_date = "2025-10-01"  # 改为你想要的日期
```

### 修改API密钥

如果FRED API密钥失效,编辑 `scripts/analyze_shutdown.py`:

```python
# 第14行
API_KEY = "你的新密钥"
```

获取免费密钥: https://fred.stlouisfed.org/docs/api/api_key.html

---

## 📅 建议使用频率

**每周三晚上或周四早上**

原因: TGA和银行准备金数据每周三发布。在数据更新后运行分析可获得最新结果。

---

## 🎯 快速测试

安装后立即测试:

```
对Claude说: "帮我分析2025年10月1日的政府停摆流动性影响"
```

期望输出:
- 流动性状态判断(EASING/TIGHTENING/STABLE/MIXED)
- 关键指标表格
- 时间线分析
- 可视化图表
- 中文结论

---

## 💡 提示

1. **首次运行可能较慢** (需要下载数据和安装依赖)
2. **后续运行很快** (约10-15秒)
3. **图表是英文** (专业金融标准)
4. **分析报告是中文** (便于理解)

---

## 📞 需要帮助?

查看完整文档:
- `README.md` - 功能概览
- `references/historical_cases.md` - 历史案例详解
- `references/data_sources.md` - 数据源技术文档

---

**安装完成后你就可以用一句话获得专业的停摆流动性分析了!** 🚀
