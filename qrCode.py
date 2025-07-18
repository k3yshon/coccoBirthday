import qrcode

urls = [
    "https://k3yshon.github.io/coccoBirthday/prank1_coconut.html",
    "https://k3yshon.github.io/coccoBirthday/prank2_tennis.html",
    "https://k3yshon.github.io/coccoBirthday/prank3_hunter.html"
]

for i, url in enumerate(urls, 1):
    img = qrcode.make(url)
    img.save(f"qr_prank_{i}.png")
