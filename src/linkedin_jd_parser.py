from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def linkedin_jd_parser(url:str) -> str:
    """_summary_

    Args:
        url (str): _description_

    Returns:
        str: _description_
    """

    driver = webdriver.Chrome()

    driver.get(url)

    show_more_button = driver.find_element(By.CLASS_NAME, "show-more-less-html__button")
    driver.execute_script("arguments[0].click();", show_more_button)

    updated_html = driver.page_source

    soup = BeautifulSoup(updated_html, "html.parser")

    driver.quit()

    job_name = soup.find('h1').text
    company_name = soup.find('a', class_='topcard__org-name-link topcard__flavor--black-link').text.strip()
    job_location = soup.find('span', class_='topcard__flavor topcard__flavor--bullet').text.strip()
    posted_time = soup.find('span', class_='posted-time-ago__text topcard__flavor--metadata').text.strip()
    job_description = soup.find('div', class_='show-more-less-html__markup relative overflow-hidden').text.strip()

    info_dict = {'Job Name': job_name, 
            'Company Name': company_name, 
            'Job Location': job_location, 
            'Posted Time': posted_time, 
            'Job Description': job_description}
    
    return info_dict

if __name__ == "__main__":
    print(linkedin_jd_parser("https://www.linkedin.com/jobs/view/3664919987"))