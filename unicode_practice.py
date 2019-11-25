import io
unicode = "utf-8"
name = "Dončić"

with open("doncic", "w", encoding="utf-8") as f:
    f.write(name)

with io.open("doncic", "r", encoding="utf-8") as f:
    print(f.read())
