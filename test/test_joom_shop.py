from selenium.webdriver import Chrome
import pytest
from selenium.webdriver.common.by import By


class TestJoomShop:
    @pytest.mark.basic_web_element_search
    def test_basic_web_element_search(self, chrome_joom_browser: Chrome):

        chrome_joom_browser.find_element(By.CSS_SELECTOR, "a[href$=entrance]").click()

        chrome_joom_browser.find_element(By.CSS_SELECTOR, "button.close___3u6yL").click()

        search_field = chrome_joom_browser.find_element(By.CSS_SELECTOR, "div input")
        search_button = chrome_joom_browser.find_element(By.CSS_SELECTOR, 'button.submit___3XMCO')

        assert search_button.is_enabled(), "Search button is enabled when dialog is not active but shouldn't"
        search_field.send_keys("Bubochka")
        search_field.clear()

        search_field.send_keys("swiss tool")

        search_button.click()

        found_tools_items = chrome_joom_browser.find_elements(By.CSS_SELECTOR, "a.content___1H7Wg")

        assert len(found_tools_items) > 10, f"Total items of search results is {len(found_tools_items)}. " \
                                            f"It is less then 10."

        for item in found_tools_items:
            price = item.find_element(By.CSS_SELECTOR, "div.price___9GCnp")
            description = item.find_element(By.CSS_SELECTOR, "div.name___1aqk8")

            # descriptions = item.find_elements(By.CSS_SELECTOR, "div.name___1aqk8")
            # assert len(descriptions) > 0
            # description = descriptions[0]

            assert price.text is not None, f"Item price text is {price.text}."
            assert description.text is not None, f"Item description text is {description.text}."
            assert price.text.__contains__('UAH'), f"Item price text do not contain 'UAH'."
            assert len(description.text) > 0, f"Description text is absent."

            should_be_not_found_elements = item.find_elements(By.CSS_SELECTOR, "div.name___zzzzzz")
            assert len(should_be_not_found_elements) == 0, f"Not existing element exist))"
