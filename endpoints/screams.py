from io import BytesIO

from PIL import Image
from flask import send_file

from utils import http
from utils.endpoint import Endpoint


class Screams(Endpoint):
    params = ['avatar0', 'avatar1']

    def generate(self, avatars, text, usernames):
        base = Image.open(self.assets.get('assets/screams/screams.bmp')).convert('RGBA')
        avatar = http.get_image(avatars[0]).resize((175, 175)).convert('RGBA')
        avatar2 = http.get_image(avatars[1]).resize((156, 156)).convert('RGBA')
        base.paste(avatar, (200, 1), avatar)
        base.paste(avatar2, (136, 231), avatar2)
        base = base.convert("RGB")

        b = BytesIO()
        base.save(b, format='jpeg')
        b.seek(0)
        return send_file(b, mimetype='image/jpeg')


def setup(cache):
    return Screams(cache)
