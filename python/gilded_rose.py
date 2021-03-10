# -*- coding: utf-8 -*-

class UpdateItem(object):

    def __init__(self, item):
        self.item = item

# add 1 to the quality of the item
    def incrementQuality(self):
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1

# subtract 1 from the quality of the item
    def decrementQuality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

# denote an expired item by changing its quality to 0    
    def updateExpired(self):
        if self.item.sell_in < 0:
            self.item.quality = 0

# decrease the Sell In value by 1    
    def updateSellIn(self):
        self.item.sell_in = self.item.sell_in - 1
    
    def updateQuality(self):
        self.updateSellIn()
        self.decrementQuality()
        if self.item.sell_in < 0:
            self.updateExpired()


# class to update legendary items
class UpdateLegendary(UpdateItem):
    def updateQuality(self):
        return

# class to update cheese items
class UpdateCheese(UpdateItem):
    def updateQuality(self):
        self.updateSellIn()
        self.incrementQuality()
        if self.item.sell_in < 0:
            self.incrementQuality()

# class to update backstage passes
class UpdateTicket(UpdateItem):
    def updateQuality(self):
        if self.item.sell_in < 11:
            self.incrementQuality()
        if self.item.sell_in < 6:
            self.incrementQuality()
        self.updateSellIn()
        if self.item.sell_in < 0:
            self.updateExpired()

# class to update conjured items
class UpdateConjured(UpdateItem):
    def decrementQuality(self):
        UpdateItem.decrementQuality(self)
        UpdateItem.decrementQuality(self)


    
class ItemCategory(object):
    
# put the items from the test class into proper update classes
    categories = {
        "Sulfuras, Hand of Ragnaros": UpdateLegendary,
        "Aged Brie": UpdateCheese,
        "Backstage passes to a TAFKAL80ETC concert": UpdateTicket,
        "Conjured Mana Cake": UpdateConjured
    }

# method to categorize the items from the test class
    @classmethod
    def categorize (cls, item):
        if item.name in cls.categories:
            return cls.categories[item.name](item)
        return UpdateItem(item)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def updateQuality(self):
        for item in self.items:
            category = ItemCategory.categorize(item)
            category.updateQuality()

# item class, do not touch! #
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)





# the original Gilded Rose Python Kata code #

    # def updateQuality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1


