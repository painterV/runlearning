import execjs


js = '''
const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM('<!DOCTYPE html><p>Hello world</p>');
window = global;
var document = dom.window.document;
function signature(){
    return 1
}
'''
ct = execjs.compile(js).call("signature")
print(ct)