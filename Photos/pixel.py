from PIL import Image

# Open the image
image = Image.open('text_cricket.jpeg')

# Resize to pixel art size
pixel_art_size = (196, 180)
image_small = image.resize(pixel_art_size, Image.NEAREST)

# Scale back up
pixel_art = image_small.resize(image.size, Image.NEAREST)

# Save the pixel art
pixel_art.save('pixel_art1.png')