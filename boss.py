class Boss:
    def __init__(self, id, name, location, location_short, zone_id, difficulty, group_size, alternative_trigger):
        self.id = id
        self.name = name
        self.location = location
        self.location_short = location_short
        self.zone_id = zone_id
        self.difficulty = difficulty
        self.group_size = group_size
        self.alternative_trigger = alternative_trigger
        self.encounter_start_found = False
        self.encounter_end_found = False


# Boss data
boss_data = [
    # 黑翼之巢
    Boss(610, "狂野的拉佐格尔", "黑翼之巢", "bwl", 469, 9, 40, []),
    Boss(611, "堕落的瓦拉斯塔兹", "黑翼之巢", "bwl", 469, 9, 40, []),
    Boss(612, "勒什雷尔", "黑翼之巢", "bwl", 469, 9, 40, []),
    Boss(613, "费尔默", "黑翼之巢", "bwl", 469, 9, 40, []),
    Boss(614, "埃博诺克", "黑翼之巢", "bwl", 469, 9, 40, []),
    Boss(615, "弗莱格尔", "黑翼之巢", "bwl", 469, 9, 40, []),
    Boss(616, "克洛玛古斯", "黑翼之巢", "bwl", 469, 9, 40, []),
    Boss(617, "奈法利安", "黑翼之巢", "bwl", 469, 9, 40, []),

    # 熔火之心
    Boss(663, "鲁西弗隆", "熔火之心", "mc", 409, 9, 40, []),
    Boss(664, "玛格曼达", "熔火之心", "mc", 409, 9, 40, []),
    Boss(665, "基赫纳斯", "熔火之心", "mc", 409, 9, 40, []),
    Boss(666, "加尔", "熔火之心", "mc", 409, 9, 40, []),
    Boss(667, "沙斯拉尔", "熔火之心", "mc", 409, 9, 40, []),
    Boss(668, "迦顿男爵", "熔火之心", "mc", 409, 9, 40, []),
    Boss(669, "萨弗隆先驱者", "熔火之心", "mc", 409, 9, 40, []),
    Boss(670, "焚化者古雷曼格", "熔火之心", "mc", 409, 9, 40, []),
    Boss(671, "管理者埃克索图斯", "熔火之心", "mc", 409, 9, 40, []),
    Boss(672, "拉格纳罗斯", "熔火之心", "mc", 409, 9, 40, []),

    # 安其拉神殿
    Boss(709, "预言者斯克拉姆", "安其拉神殿", "aq40", 531, 9, 40, []),
    Boss(710, "安其拉三宝", "安其拉神殿", "aq40", 531, 9, 40, ["克里勋爵", "亚尔基公主", "维姆"]),
    Boss(711, "沙尔图拉", "安其拉神殿", "aq40", 531, 9, 40, []),
    Boss(712, "顽强的范克瑞斯", "安其拉神殿", "aq40", 531, 9, 40, []),
    Boss(713, "维希度斯", "安其拉神殿", "aq40", 531, 9, 40, []),
    Boss(714, "哈霍兰公主", "安其拉神殿", "aq40", 531, 9, 40, []),
    Boss(715, "双子皇帝", "安其拉神殿", "aq40", 531, 9, 40, ["维克洛尔大帝", "维克尼拉斯大帝"]),
    Boss(716, "奥罗", "安其拉神殿", "aq40", 531, 9, 40, []),
    Boss(717, "克苏恩", "安其拉神殿", "aq40", 531, 9, 40, ["克苏恩之眼"]),

    # Ruins of Ahn'Qiraj
    Boss(718, "Kurinnaxx", "Ruins of Ahn'Qiraj", "aq20", 509, 148, 20, []),
    Boss(719, "General Rajaxx", "Ruins of Ahn'Qiraj", "aq20", 509, 148, 20, []),
    Boss(720, "Moam", "Ruins of Ahn'Qiraj", "aq20", 509, 148, 20, []),
    Boss(721, "Buru the Gorger", "Ruins of Ahn'Qiraj", "aq20", 509, 148, 20, []),
    Boss(722, "Ayamiss the Hunter", "Ruins of Ahn'Qiraj", "aq20", 509, 148, 20, []),
    Boss(723, "Ossirian the Unscarred", "Ruins of Ahn'Qiraj", "aq20", 509, 148, 20, []),

    # Zul'Gurub
    Boss(784, "High Priest Venoxis", "Zul'Gurub", "zg", 309, 148, 20, []),
    Boss(785, "High Priestess Jeklik", "Zul'Gurub", "zg", 309, 148, 20, []),
    Boss(786, "High Priestess Mar'li", "Zul'Gurub", "zg", 309, 148, 20, []),
    Boss(787, "Bloodlord Mandokir", "Zul'Gurub", "zg", 309, 148, 20, []),
    Boss(788, "Edge of Madness", "Zul'Gurub", "zg", 309, 148, 20, []),
    Boss(789, "High Priest Thekal", "Zul'Gurub", "zg", 309, 148, 20, []),
    Boss(790, "Gahz'ranka", "Zul'Gurub", "zg", 309, 148, 20, []),
    Boss(791, "High Priestess Arlokk", "Zul'Gurub", "zg", 309, 148, 20, []),
    Boss(792, "Jin'do the Hexxer", "Zul'Gurub", "zg", 309, 148, 20, []),
    Boss(793, "Hakkar", "Zul'Gurub", "zg", 309, 148, 20, []),

    # Onyxia"s Lair
    Boss(1084, "奥妮克希亚", "奥妮克希亚的巢穴", "ony", 249, 9, 40, []),

    # Naxxramas
    # The Arachnid Quarter
    Boss(1107, "Anub'Rekhan", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1110, "Grand Widow Faerlina", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1116, "Maexxna", "Naxxramas", "naxx", 533, 9, 40, []),
    # The Plague Quarter
    Boss(1117, "Noth the Plaguebringer", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1112, "Heigan the Unclean", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1115, "Loatheb", "Naxxramas", "naxx", 533, 9, 40, []),
    # The Military Quarter
    Boss(1113, "Instructor Razuvious", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1109, "Gothik the Harvester", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1121, "The Four Horsemen", "Naxxramas", "naxx", 533, 9, 40, ["Thane Korth'azz", "Lady Blaumeux", "Sir Zeliek", "Highlord Mograine"]),
    # The Construct Quarter
    Boss(1118, "Patchwerk", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1111, "Grobbulus", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1108, "Gluth", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1120, "Thaddius", "Naxxramas", "naxx", 533, 9, 40, []),
    # Frostwyrm Lair
    Boss(1119, "Sapphiron", "Naxxramas", "naxx", 533, 9, 40, []),
    Boss(1114, "Kel'Thuzad", "Naxxramas", "naxx", 533, 9, 40, [])
]
