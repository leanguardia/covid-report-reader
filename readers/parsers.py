class OcrDataParser:
    def parse(self, ocr_data):
        rows = ocr_data.split('\n')
        # print(ocr_data)
        # print(type(ocr_data))
        return [OcrDataRow(row) for row in rows] 

class OcrDataRow:
    def __init__(self, raw):
        self.elements = raw.split('\t')

    def text(self):
        return self.elements[-1]