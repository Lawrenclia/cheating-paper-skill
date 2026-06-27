# 两页 Cheating Paper 生成 Skill

这是一个给 Codex 用的个人 skill，用来把课程笔记、PDF、PPT、粘贴文本、已有 LaTeX/Markdown 草稿，压缩成一份适合考试前快速检索的两页 A4 正反面速查表。

它是从“信息论四栏 cheating paper”的完整制作流程里提炼出来的，核心目标很明确：内容要密、公式要真、排版要稳，最后渲染出来的 PDF 必须正好两页。

## 适合用来做什么

- 根据课程笔记整理两页速查表 / 小抄 / cheating paper
- 从 PPT、PDF、讲义里提炼公式、定义、定理、证明骨架和易错点
- 生成四栏 A4 横版 LaTeX 速查表
- 处理公式很多的课程，比如信息论、概率论、物理、数学、信号系统等
- 对已有 `.tex` 速查表做压缩、补内容、修排版、验页数

## 这个 skill 的默认标准

- A4 横版
- 四栏排版
- 页面边距默认 `0.3cm`
- 栏间距默认 `0.05cm`
- 字号默认约 `6.5pt`
- 标题使用蓝色紧凑样式
- 公式使用真正的 LaTeX，不渲染成图片
- 重要图可以用 TikZ 或原 PPT 图片
- 最终 PDF 必须正好两页

## 安装

把这个仓库 clone 到 Codex skills 目录：

```bash
git clone https://github.com/Lawrenclia/cheating-paper-skill.git ~/.codex/skills/two-page-cheating-paper
```

或者如果你已经下载了本仓库：

```bash
mkdir -p ~/.codex/skills
cp -R cheating-paper-skill ~/.codex/skills/two-page-cheating-paper
```

## 使用方法

在 Codex 里直接提到这个 skill：

```text
$two-page-cheating-paper 根据这些笔记生成一份两页 A4 正反面速查表
```

也可以这样说：

```text
用 two-page-cheating-paper 这个 skill，把这个 PDF 和 PPT 整理成两页 cheating paper
```

它会按“先提炼内容，再写 LaTeX，再编译，再检查页数，再压缩/补内容”的流程来做。

## 从 LaTeX 模板开始

仓库里提供了一个可直接复制的模板：

```text
templates/two-page-cheating-paper.tex
```

推荐开局方式：

```bash
mkdir -p latex_build
cp templates/two-page-cheating-paper.tex latex_build/cheating-paper.tex
```

然后编辑：

```text
latex_build/cheating-paper.tex
```

模板已经包含：

- `ctexart`
- A4 横版四栏
- 极小边距
- 紧凑字号和行距
- 蓝色章节标题
- 图片插入宏
- TikZ 信道/图示卡片宏
- 两页内容骨架
- 页数检查提示

## 页数验证

编译出 PDF 后运行：

```bash
python3 scripts/check_pdf_pages.py path/to/output.pdf --expect 2
```

如果不是两页，脚本会返回错误。这个 skill 的原则是：没有通过两页检查，就不算完成。

## 文件说明

- `SKILL.md`  
  skill 的核心说明，包括触发场景、工作流程、内容压缩原则、交付标准。

- `references/layout-contract.md`  
  两页 LaTeX 速查表的排版契约，包括边距、栏距、字号、图片宏、图文卡片、压缩策略和视觉检查清单。

- `templates/two-page-cheating-paper.tex`  
  可直接复制使用的 XeLaTeX 模板。

- `scripts/check_pdf_pages.py`  
  PDF 页数检查脚本，默认要求输出正好两页。

- `agents/openai.yaml`  
  skill 在 Codex 里的显示名、简介和默认提示词。

## 内容压缩原则

这个 skill 生成 cheating paper 时会优先保留：

1. 定义和符号约定
2. 核心公式和 chain rule
3. 不等式、等号条件、适用条件
4. 定理结论和证明骨架
5. 算法步骤和判题套路
6. 标准例子、典型图、容量/公式表
7. 常见误区

长段解释会被压成“公式 + 条件 + 用法 + 陷阱”的格式。证明也尽量写成骨架，而不是整段散文。

## 两页压缩策略

如果 PDF 超过两页：

1. 先删重复内容
2. 把散文改成公式或规则片段
3. 合并相邻主题
4. 缩小大图
5. 删除低频例子或背景介绍
6. 微调段距、图距、行距
7. 最后才进一步降低字号

如果 PDF 不满两页：

1. 补高频定理
2. 补证明骨架
3. 补等号条件和适用条件
4. 补小图或典型例题模式

## 设计味道

这个 skill 的风格不是“写一份漂亮讲义”，而是“做一张考试时一眼能定位的纸”。所以它会更偏向：

- 密度高
- 公式优先
- 结构清晰
- 图只在真正省字或帮助理解时加入
- 所有内容都服务于考试检索
