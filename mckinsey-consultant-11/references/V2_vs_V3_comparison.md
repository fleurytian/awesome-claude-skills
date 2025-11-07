# McKinsey Consultant V2 → V3 架构升级说明

## 🎯 核心问题

**V2.0存在的上下文消耗问题**:
- SKILL.md包含1130行完整文档(~30KB)
- Claude一次性加载所有内容到上下文
- 生成10-15页PPT后上下文接近饱和
- 大型项目(20-25页)需要频繁切换对话

## 💡 V3.0解决方案: Progressive Disclosure (渐进式披露)

### 核心理念
```
最小核心 + 按需加载 = 节省上下文
```

### 架构对比

| 维度 | V2.0 | V3.0 |
|------|------|------|
| **SKILL.md大小** | 1130行 (~30KB) | ~300行 (~8KB) |
| **加载方式** | 一次性全部加载 | 按需渐进式加载 |
| **上下文消耗** | 高 (100%) | 低 (~30%) |
| **稳定生成页数** | 10-15页 | 20-25页 |
| **references处理** | 预加载全部 | 用时才file_read |

## 📊 详细对比

### V2.0工作流
```
启动
  ↓
加载完整SKILL.md (1130行)
  ↓
[上下文已消耗30%]
  ↓
执行STEP 1-5
  ↓
[上下文已消耗50%]
  ↓
STEP 6-7: 生成第1-10页
  ↓
[上下文已消耗90%]
  ↓
第11页开始出现质量问题
  ↓
需要切换新对话
```

### V3.0工作流
```
启动
  ↓
加载精简SKILL.md (~300行)
  ↓
[上下文消耗10%]
  ↓
STEP 1: 直接执行
  ↓
STEP 2-3: 临时加载methodology.md → 用完释放
  ↓
[上下文消耗20%]
  ↓
STEP 4-5: 临时加载layouts.md + design-specs.md → 用完释放
  ↓
[上下文消耗30%]
  ↓
STEP 6-7: 临时加载excel-data-spec.md
           逐页处理(每次只保留当前页的5个搜索结果)
  ↓
第1页: 搜索→生成→清空
第2页: 搜索→生成→清空
...
第20页: 搜索→生成→清空
  ↓
[上下文消耗60%]
  ↓
可稳定完成20-25页
```

## 🔑 关键设计原则

### 1. 最小核心原则
**V2.0**:
```markdown
SKILL.md包含:
- 完整方法论说明
- 详细执行步骤
- 所有设计规范
- Excel规范
- 问题排查
- 案例参考
= 1130行全文
```

**V3.0**:
```markdown
SKILL.md只包含:
- 触发逻辑
- 工作流总览
- 执行框架
- Reference索引
- 何时加载哪个文件
= ~300行核心导航
```

### 2. 按需加载原则 (Lazy Loading)

**V2.0**:
```python
# 启动时
load_everything()  # 一次性加载所有内容
```

**V3.0**:
```python
# 启动时
load_core_only()  # 只加载SKILL.md核心

# 执行时
if step == "2-3":
    file_read("methodology.md")
    use_it()
    release_from_context()  # 用完释放

if step == "4-5":
    file_read("layouts.md")
    file_read("design-specs.md")
    use_them()
    release_from_context()

if step == "6-7":
    file_read("excel-data-spec.md")
    for each_page:
        search_data()  # 最多5次
        generate_page()
        clear_search_results()  # 每页清空
```

### 3. 逐页处理原则

**V2.0可能的问题**:
```python
# 如果不小心一次性处理多页
search_all_pages()  # 15页 × 5次搜索 = 75个搜索结果
# 上下文爆炸!
```

**V3.0强制逐页**:
```python
for page in pages:
    # 每页独立循环
    search_current_page()  # 最多5个结果
    generate_current_page()
    clear_context()  # 清空当前页数据
    # 继续下一页时上下文重置
```

## 📁 文件结构变化

### V2.0结构
```
mckinsey-consultant/
├── SKILL.md (1130行，包含一切)
└── references/
    ├── methodology.md (作为备用参考)
    ├── layouts.md
    └── ... (Claude不会主动读取)
```

### V3.0结构
```
mckinsey-consultant/
├── SKILL.md (300行，导航地图)
│   ├── 触发逻辑
│   ├── 工作流框架
│   ├── 何时加载哪个reference
│   └── 上下文优化策略
└── references/
    ├── methodology.md ← STEP 2-3时file_read
    ├── layouts.md ← STEP 4-5时file_read
    ├── design-specs.md ← STEP 4-5时file_read
    ├── excel-data-spec.md ← STEP 6时file_read
    ├── delivery-summary.md ← STEP 8需要时file_read
    ├── troubleshooting.md ← STEP 9问题时file_read
    ├── quick-guide.md ← 用户询问时file_read
    └── workflow.md ← 用户要求时file_read
```

## 🎯 上下文节省效果

### 计算示例 (生成20页PPT)

**V2.0上下文消耗**:
```
SKILL.md全文: ~10,000 tokens
STEP 1-5执行: ~5,000 tokens
STEP 6-7前10页: ~30,000 tokens
─────────────────────────
总计: ~45,000 tokens (已接近限制)
后10页: 质量下降或需要切换对话
```

**V3.0上下文消耗**:
```
SKILL.md核心: ~3,000 tokens
STEP 2-3 (临时加载methodology.md): ~1,500 tokens → 释放
STEP 4-5 (临时加载layouts + design): ~2,000 tokens → 释放
STEP 6 (临时加载excel-spec): ~1,000 tokens
STEP 6-7逐页 (每页5次搜索): 
  第1页: ~1,500 tokens → 清空
  第2页: ~1,500 tokens → 清空
  ...
  第20页: ~1,500 tokens → 清空
─────────────────────────
峰值消耗: ~8,000 tokens
总计可持续: 20-25页无压力
```

**节省**: ~70%+ 上下文消耗

## 🔄 迁移指南

### 对于现有用户

**V2.0 Dummy文件仍然兼容!**

V3.0的变化只在SKILL.md层面，Dummy.md格式完全不变，因此:

✅ **已有的Dummy文件可以直接在V3.0中使用**
✅ **已完成的项目可以用V3.0续写**
✅ **无需重新设计Dummy**

### 对于开发者

如果要基于此架构开发其他skill:

**核心原则**:
1. SKILL.md = 导航地图，不是百科全书
2. 详细内容放references/，按需file_read
3. 用完即释放，不常驻上下文
4. 大型循环必须分批处理

**实现模板**:
```markdown
# SKILL.md结构

## 核心触发逻辑
[何时启动]

## 工作流总览
[步骤框架]

## STEP 1
执行: [简要说明]
加载: 无

## STEP 2
执行: [简要说明]
加载: file_read(references/xxx.md)
释放: 用完后

## Reference索引
| 文件 | 用途 | 何时加载 |
```

## 📈 效果预测

### 用户体验改善

**V2.0典型对话**:
```
对话1: 完成STEP 1-5 + 前10页PPT
对话2: 继续第11-20页PPT (需要上传Dummy)
对话3: 优化修改
```

**V3.0典型对话**:
```
对话1: 完成STEP 1-5 + 全部20-25页PPT + 优化
```

### 稳定性提升

**V2.0**:
- 第10页后质量可能下降
- 需要频繁监控上下文
- 大项目必须拆分对话

**V3.0**:
- 20-25页稳定输出
- 上下文消耗可预测
- 减少70%+切换对话需求

## ✅ 总结

### V3.0的三大核心优势

1. **更轻量**: SKILL.md从1130行压缩到~300行
2. **更智能**: 按需加载，用完即释放
3. **更稳定**: 可稳定生成20-25页PPT

### 实现方式

- **导航地图**: SKILL.md只告诉Claude"去哪找什么"
- **渐进式披露**: 只在需要时file_read对应文档
- **逐页循环**: 强制分批处理，避免上下文爆炸

### 向后兼容

- ✅ 已有Dummy文件完全兼容
- ✅ 工作流程完全一致
- ✅ 用户使用体验无变化
- ✅ 只是内部架构优化

---

**版本**: V3.0 Progressive Disclosure Architecture
**日期**: 2025-10-26
**作者**: Qianru Tian
