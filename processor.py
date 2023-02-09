import codecs
import json
import os



# def inTake():
#     file = "logs.txt"
#     file_path = os.path.join(os.path.abspath('queue'), file)
#     queue = []
#     with codecs.open(file_path, 'r', 'utf-8') as txt_file:
#         for line in txt_file:
#             txtLine = str(line.replace('\n', ''))
#             queue.append(txtLine)
#     try:    
#         link = queue.pop()
#         print(link)
#     except IndexError:
#         print(f"No links to download")

# schedule.every(5).seconds.do(inTake)

# while True:
#     schedule.run_pending()


def logger(magnet_link):
    link_Status = "Good"
    try:
        sentLink = open("sentMsg.txt", "x")
    except Exception as e:
        if e:
            print('file already exists')
    
    with codecs.open("sentMsg.txt", "a", 'utf-8') as log:
        reportMsg = {'magnet_link': f"{magnet_link}", 'status': f"{link_Status}"}
        log.write(json.dumps(reportMsg)+'\n')
        log.close()

