#### [Return Back](../../selenium_with_python.md)

# Browser Commands

## Navigation Commands

### `get(url)`

- Description: Loads a new web page in the current browser window.
- Example:
  ```python
  driver.get("https://www.example.com")
  ```

### `back()`

- Description: Navigates backward in the browser's history.
- Example:
  ```python
  driver.back()
  ```

### `forward()`

- Description: Navigates forward in the browser's history.
- Example:
  ```python
  driver.forward()
  ```

### `refresh()`

- Description: Reloads the current web page.
- Example:
  ```python
  driver.refresh()
  ```

**Window Handling Commands**

### `maximize_window()`

- Description: Maximizes the current browser window.
- Example:
  ```python
  driver.maximize_window()
  ```

### `set_window_size(width, height)`

- Description: Sets the size of the current browser window.
- Example:
  ```python
  driver.set_window_size(1024, 768)
  ```

### `switch_to.window(window_name)`

- Description: Switches focus to a different browser window or tab.
- Example:
  ```python
  driver.switch_to.window("windowName")
  ```

### `close()`

- Description: Closes the current browser window.
- Example:
  ```python
  driver.close()
  ```

## Interaction Commands

### `find_element_by_*()`

- Description: Finds a single web element using various locators such as ID, name, XPath, CSS selector, etc.
- Example:
  ```python
  element = driver.find_element_by_id("element_id")
  ```

### `find_elements_by_*()`

- Description: Finds multiple web elements using various locators.
- Example:
  ```python
  elements = driver.find_elements_by_css_selector(".item")
  ```

### `execute_script(script, *args)`

- Description: Executes JavaScript code in the context of the current browser window.
- Example:
  ```python
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  ```

## Miscellaneous Commands

### `quit()`

- Description: Quits the browser session, closing all windows associated with it.
- Example:
  ```python
  driver.quit()
  ```

### `title`

- Description: Returns the title of the current web page.
- Example:
  ```python
  title = driver.title
  ```

### `current_url`

- Description: Returns the URL of the current web page.
- Example:
  ```python
  url = driver.current_url
  ```

These browser commands in Selenium empower you to automate web interactions effectively. Whether you're navigating between pages, interacting with elements, handling windows, or executing JavaScript, Selenium provides a comprehensive set of tools to streamline your testing and automation tasks. Experiment with these commands to create robust and efficient automation scripts tailored to your specific requirements.
