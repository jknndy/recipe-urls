from recipe_urls import scrape_urls

links = scrape_urls('https://www.eatingwell.com/recipes/')


base_urls = [
    "https://abuelascounter.com", 
    "https://www.acouplecooks.com", 
    "https://addapinch.com", 
    "http://www.afghankitchenrecipes.com", 
    "https://www.allrecipes.com", 
    "https://www.ambitiouskitchen.com", 
    "https://www.archanaskitchen.com", 
    "https://www.averiecooks.com", 
    "https://bakingmischief.com", 
    "https://www.baking-sense.com", 
    "https://barefootcontessa.com", 
    "https://www.bbc.co.uk/food/", 
    "https://www.bettycrocker.com", 
    "https://www.bigoven.com", 
    "https://bluejeanchef.com", 
    "https://www.bonappetit.com", 
    "https://www.bongeats.com", 
    "https://www.bowlofdelicious.com", 
    "https://www.budgetbytes.com",
    "https://carlsbadcravings.com",  
    "https://www.castironketo.net", 
    "https://www.cdkitchen.com", 
    "https://chefsavvy.com",
    "https://www.closetcooking.com/top-recipes/",  
    "https://cookieandkate.com/recipes/", 
    "https://www.eatingwell.com/recipes/", 
    "https://www.food.com", 
    "https://food52.com", 
    "https://www.hellofresh.com/recipes", 
    "https://ninjatestkitchen.eu", 
    "https://cooking.nytimes.com"
]

compiled_recipe_links = []

for base_url in base_urls:
    compiled_recipe_links.extend(scrape_urls(base_url))

print(len(compiled_recipe_links))

