# Twitter Media Downloader

This project is designed to download media (images) from a specified Twitter user's profile. It uses Selenium WebDriver to automate the login process, and `webdriver_manager` to manage ChromeDriver.

*[Read this in other languages: [简体中文]([README_zh.md](https://github.com/Cheolhwi/download_image/blob/master/readmezh.md))]*

## Prerequisites

Before running the executable, ensure the following prerequisites are met:

1. **VPN Connection**: If access to Twitter is restricted in your location, make sure to connect to a VPN before running the program.
2. **Chrome Browser**: Ensure that the Google Chrome browser is installed on your system. The program will automatically download the appropriate ChromeDriver version.

## Setup

### Step 1: Download the Executable

Download the `TwitterDownloader.exe` file from the [release page](https://github.com/Cheolhwi/download_image/releases/download/downloadTool/TwitterDownloader.exe).

### Step 2: Login to Twitter

1. **Run the Executable**: Double-click on `TwitterDownloader.exe` to start the program.
2. **Login**: The program will open a Chrome browser window and navigate to the Twitter login page. Manually enter your credentials and log in to your Twitter account.
3. **Save Cookies**: Once logged in, the program will save the session cookies for future use.

### Step 3: Download Media

1. **Enter Twitter Username**: After saving the cookies, you will be prompted to enter the Twitter username of the account from which you want to download media.
2. **Download Images**: The program will navigate to the user's media page and start downloading images. The download progress will be displayed in the console.

### Notes

- Ensure that your VPN is connected and stable throughout the process if required.
- Make sure to close any other instances of Chrome running on your system to avoid conflicts.

## How it Works

1. **Login Process**: The program automates the login process using Selenium WebDriver and saves the session cookies.
2. **Download Media**: Using the saved cookies, the program navigates to the specified Twitter user's media page and downloads images to a local folder.

## Dependencies

The program is built using the following libraries:

- `selenium`: For browser automation.
- `webdriver_manager`: For managing ChromeDriver versions.
- `requests`: For downloading images.
- `tqdm`: For displaying download progress.

## Running the Source Code

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

## Troubleshooting

If you encounter any issues:

1. **VPN Issues**: Ensure your VPN is properly connected.
2. **ChromeDriver Errors**: Make sure your Chrome browser is up to date.
3. **Login Issues**: If login fails, manually check your credentials and try again.

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
