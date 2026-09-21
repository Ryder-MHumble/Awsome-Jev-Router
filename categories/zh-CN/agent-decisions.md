# 代理决策

**语言 / Language:** 中文（当前） · [English](../agent-decisions.md)

对于 Jev 在代理循环内提供决策步骤的程序，请使用此类别 - 工具选择、升级、重试或停止、下一步操作选择。

## 提交格式
```md
- [Name](URL) - Industry: one-sentence description of the Jev use case.
```
## 条目

- [jev-social](https://github.com/socai-io/jev-social) - 社交媒体研究：在每一步使用 Jev `Choice` 来选择具体的 socai CLI 操作以及在 Instagram、TikTok 或 LinkedIn 上观察到的帖子或个人资料目标，在执行前拒绝格式错误或低可信度的决策。

- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - 浏览器自动化：浏览器使用的超快代理，Jev 决定要单击的每个下一个操作和元素，仅在必须键入文本时调用语言模型。
- [jev-agent-browser](https://github.com/forvela/jev-agent-browser) - 浏览器代理：父代理将有界任务委托给 Jev 循环，该循环选择键入的浏览器操作，通过代理浏览器验证它们，并将不明确或卡住的状态升级回父代理。
- [pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev) - 编码代理：将 System One 判断公开为五个 Pi 工具，以便模型做出狭隘的语义判断，同时代码和用户保持对阈值、权重和操作的控制。
- [jev-judgment](https://github.com/HyunjunJeon/jev-judgment) - 编码代理：代理技能，将封闭的编码代理判断发送给 Jev，以便判决保持键入、廉价且在运行中具有可比性。
- [limpet](https://github.com/noplan-inc/limpet) - 编码代理：通过使用 Jev 判断简单语言完成规则来阻止代理过早完成的钩子。
- [robo-harness](https://github.com/grmkris/robo-harness) - 机器人技术：SO-101 手臂工作台，Jev 决策运行程序在支出预算下从键入的候选操作中选择有界联合步骤。
- [dsh-auto-mode](https://git.allen-software.com/allenh1/dsh-auto-mode) - 编码代理：DeepSeek Harness 权限预设，其结束提示步骤让 Jev 回答代理在最终消息中留下的未决问题，仅当选择清除 0.6 置信度且自主安全 Noul 清除 0.5 时才将它们引导回去，否则将轮流返回给人类。
- [augustus](https://github.com/24601/Augustus) - 编码智能体：将选择、得分和 Noul 映射到经典方法上的智能体技能，以便智能体可以在软件中进行类型化判断，包括组合代数、问题设计诊断和需要伪造实验的验证门。
- [yoshi](https://github.com/compozy/yoshi) - 上下文管理：Claude Code 和 Codex 的代理，其中 Jev 在修剪之前判断仍需要哪些对话历史记录。
- [pi-jev (TheoOliveira)](https://github.com/TheoOliveira/pi-jev) - 编码代理：Pi 编码代理的语义工具路由和类型化系统一决策。
- [pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask) - 编码代理：为 Pi 代理提供一个安静的 Jev 决策层，用于判断，否则它将交给聊天模型。
- [fastbrowse](https://github.com/agent-labs-dev/fastbrowse) - 浏览器代理：当法学硕士阅读和计划时，Jev 从页面上的内容中选择每个操作。
- [super-jev](https://github.com/Kevthetech143/super-jev) - 决策工具：将 Jev 答案转换为有界操作，而不是让调用者自行解释。
- [jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers) - 用于 AI 编码代理的系统软件开发框架，通过 TypeSafe Jev System One 类型决策、零幻觉包审查和完成门进行升级。
- [Jev Browser](https://github.com/jkudish/jev-browser) - 浏览器自动化：由 Jev 决定每一步来驱动浏览器，与 LLM 驱动的浏览一样快速且非常便宜。
- [pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction) - 上下文管理：Pi 扩展，可逐字保留对话文本，同时使用 Jev 修剪陈旧的工具历史记录，仅当修剪无法释放足够的空间时才返回到 Pi 自己的摘要。
- [Atomic](https://github.com/bastani-inc/atomic) - 编码代理运行时：提供一流的 Jev 结构化输出提供程序，以便代理的决策通过与其其他提供程序相同的决策解析器返回类型。
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - 上下文管理：Claude 代码插件，用 Jev 决策替换压缩摘要，对每个工具调用和结果进行评分，以确定是否仍然需要它，而不是总结会话。
- [fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction) - 上下文管理：Jev 引导压缩思想的 Codex 端口，围绕会话压缩逐字恢复上下文，而不是对其进行总结。
- [public-browser](https://github.com/Silbercue/public-browser) - 浏览器控制：让 Claude Code 和 Cursor 驱动真正的 Chrome 配置文件，并使用 Jev 循环决定操作，报告令牌减少了大约 30%，成本降低了 25%。
- [pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router) - 编码代理：通过类型化的 Jev 决策来路由 Pi 的工作。
- [wakegate](https://github.com/shitianfang/wakegate) - 长时间运行的代理：在定时器或传入事件上恢复睡眠代理的 LLM 之前，Jev 根据代理自己的睡眠注释回答 `Choice`（唤醒，尚未，不相关），并且代码仅在唤醒低于 0.2 时跳过唤醒，而始终在用户消息、裸定时器、跳过限制、错误和超时时唤醒；一次运行通过了 21 个手写场景中的 21 个，自述文件将其称为冒烟测试而不是基准测试。
- [BrowserClaw](https://github.com/GoldenLoaf24h/browserclaw) - 浏览器自动化：零锁定、会话保留 Chrome MCP 服务器，将本地 Jev System One 语义微循环 (`chrome_act_toward_goal`) 与 85% 以上修剪的 DOM 树（Shadow DOM 和 iframe 穿透）结合起来，在活动登录会话上分派本机 CDP 事件 (`isTrusted: true`)，而不会窃取焦点。
- [jev-canvas](https://github.com/gaborishka/jev-canvas) - 多模式 UI：通过语音在 tldraw 画布上绘图，同时指向网络摄像头跟踪的手指；在每一份部分记录中，Jev 都会回答 8 个键入的问题（是否是命令、句子是否完整、动作、形状、颜色、目标、地点、大小），并用明码通过阈值（英语和乌克兰语）对它们进行门控，每个决策需要 300-550 毫秒。
- [jev-belay](https://github.com/valentynkit/jev-belay) - 编码代理：Claude Code Stop 钩子，读取记录作为证据，并仅在文件发生更改而没有通过检查时才调用一个包含四个问题的 Jev 调用，因任何错误而无法打开。
- [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) - 浏览器自动化：Jev Ultrafast 的非官方 Chrome 扩展端口，其中 Jev `Choice` 每一步都会选择操作和 DOM 元素，并且两次 `Noul` 检查（目标达到、卡住）否决过早的“完成”或“阻止”，仅在必须键入文本时才使用小文本模型。
- [jev-pruner](https://github.com/tamaratran/jev-pruner) - 上下文管理：Claude 代码插件，可在模型看到之前用 Jev 修剪长 Bash 输出，从而将终端噪音排除在外。
- [jev-desktop](https://github.com/yikangy873-gif/jev-desktop) - 计算机使用：在 Codex Computer Use 中提供 Jev 操作选择，在桌面操作中进行选择，而不是在每一步询问语言模型。
- [jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill) - 开发人员工具：Claude Code/ZCode 技能，通过 OpenCode Zen 的免费层将分类/路由、批处理筛选、评分和合规性检查判断卸载给 Jev，捆绑零依赖 jev.py 调用程序（transient-500 重试、WAF 安全 UA、GBK 管道安全标准输入）和生产淘宝店评论分类管道，使原始项目脱离代理上下文。
- [Yappy](https://yappy.biz/jev/) - 计算机使用：macOS 语音代理在前窗口的可访问性表中每​​一步（操作和目标控制）向 Jev 询问一个 `Choice`，仅执行经过验证的高置信度答案，并在低置信度、无效操作或未知字段值时升级为完整的 LLM 代理；作者报告每个决策需要 275–690 毫秒。
