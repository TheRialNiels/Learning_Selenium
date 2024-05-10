#### [Return Back](../../selenium_with_python.md)

# Waits in Selenium

Waits in Selenium are essential for handling synchronization issues between test automation scripts and web applications. They ensure that the script waits for specific conditions to be met before proceeding with further actions, thereby improving the stability and reliability of automated tests. Selenium provides different types of waits, including explicit wait, implicit wait, and fluent wait, each serving distinct purposes.

## Implicit Wait

### `implicitly_wait(time_to_wait)`

- **Description:** Sets a maximum amount of time for Selenium to wait for an element to appear in the DOM before raising a `NoSuchElementException`.

- **Syntax:**
  ```python
  driver.implicitly_wait(time_to_wait)
  ```

- **Example:**
  ```python
  driver.implicitly_wait(10)  # Wait for up to 10 seconds
  ```

## Explicit Wait

Explicit waits allow you to wait for a certain condition to occur before proceeding with further actions. This wait is more flexible and granular compared to implicit waits, as it waits only for specific conditions to be met.

### WebDriverWait

#### `WebDriverWait(driver, timeout).until(expected_condition)`

- **Description:** Waits until the specified condition is met or the timeout expires.

- **Syntax:**
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  element = WebDriverWait(driver, timeout).until(EC.some_condition)
  ```

- **Example:**
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "element_id")))
  ```

### Expected Conditions

#### Various expected conditions can be used with WebDriverWait:

- `presence_of_element_located(locator)`
- `visibility_of_element_located(locator)`
- `element_to_be_clickable(locator)`
- `title_contains(title)`
- `alert_is_present()`
- ...and more.

## Fluent Wait

Fluent waits provide more flexible control over wait conditions by allowing you to define polling intervals and ignore specific exceptions.

### `WebDriverWait(driver, timeout, poll_frequency, ignored_exceptions).until(condition)`

- **Description:** Waits until the specified condition is met or the timeout expires, with custom polling frequency and exceptions to ignore.

- **Syntax:**
  ```python
  from selenium.webdriver.support.ui import WebDriverWait

  wait = WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
  element = wait.until(condition)
  ```

- **Example:**
  ```python
  from selenium.webdriver.support.ui import WebDriverWait

  wait = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException])
  element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))
  ```

## Conclusion

Waits in Selenium play a crucial role in ensuring the stability and reliability of automated tests by synchronizing script execution with the behavior of web applications. By understanding and utilizing implicit waits, explicit waits with WebDriverWait, and fluent waits, you can handle various synchronization issues effectively and create robust automation scripts capable of handling dynamic web environments. Choose the appropriate wait strategy based on your specific testing requirements and the behavior of the application under test.
