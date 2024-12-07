import qrcode

# GitHub Pages URL
url = "https://anonymous11150415.github.io/birthday-wishes/"

# 创建二维码
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# 生成二维码图片
img = qr.make_image(fill_color="black", back_color="white")
img.save("birthday_qr.png")
