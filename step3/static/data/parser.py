import xml.etree.ElementTree as ET
import psycopg2

#http://initd.org/psycopg/docs/usage.html#lists-adaptation

#Connect to context-slices database
conn = psycopg2.connect("dbname=context-slices user=tianyili")

#Open a cursor to perform database operations
cur = conn.cursor()
		
tree = ET.parse('crescent.xml')
root = tree.getroot()

TABLE_NAMES = ["step3_Document", "step3_Name_Entity", "step3_Document_Entity"]
TAG_NAMES = ["docID", "docDate", "docSource", "docText"]


#build aliases dictionary
aliases = []
current_alias = []

for name in root.iter('alias'):
    for n in name:
        current_alias.append(n[0].text)
    aliases.append(current_alias)
    current_alias = []

for doc in root.iter('document'):
    docID = doc.find(TAG_NAMES[0]).text
    docDate = doc.find(TAG_NAMES[1]).text
    docSource = doc.find(TAG_NAMES[2]).text
    docText = doc.find(TAG_NAMES[3]).text

    cur.execute("INSERT INTO "+ TABLE_NAMES[0] +" VALUES (%s, %s, %s, %s)", (docID, docSource, docDate, docText))

items = []
for doc in root.iter('document'):
    for child in doc:
        if (child.tag == TAG_NAMES[0] or child.tag == TAG_NAMES[1] or child.tag == TAG_NAMES[2] or child.tag == TAG_NAMES[3]):
            continue
        if child.text not in items:
            items.append(child.text)
            cur.execute("INSERT INTO "+ TABLE_NAMES[1] +" VALUES (%s, %s)", (child.text, child.tag))

for doc in root.iter('document'):
    for child in doc:
        if (child.tag == TAG_NAMES[0] or child.tag == TAG_NAMES[1] or child.tag == TAG_NAMES[2] or child.tag == TAG_NAMES[3]):
            continue
        doc_id = doc.find("docID").text
        entity_name = child.text
        pair_id = doc_id+"_"+entity_name
        occurence = doc.find("docText").text.count(entity_name)
        for alias in aliases:
            if entity_name in alias:
                #should check if it is always primary id, but skip for now
                for i in range(1, len(alias)):
                    occurence += doc.find("docText").text.count(alias[i])
        occurence = str(occurence)
        cur.execute("INSERT INTO " + TABLE_NAMES[2] + " VALUES (%s, %s, %s, %s)", (pair_id, occurence, doc_id, entity_name))



conn.commit()

# Close communication with the database
cur.close()
conn.close()