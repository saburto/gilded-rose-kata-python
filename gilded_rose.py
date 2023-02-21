# -*- coding: utf-8 -*-

SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def validate_first(self, item):

        if self.is_item_name_valid(item) and item.quality > 0 :
            item.quality = item.quality - 1
            return

        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == BACKSTAGE:
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def update_quality(self):

        for item in self.items:

            self.validate_first(item);

            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.name != BRIE:
                    if item.name != BACKSTAGE:
                        if item.quality > 0:
                            if item.name != SULFURAS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    def is_item_name_valid(self, item):
        invalid_names = [BRIE, BACKSTAGE, SULFURAS]
        return not item.name in invalid_names

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)