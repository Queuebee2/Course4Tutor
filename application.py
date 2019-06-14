import Bio
import flask as Flask
from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML
import Bio.Blast.Record as record
from biopython_script.db_insert import DbConnector
from flask import Flask, request, render_template, url_for
from Bio.Seq import Seq

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/',methods =['POST'])
def formpje():
    text = request.form["text"]
    text = text.upper()
    text = text.replace("\n", "")
    titel = ""

    """
    result_handle = NCBIWWW.qblast("blastp", "nr", text)
    with open("my_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()
    """


    result_handle = open("my_blast.xml")
    blast_records = NCBIXML.read(result_handle)

    for alignment in blast_records.alignments:
        for hsp in alignment.hsps:
            titel += alignment.title + "<br>"
    return titel

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/FAQ')
def Frequently():
    return render_template('FAQ.html')

@app.route('/statistieken')
def stats():
    return render_template('statistieken.html')

@app.route('/contact')
def cont():
    return render_template('contact.html')

@app.route('/zelf_blasten')
def blast():
    return render_template('zelf_blasten.html')


@app.route('/selectdemo', methods=["GET","POST"])
def select_results_demo():

    if request.method == 'POST':
        if request.form['button'] == 'select_results':
            connect = DbConnector()
            results = connect.select_results()
            return render_template('resultaten_demo.html', blast_results=results)
        else:
            return render_template('resultaten_demo.html')
    else:
        return render_template('resultaten_demo.html')


if __name__ == '__main__':
    app.run(use_reloader=True, debug = True)
