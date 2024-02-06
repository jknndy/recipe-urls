from typing import List
import re
from recipe_urls._abstract import AbstractScraper

class ArchanasKitchenScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "archanaskitchen"

    def scrape(self) -> List[str]:
        href_links = [a["href"] for a in self.soup.find_all("a", href=True)]

        if not href_links:
            print(f"[archanaskitchen.py] Warning: href_links is empty for {self.base_url}")

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_links(href_links)

        return recipe_links

    def filter_links(self, href_links: List[str]) -> List[str]:
        
        # Filter out unwanted url patterns
        unwanted_patterns = [
            "about",
            "archana-s-kitchen",
            "articles",
            "brands",
            "breakfast",
            "careers",
            "collections", 
            "contact",
            "dinner",
            "ideas",
            "lunch",
            "meal",
            "media",
            "partners",
            "privacy",
            "recipes",
            "team",
            "terms",
            "values",
            "videos",
        ]

        # Site-specific regex for ArchanasKitchen
        recipe_pattern = re.compile(r'/([\w-]+)/?$')

        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set("https://www.archanaskitchen.com{}".format(link) for link in href_links if recipe_pattern.search(link) and not any(re.search(pattern, link) for pattern in unwanted_patterns))

        # Raise an error if no recipe links are found
        if not unique_links_set:
            raise ValueError("[archanaskitchen.py] No recipe links matched the defined pattern for ArchanasKitchen.")

        else:
            print(f"[archanaskitchen.py] {len(unique_links_set)} recipe links found for {self.base_url}.")

        # Convert the set back to a list
        return list(unique_links_set)

