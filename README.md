# recipe-urls (Under Development)

## Overview

`recipe-urls` is a Python package designed to gather recipe URLs from a given base URL.

## Installation

Note: This package is currently under development and not available for installation through pip.

<!-- ```bash
pip install recipe-urls
``` -->

## Usage

```python
from recipe_urls import scrape_urls
```

## Example usage

```python
base_urls = ['https://bakingmischief.com', 'https://www.allrecipes.com']
compiled_recipe_links = []

for base_url in base_urls:
    recipes = scrape_urls(base_url)
    compiled_recipe_links.extend(recipes)
```

## Supported Websites (So Far!)

- https://abuelascounter.com
- https://www.acouplecooks.com
- https://addapinch.com//
- http://www.afghankitchenrecipes.com
- https://www.allrecipes.com
- https://www.ambitiouskitchen.com
- https://www.archanaskitchen.com
- https://www.averiecooks.com
- https://bakingmischief.com
- https://www.baking-sense.com
- https://barefootcontessa.com
- https://www.bbc.co.uk/food/
- https://www.bettycrocker.com
- https://www.bigoven.com
- https://bluejeanchef.com/recipes/
- https://www.bonappetit.com
- https://www.bongeats.com
- https://www.bowlofdelicious.com
- https://www.budgetbytes.com
- https://www.food.com
- https://food52.com
- https://www.hellofresh.com/recipes
- https://cooking.nytimes.com


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.