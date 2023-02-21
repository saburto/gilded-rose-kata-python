# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_first_condition(self):
        items = [Item("foo", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert items[0].quality == 0

    def test_hand_of(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)

    def test_backstage_passes(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)
        
if __name__ == '__main__':
    unittest.main()