#!/usr/bin/env python
import requests

def main():
    print("Hello Rev.Ai")
    r = requests.get('https://api.rev.ai/revspeech/v1beta/account', headers={'Authorization': 'Bearer 01jS3bvO2rL7OS0_GRmF-Z7h77p1Cp1RF_3se_E5_9brna0XdVV8_prQjeut-2HOEIG1WzFQLrwfJ5Q9bjHXiL66bkVEg'})
    print(r.text)

if __name__ == '__main__':
  main()