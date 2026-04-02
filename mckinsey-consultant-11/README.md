# McKinsey Consultant V4.0

McKinsey顾问式商业问题解决系统，集成 mckinsey-ppt-v4 迭代式精修方法论。

## 简介

将McKinsey Problem Solving 101/102方法论系统化为8步工作流,实现从商业问题到McKinsey风格PPT的端到端解决方案。V4.0 集成了 mckinsey-ppt-v4 的PPT生成和迭代优化能力。

## 核心能力

- **Phase 1: Hypotheses Tree** - 问题定义 + MECE拆解 + 假设驱动
- **Phase 2: Dummy Pages** - 论证方式设计 + McKinsey页面布局 + 页面依赖标注
- **Phase 3: Data & Generation** - 智能数据收集 + 专业PPT生成 + **V4迭代式精修**

## V4.0 新增 (来自 mckinsey-ppt-v4)

- **迭代式优化工作流**: 5轮迭代(初稿→识别→修复→拆分→打磨)，从85分到95分
- **6类问题解决方案**: 布局遮挡/文字溢出/颜色对比度/图表标签/边框圆角/比例协调
- **McKinsey设计铁律**: 深蓝背景强制白字、大文本框直角矩形、无边框为常态
- **质量双重检查**: 生成时检查 + 生成后全面检查
- **Python-pptx工具库**: 颜色对比度自动修复、文字溢出检测、批量检查函数

## 快速开始

```
"请使用mckinsey-consultant skill,
帮我分析中国XX市场的增长情况和机会"
```

## 时间效率

- **总耗时**: 90-110分钟
- **vs传统**: 节省95%时间(3-5天→2小时)
- **输出质量**: 95分McKinsey专业级 (V4迭代后)

## 文件结构

```
mckinsey-consultant-11/
├── SKILL.md                           # 主skill (渐进式披露导航)
├── README.md
├── LICENSE
├── references/
│   ├── methodology.md                 # MECE/Issue Tree/Hypotheses
│   ├── layouts.md                     # 7种McKinsey页面布局
│   ├── design-specs.md                # 配色/字号/信息密度
│   ├── page-dependencies.md           # 页面依赖关系标注
│   ├── excel-data-spec.md             # Excel数据规范
│   ├── ppt-v4-specs.md                # ⭐ PPT V4完整生成规范
│   ├── ppt-v4-config.yaml             # ⭐ PPT配色/字号/布局参数
│   ├── ppt-v4-checklist.md            # ⭐ PPT V4质量检查清单
│   ├── ppt-v4-quickref.md             # ⭐ PPT V4快速参考
│   ├── ppt-v4-changelog.md            # ⭐ PPT V4变更日志
│   ├── delivery-summary.md            # Word报告格式
│   ├── troubleshooting.md             # 问题排查
│   ├── quick-guide.md                 # 快速入门
│   ├── workflow.md                    # 详细流程图
│   ├── examples.md                    # 案例参考
│   └── V2_vs_V3_comparison.md         # 版本对比
└── examples/
    └── basic_usage.py                 # ⭐ Python-pptx示例代码
```

## 方法论基础

- McKinsey Problem Solving 101/102
- MECE原则
- 金字塔原理
- mckinsey-ppt-v4 迭代式精修方法论 (已集成)

## License

MIT
