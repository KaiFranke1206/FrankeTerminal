def run(args):
    themes = {
        "dark": "\033[37;40m",
        "light": "\033[30;47m",
    }
    if args.strip() in themes:
        print(themes[args.strip()])
        print(f"Switched to {args.strip()} theme!")
    else:
        print("Available themes: dark, light")
