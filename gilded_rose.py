# -*- coding: utf-8 -*-

SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # public, main entry of app
    def update_quality(self):
        for item in self.items:

            self.validate_first(item)

            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                self.handle_item_sell_in_negative(item)


    def validate_first(self, item):

        if self.is_item_name_valid(item) and item.quality > 0 :
            item.quality = item.quality - 1
            return
        
        if item.quality >= 50:
            return
        
        item.quality = item.quality + 1

        self.handle_backstage(item)


    def is_item_name_valid(self, item):
        invalid_names = [BRIE, BACKSTAGE, SULFURAS]
        return not item.name in invalid_names

    def handle_backstage(self, item):
        if item.name != BACKSTAGE:
            return

        if item.quality >= 50:
            return;

        side = 1 if item.sell_in < 11 else 0
        side = side + 1 if item.sell_in < 6 else side

        item.quality = item.quality + side
        

    def handle_item_sell_in_negative(self, item):
        if item.name == BRIE:
            self.handle_brie_negative(item)
            return

        if item.name == BACKSTAGE:
            self.handle_backstage_negative(item)
            return

        if item.quality > 0 and item.name != SULFURAS:
            item.quality = item.quality - 1


    def handle_backstage_negative(self, item):
        item.quality = item.quality - item.quality

    def handle_brie_negative(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)