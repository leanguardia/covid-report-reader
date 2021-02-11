class OcrDataParser:
    def parse(self, ocr_data):
        rows = ocr_data.split('\n')
        # print(ocr_data)
        # print(type(ocr_data))
        return [OcrDataItem(row) for row in rows] 

class OcrDataItem:
    def __init__(self, raw):
        self.elements = raw.split('\t')

    def text(self):
        return self.elements[-1]

    def left(self):
        return int(self.elements[-6])

    def top(self):
        return int(self.elements[-5])

    def width(self):
        return int(self.elements[-4])

    def height(self):
        return int(self.elements[-3])
