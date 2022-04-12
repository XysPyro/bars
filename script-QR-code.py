import qrcode
# example data
data = "https://github.com/XysPyro/bars/blob/main/Bars.md"
# output file name
filename = "bars.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)