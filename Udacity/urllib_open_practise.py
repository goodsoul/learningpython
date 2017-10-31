import urllib

def read_text():
    quotes = open("C:\Test\README.txt")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()


def check_profantiy(text_to_check):
    link="http://www.wdylike.appspot.com/?q="+text_to_check
    connection = urllib.urlopen(link)
    
    output=connection.read()
    print(connection)
    print(output)
    connection.close()
                                

#read_text()
check_profantiy('test')
