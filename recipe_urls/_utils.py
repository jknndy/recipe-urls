from typing import Optional
from urllib.parse import urlparse

def get_site_origin(base_url: str) -> Optional[str]:
    site_origins = [
        'abuelascounter.com', 
        'www.acouplecooks.com', 
        'addapinch.com', 
        'www.afghankitchenrecipes.com', 
        'www.allrecipes.com', 
        'www.ambitiouskitchen.com', 
        'www.archanaskitchen.com', 
        'www.averiecooks.com',
        'bakingmischief.com',
        'www.baking-sense.com',
        'barefootcontessa.com',
        'www.bbc.co.uk',  
        'www.bettycrocker.com', 
        'www.bigoven.com', 
        'bluejeanchef.com', 
        'www.bonappetit.com', 
        'www.bongeats.com',
        'www.bowlofdelicious.com', 
        'www.budgetbytes.com', 
        'carlsbadcravings.com', 
        'www.castironketo.net', 
        'www.cdkitchen.com', 
        'chefsavvy.com', 
        'www.closetcooking.com', 
        'cookieandkate.com',
        'copykat.com', 
        'www.countryliving.com',
        'creativecanning.com',  
        'www.davidlebovitz.com', 
        'www.delish.com', 
        'domesticate-me.com', 
        'downshiftology.com', 
        'www.eatingbirdfood.com', 
        'www.eatingwell.com', 
        'www.eatliverun.com', 
        'eatsmarter.com', 
        'www.eatwell101.com', 
        'eatwhattonight.com', 
        'elavegan.com', 
        'www.ethanchlebowski.com', 
        'www.errenskitchen.com', 
        'www.epicurious.com', 
        'www.farmhouseonboone.com', 
        'www.fifteenspatulas.com', 
        'www.finedininglovers.com', 
        'fitmencook.com', 
        'fitslowcookerqueen.com', 
        'www.food.com',
        'food52.com',
        'www.foodandwine.com', 
        'www.foodnetwork.com', 
        'www.foodrepublic.com', 
        'www.hellofresh.com',
        'ninjatestkitchen.eu', 
        'cooking.nytimes.com'
    ]

    parsed_url = urlparse(base_url).hostname
    for site_origin in site_origins:
        if site_origin == parsed_url:
            return site_origin

    raise ValueError(f"URL '{base_url}' is not supported.")