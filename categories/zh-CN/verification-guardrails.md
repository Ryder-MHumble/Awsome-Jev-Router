# 验证和护栏

**语言 / Language:** 中文（当前） · [English](../verification-guardrails.md)

将此类别用于 Jev 控制输出的程序 — 验证声明、审查差异、检查生成的内容或在发布之前阻止不安全的代理操作。

## 提交格式

```md
- [Name](URL) - Industry: one-sentence description of the Jev use case.
```

## 条目

- [is-malicious](https://github.com/luantak/is-malicious) - 软件供应链安全：要求 Jev `Noul` 检查源文件和构建文件，升级可疑块以进行第二次传递，并在执行前返回涉及的文件和行。
- [jev-review](https://github.com/devagrawal09/jev-review) - 软件工程：分阶段代码审查工作流程和本地仪表板，Jev 在变更推进之前控制每个审查阶段。
- [pi-jev](https://github.com/y0usaf/pi-jev) - 代理安全：向 Pi 编码代理添加测量工具调用门，以便 Jev 在执行前检查有风险的调用。
- [OpenWork](https://github.com/different-ai/openwork) - 工程工作流程：将 Jev 作为验证法官连接到其评估测试套件中，因此代理生成的工作由键入的判决而不是文本模型来控制。
- [jev-guard](https://github.com/leepokai/jev-guard) - 代理安全：Claude Code、Codex、Pi 和 ACP 代理的提示注入和危险操作防护，由 Jev 决定阻止什么。
- [Foreman](https://github.com/thruwire/foreman) - 软件工厂：位于 Codex 工作人员之上，让 Jev 独立判断实施是否完成、测试是否充分或是否需要人工。
- [stanley-code](https://github.com/devagrawal09/stanley-code) - 编码代理：有界的 Jev 工作流程，使代理判断保持键入而不是自由形式。
- [opencompany](https://github.com/useopencompany/opencompany) - 代理工作区：通过 Jev 运行其批准审查，因此工作区操作由键入的决策控制。
- [jev-git](https://github.com/AkashPriyadarshii/jev-git) - 开发人员工具：亚秒级 Git 预提交和预推送反射门，使用 Jev 筛选分阶段的差异以获取秘密和破坏性命令。
- [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) - 运行时约束：根据用户实际要求检查来自 Pi 代理的每个副作用工具调用。
- [Hunch](https://github.com/Kelbie/hunch) - 代码审查：Jev 在本地或每个拉取请求上检查代码的简单英语规则，Jev 在每次发现时选择一个标签。
- [Abide](https://github.com/coldteadotai/abide) - 代理监督：读取编码代理所做的每一个编辑，并发现有违反 Jev 标记规则的情况，项目报告称，独立审阅者确认了 39 个标记编辑中的 10 个，以及 15 个标记轮次中的 11 个。
- [fx](https://github.com/vercel-labs/fx) - 编码代理：提供 `typesafe_permission_reviewer` 内置函数，因此代理的权限决策通过 Jev 而不是 LLM 调用运行。
- [Sniff Test](https://github.com/DanRWilloughby/snifftest) - 写作：散文 linter，每段向 Jev 提出 10 个 `Boolean` 问题（堆叠对冲、重述结束语、不是 X 但 Y 的转弯、裸成本数字），阈值为 0.7； CLI、预提交挂钩、GitHub Action 和 Claude Code 技能；测量中位数为 182 毫秒，54 个干净段落中有 1 个被标记为俳句 4.5 的 37 个段落。
- [jev-pref](https://github.com/doeixd/jev-pref) - 代码审查：将项目 AGENTS.md 中的首选项转换为 `jev-pref.json` 规则，Jev 检查每个 diff 块、暂存文件集或拉取请求，将 `fix_now` 或咨询结果返回给编码代理，并在阻止时返回非零退出代码。
- [jev-axi](https://github.com/shiftynick/jev-axi) - 代理安全：Claude Code 和 Codex 的 PreToolUse 门，Jev 对每个 shell 命令的破坏性、渗透、远程代码执行和安全削弱进行评分，在本地决定例行命令，因此不会发送任何内容，并在其存储库中的 44 个标记工具调用上得分 44/44。
- [pi-verdict](https://github.com/jesset/pi-verdict) - 代理安全：Pi 权限门，其中 Jev 对每个灰色区域工具调用回答一个选择（允许/询问/拒绝）——确定性规则首先解决明确的情况，拒绝块，询问升级到人工确​​认，错误或超时拒绝； Jev 是一个可选的实验性后端，可通过 OpenRouter 或 TypeSafe 的直接 API 访问。
- [jev-commit](https://github.com/valentynkit/jev-commit) - 开发人员工具：预提交挂钩，其中一个 Jev 调用判断提交消息是否与暂存的差异匹配，标记调试遗留问题和未提及的工作，并且仅在检测到的凭据上进行阻止。
- [Blink](https://blink.review) - 代码审查：编码代理在每次更改后运行的 CLI，Jev 几乎立即代替 LLM 审查者检查差异。
- [hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals) - 代理批准：概念验证，将 Jev 置于 Hermes 代理的命令批准之前，向用户报告决策速度提高 8.7 倍，提示数量减少 4.4 倍。
- [taste-lint](https://github.com/mblode/taste-lint) - 编写/UI：CLI，使用 Jev 概率进行语义品味检查，以在发货前捕获 UI、复制和代理指令中的 AI 错误；可衡量的规则保留在本地，活跃的发现可能会导致运行失败。
- [jev-engineering](https://github.com/eugeniughelbur/jev-engineering) - 代理安全：gates 编码代理工具首先使用确定性规则进行调用，然后进行类型化的 Jev 调用，然后发布可重新运行的 300 次调用注入测试，显示门捕获的内容以及经过的内容。
