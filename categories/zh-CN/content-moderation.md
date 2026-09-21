# 内容审核

**语言 / Language:** 中文（当前） · [English](../content-moderation.md)

使用此类别对用户生成的大量内容进行政策和滥用决策。

## 提交格式
```md
- [Name](URL) - Industry: one-sentence description of the Jev use case.
```
## 条目

- [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) - 社区审核：Discord 机器人使用 Jev 对传入消息进行网络钓鱼、垃圾邮件和社会工程评分，并驱动四阶段升级阶梯，将赦免的消息注入上下文中作为经过验证的安全先例。
- [jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) - 垃圾邮件过滤：使用 Jev `Boolean` 问题进行零样本垃圾邮件分类，以 TF-IDF 基线为基准。
- [mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation) - AI 助手：Mastra 输入处理器询问 Jev `Boolean`“必须阻止此消息吗？”在一个请求中加上 `Choice` 类别，在 0.7 时中止回合，并在截止日期和断路器后未能打开；在生产中，它以大约 0.4 秒的中位数阻止 9/9 的恶意消息和 0/49 的真实消息，比 LLM 主持人便宜约 4 倍。
- [Jev Chat for Twitch](https://github.com/ethanplusai/jev-chat-for-twitch) - 实时聊天过滤：自带密钥的 Chrome 扩展程序，可通过匿名 IRC WebSocket 读取 Twitch 频道的聊天，以 20 条为一组向 Jev 询问每条消息一个类别 `Choice`，并在第二列中仅显示与所选意图匹配的消息（有用、问题、有趣、反馈）；每条消息大约 504 个输入令牌，每秒 2 条消息的聊天大约每小时 0.15 美元，每秒 50 条消息的聊天每小时大约 0.76 美元。
