# Twitter Media Downloader

*Read this in other languages: [English](#english), [简体中文](#简体中文)*

---

## English

This project is designed to download media (images) from a specified Twitter user's profile. It uses Selenium WebDriver to automate the login process, and `webdriver_manager` to manage ChromeDriver.

### Prerequisites

Before running the executable, ensure the following prerequisites are met:

1. **VPN Connection**: If access to Twitter is restricted in your location, make sure to connect to a VPN before running the program.
2. **Chrome Browser**: Ensure that the Google Chrome browser is installed on your system. The program will automatically download the appropriate ChromeDriver version.

### Setup

#### Step 1: Download the Executable

Download the `TwitterDownloader.exe` file from the [release page](https://github.com/Cheolhwi/download_image/releases/download/downloadTool/TwitterDownloader.exe).

#### Step 2: Login to Twitter

1. **Run the Executable**: Double-click on `TwitterDownloader.exe` to start the program.
2. **Login**: The program will open a Chrome browser window and navigate to the Twitter login page. Manually enter your credentials and log in to your Twitter account.
3. **Save Cookies**: Once logged in, the program will save the session cookies for future use.

#### Step 3: Download Media

1. **Enter Twitter Username**: After saving the cookies, you will be prompted to enter the Twitter username of the account from which you want to download media.
2. **Download Images**: The program will navigate to the user's media page and start downloading images. The download progress will be displayed in the console.

### Notes

- Ensure that your VPN is connected and stable throughout the process if required.
- Make sure to close any other instances of Chrome running on your system to avoid conflicts.

### How it Works

1. **Login Process**: The program automates the login process using Selenium WebDriver and saves the session cookies.
2. **Download Media**: Using the saved cookies, the program navigates to the specified Twitter user's media page and downloads images to a local folder.

### Dependencies

The program is built using the following libraries:

- `selenium`: For browser automation.
- `webdriver_manager`: For managing ChromeDriver versions.
- `requests`: For downloading images.
- `tqdm`: For displaying download progress.

### Running the Source Code

If you want to run the source code, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Cheolhwi/download_image.git
    cd download_image
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the program**:
    ```bash
    python main.py
    ```

### Troubleshooting

If you encounter any issues:

1. **VPN Issues**: Ensure your VPN is properly connected.
2. **ChromeDriver Errors**: Make sure your Chrome browser is up to date.
3. **Login Issues**: If login fails, manually check your credentials and try again.

## 简体中文

这个项目旨在从指定的Twitter用户的资料中下载媒体（图像）。它使用Selenium WebDriver来自动化登录过程，并使用`webdriver_manager`来管理ChromeDriver。

### 前提条件

在运行可执行文件之前，请确保满足以下前提条件：

1. **VPN连接**：如果您的位置限制访问Twitter，请确保在运行程序之前连接到VPN。
2. **Chrome浏览器**：确保系统上安装了Google Chrome浏览器。程序会自动下载相应版本的ChromeDriver。

### 设置

#### 步骤1：下载可执行文件

从[发布页面](https://github.com/Cheolhwi/download_image/releases/download/downloadTool/TwitterDownloader.exe)下载 `TwitterDownloader.exe` 文件。

#### 步骤2：登录Twitter

1. **运行可执行文件**：双击 `TwitterDownloader.exe` 以启动程序。
2. **登录**：程序将打开一个Chrome浏览器窗口并导航到Twitter登录页面。手动输入您的凭据并登录到您的Twitter帐户。
3. **保存Cookies**：登录后，程序将保存会话Cookies以供将来使用。

#### 步骤3：下载媒体

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

