#### [Return Back](../../selenium_with_python.md)

# Handling Drag and Drop in Selenium

Drag and drop interactions involve clicking and holding an element, dragging it to a new location, and then releasing it. Selenium provides methods to simulate these actions using the `ActionChains` class, allowing you to automate drag and drop functionality in web applications.

## Importing ActionChains

### `from selenium.webdriver.common.action_chains import ActionChains`

- **Description:** Import the `ActionChains` class from Selenium for performing mouse actions.

- **Syntax:**
  ```python
  from selenium.webdriver.common.action_chains import ActionChains
  ```

## Performing Drag and Drop

### `click_and_hold(draggable_element)`

- **Description:** Clicks and holds the specified draggable element.

- **Syntax:**
  ```python
  actions.click_and_hold(draggable_element).perform()
  ```

### `move_to_element(target_element)`

- **Description:** Moves the mouse pointer to the specified target element.

- **Syntax:**
  ```python
  actions.move_to_element(target_element).perform()
  ```

### `release()`

- **Description:** Releases the mouse button to drop the draggable element at its current position.

- **Syntax:**
  ```python
  actions.release().perform()
  ```

## Example Usage

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Initialize WebDriver
driver = webdriver.Chrome()

# Open URL with draggable elements
driver.get("https://www.example.com")

# Find draggable and target elements
draggable = driver.find_element_by_id("draggable_element")
target = driver.find_element_by_id("target_element")

# Perform drag and drop action
actions = ActionChains(driver)
actions.click_and_hold(draggable).move_to_element(target).release().perform()

# Close WebDriver
driver.quit()
```

# Handling Drag and Drop of Elements in a Frame

When dealing with drag and drop interactions involving elements within a frame, it's essential to switch the WebDriver's focus to the frame containing the draggable elements before performing the action. Below is an example demonstrating how to handle drag and drop operations when the draggable elements are located within a frame.

## Importing Required Libraries

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
```

## Initializing WebDriver and Opening the URL

```python
# Initialize WebDriver
driver = webdriver.Chrome()

# Open URL containing draggable elements within a frame
driver.get("https://www.example.com")

# Switch to the frame containing draggable elements
driver.switch_to.frame("frame_name_or_id")
```

## Locating Draggable and Target Elements

```python
# Find draggable and target elements within the frame
draggable = driver.find_element_by_id("draggable_element_id")
target = driver.find_element_by_id("target_element_id")
```

## Performing Drag and Drop Action

```python
# Perform drag and drop action within the frame
actions = ActionChains(driver)
actions.drag_and_drop(draggable, target).perform()
```

## Switching Back to Default Content (Main Document)

After completing the drag and drop action within the frame, it's essential to switch the WebDriver's focus back to the default content (main document) if further interactions are required outside the frame.

```python
# Switch back to the default content (main document)
driver.switch_to.default_content()
```
