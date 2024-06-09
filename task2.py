from PIL import Image


def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        width, height = img.size
        encrypted_img = Image.new(img.mode, (width, height))

        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                encrypted_pixel = tuple((p + key) % 256 for p in pixel)
                encrypted_img.putpixel((x, y), encrypted_pixel)

        encrypted_img.save("encrypted_image.png")
        print("Image encrypted successfully!")
    except IOError:
        print("Unable to open image file")


def decrypt_image(encrypted_image_path, key):
    try:
        encrypted_img = Image.open(encrypted_image_path)
        width, height = encrypted_img.size
        decrypted_img = Image.new(encrypted_img.mode, (width, height))

        for x in range(width):
            for y in range(height):
                encrypted_pixel = encrypted_img.getpixel((x, y))
                decrypted_pixel = tuple((p - key) % 256 for p in encrypted_pixel)
                decrypted_img.putpixel((x, y), decrypted_pixel)

        decrypted_img.save("decrypted_image.png")
        print("Image decrypted successfully!")
    except IOError:
        print("Unable to open encrypted image file")


def main():
    image_path = input("Enter the path of the image to encrypt: ").strip('"')
    key = int(input("Enter the encryption key (an integer between 1 and 255): "))

    encrypt_image(image_path, key)
    encrypted_image_path = "encrypted_image.png"

    decrypt_option = input("Do you want to decrypt the image (yes/no)? ").lower()
    if decrypt_option == "yes":
        decrypt_image(encrypted_image_path, key)
        print("Decrypted image saved as 'decrypted_image.png'.")


if __name__ == "__main__":
    main()