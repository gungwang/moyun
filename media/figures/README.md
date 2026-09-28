# 人物素材与参考 / Figure Assets and References

人物 PNG 是原创透明位图，由 `scripts/generate_ink_figures.py` 绘制；参考作品用于研究比例、衣袍、姿态和笔线，不直接裁切或复用馆藏像素。人物以 WebGL 墨层 stamp 绘制，可随水流扩散。

## 角色 / Roles

- `young_man.png`：青年男主角，交领长袍、文士巾。
- `young_woman.png`：青年女主角，长袖、发髻与飘带。
- `elder_man.png`、`elder_woman.png`：老年男女主角，分别配长须/手杖与发髻/披帛。
- `scholar.png`、`attendant.png`、`traveler.png`、`qin_player.png`：学者、侍从、行旅者、携琴者。
- `boatman.png`、`horse_carriage.png`：舟中人物与马车、车夫。

重新生成需要 Pillow：

```bash
python -m pip install Pillow
python scripts/generate_ink_figures.py
```

## 馆藏参考 / Museum References

Cleveland Museum of Art Open Access API 将以下图像标记为 CC0。这里仅将其作为风格参考；PNG 角色由本项目脚本独立绘制。

- [A Lady, Chen Hongshou, 1979.27.2.16](https://clevelandart.org/art/1979.27.2.16)：独立仕女形象与衣袍比例。
- [Lady Xuanwen Giving Instruction on the Rites of Zhou, 1961.89](https://clevelandart.org/art/1961.89)：老年女性与年轻学者群像；馆方说明其人物使用细劲的“铁线描”，面部比例有意拉长。
- [Laozi Riding an Ox, Chen Hongshou, 1979.27.1.2](https://clevelandart.org/art/1979.27.1.2)：老年文士、长须与乘行姿态。
- [Portrait of Zhongqing in a Landscape, Chen Hongshou, 1979.27.1.8](https://clevelandart.org/art/1979.27.1.8)：山水中的文士尺度与站姿。
- [Scholar Watching the Waterfall, Luo Ping, 1975.95](https://clevelandart.org/art/1975.95)：主客同游，风吹衣袍的行旅姿态。
- [Pine Wind from Myriad Villages, Wu Li, 1954.584](https://clevelandart.org/art/1954.584)：携琴行者与松下对坐人物。
