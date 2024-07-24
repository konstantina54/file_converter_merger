from flask import Flask, render_template, flash, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = os.urandom(24)

def upload_pic():
    uploadedFile = request.files['file']
    print(uploadedFile)
    # do we need this if if we trigger the function only when there is a file?
    if uploadedFile.filename != "":
        fileName = secure_filename(uploadedFile.filename)
        uploadedFile.save(os.path.join('uploads/', fileName))
        return fileName
    # else:
    #     flash("Please make sure you add first and last name")

@app.route('/')
def speakersPic():
    return render_template('uploadFile.html')

@app.route('/uploads', methods=['POST'])
def picture_uploaded():
    if request.method == 'POST':
    # something2 = request.form['picture']
        upload_pic()
        # need to make sure this goes the rith path
        # return needs to be at the end!!!!!!!!
        return render_template("fileUploaded.html", name=upload_pic())
    else:
        flash("Please make sure you add first and last name")

if __name__ == "__main__":
    app.run(debug=True)