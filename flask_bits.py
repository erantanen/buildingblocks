'''
This is a collection of flask bits ...

odd assortment of components tied to other things?

'''


# this is part of an ajax mechanism for
#  drop down lists

@app.route("/list")
def list_state():
    rows = execute_query("""SELECT state FROM natlpark""")
    temp_list = []
    for elm in rows:
        temp_list.append(elm[0])

    return jsonify(result=temp_list)
