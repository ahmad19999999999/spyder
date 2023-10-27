from PIL import Image, ImageOps

# Step 1: Load and show an image
image = Image.open('image.png.jpg')
image.show()
input("Press Enter to continue...")  # Wait for user input to proceed

# Step 2: Summarize details about the image
format = image.format
mode = image.mode
size = image.size
print(f"Format: {format}\nMode: {mode}\nSize: {size}")

# Step 3: Convert the image to Greyscale mode
greyscale_image = ImageOps.grayscale(image)
greyscale_image.show()
input("Press Enter to continue...")

# Step 4: Create Thumbnails (200x200)
thumbnail = image.copy()
thumbnail.thumbnail((200, 200))
thumbnail.show()
input("Press Enter to continue...")

# Step 5: Crop the image
box = (50, 50, 150, 150)  # Define the coordinates of the crop box (left, upper, right, lower)
cropped_image = image.crop(box)
cropped_image.show()
input("Press Enter to continue...")

# Step 6: Rotate the image by 30%
rotated_image = image.rotate(30)
rotated_image.show()
input("Press Enter to continue...")

# Step 7: Save the image in a different format (PNG)
image.save('image.png.jpg', 'PNG')
image.show()
input("Press Enter to continue...")

# Step 8: Create text
text = "Information Technology, Information System, Text Mining, Web Mining, Data Mining, Artificial Intelligence, Human Resources"

# Step 9: Lower & Upper case the text
lower_text = text.lower()
upper_text = text.upper()

# Step 10: Split each text
text_list = text.split(', ')

# Step 11: Text concatenation with "&"
concatenated_text = ' & '.join(text_list)

# Step 12: Replace "Information" with "Info"
replaced_text = text.replace('Information', 'Info')

# You can print and visualize the text manipulations here
print("Original Text:", text)
print("Lowercase Text:", lower_text)
print("Uppercase Text:", upper_text)
print("Split Text List:", text_list)
print("Concatenated Text:", concatenated_text)
print("Replaced Text:", replaced_text)
