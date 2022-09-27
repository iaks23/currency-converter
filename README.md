# 💰 Frankfurter Currency Converter
<img src="https://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/9f54815822d853b.png" align="right" width="120"/>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge powered-by-electricity](http://ForTheBadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)

A currency converter to calculate rates from historical dates using the [FrankfurterAPI](https://www.frankfurter.app)

[![star-useful](https://img.shields.io/badge/🌟-If%20useful-red.svg)](https://shields.io) 
[![view-repo](https://img.shields.io/badge/View-Repo-blueviolet)](https://github.com/iaks23?tab=repositories)
[![view-profile](https://img.shields.io/badge/Go%20To-Profile-orange)](https://github.com/iaks23) 

## 🪪 Author
##### Name: Akshaya Parthasarathy
##### Student ID: 14081133

## 💡 Description

### The Application

The currency converter python programs takes in input arguements of a partivular date and two currency codes from the user, and provides the conversion rate as well as the inverse rate for the specified date. 

### Challenged faced

> Working with JSON response objects 

Some of the responses recceived in making API calls involved nested JSON objects which take a while to decode and figure out.

> Figuring out the correct URL

In cases where the URL needs to take in multiple arguments, such as calculating rate for a particular time, and incorrect URL can result in errors.

### Future Implementations

A currency converter app can be expanded further to retrieve a timeline of rates to figure out the days in which rates of a particular country was the highest or lowest. 

It can also be combined with a simple alert feature using Python to set up an automated mail or alert system to tell the user of particular currency rates of interest. 

## 🛠 How to Setup

In order to run this program or edit the code, you will require Python 3 and Visual Studio Code.

You can download and install VS Code from [here](https://code.visualstudio.com)

Please make sure your workstation is installed with Python 3, preferably.  

<details> 
  <summary>
    For Windows Users
  </summary>
  
  See how you can install python 
  [here](https://phoenixnap.com/kb/how-to-install-python-3-windows) 
  
 </details>
  
  <details> 
  <summary>
    For MAC OS Users
  </summary>
  
  
  
  You can download latest version of Python [here](https://www.python.org/downloads/macos/) 
 
  
  
  </details>

## ⚙️ How to Run the Program

Run the following command on your Windows Command Prompt/MAC OS Terminal

```python
python main.py 2019-09-07 USD AUD
```

The general pattern to run the program is: 

```python
python main.py <YYYY-MM-DD> <ORIGIN CURRENCY CODE> <DESTINATION CURRENCY CODE>
```

## 📂 Project Structure

```

.main/              <- Main branch
│
├── README.md        <- Markdown file containing project details
│
├── main.py           <- Main python file to call all other functions from
│
├── api.py        <- Python file that makes call to the API
│
├── checks.py           <- Python file to perform validation on user inputs
│
├── frankfurter.py          <- Python file to perform validation checks on currency conversions
│
├── currency.py           <- Python file that retrieves all data, calculates inverse rates, and displays output to users
│
├── test.py           <- Python unit tests

```


## 📎 Citations

1) https://www.frankfurter.app
2) https://github.com/hakanensari/frankfurter
