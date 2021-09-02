import os
directory = "./"

paths = list(filter(lambda x: all(map(lambda y: y[-3:] == '.md', x[2])) and len(x[2]) > 0, os.walk(directory)))

## need to add validation for every dir having readmes

paths_dict = {}
for path in paths:
    paths_dict[path[0]] = {"files": path[2], "dirs": path[1]}

### 

def parse_toc(ident, key) -> str:
    root = f'{ident*4*" "}* [{key.split("/")[-1].replace(".md", "").capitalize()}]({key[2:]}/README.md)'
    try:
        current_val = paths_dict[key]
    except KeyError:
        return ""

    if len(current_val["files"]) > 0:
        files = "\n".join([f'{(ident+1)*4*" "}* [{fil.replace(".md","").capitalize().replace("-"," ").replace("_"," ")}]({key[2:]}/{fil})' for fil in current_val["files"] if fil != "README.md"])
        within_dirs = [root] + [files] + [parse_toc(ident+1, f"{key}/{new_key}") for new_key in current_val["dirs"]]
    else:
        within_dirs = [root] + [parse_toc(ident+1, f"{key}/{new_key}") for new_key in current_val["dirs"]]
    for dir_ in current_val["dirs"]:
        del paths_dict[key + "/" + dir_]

    if ident == 0:
        res_txt = "\n".join(within_dirs)
    else:
        res_txt = "\n".join(within_dirs)
    return res_txt

###

tst_out = "\n".join(list(map(lambda x: parse_toc(0, x), list(paths_dict))))

while "\n\n" in tst_out:
    tst_out = tst_out.replace("\n\n","\n")
print(tst_out.replace("\n* [","\n\n* ["))

