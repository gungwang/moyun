"""Generate transparent ink-figure sprites for the canvas painter.

Requires Pillow: python -m pip install Pillow
Run from the repository root: python scripts/generate_ink_figures.py
"""
from pathlib import Path
import math

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "media" / "figures"
SCALE = 4
WIDTH, HEIGHT = 220, 340
INK = (25, 26, 28)


def px(point):
    return round(point * SCALE)


def draw_line(draw, points, width=1.8, opacity=190):
    coordinates = [(px(point[0]), px(point[1])) for point in points]
    draw.line(coordinates, fill=(*INK, opacity), width=max(1, px(width)), joint="curve")


def draw_polygon(draw, points, opacity=44, outline=188, width=1.8):
    coordinates = [(px(point[0]), px(point[1])) for point in points]
    draw.polygon(coordinates, fill=(*INK, opacity))
    draw.line(coordinates + [coordinates[0]], fill=(*INK, outline), width=px(width), joint="curve")


def draw_ellipse(draw, bounds, fill=40, outline=180, width=1.5):
    scaled = tuple(px(value) for value in bounds)
    draw.ellipse(scaled, fill=(*INK, fill), outline=(*INK, outline), width=px(width))


def draw_head(draw, role):
    draw_ellipse(draw, (94, 31, 120, 66), fill=28, outline=196, width=1.8)
    draw_line(draw, [(101, 49), (105, 51), (110, 49)], width=1.2, opacity=145)
    draw_line(draw, [(101, 57), (107, 59), (112, 57)], width=1.0, opacity=125)
    draw_line(draw, [(99, 67), (98, 78), (104, 83)], width=1.7, opacity=170)

    if role in {"young_man", "scholar", "attendant", "traveler", "qin_player", "boatman"}:
        draw_polygon(draw, [(91, 39), (91, 25), (98, 18), (117, 18), (124, 25), (123, 36), (116, 31), (99, 32)], 148, 198, 1.5)
        draw_line(draw, [(88, 36), (126, 35)], width=2.1, opacity=175)
    elif role in {"elder_man"}:
        draw_polygon(draw, [(91, 42), (92, 27), (98, 18), (116, 18), (123, 28), (122, 42), (115, 33), (99, 34)], 140, 190, 1.4)
        draw_line(draw, [(99, 64), (102, 76), (107, 82), (111, 72), (115, 62)], width=3, opacity=175)
        draw_line(draw, [(102, 68), (105, 75), (108, 68)], width=1.2, opacity=105)
    else:
        draw_ellipse(draw, (88, 17, 101, 35), fill=160, outline=196, width=1.3)
        draw_ellipse(draw, (113, 16, 127, 34), fill=158, outline=196, width=1.3)
        draw_line(draw, [(98, 24), (103, 17), (111, 17), (117, 24)], width=2.2, opacity=185)
        draw_line(draw, [(119, 25), (132, 21), (137, 26)], width=1.1, opacity=150)


def draw_robes(draw, role):
    if role == "young_woman":
        robe = [(99, 72), (83, 77), (73, 96), (50, 111), (30, 145), (47, 157), (72, 137), (77, 126), (77, 183), (57, 291), (73, 306), (108, 296), (146, 308), (163, 292), (132, 182), (132, 126), (141, 138), (166, 157), (183, 144), (156, 104), (132, 83), (117, 73)]
    elif role == "elder_man":
        robe = [(100, 74), (82, 80), (73, 104), (52, 118), (36, 154), (51, 166), (75, 144), (80, 135), (79, 189), (65, 289), (82, 307), (108, 298), (138, 306), (154, 290), (130, 186), (131, 132), (142, 146), (163, 166), (179, 152), (151, 111), (128, 84), (117, 73)]
    elif role == "elder_woman":
        robe = [(99, 73), (82, 79), (69, 105), (47, 126), (34, 159), (52, 169), (75, 146), (78, 134), (77, 183), (55, 290), (74, 308), (108, 297), (145, 307), (163, 289), (132, 183), (132, 134), (145, 149), (168, 168), (185, 155), (156, 116), (130, 84), (117, 74)]
    elif role == "attendant":
        robe = [(100, 73), (82, 80), (74, 102), (55, 117), (41, 146), (55, 157), (77, 139), (82, 131), (80, 185), (65, 281), (82, 296), (109, 287), (137, 296), (151, 281), (131, 184), (132, 131), (145, 143), (165, 158), (179, 146), (153, 112), (129, 84), (117, 74)]
    elif role == "traveler":
        robe = [(98, 74), (80, 81), (70, 104), (48, 119), (29, 154), (48, 167), (74, 144), (79, 134), (77, 188), (56, 289), (75, 306), (109, 296), (145, 307), (162, 290), (132, 185), (131, 134), (146, 149), (168, 169), (187, 154), (158, 112), (129, 84), (117, 74)]
    elif role == "qin_player":
        robe = [(100, 74), (81, 82), (72, 105), (54, 121), (37, 153), (54, 163), (78, 144), (82, 132), (82, 187), (66, 286), (83, 300), (109, 290), (137, 300), (153, 285), (132, 184), (131, 133), (144, 146), (165, 163), (181, 149), (154, 111), (129, 84), (117, 74)]
    elif role == "boatman":
        robe = [(97, 78), (82, 85), (77, 106), (59, 127), (47, 155), (65, 167), (83, 146), (89, 135), (95, 176), (74, 230), (57, 257), (72, 271), (111, 258), (143, 276), (158, 260), (132, 220), (126, 176), (136, 144), (156, 163), (173, 152), (151, 116), (129, 87), (116, 77)]
    else:
        robe = [(100, 73), (82, 80), (73, 101), (52, 118), (34, 151), (51, 164), (75, 142), (80, 132), (79, 185), (58, 291), (76, 307), (108, 297), (143, 308), (160, 290), (132, 184), (132, 131), (144, 144), (165, 163), (181, 149), (154, 112), (129, 84), (117, 73)]

    draw_polygon(draw, robe, 55, 205, 2.0)
    draw_polygon(draw, [(85, 78), (99, 84), (110, 109), (123, 80), (132, 86), (116, 126), (106, 139), (91, 113)], 22, 155, 1.1)

    draw_line(draw, [(100, 76), (91, 92), (112, 116), (94, 132)], width=2.0, opacity=205)
    draw_line(draw, [(118, 77), (128, 93), (108, 115)], width=1.6, opacity=170)
    draw_line(draw, [(80, 128), (109, 137), (132, 128)], width=2.2, opacity=188)
    draw_line(draw, [(83, 153), (100, 171), (91, 218), (73, 285)], width=1.35, opacity=118)
    draw_line(draw, [(119, 151), (109, 185), (126, 228), (147, 286)], width=1.35, opacity=118)
    draw_line(draw, [(99, 164), (107, 230), (108, 289)], width=1.2, opacity=105)
    draw_line(draw, [(68, 144), (85, 151), (95, 166)], width=1.35, opacity=128)
    draw_line(draw, [(144, 143), (130, 153), (119, 169)], width=1.35, opacity=128)
    draw_line(draw, [(74, 289), (107, 296), (145, 291)], width=2.0, opacity=190)
    draw_line(draw, [(83, 299), (72, 311), (57, 312)], width=2.0, opacity=185)
    draw_line(draw, [(128, 300), (147, 311), (164, 311)], width=2.0, opacity=185)

    if role == "young_woman":
        draw_line(draw, [(53, 155), (29, 185), (45, 211), (70, 195)], width=2.0, opacity=165)
        draw_line(draw, [(169, 155), (193, 178), (177, 199)], width=2.0, opacity=165)
        draw_line(draw, [(137, 82), (164, 97), (181, 120), (188, 132)], width=1.8, opacity=140)
    if role == "elder_man":
        draw_line(draw, [(136, 104), (176, 310)], width=2.4, opacity=205)
        draw_line(draw, [(101, 68), (98, 83), (104, 92), (111, 81), (114, 68)], width=3.4, opacity=190)
    if role == "elder_woman":
        draw_line(draw, [(49, 161), (36, 190), (55, 205)], width=2.6, opacity=178)
        draw_line(draw, [(177, 160), (191, 191)], width=2.4, opacity=178)
        draw_line(draw, [(92, 70), (93, 89), (102, 97), (112, 88), (119, 70)], width=2.2, opacity=160)
    if role == "attendant":
        draw_polygon(draw, [(145, 105), (170, 109), (178, 135), (154, 133)], 82, 180, 1.6)
        draw_line(draw, [(151, 114), (172, 119)], width=1.2, opacity=138)
    if role == "traveler":
        draw_polygon(draw, [(66, 102), (48, 88), (30, 100), (47, 123)], 70, 170, 1.4)
        draw_line(draw, [(156, 117), (177, 311)], width=2.2, opacity=190)
    if role == "qin_player":
        draw_polygon(draw, [(47, 145), (178, 150), (185, 161), (44, 157)], 70, 190, 1.4)
        draw_line(draw, [(69, 151), (162, 155)], width=1.3, opacity=175)
        for index in range(5):
            x = 67 + index * 20
            draw_line(draw, [(x, 148), (x + 1, 156)], width=0.8, opacity=120)
    if role == "boatman":
        draw_line(draw, [(154, 119), (183, 226)], width=2.6, opacity=185)
        draw_line(draw, [(60, 258), (111, 272), (158, 260)], width=2.3, opacity=175)
    if role == "scholar":
        draw_polygon(draw, [(82, 27), (87, 18), (117, 18), (124, 27), (122, 31), (85, 31)], 158, 198, 1.4)
        draw_line(draw, [(90, 19), (90, 9), (115, 9), (117, 19)], width=1.8, opacity=178)
        draw_polygon(draw, [(143, 97), (155, 95), (159, 133), (146, 136)], 70, 170, 1.3)
    if role == "young_man":
        draw_line(draw, [(146, 146), (160, 122), (166, 104)], width=1.9, opacity=160)
        draw_polygon(draw, [(158, 99), (165, 97), (169, 108), (162, 111)], 105, 180, 1.2)
    if role == "elder_woman":
        draw_line(draw, [(100, 17), (100, 9), (117, 11), (126, 19)], width=1.8, opacity=170)


def draw_figure(role):
    image = Image.new("RGBA", (WIDTH * SCALE, HEIGHT * SCALE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw_head(draw, role)
    draw_robes(draw, role)
    return image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def draw_horse_carriage():
    image = Image.new("RGBA", (360 * SCALE, 230 * SCALE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    draw_polygon(draw, [(30, 94), (42, 74), (66, 64), (99, 68), (126, 84), (145, 99), (137, 116), (117, 120), (96, 112), (68, 114), (46, 107)], 54, 208, 2.4)
    draw_polygon(draw, [(113, 91), (130, 65), (145, 48), (163, 50), (176, 63), (170, 77), (156, 73), (144, 101), (131, 111)], 58, 202, 2.0)
    draw_polygon(draw, [(161, 55), (166, 39), (172, 51), (179, 57), (174, 70)], 92, 188, 1.4)
    draw_polygon(draw, [(148, 52), (148, 36), (156, 49), (162, 55)], 88, 182, 1.3)
    draw_line(draw, [(132, 56), (141, 48), (151, 55), (158, 47), (165, 56)], width=2.1, opacity=182)
    draw_ellipse(draw, (163, 61, 167, 65), fill=205, outline=210, width=1)
    draw_line(draw, [(171, 72), (180, 75), (174, 80)], width=1.4, opacity=172)
    draw_line(draw, [(46, 87), (31, 73), (24, 79), (36, 95)], width=2.1, opacity=174)

    draw_polygon(draw, [(45, 102), (60, 104), (58, 138), (51, 160), (42, 161), (46, 138)], 45, 198, 1.8)
    draw_polygon(draw, [(70, 108), (82, 109), (83, 140), (91, 157), (83, 162), (71, 143)], 45, 198, 1.8)
    draw_polygon(draw, [(113, 105), (126, 105), (135, 136), (133, 158), (124, 159), (121, 137)], 48, 198, 1.8)
    draw_polygon(draw, [(131, 101), (141, 101), (150, 130), (153, 152), (145, 156), (137, 133)], 45, 198, 1.8)
    for hoof in [(40, 157, 53, 164), (81, 157, 94, 165), (122, 154, 136, 162), (144, 150, 158, 158)]:
        draw_ellipse(draw, hoof, fill=105, outline=198, width=1.2)

    draw_line(draw, [(145, 84), (177, 91), (199, 100)], width=1.4, opacity=172)
    draw_line(draw, [(145, 95), (180, 110), (206, 115)], width=1.2, opacity=158)
    draw_line(draw, [(164, 116), (201, 124), (214, 129)], width=2.2, opacity=190)
    draw_line(draw, [(163, 123), (200, 139), (213, 144)], width=2.2, opacity=178)

    draw_ellipse(draw, (202, 137, 263, 198), fill=8, outline=202, width=3.0)
    draw_ellipse(draw, (211, 146, 254, 189), fill=0, outline=140, width=1.6)
    draw_ellipse(draw, (224, 159, 241, 176), fill=24, outline=180, width=1.3)
    draw_ellipse(draw, (293, 137, 354, 198), fill=8, outline=202, width=3.0)
    draw_ellipse(draw, (302, 146, 345, 189), fill=0, outline=140, width=1.6)
    draw_ellipse(draw, (315, 159, 332, 176), fill=24, outline=180, width=1.3)
    for spoke_index in range(8):
        angle = spoke_index * math.pi / 4
        for wheel_center in (232.5, 323.5):
            draw_line(draw, [(wheel_center, 167.5), (wheel_center + math.cos(angle) * 25, 167.5 + math.sin(angle) * 25)], width=1.05, opacity=148)

    draw_line(draw, [(191, 132), (341, 132)], width=2.4, opacity=194)
    draw_line(draw, [(202, 128), (202, 151), (350, 151)], width=2.1, opacity=182)
    draw_polygon(draw, [(190, 77), (201, 57), (220, 49), (299, 49), (323, 58), (338, 78), (331, 88), (198, 88)], 56, 206, 2.3)
    draw_polygon(draw, [(202, 85), (330, 85), (330, 139), (202, 139)], 42, 195, 2.0)
    draw_line(draw, [(193, 88), (338, 88)], width=2.1, opacity=190)
    draw_line(draw, [(214, 94), (265, 94), (265, 122), (214, 122), (214, 94)], width=1.8, opacity=184)
    draw_line(draw, [(239, 94), (239, 122)], width=1.1, opacity=142)
    draw_line(draw, [(214, 108), (265, 108)], width=1.1, opacity=142)
    draw_line(draw, [(278, 91), (278, 133)], width=1.6, opacity=173)
    draw_line(draw, [(292, 93), (292, 132)], width=1.2, opacity=143)

    draw_ellipse(draw, (276, 56, 299, 85), fill=30, outline=194, width=1.5)
    draw_polygon(draw, [(273, 67), (274, 55), (283, 50), (297, 54), (301, 64), (294, 60), (281, 61)], 154, 194, 1.3)
    draw_line(draw, [(279, 83), (270, 99), (288, 109), (302, 94)], width=4.4, opacity=186)
    draw_line(draw, [(278, 94), (261, 108), (248, 105)], width=2.5, opacity=178)
    draw_line(draw, [(298, 92), (309, 106), (322, 106)], width=2.5, opacity=178)
    draw_line(draw, [(322, 106), (194, 76), (172, 69)], width=1.1, opacity=138)

    return image.resize((360, 230), Image.Resampling.LANCZOS)


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    roles = (
        "young_man", "young_woman", "elder_man", "elder_woman", "scholar",
        "attendant", "traveler", "qin_player", "boatman",
    )
    for role in roles:
        draw_figure(role).save(OUTPUT / f"{role}.png", optimize=True)
    draw_horse_carriage().save(OUTPUT / "horse_carriage.png", optimize=True)
    print(f"Generated {len(roles) + 1} ink figures in {OUTPUT}")


if __name__ == "__main__":
    main()