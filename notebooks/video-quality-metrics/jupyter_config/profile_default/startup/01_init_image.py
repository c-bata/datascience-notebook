image_dir = path.join(path.dirname(path.abspath(__name__)), "image")

# Reference Image
rgb_img = Image.open(path.join(image_dir, "lena.png"))
rgb_img.thumbnail((256, 256), Image.ANTIALIAS)
rgb_array = np.asarray(rgb_img)

# Grayscale
grayscale_img = rgb_img.convert('L')
grayscale_array = np.asarray(grayscale_img)

# Luminous Linear Transform
grayscale_luminous_array = np.clip(grayscale_array * 1.05, 0, 255)
grayscale_luminous_img = Image.fromarray(np.uint8(grayscale_luminous_array))

# Blur
grayscale_blur_img = grayscale_img.filter(ImageFilter.GaussianBlur(3))
grayscale_blur_array = np.asarray(grayscale_blur_img)

# Blockiness
grayscale_blockiness_img = grayscale_img.resize([x // 3 for x in grayscale_img.size]).resize(grayscale_img.size)
grayscale_blockiness_array = np.asarray(grayscale_blockiness_img)


