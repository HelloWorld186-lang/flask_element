from flask import Flask, render_template, redirect, request, flash , Response
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators

app = Flask(__name__)
app.secret_key = "secret key"

# WTForm
# textfiled 
# booleanfirld
# decimalfield
# integerfiled 
# radiofield
# selectfield 
# textAreaField
# passwordfield 
# submitField
class NameForm(FlaskForm):
    name = TextAreaField("Your name:", [validators.DataRequired("Please enter your name.")])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        flash(f"Form submitted successfully with name: {name}")
        return redirect('/')
        # return Response(name)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
