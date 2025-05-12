# Network-Communication-detector

A Python tool that monitors suspicious mining activity on your system by checking network connections on common mining ports. The program uses `psutil` to get system information and `pystyle` to enhance terminal output with colors and effects.
## How the Script Works

This script is designed to **detect potential cryptocurrency mining activity** by monitoring your computer's **network connections** in real time.

###  Step-by-Step Breakdown

1. **Imports system tools**  
   The script uses `psutil` to access low-level system data like active network connections and running processes.

2. **Stylized interface**  
   With `pystyle`, the script prints a stylish ASCII banner and colorful output for better readability and user experience.

3. **Monitors active connections**  
   It constantly checks for active network connections using:
   ```python
   psutil.net_connections(kind='inet')
4. **Live monitoring**
  The script runs in a loop with a refresh interval (default is 2 seconds).
  During each refresh:

  It updates the list of active connections

  **Prompts the user to:**

  Press c to clear today's log file

  Press q to quit the monitoring

5. **Optional log clearing**
If you choose to clear the log, the script will delete the current day's log file (if it exists).


## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).
### Key Features:
![Terminal Output](path/to/your/image.png)


### Steps to install:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Network-Communication-detector.git
