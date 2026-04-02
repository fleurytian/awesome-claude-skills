# McKinsey PPT V4 快速参考

## 核心原则
1. **Storyline驱动** - 标题即论点
2. **三层架构** - 20pt/11pt/8pt
3. **So What原则** - 数据→洞察→行动
4. **直角矩形** - 大框不用圆角
5. **无边框** - 简洁是美德

## 配色速查
```
PRIMARY_BLUE   = #002960  深蓝（标题、强调）
SECONDARY_BLUE = #0065BD  中蓝（数据、图表）
LIGHT_BLUE     = #C9F0FF  浅蓝（背景、洞察框）
IKEA_YELLOW    = #FFDB00  黄色（极度强调）
GRAY           = #808080  灰色（注释）
LIGHT_GRAY     = #F5F5F5  浅灰（背景）
WHITE          = #FFFFFF  白色（深色背景文字）
```

## 形状速查
```python
# 大内容框 - 直角矩形，无边框
MSO_SHAPE.RECTANGLE + line.fill.background()

# 小标签 - 可用圆角
MSO_SHAPE.ROUNDED_RECTANGLE (宽<1.5英寸)

# 洞察框 - 直角+功能性边框
MSO_SHAPE.RECTANGLE + 1.5pt边框
```

## 强制规则 ⭐
```python
# 1. 深蓝背景 → 白色文字
if background == PRIMARY_BLUE:
    textColor = WHITE

# 2. 大文本框 → 直角矩形
if width > 3 inches:
    shape = MSO_SHAPE.RECTANGLE

# 3. 默认无边框
shape.line.fill.background()
```

## 迭代流程
```
第1轮: 快速生成（10分钟）
第2轮: 问题识别（5分钟）
第3轮: 批量修复（8分钟）
第4轮: 内容拆分（6分钟）
第5轮: 细节打磨（5分钟）
```

## 常见问题修复
1. **文字看不见** → 检查背景色，改文字为白色
2. **元素遮挡** → 删除重建，不要微调
3. **文字溢出** → 缩小字号8pt + 增加高度30%
4. **页面太拥挤** → 拆分为2-3页
5. **大框用圆角** → 改为直角矩形
6. **到处是边框** → 批量去除
