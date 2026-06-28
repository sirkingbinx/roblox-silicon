import os

class rsil_data:
    def __init__(self, fname: str, mode: int):
        self.filepath = fname
        self.filedata = {}

        # write
        if mode == 0:
            open(self.filepath, "w")
        
        # read
        if mode == 1:
            if not (os.path.exists(self.filepath) and os.path.isfile(self.filepath)):
                return
            
            with open(self.filepath, "r") as file:
                for line in file.readlines():
                    kv = line.split("=")

                    if len(kv) > 2:
                        print("Syntax error in roblox-silicon-dat: KV pair - {key}={value}")

                    self.filedata[kv[0].strip()] = kv[1].strip()
    
    def write(self, key: str, value: str):
        self.filedata[key] = value
    
    def flush(self):
        with open(self.filepath, "w") as file:
            for k, v in self.filedata.items():
                file.write(f"{k}={v}\n")
            
            file.flush()
            