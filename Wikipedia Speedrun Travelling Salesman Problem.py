from bs4 import BeautifulSoup as bs
import requests as req

def splittingAllOfHTML(word): #first attempt at splitting up the entire html document, slow and messy for words with many definitions, takes entire HTML text and processors it
    word_URL = "http://wordnetweb.princeton.edu/perl/webwn?s={}&sub=Search+WordNet&o2=&o0=&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=0".format(word)
    def_HTML = req.get(url=word_URL)
    soup = bs(def_HTML.content, 'html.parser')
    soupText = soup.get_text()
    typList = ["Noun", "Verb", "Adjective", "Adverb"] # may need Pronoun
    all_word_defs_beforeFormat = []
    #all_word_defs = []
    for t in typList:
        try:
            if t not in soupText:
                continue
            all_word_defs_beforeFormat.append(soupText.split(t)[-1])  
        except:
            print("EXCEPTION: NO " + t + " FOUND")
    removalList = ["\n", "S: ", "(n) ", "(v)", "(adj)", "(adv)"]
    #for i in all_word_defs_beforeFormat:
    all_word_defs = str(all_word_defs_beforeFormat[0])
    for Old in removalList:
        (all_word_defs.replace(Old, ""))
        
        #x = str(i)
        #print(x)
    print(all_word_defs)
    


    #print(all_word_defs_beforeFormat)
    
    #word_defs = soup.find_all('a')
    #print (word_defs.get('href'))
    #for i in soup.find_all('a'):#word_defs:
    #    print (i.get('href'))

def split_words_from_wiki_link(link_to_split): # takes in links and splits to words, too many splits, better to parse in title and remove items
    try:
        current_wikipedia_page = link_to_split
        page_name = current_wikipedia_page.split("/wiki/")[-1]
        if "File:" not in page_name:
            print(page_name)
            if "/w/" not in page_name:
                if "_" in page_name:
                    page_words = page_name.split("_")
                return page_words
            else:
                return("is w")
        else:
            return("is file")
    except:
        return ("not wiki")

def title_splitter(titles): # not necessary, defines word in context with all words
    split_titles = []
    for i in titles:
        i.split(" ")
        print (i)
        split_titles.append(i)
    return split_titles







def categorySplit(title_list):
    no_category_list = []
    num = 0
    for i in title_list:
        if "Category:" in str(i): # breaks too soon if right-side summary box contains a category link
            if num >= 1:
                break
            else:
                num += 1
        else:
            no_category_list.append(i)
    return no_category_list
def editSplit(title_list):
    no_edit_catagory_refs = []
    for i in title_list:
        if "Edit section: References" in str(i):
            break
        if "Edit section:" in str(i):
            continue
        else:
            no_edit_catagory_refs.append(i)
    return no_edit_catagory_refs
def wiki_title_filter(link_title_list):
    remove_category_list = categorySplit(link_title_list) # removes 'categorys' links
    remove_edit_list = editSplit(remove_category_list) # removes page edit links reference section
    remove_404_list = [i for i in remove_edit_list if "(page does not exist)" not in str(i)] # removes non-existant pages
    remove_None_list = [i for i in remove_404_list if i != None] # removes links with no title
    #"Wikipedia", "Citation"needed
    #print(remove_None_list)
    return remove_None_list

def get_def(word): #extracts just the <li> elements and then filters out links and makes list of definitions for the input word
    word_with_plus = word.replace(" ", "+")
    word_URL = "http://wordnetweb.princeton.edu/perl/webwn?s={}&sub=Search+WordNet&o2=&o0=&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=0".format(word_with_plus)
    def_HTML = req.get(url=word_URL)
    soup = bs(def_HTML.content, 'html.parser')
    word_definitions = []
    all_li_elements = soup.findAll('li')
    if len(all_li_elements) == 0:
        return 404
        #return "No Definition Found -- {}".format(word)
    for li_lists in all_li_elements: # gets all <li> elements
         for i in li_lists:
            try:
                extracted_defs_with_punctuation = i.split("</a>")[-1] # must be after </a>, only before definitions
                messy_word_defs = extracted_defs_with_punctuation.split("</li>")[0] # must end with </li>, only after definitions
                for punct in [", ", "\n", "(", ")", "e.g. ", ".", ";", ":"]: # list to clean up definitions to make parsing words possible
                    messy_word_defs = messy_word_defs.replace(punct, "")
                word_definitions.append(messy_word_defs) # adds each definition after being cleaned

                for ding in word_definitions:
                    if (len(ding)) < 2: # removes spaces and other single punctuation from the list
                        word_definitions.remove(ding)
            except: # exception raised if not a definition due to splitting at </a> and </li>
                pass

    return word_definitions




def get_links_from_current_wikipedia_page(wikipedia_page):
    req_HTML = req.get(url=wikipedia_page)
    soup = bs(req_HTML.content, 'html.parser')
    all_titles_on_page = []
    definitions_list = []
    for link in soup.findAll('a'):
        all_titles_on_page.append(link.get('title'))
        filtered_title_list = wiki_title_filter(all_titles_on_page)
    for word in filtered_title_list:
        definitions_list = get_def(word)
        if definitions_list == 404:
            continue
        print (definitions_list)


get_links_from_current_wikipedia_page("https://en.wikipedia.org/wiki/Naked_eye")#"https://en.wikipedia.org/wiki/Orion_Nebula")
