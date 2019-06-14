import Bio

from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML
import Bio.Blast.Record as record
from biopython_script.DbConnector import DbConnector
from flask import Flask, request, render_template, url_for, Markup
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

    
    result_handle = NCBIWWW.qblast("blastp", "nr", text)
    with open("my_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()
    


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


# test jinja2 variable om data over te brengen of
# 'injecteren' in het javascript in de hmtl
data = ['Pseudomonas','Streptomyces', 'Apteryx','Minicystis', 'Desulfuromonas', 'Segniliparus'
					    , 'Hydrogenophaga','Woeseia','Thermobifida', 'Chitinophaga','PREDICTED: Paralichthys'
					     ,'Scytonema',
					     'Minicystis', 'Pusillimonas', 'Methylobacterium','Sphingopyxis', ' Gemmatimonas'
					    ,'Coraliomargarita','PREDICTED: Salmo','Ruminiclostridium', 'Dechloromonas ',
					    'Rhodopirellula','Truepera ', 'Nitrosococcus', 'Gammaproteobacteria','Herbaspirillum ',
					     'Steroidobacter', 'Luteimonas', 'Solitalea', 'Pigmentiphaga', 'Aminobacter', 'Micromonospora ',
					     'Thermaerobacter', 'Parambassis', 'Stenotrophomonas', 'Salmo', 'Halocella', 
					     'Desulfovibrio', 'Brevibacterium', 'Xanthomonas', 'Pseudoxanthomonas',
					     'Marinithermus', 'Ochrobactrum', 'Limnochorda', 'Nocardioides', 'Nonomuraea'
					    ]
@app.route('/statistieken')
def stats():
    return render_template('statistieken.html', data=Markup(data))



@app.route('/zelf_blasten')
def blast():
    return render_template('zelf_blasten.html')


@app.route('/selectdemo', methods=["GET","POST"])
def select_results_demo():

    if request.method == 'POST':
        if request.form['button'] == 'select_results':
            connect = DbConnector()
            results = connect.select_results()
            results_html_table = Markup(createHtmlTable(results))
            return render_template('resultaten_demo.html', blast_results=results_html_table)
        else:
            return render_template('resultaten_demo.html')
    else:
        return render_template('resultaten_demo.html')

def createHtmlTable(rows):
    ts = "<div id = 'complete_tabel'>"
    ts += "<div id = 'div1'>"
    ts += "<table border = '1' id = 'tabel1'>"
    ts += "<tr style= 'padding-right: 15px' ><th>resultaat id</th><th>accessiecode</th><th>e value</th><th>perc. id</th><th>total coverage</th><th>Query coverage</th><th>max scores</th><th>sequentie</th><th>seq. id</th><th>eiwit id</th><th>geslachtsnaam</th></tr>"
    ts += "</div>"
    ts += "</table>"
    ts += "<div id = 'div2'>"
    ts += "<table border = '1' id = 'tabel2'>"
    for row in rows:
        ts += "<tr>"
        for column in row:
            ts += "<td>" + str(column) + "</td>"
        ts += "</tr>"
    ts += "</table>"
    ts += "</div>"
    ts += "</div>"
    return ts


if __name__ == '__main__':
    print('hello')
    app.run(use_reloader=True, debug = True)
