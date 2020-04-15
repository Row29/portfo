from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name)


def write_to_file(data):
    try:
        with open('database.txt', mode='a') as database:
            for key, val in data.items():
                entry = f'{key}: {val}'
                database.write(entry)
                database.write('\n')
    except FileNotFoundError as err:
        print('file does not exist')
        raise err
    except IOError as err:
        print('IOError')
        raise err


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to datbase'
    else:
        return 'something went wrong'


# try:
# 	with open('sad.txt', mode='r') as my_file:
# 		# text = my_file.write(':(')
# 		# print(text)
# 		print(my_file.read())
# except FileNotFoundError as err:
# 	print('file does not exist')
# 	raise err
# except IOError as err:
# 	print('IOError')
# 	raise err
