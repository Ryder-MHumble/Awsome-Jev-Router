# 校准与研究

**语言 / Language:** 中文（当前） · [English](../calibration-research.md)

将此类别用于研究或利用 Jev 校准置信度的工作 — RLCD 式训练、概率质量、阈值选择、不确定性分析。

## 提交格式
```md
- [Name](URL) - Industry: one-sentence description of the Jev use case.
```
## 条目

- [decider](https://github.com/Mapika/decider) - 开放模型：通过 Qwen3.5-2B 微调重现 System One 形状，一次性发出具有校准概率的键入决策。
- [openjev](https://github.com/zhihz/openjev) - 开放研究：独立的本地预览，从上下文、问题和候选答案中回答双语概率问题，灵感来自 TypeSafe Jev。
- [Parallel Constrained Decoding (Qwen2.5-1B-RLCD)](https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding) - 开放研究：RLCD 训练的 Qwen2.5-1B 演示探索开源并行约束解码作为 Jev 的替代方案。
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - 开放副本：一个 0.6B 并行决策模型，返回完整概率分布，无需输出令牌解码，附带其训练管道、权重和数据集。
- [open-alternative-jev](https://github.com/ikermoel/open-alternative-jev) - 开放替代方案：在您自己的 GPU 上本地运行 Jev 型决策模型。
- [mini-jev](https://github.com/r-ms/mini-jev) - 本地复制：在本地 LLM 之上实现 Jev 的类型化决策接口。
- [Laya](https://github.com/NandhaKishorM/laya) - 开放替代方案：非自回归决策模型，通过 RLCD 训练的校准概率在一次约 35 毫秒的前向传递中回答 `choice`、`score` 和 `noul` 问题，发布在 PyPI 和 Hugging Face 上。
- [Jev-compatible public API](https://x.com/ekzhang1/status/2100651678110515383) - 开放研究：由开放 Qwen3.6-35B-A3B 模型支持的公共 Jev 型 API，因此任何人都可以尝试类型化决策接口。
- [kev](https://github.com/jaredpalmer/kev) - 可训练的复制品：Qwen2.5-0.5B 之上的一个类似 Jev 的微型模型，可以在 MacBook 上训练和运行，附带自己的研究运行和评估脚本。
- [jevinci](https://github.com/achimala/jevinci) - 创意实验：通过让 Jev 并行预测每个像素的颜色来绘制图像，预测的置信度决定每个笔划的绘制宽度。
- [jev-local](https://github.com/us/jev-local) - 本地复制：Jev 兼容的 `POST /v1/systemone` 服务器通过开放权重自信地回答键入的 `Choice`/`Score`/`Noul` 问题，经验证为具有温度拟合校准的官方 SDK 插件（set3 n=1316，总体 0.83）。
- [LitJev](https://github.com/zhengxuyu/litjev) - 本地复制：Jev 的复制，可将任何 Qwen 模型转换为快速决策模型，提供相同的 `/v1/systemone` 模式（选择、分数、Noul），无需训练，也无需生成答案文本。
- [CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms) - 专家决策模型：一个 706,048 个参数、2.8 MB 类似 jev 的选项评分器，在一次并行传递中对每个表单字段的“填写”/“检查”/“单击”/“跳过”进行评分，报告其自己的表单填写评估结果为 99.7%，而 Jev 的结果为 83.6%——是主场专家，而不是一般胜利。
- [jevlike](https://github.com/vinnylarouge/jevlike) - 训练库：构建一个小型模型，在不断变化的文本选项列表中进行选择，并在一次传递中返回每个选项的一个概率 - 构建基础 CUA-S1-FORMS。
- [jevbetter](https://github.com/olanotolu/jevbetter) - 改进的记分器：使用散列的 n-gram 编码器、竞争对手感知注意力和门控头，在可变的文本选项列表上提供更强大的一次性记分器。
- [jevlike-esp32](https://github.com/david-cermak/jevlike-esp32) - 边缘部署：将 jevlike 记分器导出为带有 C 记分器和主机端检查的 ESP32 固件，将一次性决策放在微控制器上。
- [von](https://github.com/wfzyx/von) - 开放替代方案：395M 非自回归 System One 模型，可在 15 毫秒内以校准概率回答键入的问题，定位为 Jev 的本地直接替代品。
- [JevForge](https://github.com/zwliJay/jev-forge) - 开放研究：用于可审计数据构建的端到端堆栈、Qwen3.5-0.8B 培训、固定 Mind2Web 和 OOD 评估、本地服务以及初步 RLCD 基线。
- [minojev](https://github.com/zeredy879/minojev) - 开放副本：一种 547k 参数模型，可回答运行时定义的 `Choice`（2-255 个候选者）、`Boolean` 和 `Score` 问题，在一次前向传递中具有开发校准分布和零输出标记，使用提交的数据集、预测和 ECE 结果（迷宫 0.016）在 CPU 上从头开始训练。
- [Luce](https://github.com/scienthoon/luce) - 开放配方：用一句话描述决策任务，LLM 老师编写训练数据，Qwen3-4B-Base 上的 LoRA + 决策头在一次前向传递中以校准概率回答选择/分数/布尔问题；在 12 GB 卡上进行训练。在相同的测试项目上，在 Jev 旁边报告准确性和 ECE（规则生成的票证 91.1 与 75.1，网络钓鱼 97.4 与 62.6，GitHub 问题优先级 41.1 与 37.5）；无需 GPU 的浏览器重放演示。
- [poorjev](https://github.com/rupeshpoojary9/poorjev) - 本地复制：在商品零样本 NLI 模型上实现 Jev 类型的 `Choice`/`Score`/`Noul` 接口，并通过温度缩放和保形弃权使信心诚实，交付可复制的校准评估（ECE 0.170 至 0.071，交叉验证），无需 API 密钥即可离线运行。
- [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) - 开放决策引擎：经过校准的 151M 非自回归模型，报告在类型决策基准测试中击败了 TypeSafe Jev 和 Laya，并附带自己的测试套件。
