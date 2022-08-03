from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/')
def query():
    name = request.args.get('name')
    message = request.args.get('message')
    if not name or not message:
        return redirect('/?name=Rekruto&message=Давай дружить')
    return f'Hello {name}! {message}!'


if __name__ == '__main__':
    app.run(debug=False)
