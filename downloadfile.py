import dropbox
access_token = '***************'
dbx = dropbox.Dropbox(access_token)                    
f = open("frozen_inference_graph.pb","wb")
metadata,res = dbx.files_download("/frozen_inference_graph.pb") 
f.write(res.content)



