# Twitter Media Downloader

这个项目旨在从指定的Twitter用户的资料中下载媒体（图像）。它使用Selenium WebDriver来自动化登录过程，并使用`webdriver_manager`来管理ChromeDriver。

*[阅读其他语言的内容: [English](https://github.com/Cheolhwi/download_image/blob/master/README.md)]*

## 前提条件

在运行可执行文件之前，请确保满足以下前提条件：

1. **VPN连接**：如果您的位置限制访问Twitter，请确保在运行程序之前连接到VPN。
2. **Chrome浏览器**：确保系统上安装了Google Chrome浏览器。程序会自动下载相应版本的ChromeDriver。

## 设置

### 步骤1：下载可执行文件

从[发布页面](https://github.com/Cheolhwi/download_image/releases/)下载 `TwitterDownloader.exe` 文件。

### 步骤2：登录Twitter

1. **运行可执行文件**：双击 `TwitterDownloader.exe` 以启动程序。
2. **登录**：程序将打开一个Chrome浏览器窗口并导航到Twitter登录页面。手动输入您的凭据并登录到您的Twitter帐户。
3. **保存Cookies**：登录后，程序将保存会话Cookies以供将来使用。

### 步骤3：下载媒体

1. **输入Twitter用户名**：保存Cookies后，系统将提示您输入要从中下载媒体的帐户的Twitter用户名。
2. **下载图像**：程序将导航到用户的媒体页面并开始下载图像。下载进度将显示在控制台中。

### 注意事项

- 如果需要，请确保您的VPN在整个过程中都已连接并保持稳定。
- 确保关闭系统上运行的其他Chrome实例以避免冲突。

### 工作原理

1. **登录过程**：程序使用Selenium WebDriver自动化登录过程并保存会话Cookies。
2. **下载媒体**：使用保存的Cookies，程序导航到指定的Twitter用户的媒体页面并将图像下载到本地文件夹。

### 依赖项

该程序使用以下库构建：

- `selenium`：用于浏览器自动化。
- `webdriver_manager`：用于管理ChromeDriver版本。
- `requests`：用于下载图像。
- `tqdm`：用于显示下载进度。

### 运行源代码

如果您想运行源代码，请按照以下步骤操作：

1. **克隆仓库**：
    ```bash
    git clone https://github.com/Cheolhwi/download_image.git
    cd download_image
    ```

2. **安装依赖项**：
    ```bash
    pip install -r requirements.txt
    ```

3. **运行程序**：
    ```bash
    python main.py
    ```

### 故障排除

如果您遇到任何问题：

1. **VPN问题**：确保您的VPN已正确连接。
2. **ChromeDriver错误**：确保您的Chrome浏览器是最新的。
3. **登录问题**：如果登录失败，请手动检查您的凭据并重试。

## 贡献

欢迎贡献。请随时打开问题或提交拉取请求。

## 许可证

这个项目是根据MIT许可证授权的。
