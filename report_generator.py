from pypdf import PdfWriter

pdfs = ['tex/output/task1/distribution_function.pdf', 'tex/output/task1/polygon.pdf',
        'tex/output/task2/cumulative_8_bins.pdf', 'tex/output/task2/histogram_8_bins.pdf', 'tex/output/task2/ogive_8_bins.pdf',
        'tex/output/boxplot.pdf']

merger = PdfWriter()

for pdf in pdfs:
    merger.append(pdf)

merger.write('result.pdf')
merger.close()