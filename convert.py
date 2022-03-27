from sys import path_importer_cache
import fitz
import json

#將每句分開存入
def parse1(file):
    doc = fitz.open(file)
    print ("number of pages: %i" % doc.pageCount)
    text = {}
    index=0
    #print(doc.metadata)
    for i in range(doc.pageCount):
        content = doc.loadPage(i)
        paper_context=content.getText("text").split("\n")
        for j in paper_context:
            if j.replace(" ","") != "" :
                text[index]=j
                index+=1
    print(text)
    return text

#將每頁分開存入
def parse2(file):
    doc = fitz.open(file)
    print ("number of pages: %i" % doc.pageCount)
    text = {}
    index=0
    for i in range(doc.pageCount):
        content = doc.loadPage(i)
        if content.getText("text").replace(" ","") != "" :
            text[index]=content.getText("text").replace("\n","")
            index+=1
    print(text)
    #text = text.replace("\n","")
    return text

#整份文件
def parse3(file):
    doc = fitz.open(file)
    print ("number of pages: %i" % doc.pageCount)
    text = ""
    #print(doc.metadata)
    for i in range(doc.pageCount):
        content = doc.loadPage(i)
        text += content.getText("text")
    print(text)
    #text = text.replace("\n","")
    return text
    

if __name__ == '__main__':
    file = '茶葉知識文獻拷貝.pdf'
    save_version=int(input("1.行 2.頁 3.整份文件  請輸入:"))
    output_file =  open(f"{file[:-4]}.json","w")
    # coding: utf-8

    if save_version==1:json.dump(parse1(file),output_file)
    elif save_version==2:json.dump(parse2(file),output_file)
    else: json.dump(parse3(file),output_file)
    
    output_file.close()

