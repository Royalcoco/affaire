import hashlib
import random
def __init__(self, options  =   {})  : self.options = options.launch_options or {} if options.launch_options    else {} 
def __init__(self, options  =   {})  : self.options = options.launch_options or {} if options.launch_options    else {}
class StockOptions:
    def __init__(self, stock, strike, expiry, option_type, premium):
        self.stock = stock
        self.strike = strike
        self.expiry = expiry
        self.option_type = option_type
        self.premium = premium
        
        self.options = {    'stock': self.stock,    'strike': self.strike,    'expiry': self.expiry,    'option_type': self.option_type,    'premium': self.premium}
        self.options['options'] = self.options
        self.options['option_type'] = self.options['option_type'].upper()   + ' ' + self    .options['stock']   + ' ' + self.   options['strike'] + ' ' +   self. options['expiry'] + ' ' + self. options[' option_type'] + ' ' + self. options['premium']  + ' ' + self. options[' option_type']   + ' ' + self.price()
        
    def price(self):       return self.options['premium']
    __init__.__annotations__ = {'stock': str, 'strike': float, 'expiry': str, 'option_type': str, 'premium': float} 
    price.__annotations__ = {'return': float}
    select = lambda self, key: self.options[key]
    from_dict = lambda self, options: StockOptions(options['stock'], options['strike'], options['expiry'], options['option_type'], options['premium']) 
    where = lambda self, key: self.options[key + '_where clause'] or self.options[key + }(Current_date) = date and TimeZone.tzinfo == 'UTC'
    
    
def mine_block(previous_block, transactions, difficulty):
    nonce = 0
    while True:
        data = str(previous_block) + str(transactions) + str(nonce)
        hash_value = hashlib.sha256(data.encode()).hexdigest()
        if hash_value[:difficulty] == '0' * difficulty:
            return hash_value, nonce
        nonce += 1
    
def mine_block(previous_block, transactions, difficulty):
    

# Exemple d'utilisation
previous_block = "0000000000000000000000000000000000000000000000000000000000000000"
transactions = ["Transaction 1", "Transaction 2", "Transaction 3"]
difficulty = 4

mined_hash, nonce = mine_block(previous_block, transactions, difficulty)
print("Block mined successfully!")
print("Hash:", mined_hash)
print("Nonce:", nonce)

# Block mined successfully!
# Hash: 0000a3b3b0c8b6f

import cv2
import numpy as np

def crop(image, x, y, width, height):
    return image[y:y+height, x:x+width]

def resize(image, width, height):
    return cv2.resize(image, (width, height))

def apply_filter(image, filter_type):
    if filter_type == 'grayscale':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'blur':
        return cv2.GaussianBlur(image, (5, 5), 0)
    elif filter_type == 'edge':
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    else:
        return image

# Chargement de l'image
image = cv2.imread('input.jpg')

# Exemple d'utilisation des fonctionnalités
cropped_image = crop(image, 100, 100, 200, 200)
resized_image = resize(image, 800, 600)
filtered_image = apply_filter(image, 'blur')

# Affichage des résultats
cv2.imshow('Cropped Image', cropped_image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
