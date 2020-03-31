
from flask import Flask,request,send_file
import numpy as np
from  modelprt import prd
import  json
predict =prd()
app = Flask(__name__,  )
@app.route('/',methods=['GET'])
def  main():
    data= request.args.get("data")
    data= data.replace(" ", "")
    data= [ float(x) for x in data.split(",")]
    data=np.array(data)
    dic={}
    dic['predict']=predict.prdt(data).tolist()
    return  json.dumps(dic)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090,debug=False, threaded=False)
