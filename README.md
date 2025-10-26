# Claude Skills by Fleury

<div align="center">

[![Author](https://img.shields.io/badge/Author-Fleury-blue)](https://github.com/fleurytian)
[![小红书](https://img.shields.io/badge/小红书-@如宝｜AI&Analytics-red)](https://www.xiaohongshu.com/user/profile/56d1a32184edcd71a06dcc55?xsec_token=ABZohenXDHnRbNau0jBvZWdjPAZ3gXdQw3bGs0cbzgNms%3D&xsec_source=pc_search)
[![Email](https://img.shields.io/badge/Email-fleurytian@gmail.com-green)](mailto:fleurytian@gmail.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

精选高质量Claude Skills集合 | 专注商业分析与内容创作

</div>

---

## 📚 Skills 目录

### 1️⃣ McKinsey Consultant Skill
**McKinsey顾问式商业问题解决系统**

一个将McKinsey Problem Solving 101/102方法论系统化为完整工作流的Claude Skill,实现从商业问题到专业PPT的端到端解决方案。

#### ✨ 核心能力

- **Phase 1: Hypotheses Tree** 
  - 问题精准定义
  - MECE原则拆解
  - 假设驱动分析

- **Phase 2: Dummy Pages** 
  - 论证方式设计
  - McKinsey经典页面布局
  - 逻辑框架搭建

- **Phase 3: Data & Generation** 
  - 智能数据收集
  - 专业PPT自动生成
  - 迭代优化机制

#### 💡 开发者说

**✅ 核心优势**

1. **遵循咨询公司真实工作流**
   - Hypothesis-driven approach: 先提假设,再验证
   - Dummy-first: 先设计页面框架,再找数据填充
   - 符合McKinsey方法论的完整工作思路

2. **输出质量高**
   - Hypothesis结构MECE,逻辑严密
   - 页面样式丰富,支持多种McKinsey经典布局
   - 每个页面都有对应的数据来源和参考文献记录

3. **可追溯性强**
   - 自动记录每个论点的数据源
   - 便于审查和验证
   - 支持多次迭代优化

**⚠️ 局限性说明**

受限于当前模型能力,存在以下技术限制:

1. **上下文窗口限制**
   - 复杂项目容易超出上下文长度
   - 需要分段生成PPT (通过多次对话完成)
   - **解决方案**: 设计了Dummy Pages独立导出功能,可在新对话中复用

2. **假设验证机制待完善**
   - 当Hypothesis被证伪时,整个storyline可能不够solid
   - 目前缺少自动推翻storyline并重构的机制
   - **建议做法**: 人工review后重新调整hypothesis tree

#### 🎯 适用场景

- 市场机会分析
- 商业策略咨询
- 行业研究报告
- 投资决策支持
- 管理咨询项目

#### 🚀 快速开始

```
"请使用mckinsey-consultant skill,
帮我分析中国XX市场的增长情况和机会"
```

#### 📊 查看示例

仓库中提供了完整的示例输出:
- `mckinsey-sample-PPT.pptx` - 完整的McKinsey风格PPT示例

#### 📖 方法论基础

- McKinsey Problem Solving 101/102
- MECE原则 (Mutually Exclusive, Collectively Exhaustive)
- 金字塔原理 (Pyramid Principle)
- McKinsey设计规范

---

### 2️⃣ 咪蒙写作风格复刻 Skill
**10万+爆款文章创作指南**

完整复刻咪蒙的写作技巧与风格特征,帮助创作具有强情感共鸣和传播力的内容。

#### ✨ 核心技巧

**1. 标题制造 (决定80%点击率)**
- 7大标题公式 (反常识、对话式质问、反向节日等)
- 5大核心特征 (情绪冲击、违背常识、口语化等)
- 标题测试标准与自检清单

**2. 开篇设计 (前3段决定跳出率)**
- 5种黄金开头类型
- 三段黄金结构
- 快速抓住读者注意力

**3. 情绪调动**
- 完整情绪曲线设计
- 情绪爆发点制造技巧
- 情绪强化词库

**4. 故事叙事**
- 多线叙事结构
- 悬念设置与信息差
- 细节描写与五感调动

**5. 金句提炼**
- 4大金句创作公式
- 最佳使用位置
- 传播性打磨

**6. 结尾设计**
- 4种经典结尾类型
- 升华与行动召唤
- 避免常见误区

#### 💡 开发者说

**✅ 核心优势**

1. **金句犀利,视角独特**
   - 能够产出极具冲击力的标题和金句
   - 善于从意想不到的角度切入话题
   - 价值观输出明确,立场鲜明

2. **行文细腻丝滑**
   - 情绪调动自然流畅
   - 故事叙事张力十足
   - 能够引发强烈的情感共鸣

3. **技巧体系完整**
   - 涵盖从标题到结尾的完整创作流程
   - 15项自检清单确保质量
   - 案例拆解清晰易学

**⚠️ 使用建议**

1. **避免套路化**
   - 重复使用后容易形成明显的套路感
   - **建议**: 变换角度和主题,避免连续创作类似内容
   - 可结合自己的风格进行改编

2. **Bullet Point习惯待优化**
   - 当前版本输出时仍有bullet point偏多的倾向
   - 咪蒙原文更多使用自然段落而非列表
   - **建议**: 在prompt中明确要求"用段落形式,不要用bullet points"

3. **持续学习优化**
   - 可从咪蒙文集学习更多案例: http://120.26.97.111/%E5%92%AA%E8%92%99%E6%96%87%E7%AB%A0/
   - 将更多原文输入给Claude,帮助它更好地学习风格
   - 用实际案例纠正偏差

#### 🎯 适用场景

- ✅ 情感共鸣类文章 (友情/爱情/亲情)
- ✅ 社会现象评论 (借钱/婚姻/阶层)
- ✅ 女性话题讨论 (审美/独立/困境)
- ✅ 故事化叙事 (真人真事改编)
- ✅ 价值观输出 (正向但不鸡汤)

#### 🚀 快速开始

```
"请使用mimeng-writing skill,
帮我写一篇关于[主题]的爆款文章"
```

**优化Tip**: 如果发现输出使用了过多bullet points,可以这样说:
```
"请用咪蒙的风格重写,用自然的段落形式,
不要用列表或bullet points,要像在讲故事一样"
```

#### 📊 查看示例

仓库中提供了完整的示例输出:
- `mimeng-sample.md` - 咪蒙风格文章完整示例

#### 📖 写作技巧体系

- **10大痛点主题挖掘**
- **15项创作清单**
- **完整实战流程**
- **经典案例拆解**

---

## 🛠 如何使用

### 1. 安装到Claude

这些Skills需要在支持Skills功能的Claude环境中使用,官方教学:https://www.anthropic.com/news/skills

### 2. 在对话中激活

在对话开始时明确说明要使用哪个Skill:

```
"请使用mckinsey-consultant skill,帮我..."
```

或

```
"请使用mimeng-writing skill,帮我..."
```

---

## 📂 仓库结构

```
fleurysclaudeskills/
├── README.md                          # 本文件
├── mckinsey-sample-PPT.pptx          # McKinsey Skill示例输出
├── mimeng-sample.md                   # 咪蒙 Skill示例输出
├── mckinsey-consultant/
│   ├── SKILL.md                      # Skill主文件
│   ├── references/                    # 参考文档
│   │   ├── methodology.md            # 详细方法论
│   │   ├── layouts.md                # McKinsey页面布局
│   │   ├── design-specs.md           # 设计规范
│   │   ├── examples.md               # 完整案例
│   │   └── troubleshooting.md        # 常见问题
│   └── README.md                     # Skill说明
└── mimeng-writing/
    ├── SKILL.md                      # Skill主文件
    └── README.md                     # Skill说明
```

---

## 🎓 适合人群

### McKinsey Consultant Skill

- 管理咨询顾问
- 商业分析师
- 投资分析师
- 战略规划人员
- MBA学生
- 创业者

### 咪蒙写作风格复刻 Skill

- 内容创作者
- 公众号运营
- 小红书博主
- 自媒体从业者
- 文案策划
- 新媒体编辑

---

## 💡 创作理念

这些Skills的开发遵循以下原则:

1. **实战导向**: 基于真实场景和需求开发
2. **系统化**: 将复杂方法论结构化、可执行
3. **高质量**: 追求专业级输出标准
4. **高效率**: 大幅提升工作效率
5. **可迭代**: 持续优化和完善
6. **透明化**: 说明优势与局限,诚实呈现

---

## 📈 更新日志

### McKinsey Consultant
- ✅ v1.0: 完整的8步工作流实现
- ✅ v1.1: 新增Dummy Pages独立导出功能
- 🔄 规划中: Hypothesis自动验证与storyline重构机制

### 咪蒙写作
- ✅ v1.0: 完整的写作技巧体系
- 🔄 优化中: 减少bullet point使用,更贴近原文风格
- 📚 持续学习: 不断增加咪蒙文章案例库

---

## 🤝 贡献

欢迎提交Issue和Pull Request!

如果你:
- 发现了bug
- 有改进建议
- 想要贡献新的Skill
- 有更好的示例或文章资源

请随时联系我或提交PR。

---

## 📬 联系方式

- **GitHub**: [@fleurytian](https://github.com/fleurytian)
- **小红书**: @如宝｜AI&Analytics
- **Email**: fleurytian@gmail.com

---

## 🙏 致谢

感谢所有使用和支持这些Skills的朋友们!

特别感谢:
- McKinsey方法论的启发
- 咪蒙文章的创作灵感
- 所有提供反馈和建议的用户

---

## ⭐️ Star History

如果这个项目对你有帮助,欢迎给个Star⭐️!

---

## 📄 License

本项目采用 [MIT License](LICENSE) 开源协议。

---

<div align="center">

**Made with ❤️ by Fleury**

*让AI更懂商业,让内容更有温度*

</div>
