#APII123
from fastapi import FastAPI, HTTPException
from flask import Flask,send_file
from PIL import Image
import requests
from io import BytesIO
from flask import Flask, request, jsonify
import sys

app=Flask(__name__)

# Function to fetch image from URL
def fetch_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img

# Function to process the image (example: crop and convert to transparent PNG)
def process_image(image, crop_coordinates=None):
    # Make sure the image has an alpha channel (RGBA)
    image = image.convert("RGBA")
    
    # If crop coordinates are provided (x, y, width, height), crop the image
    if crop_coordinates:
        image = image.crop(crop_coordinates)
    
    # Make the background transparent (optional step)
    # If you want to remove the white background, for example
    pixels = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # If the pixel is mostly white (can be adjusted), make it transparent
            if r > 200 and g > 200 and b > 200:
                pixels[x, y] = (r, g, b, 0)  # Set alpha to 0 (transparent)
    
    return image

# Function to save the image as a transparent PNG
def save_image(image, output_path):
    image.save(output_path, format="PNG")

# Example usage
try:
    image_url =str(input())  # Replace with your image URL
    output_file = "E:\My project\output1.png"  # Replace with desired output path
    x=int(input())
    y=int(input())
    width=int(input())
    height=int(input())
except (TypeError,ValueError):
    print('error')
    exit()

# Fetch the image from the URL
image = fetch_image(image_url)

# Process the image (optional: provide crop coordinates like (x, y, width, height))
crop_coordinates = (x,y ,width ,height )  # Example crop coordinates
processed_image = process_image(image, crop_coordinates)

# Save the processed image as a transparent PNG
save_image(processed_image, output_file)

print(f"Processed image saved to {output_file}")
@app.route("/image")
def imagee():
    return send_file("E:\My project\output1.png",mimetype='output1.png')
imagee()
if __name__=="__main__":
    app.run(debug=True)


'''def fetch_image(processed_image):
    try:
        response = requests.get(processed_image)
        if response.status_code == 200:
            return Image.open(BytesIO(response.content)).convert("RGBA")
        else:
            raise HTTPException(status_code=400, detail="Failed to fetch image from URL")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching image: {str(e)}")'''