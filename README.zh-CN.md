# 画与歌

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![在线体验](https://img.shields.io/badge/在线体验-axtonliu.github.io%2Fmoyun-B03A2A.svg)](https://axtonliu.github.io/moyun/)

一张会呼吸的宣纸。墨在显卡上实时解流体方程，每一笔都有琴声。看不见的手逐笔画出十种水墨场景，并为每幅画题诗、钤印。

**[打开体验 →](https://axtonliu.github.io/moyun/)** · [English](README.md)

![自动生成的水墨山水，带题诗与朱砂日](media/preview.jpg)

## 怎么玩

- **看**：打开页面会自动画一幅山水。也可从底栏选择场景：校园银杏道、图书馆、操场、学生宿舍、花园、溪畔行人、林间飞鸟、城市街头马车、昆明街景，或原有山水。每种场景都有对应构图和题诗，细节每次现算。
- **画**：先选浓墨、朱砂、蓝、黄、绿或清水，再选细、中、粗笔锋，按住拖动即可作画。走得慢墨就浓，走得快笔就枯；写到后面自然出现飞白。
- **搅**：选「清水」，在画好的画上用力搅一搅，墨会像被水冲开一样流动。
- **听**：琴声只用宫商角徵羽五个音，怎么画都不会走调。

## 背后

页面核心是一个 HTML 文件，人物使用 `media/figures/` 下的 10 张本地透明 PNG。无需运行时 JavaScript 库、外链图片或录音文件。

- **流体**：WebGL2 片元着色器求解不可压缩 Navier–Stokes，每帧依次做旋度、涡量约束、散度、24 次 Jacobi 压力迭代、梯度相减投影、半拉格朗日平流。
- **洇墨**：RGBA 四通道分别存游离墨、带符号色素（朱砂/花青）、水分和带符号色素（赭黄/石绿）。四种颜色随纸纤维噪声洇开，水分逐渐蒸发。
- **笔**：沿路径等距盖高斯印章，行笔速度决定笔径，墨量随距离衰减，墨尽时沿笔触法向切出刷毛条纹。
- **琴**：Karplus–Strong 拨弦物理模型合成，上滑与吟用 `playbackRate` 自动化实现。
- **场景**：十种带种子的构图由笔触逐步生成。山水含五种随机视点，远山、瀑布、亭阁、村落、日月云鸟会变化；松、柳、梅也有不同树形。横屏与竖屏分别调整构图和景深。

## 本地运行

```bash
git clone https://github.com/axtonliu/moyun.git
cd moyun
python3 -m http.server 8000
# 打开 http://127.0.0.1:8000/
```

需要支持 WebGL2 的浏览器（新版 Chrome、Edge、Safari、Firefox 均可）。

录制作画视频（16:9 与 9:16，含琴声）：

```bash
pip install playwright && python3 -m playwright install chromium
python3 scripts/record.py --url http://127.0.0.1:8000/ --out media
```

## 致谢

流体求解流程来自 Jos Stam《Stable Fluids》（1999）与 GPU Gems 第 38 章；Pavel Dobryakov 的 [WebGL-Fluid-Simulation](https://github.com/PavelDoGreat/WebGL-Fluid-Simulation) 让这套方法在网页上广为人知，也启发了着色器的组织方式。拨弦合成来自 Karplus 与 Strong（1983）。字体为马善政毛笔体、思源宋体、IBM Plex Mono（SIL OFL）。

本作品由 Claude（Opus 5.5）在一次对话中写成，起点是一句开放的邀请：做一件让每个看到的人都惊叹的事。

## 许可

MIT，见 [LICENSE](LICENSE)。

---

## Author | 作者

**Axton Liu** — AI Educator & Creator

- Website: [axtonliu.ai](https://www.axtonliu.ai)
- YouTube: [@AxtonLiu](https://youtube.com/@AxtonLiu)
- Twitter/X: [@axtonliu](https://x.com/axtonliu)

### Learn More

- [MAPS™ AI Agent Course](https://www.axtonliu.ai/aiagent) - Systematic AI agent skills training
- [Claude Skills: A Systematic Guide](https://www.axtonliu.ai/newsletters/ai-2/posts/claude-agent-skills-maps-framework) - Complete methodology
- [AI Elite Weekly Newsletter](https://www.axtonliu.ai/newsletters/ai-2) - Weekly AI insights
- [Free AI Course](https://www.axtonliu.ai/axton-free-course) - Get started with AI

---

© AXTONLIU™ & AI 精英学院™ 版权所有
