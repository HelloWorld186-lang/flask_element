from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/review')
def review_fun():
    user_name = request.args.get('user_name')
    user_email = request.args.get('user_email')
    user_phone = request.args.get('user_phone')
    user_address = request.args.get('user_address')
    user_photo = request.args.get('user_photo')
    return render_template('review.html', user_name=user_name, user_email=user_email, user_phone=user_phone, user_address=user_address, user_photo=user_photo)

@app.route('/', methods=['GET', 'POST'])
def form_fun():
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['email']
        user_phone = request.form['phone']
        user_address = request.form['address']
        user_photo = request.files['profile_photo']
        if user_photo.filename != '':
            user_photo.save(f'static/img/{user_photo.filename}')
        if user_name and user_email and user_phone and user_address and user_photo:
            return redirect(url_for('review_fun', user_name=user_name, user_email=user_email, user_phone=user_phone, user_address=user_address, user_photo=user_photo.filename))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

