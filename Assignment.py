# the script reads the config text file and converts it to json and serve the data over rest API

#importing the required modules
from itertools import groupby
import json
from flask import Flask

# code to read text file and convert it to json file
with open(r"C:\Users\Levono\Desktop\python\Assignment\config.txt") as f, open(r"C:\Users\Levono\Desktop\python\Assignment\config.json","w") as out:
    grouped = groupby(map(str.strip,f), key=lambda x: x.startswith("!"))
    names  = ["Interfaces","ip_address","description"]
    for k,v in grouped:
        if not k:
            json.dump(dict(zip(names,v)),out)
            out.write("\n")

# code to read json file and convert it to the required output			
with open(r"C:\Users\Levono\Desktop\python\Assignment\config.json","r") as out, open(r"C:\Users\Levono\Desktop\python\Assignment\config1.json","w") as out1:
    while out:
        try:
            out_lines = out.readline()
            out_lines_json = json.loads(out_lines)
            sub_net = out_lines_json['ip_address'].split(' ')[3]
            ip_address = out_lines_json['ip_address'].split(' ')[1]
            interface = out_lines_json['Interfaces'].split(' ')[1]
            description = out_lines_json['description'].split(' ')[1]
            values = [interface,ip_address,sub_net,description]
            keys = ["interface","ip address","sub net","description"]
            json.dump(dict(zip(keys,values)),out1)
            out1.write("\n")
        except Exception as e:
            break
			
app = Flask(__name__)
@app.route('/interface/all/')
def get_interface_all():
    with open(r"C:\Users\Levono\Desktop\python\Assignment\config1.json","r") as  jsonfile:
        file_data = jsonfile.readline()
        file_data_json = json.loads(file_data)
        return file_data_json['interface']
    
@app.route('/interface/<name>')
def get_interface_name(name):
    with open(r"C:\Users\Levono\Desktop\python\Assignment\config1.json","r") as  jsonfile:
        while jsonfile:
            try:
                file_data = jsonfile.readline()
                file_data_json = json.loads(file_data)
                if file_data_json['description'] == name:
                    return file_data_json['interface']
            except:
                break
if __name__ == '__main__':
    app.run()