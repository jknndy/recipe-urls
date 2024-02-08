from typing import Any

from recipe_urls.abuelascounter import AbuelasCounterScraper
from recipe_urls.acouplecooks import ACoupleCooksScraper
from recipe_urls.addapinch import AddAPinchScraper
from recipe_urls.afghankitchenrecipes import AfghanKitchenRecipesScraper
from recipe_urls.allrecipes import AllRecipesScraper
from recipe_urls.ambitiouskitchen import AmbitiousKitchenScraper
from recipe_urls.archanaskitchen import ArchanasKitchenScraper
from recipe_urls.averiecooks import AverieCooksScraper
from recipe_urls.bakingmischief import BakingMischiefScraper
from recipe_urls.bakingsense import BakingSenseScraper
from recipe_urls.barefootcontessa import BarefootContessaScraper
from recipe_urls.bbc import BBCScraper
from recipe_urls.bettycrocker import BettyCrockerScraper
from recipe_urls.bigoven import BigOvenScraper
from recipe_urls.bluejeanchef import BlueJeanChefScraper
from recipe_urls.bonappetit import BonAppetitScraper
from recipe_urls.bongeats import BongEatsScraper
from recipe_urls.bowlofdelicious import BowlOfDeliciousScraper
from recipe_urls.budgetbytes import BudgetBytesScraper
from recipe_urls.carlsbadcravings import CarlsbadCravingsScraper
from recipe_urls.castironketo import CastIronKetoScraper
from recipe_urls.food import FoodScraper
from recipe_urls.food52 import Food52Scraper
from recipe_urls.hellofresh import HelloFreshScraper
from recipe_urls.nytimes import NyTimesScraper

from recipe_urls._abstract import AbstractScraper
from recipe_urls._utils import get_site_origin

SCRAPERS = {
    AbuelasCounterScraper.host(): AbuelasCounterScraper, 
    ACoupleCooksScraper.host(): ACoupleCooksScraper, 
    AddAPinchScraper.host(): AddAPinchScraper,
    AfghanKitchenRecipesScraper.host(): AfghanKitchenRecipesScraper,
    AllRecipesScraper.host(): AllRecipesScraper, 
    AmbitiousKitchenScraper.host(): AmbitiousKitchenScraper, 
    ArchanasKitchenScraper.host(): ArchanasKitchenScraper, 
    AverieCooksScraper.host(): AverieCooksScraper, 
    BakingMischiefScraper.host(): BakingMischiefScraper, 
    BakingSenseScraper.host(): BakingSenseScraper, 
    BarefootContessaScraper.host(): BarefootContessaScraper, 
    BBCScraper.host(): BBCScraper, 
    BettyCrockerScraper.host(): BettyCrockerScraper, 
    BigOvenScraper.host(): BigOvenScraper, 
    BlueJeanChefScraper.host(): BlueJeanChefScraper, 
    BonAppetitScraper.host(): BonAppetitScraper, 
    BongEatsScraper.host(): BongEatsScraper, 
    BowlOfDeliciousScraper.host(): BowlOfDeliciousScraper, 
    BudgetBytesScraper.host(): BudgetBytesScraper, 
    CarlsbadCravingsScraper.host(): CarlsbadCravingsScraper, 
    CastIronKetoScraper.host(): CastIronKetoScraper, 
    FoodScraper.host(): FoodScraper, 
    Food52Scraper.host(): Food52Scraper, 
    HelloFreshScraper.host(): HelloFreshScraper, 
    NyTimesScraper.host(): NyTimesScraper
}

def scrape_urls(base_url: str) -> AbstractScraper:
    site_origin = get_site_origin(base_url)
    scraper_class = SCRAPERS.get(site_origin)

    if scraper_class:
        scraper_instance = scraper_class(base_url)
        return scraper_instance.scrape()
    else:
        print(f"[__init__.py] Warning: No scraper found for {site_origin}.")
        return []