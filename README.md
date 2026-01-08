The goal of this assignment was to design a framework that can be easily extended for real API testing,

while keeping scenarios readable and well-documented.



Tech Stack



Python 3.10+



Behave (BDD framework)



\## Installation



1\. Clone the repository:



```bash

git clone https://github.com/Nithin3076/yuno-payment-automation.git

cd yuno-payment-automation





\\## Overview of Scenarios



\\### Purchase

\\- Minimal fields (Sanity, Regression)

\\- Maximal fields (Regression, Integration)

\\- Invalid card (Negative, Regression)



\\### Authorization

\\- Minimal fields (Sanity)

\\- Maximal fields (Regression)

\\- Invalid amount (Negative, Regression)



\\### Refund

\\- Full refund (Regression)

\\- Invalid payment id (Negative, Regression)



\\### Verify

\\- Valid card (Sanity, Regression)

\\- Invalid card (Negative, Regression)


