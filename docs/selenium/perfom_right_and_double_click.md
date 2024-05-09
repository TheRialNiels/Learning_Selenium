#### [Return Back](../../selenium_with_python.md)

# Performing Right and Double Click in Selenium

In Selenium, you can simulate right-click and double-click actions using the `ActionChains` class. These actions are useful for interacting with context menus, triggering specific functionalities, or selecting multiple items.

## Importing ActionChains

### `from selenium.webdriver.common.action_chains import ActionChains`

- **Description:** Import the `ActionChains` class from Selenium to perform mouse actions.

- **Syntax:**
  ```python
  from selenium.webdriver.common.action_chains import ActionChains
  ```

## Performing Right Click

### `context_click(on_element)`

- **Description:** Performs a right-click action on the specified element.

- **Syntax:**
  ```python
  actions = ActionChains(driver)
  actions.context_click(element).perform()
  ```

- **Example:**
  ```python
  from selenium.webdriver.common.action_chains import ActionChains

  element = driver.find_element_by_id("element_id")
  actions = ActionChains(driver)
  actions.context_click(element).perform()
  ```

## Performing Double Click

### `double_click(on_element)`

- **Description:** Performs a double-click action on the specified element.

- **Syntax:**
  ```python
  actions = ActionChains(driver)
  actions.double_click(element).perform()
  ```

- **Example:**
  ```python
  from selenium.webdriver.common.action_chains import ActionChains

  element = driver.find_element_by_id("element_id")
  actions = ActionChains(driver)
  actions.double_click(element).perform()
  ```

## Example Usage

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Initialize WebDriver
driver = webdriver.Chrome()

# Open URL with elements to interact with
driver.get("https://www.example.com")

# Find element for right-click action
right_click_element = driver.find_element_by_id("right_click_element")

# Perform right-click action
actions = ActionChains(driver)
actions.context_click(right_click_element).perform()

# Find element for double-click action
double_click_element = driver.find_element_by_id("double_click_element")

# Perform double-click action
actions = ActionChains(driver)
actions.double_click(double_click_element).perform()

# Close WebDriver
driver.quit()
```

## Conclusion

Performing right-click and double-click actions in Selenium allows you to simulate user interactions that involve these mouse actions. By using the `ActionChains` class and its methods like `context_click()` and `double_click()`, you can programmatically trigger context menus, select multiple items, or perform specific functionalities that respond to these mouse actions. Incorporate right-click and double-click actions into your Selenium automation scripts to enhance their versatility and simulate real-world user interactions effectively.
