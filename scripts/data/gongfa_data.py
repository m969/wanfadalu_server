# -*- coding: utf-8 -*-

data = \
    {
        1001: 
        {
            'gongFaName': '基础弓箭术',
            'skillList':
                [
                    { 'class': "Shoot", 'quality': 0.1, 'levelSpLimit': {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900}, 'strategies': ["一次伤害策略"] },
                    { 'class': "GongKan", 'quality': 0.1, 'levelSpLimit': {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900}, 'strategies': ["伤害策略"] },
                    { 'class': "ArrowExplode", 'quality': 0.1, 'levelSpLimit': {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900}, 'strategies': ["伤害策略", "爆炸策略"] }
                ]
        },
        1002:
        {
            'gongFaName': '基础冰系法术',
            'skillList':
                [
                    { 'class': "SkillE", 'quality': 0.2, 'levelSpLimit': {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900}, 'strategies': ["伤害策略", "禁锢策略", "冰霜策略"] }
                ]
        },
        1003:
        {
            'gongFaName': '基础土系法术',
            'skillList':
                [
                    { 'class': "SkillW", 'quality': 0.2, 'levelSpLimit': {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900}, 'strategies': ["伤害策略"] }
                ]
        }
    }

allData = {'角色功法数据': data }
