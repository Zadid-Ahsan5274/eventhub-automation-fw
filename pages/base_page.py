"""
BasePage holds behaviour shared by every page object in the framework:
navigation, common header/footer elements, and generic wait helpers.
All page objects should extend this class.
"""

from playwright.sync_api import Page, Expect, Locator

class BasePage:
    def __init__(self,page:Page):
        self.page = page
        self.explore_all_courses_button = self.page.get_by_role("link", name='Explore all courses at RahulShettyAcademy.com')
        self.explore_skill_assessment_button = self.page.get_by_role("link",name='Explore Skill Assessments — QA Job Hiring Platform')

    def goto(self,path:str="/")->None:
        """Navigates to a relative path off the configured base_url."""
        self.page.goto(path,wait_until="domcontentloaded")

    