from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def index():
    red = random.sample(range(1,34),6)
    red.sort()
    blue = random.randint(1,16)
    res = f"红球：{' '.join(f'{x:02d}' for x in red)}  蓝球：{blue:02d}"
    return render_template_string(f'''
    <html>
    <body style="text-align:center;font-size:24px;padding-top:50px;">
        <h1>彩票随机生成器</h1>
        <p>{res}</p>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
