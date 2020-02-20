from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS
# from algorithms.classes.histogram_class import Histogram
from algorithms.classes.listogram import Listogram
from algorithms.classes.dictogram import Dictogram
import os
import sys

app = FlaskAPI(__name__)
CORS(app)

words = open('./text_files/words.txt','r')
words = ''.join(words.readlines()).split()

listo = Listogram(words).listogram_samples(10)
dicto = Dictogram(words).dictogram_samples(10)

histograms = {
    0: listo,
    1: dicto
}

# notes = {
#     0: 'do the shopping',
#     1: 'build the codez',
#     2: 'paint the door',
# }




@app.route("/", methods=['GET'])
def notes_list():
    """
    List or create notes.
    """
    # request.method == 'GET'
    sentences = [sentence for (index, sentence) in histograms.items()]
    return sentences

# @app.route("/int:key", methods=['GET'])
# def one_note(key):
    
#     # request.method == 'GET'
#     if key not in notes:
#         raise exceptions.NotFound()
#     return note_repr(key)

# @app.route("/int:key", methods=['POST'])
# def add_note(key):
#         if request.method == 'POST':
#             note = str(request.data.get('text', ''))
#             idx = max(notes.keys()) + 1
#             notes[idx] = note
#         return note_repr(idx), status.HTTP_201_CREATED

# @app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
# def notes_detail(key):
#     """
#     Retrieve, update or delete note instances.
#     """
#     if request.method == 'PUT':
#         note = str(request.data.get('text', ''))
#         notes[key] = note
#         return note_repr(key)

#     elif request.method == 'DELETE':
#         notes.pop(key, None)
#         return '', status.HTTP_204_NO_CONTENT


# @app.route("/<int:key>/", methods=['PUT'])
# def change_note(key):
#     if request.method == 'PUT':
#         note = str(request.data.get('text', ''))
#         notes[key] = note
#         return note_repr(key)

# @app.route("/<int:key>/", methods=['DELETE'])
# def delete_note(key):
#         if request.method == 'DELETE':
#             notes.pop(key, None)
#             return '', status.HTTP_204_NO_CONTENT


if __name__ == "__main__":
    app.run(debug=True)