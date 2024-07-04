<br />
<div align="center">
  
<h3 align="center">Cryptocurrency correlation</h3>

  <p align="center">
    A simple program for calculating the Pearson correlation coefficient for 
    two cryptocurrency pairs
</div>

## About The Program
The program calculates the p-value and correlation coefficient between 
cryptocurrencies for a given period using 1-day interval close price. 



## Usage
To use the program, specify the parameters inside the code. Choose two pairs for
the calculation, a list of sample pairs is provided at the bottom of the code.
Next, choose the `period`, for example 30 corresponds to 30 days counting from
a given date down to a month before that. Be aware that calculation with a period 
of 365 days will take 10-20 minutes to complete. By default, current date is 
assumed, to choose a different date - simply uncomment the `date` variable and 
input the date.

![alt text](/images/image1.png)

It's possible to use different intervals than 1-day, but it involves some 
minor modifications to the program. Change the `interval` variable to 
the desired value, like "1h" and change the number of seconds in a day - "86400"
to a number of seconds in an hour.

## Prerequisites
To run the program, a few packages are required:

* numpy
  ```sh
  pip install numpy
  ```
* requests
  ```sh
  pip install requests
  ```
* scipy
  ```sh
  pip install scipy
  ```

