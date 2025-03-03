# 中山大学健身房自动预约

本 Python 脚本使用 Selenium 自动预约中山大学健身房。

## 先决条件

1. **已安装 Google Chrome 浏览器。**
2. **ChromeDriver 版本需与 Chrome 浏览器匹配。**
3. **已安装 Python 3.x。**
4. **安装所需的 Python 库：**
   ```sh
   pip install selenium webdriver-manager
   ```
5. **chrome安装tampermonkey插件，安装脚本：**
   ```sh
   https://greasyfork.org/zh-CN/scripts/419757-%E4%B8%AD%E5%A4%A7%E8%87%AA%E5%8A%A8%E9%AA%8C%E8%AF%81%E7%A0%81%E8%AE%A4%E8%AF%81
   ```


## 使用方法

1. **克隆或下载此仓库。**
2. **修改脚本以设置 Chrome 配置文件路径：**
   ```python
   options.add_argument("--user-data-dir=/Users/username/Library/Application Support/Google/Chrome")
   options.add_argument("profile-directory=Profile 3")
   ```
   **更改上述路径，使其与本地 Chrome 用户数据和配置文件匹配。**
3. **运行脚本：**
   ```sh
   python final.py
   ```
4. **在提示时输入预约时间：**
   - `T1416` → 14:00 - 16:00
   - `T1618` → 16:00 - 18:00
   - `T1820` → 18:00 - 20:00
   - `T2022` → 20:00 - 22:00

## 功能

- **使用已登录的 Chrome 配置文件自动登录。**
- **自动选择深圳校区和健身房。**
- **预约后天的健身时间。**
- **遇到错误时保存屏幕截图和网页源代码。**

## 注意事项

- **确保您已在 Chrome 配置文件中登录健身房预约网站。**
- **XPath 可能会变化，如果脚本无法运行，请更新 XPath。**

## 故障排除

- **如果脚本失败，请查看保存的 `error.png` 截图和 `page.html` 进行调试。**
- **确保 ChromeDriver 为最新版本：**
  ```sh
  pip install --upgrade webdriver-manager
  ```
