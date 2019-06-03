# biopython automated fastaQ blasting


# changes
This is the first relevant changelog, containing some information on how to use the program as it is now.
### usage
- set fastaQ filenames in the `FILES` global
- put your kwarg dicts in the `BLAST_KWARG_LIST` global, make sure the programs can be used for the dataset (no tblastn with a nucleotide sequence, for example.)
	- any kwargs used by `Bio.Blast.NCBIWWW.qblast` can be passed in this dictionary
- make sure the main function uses the FILES global, this can be set in the 6th line `header_data_dict = parseFastaQ("<yourListOfFilenames>", "<yourListOfIdentifiers>")`
identifiers are not necessary.
-
### main
- add function: `saveData(data, filename)`
	- appends the items of a list to a csv file
- add function: `testFastathing()`
	- tests if every sequence in every file in a list of fastaQ files is DNA (can easily be edited to test for proteins)
- add: TO DO list
- add:  a bunch of hardcoded lists/dictionaries to be used for testing and quick access to certain strings/lists/dicts
	- add:  `DEFAULT_HEADERS`
		- list of used headers in csv file (later this can be used to query a dictionary for certain 'wanted' items to be put in the csv file)
	- add: `BLAST_KWARGS_LIST`
		- a list of premade kwargs dictionaries to be passed to qblast. Before passing, the value of  the 'sequence' key has to be set to the DNA/protein string to query a database with. (this is done in the main function)
	- removed/disabled: temporary csv solution.

### blastaseq
- now takes and passes kwargs to qblast
