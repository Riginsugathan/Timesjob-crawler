# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TimesjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    experience = scrapy.Field()
    jobdescription = scrapy.Field()
    jobfunction = scrapy.Field()
    industry = scrapy.Field()
    specialization = scrapy.Field()
    role = scrapy.Field()
    qualification = scrapy.Field()
    skills = scrapy.Field()
    about_hiring_company_name = scrapy.Field()
    about_hiring_company_website = scrapy.Field()
    about_hiring_company_industry = scrapy.Field()
    about_hiring_company_turnover = scrapy.Field()
    about_hiring_company_size = scrapy.Field()
    url = scrapy.Field()
    pass
