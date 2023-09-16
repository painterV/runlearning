XPath（XML Path Language）是一种用于在 XML 文档中定位和选择元素的语言。在网页爬虫中，XPath 也常用于解析和提取 HTML 页面的元素。以下是XPath的一些基本用法和示例：

**XPath 基本用法：**

1. **选取元素：**
   - 使用 `/` 来选择直接子元素，例如 `/html/body/div` 会选取 HTML 文档中 `<html>` 下的 `<body>` 下的所有 `<div>` 元素。
   - 使用 `//` 来选择所有后代元素，例如 `//div` 会选取文档中所有的 `<div>` 元素。

2. **谓语（Predicates）：**
   - 使用方括号 `[]` 来添加谓语，以过滤选择的元素。
   - 例如，`//div[@class="example"]` 会选取所有 class 属性为 "example" 的 `<div>` 元素。

3. **属性选择：**
   - 使用 `@` 符号来选取元素的属性。
   - 例如，`//a[@href]` 会选取所有包含 `href` 属性的 `<a>` 元素。

4. **文本内容：**
   - 使用 `text()` 函数来选取元素的文本内容。
   - 例如，`//h1/text()` 会选取所有 `<h1>` 元素的文本内容。

5. **位置：**
   - 使用数字来选择特定位置的元素。
   - 例如，`//div[1]` 会选取文档中第一个 `<div>` 元素。

**XPath 示例：**

假设您有以下HTML文档：

```html
<html>
  <body>
    <div class="container">
      <h1>Title</h1>
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
      </ul>
    </div>
  </body>
</html>
```

以下是一些XPath示例：

- 选取 `<h1>` 元素的文本内容：

  ```
  //h1/text()
  ```

- 选取所有 `<li>` 元素的文本内容：

  ```
  //li/text()
  ```

- 选取 class 为 "container" 的 `<div>` 元素下的所有 `<li>` 元素：

  ```
  //div[@class="container"]//li
  ```

- 选取第一个 `<li>` 元素的文本内容：

  ```
  //li[1]/text()
  ```

XPath 是一个强大的工具，可以帮助您精确地定位和提取网页中的元素。您可以使用不同的 XPath 表达式来适应不同的选择和提取需求。在爬虫和数据提取任务中，XPath 是一种常用的技术。