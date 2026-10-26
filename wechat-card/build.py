import pathlib
import qrcode

URL = "https://jzjia7.github.io/"
HERE = pathlib.Path(__file__).parent

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0)
qr.add_data(URL)
qr.make(fit=True)
matrix = qr.get_matrix()
n = len(matrix)

path = "".join(
    f"M{x},{y}h1v1h-1z"
    for y, row in enumerate(matrix)
    for x, on in enumerate(row)
    if on
)
svg = (
    f'<svg viewBox="0 0 {n} {n}" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">'
    f'<path d="{path}" fill="currentColor"/></svg>'
)

template = (HERE / "card.template.html").read_text(encoding="utf-8")
(HERE / "card.html").write_text(template.replace("{{QR}}", svg), encoding="utf-8")
print(f"QR {n}x{n} modules")
