from os import walk

import cv2
import pandas as pd
import pytesseract as ocr

from readers.parsers import OcrDataParser
from readers.report_reader import ReportReader
from img.processing import process#, grayscale, threshold 


reports_path = 'img/reportes_salud/'

_, _, filenames = next(walk(reports_path))
# filenames = ['1353866415820955648_0.png']

failed_files = ['.DS_Store',
          '1339026608439627778_0.png',
          '1338657548040286210_0.png',
          '1340836592127074304_0.png',
          '1355681007500976133_0.png',
          '1347715466790363136_0.png',
          '1343723603758604292_0.png',
          '1356409086234009602_0.png',
          '1341198161566720001_0.png',
        ]

df_data = {
  'number': [],
  'date': [],
  'time': [],
  'new_cases': [],
  'new_deaths': [],
  'recovered': [],
  'active': [],
  'deaths': [],
  'suspicious': [],
  'accumulated': [],
  'discarted': [],
  'beni': [],
  'chuquisaca': [],
  'cochabamba': [],
  'la_paz': [],
  'pando': [],
  'santa_cruz': [],
  'tarija': []
}
for filename in filenames:
    print("\n> Processing:", filename)
    if filename in failed_files: print('skip'); continue
    
    img = cv2.imread(reports_path + filename)
    # show_img(img)
    print("Shape:", img.shape)
    processed = process(img)
    reader = ReportReader(processed)
    try:
      report = reader.read()
      print(report)
      accumulate_report(report)
    except IndexError as e:
      print("Failed " + filename)


print(df_data)
df = pd.DataFrame(df_data)
df.to_csv('full.csv', index=False)

    # :::::: OCR ::::::
    
    # processed = process(img)
    # ocr_data = ocr.image_to_data(processed)
    # conf = r'--oem 3 --psm 6'
    # string = ocr.image_to_data(processed, config=conf)
    # print(ocr_data)

    ## :::::: THE PARSER ::::::

    # rows = OcrDataParser().parse(string)
    # print("ROWS: {}".format(len(rows)))
    # for row in rows[1:-1]:
    #     # print(row.text())
    #     top_left = (row.left(), row.top())
    #     # print(top_left)
    #     bottom_right  = (row.left() + row.width(), row.top() + row.height())
    #     # print(bottom_right)
    #     processed = cv2.rectangle(processed, top_left, bottom_right, (0, 0, 0), 2)
    # show_img(processed)

