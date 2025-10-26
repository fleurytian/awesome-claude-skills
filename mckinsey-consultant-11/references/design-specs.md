# McKinsey设计规范详解

McKinsey PPT的完整设计规范,基于mckinsey-ppt-v4。

## 配色方案

```python
PRIMARY_BLUE = RGBColor(0, 41, 96)      # #002960 深蓝
SECONDARY_BLUE = RGBColor(0, 101, 189)  # #0065BD 中蓝
LIGHT_BLUE = RGBColor(201, 240, 255)    # #C9F0FF 浅蓝
IKEA_YELLOW = RGBColor(255, 219, 0)     # #FFDB00 黄色
WHITE = RGBColor(255, 255, 255)         # #FFFFFF 白色
GRAY = RGBColor(128, 128, 128)          # #808080 灰色
```

**使用原则**:
- PRIMARY_BLUE: 主标题,表头,重要标注
- SECONDARY_BLUE: 图表主色,二级标题
- LIGHT_BLUE: 洞察框背景,辅助区域
- IKEA_YELLOW: 强调,警示,推荐标记
- WHITE: 深蓝背景上的文字
- GRAY: 次要信息,注释,来源

## 排版规范

```python
# 页面尺寸
SLIDE_WIDTH = 10.0 英寸
SLIDE_HEIGHT = 5.625 英寸  # 16:9

# 内容区域
CONTENT_LEFT = 0.8 英寸    # 左边距
CONTENT_WIDTH = 8.4 英寸   # 内容区宽度
CONTENT_TOP = 1.0 英寸     # 上边距(标题下)

# 字体规范
TITLE_FONT_SIZE = 18pt     # 页面标题
BODY_FONT_SIZE = 11pt      # 正文
CAPTION_FONT_SIZE = 9pt    # 注释/来源
MIN_FONT_SIZE = 7pt        # 最小字号
```

## 强制规则 ⚠️

### 规则1: 深蓝背景必配白色文字

**场景**:
- 表格表头
- 洞察框标题
- 突出显示区域
- 序号标签

**代码**:
```python
if bgColor == PRIMARY_BLUE or bgColor == SECONDARY_BLUE:
    textColor = WHITE
```

**检查点**:
- 表头文字是否为白色
- 深蓝洞察框内文字是否为白色
- 序号圆圈内数字是否为白色

### 规则2: 大文本框用直角矩形

**原则**: McKinsey追求严谨专业,大文本框必须用直角

**适用**:
- 标题框(宽度>3英寸)
- 正文内容框
- 数据分析框
- 洞察总结框

**代码**:
```python
if width > 3.0:
    shape_type = MSO_SHAPE.RECTANGLE  # 直角
else:
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE  # 可用圆角
```

**例外**: 小标签(<1.5英寸)可用圆角

### 规则3: 默认无边框

**原则**: 极简主义,无边框是常态

**无边框元素**:
- 所有文本框
- 数据标注
- 图表标签
- 页脚信息

**代码**:
```python
shape.line.fill.background()  # 去除边框
```

**有边框元素**(例外):
- 表格(分隔单元格)
- 强调框(突出重要性)
- 洞察框(明确边界)

### 规则4: 论点式标题

每页标题必须是**完整论点**,而非话题。

**错误示例**:
- "市场分析"
- "竞争格局"
- "用户数据"

**正确示例**:
- "有声书和在线课程驱动市场增长,传统播客仅占5%"
- "特来电/星星充电占据半壁江山,格局未固化"
- "在线课程单用户价值是有声书的3倍"

### 规则5: 高信息密度

**原则**: 充分利用空间,但避免拥挤

**密度阈值**:
```python
density = textLength / (width * height)
safe: <50 字符/平方英寸
warning: 50-70 字符/平方英寸
critical: >70 字符/平方英寸  # 需要拆分页面
```

**解决方案**:
- 缩小字号(最小7pt)
- 增加容器高度
- 精简文字
- 拆分为2-3页

## 质量检查清单

生成后必检:
```
□ 深蓝背景文字为白色
□ 表头文字为白色
□ 大文本框用直角矩形
□ 无元素遮挡/重叠
□ 无文字溢出
□ 图表标签完整显示
□ 时间轴/图表宽度一致
□ 无不必要边框
□ 单页密度<70字符/平方英寸
□ 标题是论点而非话题
```

---

## 信息密度标准 ⭐ 学习mckinsey-ppt-v4

### McKinsey追求高信息密度

**核心理念**: 每平方英寸都有价值,充分利用空间

**密度计算**:
```python
density = textLength / (width * height)

# 密度标准
optimal: 50-70 字符/平方英寸   # McKinsey标准
acceptable: 40-50 字符/平方英寸
warning: <40 字符/平方英寸     # 太空旷
critical: >80 字符/平方英寸    # 太拥挤,需拆分
```

### 提升信息密度的方法

#### 方法1: 增加数据标注

**Before** (密度35):
```
柱状图显示市场规模
无具体数字标注
```

**After** (密度58):
```
柱状图 + 每柱顶部标注具体数值
+ 增长率标注
+ 关键年份特殊标记
```

#### 方法2: 添加洞察框

**原则**: 空白区域添加小洞察框

```python
# 检测空白区域
if (emptySpace > 2 square inches):
    addInsightBox({
        position: 'right',
        width: 2.5,
        height: 1.2,
        content: '关键洞察点'
    })
```

#### 方法3: 扩展图例

**Before**:
```
简单图例: ■ 类别A  ■ 类别B
```

**After**:
```
详细图例:
■ 类别A (45.2亿元, 占比32%)
■ 类别B (67.8亿元, 占比48%)
+ 趋势说明
```

#### 方法4: 缩小字号释放空间

```python
if (fontSize == 9pt && density < 45):
    fontSize = 8pt  # 缩小1pt
    # 空间增加12%,可放更多内容
```

#### 方法5: 扩大图表

**原则**: 图表不是装饰,要占主要空间

```python
# Before: 图表占40%
chartHeight = 1.8 inches

# After: 图表占60-70%
chartHeight = 2.5 inches
# 可显示更多数据系列/维度
```

### McKinsey页面典型布局

#### 高密度数据页 (密度65)

```
┌─────────────────────────────────────┐
│ 有声书驱动增长,在线课程客单价高3倍  │ ← 论点式标题(18pt)
├─────────────────────────────────────┤
│         ┌─────────────────────┐     │
│ 2019    │ 45.2亿 │ 12.3亿    │     │
│ 2020    │ 82.1亿 │ 23.5亿    │     │ ← 时间轴+数据标注
│ 2021    │ 134.5亿│ 45.2亿    │     │
│ 2022    │ 189.3亿│ 78.9亿    │     │
│ 2023    │ 256.7亿│ 123.4亿   │     │
│         └─────────────────────┘     │
│                                     │
│ ┌──────────────┬──────────────┐    │
│ │ 有声书占比   │ 在线课程占比 │    │
│ │ 67.5%        │ 32.5%        │    │ ← 对比数据
│ └──────────────┴──────────────┘    │
│                                     │
│ ┌─────────────────────────────┐   │
│ │ 💡 洞察                      │   │
│ │ 虽然有声书规模大,但在线课程 │   │ ← 洞察框
│ │ 单用户价值是有声书的3倍      │   │
│ └─────────────────────────────┘   │
│                                     │
│ 来源: 艾瑞咨询2024  8pt gray      │ ← 来源
└─────────────────────────────────────┘

总字符: ~380
总面积: 6.5 平方英寸
密度: 58 字符/平方英寸 ✓
```

### 常见"空旷"问题

#### 问题1: 图表太小

**表现**: 图表只占页面30%,大片空白

**修复**:
```python
# Before
chartHeight = 1.5 inches  # 太小

# After
chartHeight = 2.5 inches  # 占60-70%空间
# 可以显示更多系列/标注
```

#### 问题2: 缺少数据标注

**表现**: 柱状图/折线图无具体数值

**修复**:
```python
for dataPoint in chart:
    addLabel({
        text: dataPoint.value,
        fontSize: 8,
        position: 'above'
    })
```

#### 问题3: 未利用空白区域

**表现**: 右侧/底部大片空白

**修复**:
```python
if (rightEmptySpace > 2.0):
    addInsightBox(rightSide)
if (bottomEmptySpace > 1.5):
    addDataTable(bottom)
```

### 密度检查清单

生成后检查:
```
□ 每页密度40-70字符/平方英寸
□ 图表占页面60-70%空间
□ 关键数据点有标注
□ 空白区域<20%
□ 洞察框突出要点
□ 图例信息完整
□ 无"空旷感"
```

### 特殊页面密度标准

```javascript
const DENSITY_BY_PAGE_TYPE = {
  coverPage: {
    density: 'low (10-20)',
    reason: '封面追求简洁大气'
  },
  
  contentPage: {
    density: 'high (50-70)',
    reason: '正文页信息密集'
  },
  
  summaryPage: {
    density: 'medium (35-50)',
    reason: '总结页突出关键点'
  },
  
  actionPage: {
    density: 'medium-high (45-60)',
    reason: '行动页清晰但完整'
  }
};
```
