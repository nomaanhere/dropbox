import dropbox
access_token = 'oG7g0mYYCfAAAAAAAAAACuBzidmIGZBUfy1U4tx2wSA7wW4mQt3CodpDet_nMkqL'
dbx = dropbox.Dropbox(access_token)                    
f = open("frozen_inference_graph.pb","wb")
metadata,res = dbx.files_download("/frozen_inference_graph.pb") 
f.write(res.content)



