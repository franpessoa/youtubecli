from .download import playlist, video
import sys

class IncorrectLeadingArgumentError(Exception):
    pass

class IncorrectArgumentNumberError(Exception):
    pass

def parser():
    try:
        args = sys.argv[1:]
        if len(args) == 0:
            print("""Usage:
            youtube --video youtube.com/link >>> To download a video
            youtube --playlist youtube.com/link >>> To download a playlist""")
        
        elif len(args) != 2:
            raise IncorrectArgumentNumberError(f"youtube requires 2 arguments, {len(args)} were given")
        
        else:
            if args[0] == "--playlist":
                playlist(args[1])
            
            elif args[0] == "--video":
                video(args[1])
            
            else:
                raise IncorrectLeadingArgumentError(f"First argument needs to be --playlist or --video, {args[0]} was given")
    
    except KeyboardInterrupt:
        print("By by")
