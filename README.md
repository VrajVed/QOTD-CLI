# Quote of the day CLI program

A simple script to execute on your powershell terminal, that fetches a random code from a quote site, parses the json data and prints the output in your terminal!</br>

## Usage:

To Use, Clone the repo and run the following in your powershell:</br>
`git clone https://github.com/VrajVed/QOTD-CLI.git`</br>
`cd  QOTD-CLI`</br>
Navigate to the src file and execute the program: </br>
`cd src`</br>
`python QOTD-CLI.py`</br>

#### Alternatively, through powershell profile:

`notepad.exe $PROFILE`</br>
Navigate to your cloned script for the path, and type in the following:
`& python "your_file_path.py"`
Save the file, close the powershell terminal, and open the terminal. It will display your quote.

Note - *You might need to change execution policy if windows blocks it:*</br>
`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` and now you're good to go

## Features: 
- Fetches a random quote everytime.
- Fast and efficient.
- Displays the quote and the author in a clean format.
- Simple, readable script in python.
- Aesthetically pleasing and no bs.

## Requirements:
- user should have python v3.0+ installed.
- user should have `requests` library installed.</br>
If not, run `pip install requests`

## My Inspiration:
A good inspirational quote always helps you no matter how low you feel. Aesthetically pleasing and works like a charm.

## License:
This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).</br>
You are free to use, modify, and distribute this software under the terms of the GPLv3. Any modifications or derivative works must also be open-sourced under the same license.

# Thank you for using my program !
