from PIL import Image

image1 = Image.open('cats.JPG')
print(f'Image mode: {image1.mode}')
print(f'Image size: {image1.size}')
print(f'Image width: {image1.width} pixels')
print(f'Image height: {image1.height} pixels')
print(f'Image format: {image1.format}')
image1.show()
