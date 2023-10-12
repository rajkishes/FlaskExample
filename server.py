from flask import Flask, render_template, request
from scripts import forms, build

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/buildinterface', methods=["GET", "POST"])
def buildinterface():
    form = forms.buildinterface_form(request.form)
    if request.method == 'POST' and form.validate():
        config = build.build_interface(**form.data)
        return(f'<pre>{config}</pre>')
    return render_template('buildinterface.html', form=form)

@app.route('/buildmsb', methods=["GET", "POST"])
def buildmsb():
    form = forms.buildmsb_form(request.form)
    if request.method == 'POST' and form.validate():
        config = build.build_msb(**form.data)
        return(f'<pre>{config}</pre>')
    return render_template('buildmsb.html', form=form)

if __name__ == "__main__":
    app.run()