import {Locator, Page} from "@playwright/test";

export class RegisterPage{
    private readonly page:Page;
    private readonly email_text_field:Locator;
    private readonly password_text_field:Locator;
    private readonly confirm_password_text_field:Locator;
    private readonly create_account_button:Locator;
    private readonly sign_in_link:Locator;
    private readonly explore_all_courses_button:Locator;
    private readonly explore_skill_assessments_button:Locator;
    private readonly email_blank_warning_message:Locator;
    private readonly password_blank_warning_message:Locator;

    constructor(page:Page){
        this.page = page;
        this.email_text_field = page.locator("#register-email");
        this.password_text_field = page.locator("#register-password");
        this.confirm_password_text_field = page.getByPlaceholder('Repeat your password', { exact: false });
        this.create_account_button = page.locator("#register-btn");
        this.sign_in_link = page.getByRole('link', { name: /Sign in/i });
        this.explore_all_courses_button = page.getByRole('link', { name: 'Explore all courses at RahulShettyAcademy.com' });
        this.explore_skill_assessments_button = page.getByRole('link', { name: 'Explore Skill Assessments — QA Job Hiring Platform' });
        this.email_blank_warning_message = page.getByText('Enter a valid email', { exact: false });
        this.password_blank_warning_message = page.getByText('Password does not meet the requirements below', { exact: false });
    }

    async navigateToRegisterPage(){
        await this.page.goto("https://eventhub.rahulshettyacademy.com/register");
    }

    async clickRegisterButton(){
        await this.create_account_button.click();
    }

    async setEmail(email:string){
        await this.email_text_field.fill(email);
    }



    

}