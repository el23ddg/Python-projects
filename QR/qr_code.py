# Generate QR code with Python
import qrcode
website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5) #adds the details of the box
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white') #adds the colour of the rr code
img.save('youtube_qr.png')
