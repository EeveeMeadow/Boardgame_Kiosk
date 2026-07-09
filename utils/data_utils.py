import base64


def decode_db_image(img_bytes: bytes, mime_type: str = 'image/png') -> str:
    decoded = base64.b64encode(img_bytes).decode('utf-8')
    return f'data:{mime_type};base64,{decoded}'
