#### [Return Back](../../selenium_with_python.md)

# Handling Multiple Windows in Selenium

Selenium allows you to interact with multiple browser windows or tabs during automation tasks. This capability is useful for scenarios where actions need to be performed across different windows, such as opening links in new tabs or handling pop-up windows.

## Switching Between Windows

### `window_handles`

- **Description:** Returns a list of window handles for all open browser windows.

- **Syntax:**
  ```python
  handles = driver.window_handles
  ```

- **Example:**
  ```python
  # Get window handles
  window_handles = driver.window_handles
  ```

### `switch_to.window(window_handle)`

- **Description:** Switches focus to the specified window handle.

- **Syntax:**
  ```python
  driver.switch_to.window(window_handle)
  ```

- **Example:**
  ```python
  # Switch to the second window
  driver.switch_to.window(window_handles[1])
  ```

## Handling New Windows

### `window_handles`

- **Description:** Use `window_handles` to get handles of all open windows before and after opening a new window. The new window handle will be the one not present in the initial list.

- **Example:**
  ```python
  initial_handles = driver.window_handles

  # Open a new window (e.g., by clicking a link)

  new_handles = [handle for handle in driver.window_handles if handle not in initial_handles]
  new_window_handle = new_handles[0]

  driver.switch_to.window(new_window_handle)
  ```

## Example Usage

```python
from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Open main window
driver.get("https://www.example.com")

# Click a link that opens a new window
link = driver.find_element_by_link_text("Open New Window")
link.click()

# Get window handles
window_handles = driver.window_handles

# Switch to the new window
new_window_handle = [handle for handle in window_handles if handle != driver.current_window_handle][0]
driver.switch_to.window(new_window_handle)

# Perform actions on the new window
print("Title of new window:", driver.title)

# Close the new window
driver.close()

# Switch back to the main window
driver.switch_to.window(window_handles[0])

# Close main window
driver.quit()
```

## Conclusion

Handling multiple windows in Selenium allows you to automate scenarios involving interactions across different browser windows or tabs. By leveraging methods like `window_handles` and `switch_to.window()`, you can seamlessly switch between windows and perform actions as needed. Incorporate window handling techniques into your automation scripts to effectively manage complex workflows and enhance the versatility of your Selenium tests.
