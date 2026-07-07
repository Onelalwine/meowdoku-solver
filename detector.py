<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Meowdoku Solver</title>
</head>
<body>

<h1>Meowdoku Solver</h1>

<form method="POST" enctype="multipart/form-data">
    <input type="file" name="image" accept="image/*">
    <button type="submit">上传图片</button>
</form>

{% if image %}
    <hr>

    <img src="{{ image }}" style="max-width:500px">

    <h3>图片信息</h3>

    <p>宽度：{{ info.width }}</p>
    <p>高度：{{ info.height }}</p>
    <p>模式：{{ info.mode }}</p>

    <h3>AI提示</h3>

    <p>{{ hint.message }}</p>

{% endif %}

</body>
</html>
