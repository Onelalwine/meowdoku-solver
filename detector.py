from PIL import Image


def load_image(image_path):
    """
    读取图片并返回基本信息
    """
    img = Image.open(image_path)

    return {
        "width": img.width,
        "height": img.height,
        "mode": img.mode
    }
