"""
BasePage holds behaviour shared by every page object in the framework:
navigation, common header/footer elements, and generic wait helpers.
All page objects should extend this class.
"""

from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self,page:Page):
        self.page = page
        self.explore_all_courses_button = self.page.get_by_role("link", name='Explore all courses at RahulShettyAcademy.com')
        self.explore_skill_assessment_button = self.page.get_by_role("link",name='Explore Skill Assessments — QA Job Hiring Platform')

    def goto(self,path:str="/")->None:
        """Navigates to a relative path off the configured base_url."""
        self.page.goto(path,wait_until="domcontentloaded")

    def get_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url

    def click_explore_all_courses(self):
        self.explore_all_courses_button.click()

    def click_explore_skill_assessment(self):
        self.explore_skill_assessment_button.click()

    def wait_for_page_load(self)->None:
        try:
            self.page.wait_for_load_state("networkidle",timeout=15_000)
        except Exception:
            # networkidle can time out on pages with polling/analytics scripts; safe to ignore.
            pass
    def expect_heading_to_contain(self,text:str)->None:
        heading = self.page.locator("h2").first
        expect(heading).to_contain_text(text,ignore_case=True,timeout=15_000)

