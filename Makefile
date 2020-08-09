    
main.pdf: main.tex  test.png htmldate.py
	latexmk -pdf

test.png: htmldate.py dates.csv
	python htmldate.py


dates.csv:
	wget https://owlya.s3.us-east-2.amazonaws.com/dates.csv

.PHONY: clean almost_clean

clean: almost_clean
	rm -f test.png
	rm -f main.pdf

almost_clean:
	latexmk -c
	rm -rf __pycache__
	rm -f data.csv
