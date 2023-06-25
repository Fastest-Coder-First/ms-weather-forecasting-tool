
# weather-forecasting-tool &nbsp;
## Introduction 
A simple command line tool to get weather forecast for a given city. Made using object-oriented programming in Python, that shows current weather and weather forecast for today, tomorrow and next 5 days.
___

### Check Out:
1. [Demo Video](#demo-video)
1. [Instructions](#instructions)
2. [Architecture Diagrams](#architecture-diagrams)
3. [Github Copilot Usecases](#github-copilot-use-cases)
5. [Tech Stack](#tech-stack)
6. [Team](#made-with--by)
___

## Demo Video

https://github.com/Fastest-Coder-First/ms-weather-forecasting-tool/assets/63065397/87ee92f6-23aa-44aa-b567-12fe18cd0200

___

## Instructions
### SET-UP
- Clone the repository:
    ```bash
    git clone https://github.com/Fastest-Coder-First/ms-weather-forecasting-tool.git
    ```
- Sign up on [OpenWeather](https://home.openweathermap.org/) to get your private API key.
- Copy the default API key from the "API keys" tab.
- Run the following commands in the terminal:
- Create `./secrets.ini`
  ```bash
    cd ~/<path-to-the-root-of-cloned-instance>
    touch secrets.ini
  ```
- Open the `./secrets.ini` file in your preferred editor:
  ```bash
    vim secrets.ini
  ```
- Add the api key copied previously instead of `<YOUR-OPENWEATHER-API-KEY>`
  ```bash
    [openweather]
    api_key=<YOUR-OPENWEATHER-API-KEY>
  ```
  
<br>

### EXECUTE
- cd into the project folder.
  ```bash
  cd ~/<path-to-the-root-of-cloned-instance>
  ```
- Run `./main.py`
  ```bash
    python3 main.py
  ```

___

## Architecture Diagrams

### Class Design
![uml diagram](https://github.com/Fastest-Coder-First/ms-weather-forecasting-tool/assets/63065397/1fe92616-5aa4-4392-a1b3-f02a0e526811)

### Flow Diagram
![architecture diagram](https://github.com/Fastest-Coder-First/ms-weather-forecasting-tool/assets/63065397/3a4c3713-68d2-4ff7-a04d-9ba2d22be117)

___

<br>

## GitHub Copilot use cases
- We have made extensive use of GitHub Copilot.
    - To generate the base class structure
    - To write getter and setter methods
    - To design the menu for CLI
    - For comments
    - Documentation Stuff
    - To write the variable and method names following naming conventions

## Other GitHub Uses :octocat:
- GitHub GUI (Github Desktop)
- GitHub teams
- We have done all the git operations on GitHub Desktop - the best GUI for Git:
    - git clone
    - git commit
    - git branch
    - git push
    - merging
- We've also used GitHub web-app, for:
    - making PRs
    - merging PRs
    - resolving conflicts
 
> PS: Now this upgraded GitHub web and desktop UI is so much better, that even after being developers, we wanted to try using the GitHub web and desktop versions instead of command line for git operations. And it was really convenient. Kudos to GitHub!


___

<br>

## Tech Stack
- Python


___

<br>


## Made with 🤍 by:

- MVP - [(click-to-see-who-😉)](https://github.com/features/copilot)
- Mudita Baid - [muditabaid](https://github.com/muditabaid)
- Yashvardhan Baid - [code-chaser](https://github.com/code-chaser)



___
> #### _*Hope you like it!*_
___
