from compileall import compile_dir, compile_path


def build(args):  
    if "quantum" in args.target:  
        compile_dir(args.file)  
    if "web" in args.target:  
        compile_path(args.file)  
    print("🪽 Build successful!")  