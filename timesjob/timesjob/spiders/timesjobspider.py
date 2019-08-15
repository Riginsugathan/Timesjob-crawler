# -*- coding: utf-8 -*-
import scrapy
from ..items import TimesjobItem
import time
import random

class TimesjobspiderSpider(scrapy.Spider):
    name = 'timesjobspider'
    allowed_domains = ['www.timesjobs.com']
    start_page_number = 1
    start_urls = ['https://www.timesjobs.com/jobs-sitemap/1']

    def parse(self, response):
        first_page_urls = response.css('.job-site-map a::attr(href)').extract()
        for singlepageurl in first_page_urls:
            yield response.follow(singlepageurl,callback=self.start_second_page_crawler)
        

    def start_second_page_crawler(self,response):
        second_page_urls = response.css('.job-site-map a::attr(href)').extract()
        for singlepageurls in second_page_urls:
            yield response.follow(singlepageurls,callback=self.start_job_details_crawl)

    def start_job_details_crawl(self,response):
        item = TimesjobItem()
        item['title'] = response.css('.jd-job-title::text').extract()[0].replace("\r\n",'').strip() if response.css('.jd-job-title::text').extract()[0] else ''
        item['company'] = response.css('h2::text').extract()[0].replace("\r\n",'').strip() if response.css('h2::text').extract()[0] else ''
        item['experience'] = response.css('.top-jd-dtl li:nth-child(1)::text').extract()[0].replace("\r\n",'').strip() if response.css('.top-jd-dtl li:nth-child(1)::text').extract()[0] else ''
        item['jobdescription'] = response.css('h3+ p::text').extract()
        item['jobfunction'] = response.css('#applyFlowHideDetails_1 .clearfix:nth-child(1) .basic-info-dtl::text').extract()[0].replace("\r\n",'').strip() if len(response.css('#applyFlowHideDetails_1 .clearfix:nth-child(1) .basic-info-dtl::text').extract())>0 else ''
        item['industry'] = response.css('#applyFlowHideDetails_1 .clearfix:nth-child(2) .basic-info-dtl::text').extract()[0].replace("\r\n",'').strip() if len(response.css('#applyFlowHideDetails_1 .clearfix:nth-child(2) .basic-info-dtl::text').extract())>0 else ''
        item['specialization'] = response.css('#applyFlowHideDetails_1 .clearfix:nth-child(3) .basic-info-dtl::text').extract()[0].replace("\r\n",'').strip() if len(response.css('#applyFlowHideDetails_1 .clearfix:nth-child(3) .basic-info-dtl::text').extract())>0 else ''
        item['role'] = response.css('#applyFlowHideDetails_1 .clearfix:nth-child(4) .basic-info-dtl::text').extract()[0].replace("\r\n",'').strip() if len(response.css('#applyFlowHideDetails_1 .clearfix:nth-child(4) .basic-info-dtl::text').extract())>0 else ''
        item['qualification'] = response.css('.basic-info-dtl li::text').extract()[0].replace("\r\n",'').strip() if len(response.css('.basic-info-dtl li::text').extract())>0 else ''
        item['skills'] = response.css('.jd-skill-tag a::text').extract()
        item['about_hiring_company_name'] = response.css('.jd-comp-main .basic-info-dtl::text').extract()[0].replace("\r\n",'').strip() if len(response.css('.jd-comp-main .basic-info-dtl::text').extract())>0 else ''
        item['about_hiring_company_website'] = response.css('#applyFlowHideDetails_4 a::text').extract()
        item['about_hiring_company_industry'] = response.css('#applyFlowHideDetails_4 .clearfix:nth-child(2) .basic-info-dtl::text').extract()[0].replace("\r\n",'').strip() if len(response.css('#applyFlowHideDetails_4 .clearfix:nth-child(2) .basic-info-dtl::text').extract())>0 else ''
        item['about_hiring_company_turnover'] = response.css('#applyFlowHideDetails_4 .clearfix .clearfix:nth-child(3) .basic-info-dtl::text').extract()[0].replace("\r\n",'').strip() if len(response.css('#applyFlowHideDetails_4 .clearfix .clearfix:nth-child(3) .basic-info-dtl::text').extract())>0 else ''
        item['about_hiring_company_size'] = response.css('#applyFlowHideDetails_4 .clearfix:nth-child(4) .basic-info-dtl::text').extract()[0].replace("\r\n","").strip() if len(response.css('#applyFlowHideDetails_4 .clearfix:nth-child(4) .basic-info-dtl::text').extract())>0 else ''
        item['url'] = response.request.url
        yield item