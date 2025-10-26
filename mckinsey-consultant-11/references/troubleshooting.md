# 常见问题解决

基于mckinsey-ppt-v4实战经验总结的常见问题和解决方案。

## 问题1: 深蓝背景深蓝文字看不见

**表现**: 表头/洞察框/序号标签文字不可见

**原因**: 未强制设置白色文字

**解决**:
```python
# 生成后执行强制检查
for shape in slide.shapes:
    if shape.fill.type == 1:
        bg = shape.fill.fore_color.rgb
        if bg == PRIMARY_BLUE or bg == SECONDARY_BLUE:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    run.font.color.rgb = WHITE
```

## 问题2: 元素遮挡/重叠

**表现**: 标题框与内容框重叠,图表被文本遮挡

**原因**: 未预留充足间距

**解决**: 删除所有元素,从零重建布局
1. 删除页面所有形状
2. 规划布局(上→下,左→右)
3. 预留间距(至少0.2英寸)
4. 验证无遮挡

## 问题3: 文字溢出

**表现**: 文本框内容显示不全

**原因**: 文本框太小或字号太大

**解决**:
```python
# 策略1: 缩小字号(9pt→8pt)
# 策略2: 扩大容器(height * 1.3)
# 策略3: 精简文字
# 策略4: 拆分为2页
```

## 问题4: 柱状图标签第二行不显示

**表现**: 横轴标签只显示第一行

**原因**: 标签容器高度不足

**解决**:
```python
labelBox = createTextBox({
    height: 0.35  # 增加到0.35英寸(原0.25)
})
# 第一行: 主标签(10pt bold)
# 第二行: 副标签(7pt gray)
```

## 问题5: 时间轴与图表宽度不一致

**表现**: 看起来不协调

**原因**: 各元素独立设置宽度

**解决**:
```python
const CONTENT_WIDTH = 8.4  # 统一宽度
timeline.width = CONTENT_WIDTH
chart.width = CONTENT_WIDTH
```

## 问题6: 内容密度过高

**表现**: 单页挤了10+要点,拥挤

**原因**: 未考虑认知负荷

**解决**: 拆分为2-3页
- 原则: 复杂内容分页展示
- 好处: 每页更聚焦,阅读更舒适

## 问题7: 使用了圆角矩形

**表现**: 大文本框用圆角,不够专业

**原因**: 未遵循McKinsey风格

**解决**:
- 大文本框(>3英寸): MSO_SHAPE.RECTANGLE
- 小标签(<1.5英寸): 可用ROUNDED_RECTANGLE

## 迭代优化流程

**Round 1**: 生成初版(求快)
**Round 2**: 用户标注问题
**Round 3**: Claude针对性修复
**Round 4**: 内容拆分(如需要)
**Round 5**: 细节打磨

**总耗时**: 2-4轮,20-40分钟
